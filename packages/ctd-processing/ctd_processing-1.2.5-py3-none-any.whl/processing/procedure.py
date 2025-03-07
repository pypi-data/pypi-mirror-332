from pathlib import Path
import sys
import shutil
from datetime import datetime, timezone
import logging
from seabirdfilehandler.datatablefiles import CnvFile
from processing.seabird.module import ProcessingModule
from processing.seabird.step import ProcessingStep
from processing.settings import IncompleteConfigFile, Configuration
from processing.modules import map_proc_name_to_class
from processing.utils import default_seabird_exe_path

logger = logging.getLogger(__name__)


class Procedure:
    """
    Runs a couple of processing steps in sequence on one or more CTD data
    source files.

    It can use seabird internal processing modules, as well as custom ones.
    These can be in the form of independent windows exes or just pure python
    code. The input data can be .hex, .cnv or pandas DataFrames. The input and
    all module and extra information is stored in a dict that usually will be
    generated by the settings Configuration module that reads a toml config.

    Parameters
    ----------
    configuration: dict | Configuration:
        The information necessary to run a processing procedure.

    seabird_exe_directory: Path | str | None = None:
        The path to the directory where the Sea-Bird exes reside in.
        Usually not necessary, as this Class knows the default install path.

    available_hex_converters: list[str] = ["datcnv"]:
        A list of the known hex converters.

    auto_run: bool = True:
        Whether to autopilot the whole procedure.

    procedure_fingerprint_directory: Path | str | None = None:
        A path to a directory where the fingerprint are meant to be stored in.
        If none given, this option is considered to be turned off.

    file_type_dir: Path | str | None = None:
        A path to a directory where the individual Sea-Bird file types are
        differentiated into respective directories.
        If none given, this option is considered to be turned off.

    verbose: bool = False:
        Sets whether the Sea-Bird modules are run silently or not.

    timeout: int = 60:
        The time in seconds after which individual processing steps will be
        killed automatically.

    Returns
    -------
    In auto_run mode, a .cnv file or an instance of CnvFile, depending on the
        file_type parameter inside of the configuration.
    Otherwise it is an invocation that collected and evaluated the information
        necessary to run a processing procedure on one or more target files.

    """

    def __init__(
        self,
        configuration: dict | Configuration,
        seabird_exe_directory: Path | str | None = None,
        available_hex_converters: list[str] = ["datcnv"],
        auto_run: bool = True,
        procedure_fingerprint_directory: Path | str | None = None,
        file_type_dir: Path | str | None = None,
        verbose: bool = False,
        timeout: int = 60,
    ) -> None:
        self.config = configuration
        if isinstance(configuration, Configuration):
            configuration = configuration.data
        self.available_hex_converters = available_hex_converters
        self.procedure_fingerprint_directory = procedure_fingerprint_directory
        self.file_type_dir = file_type_dir
        self.verbose = verbose
        self.timeout = timeout
        # perform thorough input check on the config, which is either loaded
        # from a toml file or generated from some code
        self.input_check(configuration)
        # set default exe dir, when none given
        if seabird_exe_directory is None:
            self.exe_directory = default_seabird_exe_path()
        else:
            self.exe_directory = Path(seabird_exe_directory)
        self.xmlcon = None
        if auto_run:
            self.run()

    def run(self, files: Path | str | list = []):
        """
        Runs given file(s) or uses the one(s) inside of the config.

        A 'run' consists of the application of all the given modules to all
        given files. It is the structure that can be represented by a
        fingerprint file.

        Parameters
        ----------
        files: Path | str | list :
            The input file(s).
             (Default value = [])
        """
        if not isinstance(files, list):
            self.input = [Path(files)]
            self.config["input"] = [str(file) for file in self.input]
        else:
            if len(files) > 0:
                self.input = [Path(file) for file in files]
        # check whether we are working on hexes or cnvs and react accordingly
        try:
            first_module = list(self.modules.keys())[0]
        except IndexError:
            return
        if first_module in self.available_hex_converters:
            # remove the first module information and only use it for the
            # conversion.
            hex_converter = self.modules.pop(first_module)
            # convert files to cnvs and continue working as usual
            self.cnvs = [
                self.convert(file, {first_module: hex_converter})
                for file in self.input
            ]
        else:
            self.cnvs = self.load_cnvs()
        self.go()
        self.procedure_fingerprint()

    def input_check(self, configuration: dict):
        """
        Thorough input/format check of the processing configuration, that
        either stems from a .toml config file, or is a self-build dictionary.
        Checks for the presence of certain keys, and then, depending on their
        importance, either fails or sets default values.

        Parameters
        ----------
        configuration: dict :
            The configuration information whose format will be checked.
        """
        try:
            # TODO: handle non list input
            self.input = [Path(file) for file in configuration["input"]]
        except KeyError:
            self.input = ["placeholder"]
        except TypeError as error:
            raise IncompleteConfigFile(
                f"Input information has a wrong format: {error}. Aborting."
            )
        try:
            self.psa_directory = configuration["psa_directory"]
        except KeyError:
            self.psa_directory = None
        if self.file_type_dir:
            self.output_dir = Path(self.file_type_dir).joinpath("cnv")
        else:
            try:
                self.output_dir = Path(configuration["output_dir"])
            except KeyError:
                self.output_dir = self.input[0].parent
        if not self.output_dir.exists():
            self.output_dir.mkdir(parents=True)
        try:
            self.output_name = configuration["output_name"]
        except KeyError:
            self.output_name = None
        try:
            self.output_type = configuration["output_type"]
        except KeyError:
            self.output_type = "cnv"
        try:
            self.modules = configuration["modules"].copy()
            assert isinstance(self.modules, dict)
            for module in list(self.modules.values()):
                assert isinstance(module, dict)
        except KeyError:
            raise IncompleteConfigFile(
                "No processing modules given. Aborting."
            )
        except AssertionError as error:
            raise IncompleteConfigFile(
                f"Module information is misconfigured: {error}. Aborting."
            )

    def load_cnvs(self) -> list[CnvFile]:
        """Creates CnvFile instances from the input file paths."""
        cnvs = []
        for file in self.input:
            try:
                cnvs.append(CnvFile(file))
            except Exception as error:
                logger.warning(error)
        return cnvs

    def is_seabird_module(self, module: dict) -> bool:
        """
        Answers the simple boolean question, whether the module in question is
        a seabird module or not.

        Does that by checking for the presence of a certain key 'psa'. All
        modules that are meant to run as a standalone executable should follow
        this principle and set their config file to the psa key.

        Parameters
        ----------
        module: dict :
            The specific module parameters.

        Returns
        -------

        """
        for key in list(module.keys()):
            if key == "psa":
                return True
        return False

    def create_seabird_module(self, module_info: dict) -> ProcessingModule:
        module_name = list(module_info.keys())[0]
        psa = Path(module_info[module_name]["psa"])
        if len(psa.parents) > 0 and not self.psa_directory:
            self.psa_directory = psa.parent
        module = ProcessingModule(
            name=module_name,
            exe_dir=self.exe_directory,
            psa_dir=self.psa_directory,
            psa_path=psa,
        )
        if "file_suffix" in module_info[module_name].keys():
            module.new_file_suffix = module_info[module_name]["file_suffix"]
        return module

    def create_seabird_step(
        self,
        module: ProcessingModule,
        input_path: Path | str,
    ) -> ProcessingStep:
        step = ProcessingStep(
            module=module,
            input_path=input_path,
            xmlcon_path=self.xmlcon,
            output_path=self.output_dir,
            verbose=self.verbose,
        )
        return step

    def convert(
        self,
        hex_path: Path,
        hex_converter: dict,
    ) -> CnvFile:
        """
        Covers the conversion of hex to cnv file.

        At the moment, this is simply done by using DatCnv, so we could just
        use the general Sea-Bird module pipeline. This is therefore meant to
        be future-compatible for a time where we might have developed other
        hex-converters.

        Parameters
        ----------
        hex_path: Path :
            The path to the target hex file.

        hex_converter: dict :
            The module parameters for the conversion.

        Returns
        -------

        """
        module = self.create_seabird_module(hex_converter)
        step = self.create_seabird_step(module, hex_path)
        step.run()
        try:
            cnv = CnvFile(self.output_dir.joinpath(hex_path.stem + ".cnv"))
        except FileNotFoundError:
            message = f"Failed to convert {hex_path}, using {list(hex_converter.keys())[0]}."
            sys.exit(message)
        else:
            self.xmlcon = step.xmlcon
            return cnv

    def new_file_path(self, file: Path) -> Path:
        """
        Creates the new output file path.

        Takes the file type directory or the given output directory and joins
        them with the given output name.

        Parameters
        ----------
        file: Path :
            The current path to the target file.

        Returns
        -------
        The new path to write the target file to.

        """
        new_name = self.output_name if self.output_name else file.name
        if self.file_type_dir:
            directory = Path(self.file_type_dir).joinpath("cnv")
            if not directory.exists():
                directory.mkdir(parents=True)
        else:
            directory = self.output_dir
        return directory.joinpath(new_name)

    def go(self) -> CnvFile | None:
        """
        Performs the processing on all target files.

        This is the 'main' method of the procedure. All previous methods
        prepare data for this method to then finally transform the input files
        into the wanted format.
        The main purpose of this method is the coordination of the two
        different forms of processing modules: standalone executables with
        config files, mainly Sea-Bird processing modules, and python-internal
        classes that implement the Module interface. The caveats are mainly
        the switching from one form to the other. This for example results in
        a in or out parsing of a CnvFile object.

        The output is controlled by self.output_type and is either a cnv file
        at a target path or a CnvFile object.
        """
        for cnv in self.cnvs:
            path_to_cnv = self.new_file_path(cnv.path_to_file)
            try:
                shutil.copy(cnv.path_to_file, path_to_cnv)
            except shutil.SameFileError:
                pass
            last_step = "first"
            for module_name, module_info in self.modules.items():
                module = {module_name.lower(): module_info}
                if self.is_seabird_module(module_info):
                    seabird_module = self.create_seabird_module(module)
                    step = self.create_seabird_step(
                        seabird_module, path_to_cnv
                    )
                    if last_step == "internal":
                        cnv.to_cnv(
                            file_name=path_to_cnv,
                            use_current_df=True,
                            use_current_processing_header=True,
                        )
                    step.run(timeout=self.timeout)
                    last_step = "seabird"
                else:
                    step = (
                        map_proc_name_to_class(module_name),
                        module_info,
                    )
                    own_module, parameters = step
                    if last_step == "seabird":
                        cnv = CnvFile(path_to_cnv)
                    cnv = own_module()(
                        input=cnv,
                        parameters=parameters,
                        name=module_name,
                    )
                    last_step = "internal"
            # handle output
            if not self.output_type == "cnv":
                return cnv
            else:
                if last_step == "internal":
                    cnv.to_cnv(
                        path_to_cnv,
                        True,
                        True,
                    )

    def procedure_fingerprint(self) -> Configuration | None:
        """
        Handles the creation of individual processing procedure fingerprints.

        A fingerprint is a 'receipt' of one invocation of this class to one or
        more target files or data. It shall serve the purpose of an easy to
        understand proof of what exactly has been done with the data to
        retreive the given result. The especially neat thing is, that they are
        at the very same time plain configuration files, allowing the easy
        re-running of processing procedures. What distinguishes them from the
        usual configuration files, is one, the exact target file list, that can
        be ommitted upon invocation, and a timestamp that prefixes the source
        file name and adheres to ISO 8601.
        """
        if self.procedure_fingerprint_directory is None:
            return
        # producing fingerprint that adheres to ISO 8601
        timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        directory = Path(self.procedure_fingerprint_directory).absolute()
        if not directory.exists():
            directory.mkdir(parents=True)
        if isinstance(self.config, dict):
            name = Path("processing_config.toml")
            config = Configuration(
                path=directory.joinpath(f"{timestamp}_{name}"),
                data=self.config,
            )
        else:
            config = self.config
            name = config.path.name
        config.write(directory.joinpath(f"{timestamp}_{name}"))
        return config
