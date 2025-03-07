"""
console application environment
===============================

an instance of the :class:`ConsoleApp` class is representing a python application with dynamically configurable logging,
debugging features (inherited from :class:`~ae.core.AppBase`), command line arguments and config files and options.

the helper function :func:`sh_exec` provided by this portion simplifies the execution of shell/console commands.


define command line arguments and options
-----------------------------------------

the methods :meth:`~ConsoleApp.add_argument` and :meth:`~ConsoleApp.add_option` are defining command line arguments and
:ref:`config options <config-options>`, finally parsed/loaded by calling :meth:`~ConsoleApp.run_app`::

    ca = ConsoleApp(app_title="command line arguments demo", app_version="3.6.9")
    ca.add_argument('argument_name_or_id', help="Help text for this command line argument")
    ca.add_option('option_name_or_id', "help text for this command line option", "default_value")
    ...
    ca.run_app()

the values of the commend line arguments and options are determined via the methods :meth:`~ConsoleApp.get_argument` and
:meth:`~ConsoleApp.get_option`. additional configuration values, stored in :ref:`INI/CFG files <config-files>`, are
accessible via the :meth:`~ConsoleApp.get_variable` method.


auto-collected app name, title and version
------------------------------------------

.. _app-title:
.. _app-version:

if one of the kwargs :paramref:`~ConsoleApp.app_title` or :paramref:`~ConsoleApp.app_version` is not specified in the
init call of the :class:`ConsoleApp` class instance, then they will automatically get determined from your app main
module: the app title from the docstring title, and the application version string from the `__version__` variable::

    \"\"\" module docstring title \"\"\"
    from ae.console import ConsoleApp

    __version__ = '1.2.3'

    ca = ConsoleApp()

    assert ca.app_title == "module docstring title"
    assert ca.app_version == '1.2.3'

.. _app-name:

:class:`ConsoleApp` also determines on instantiation the name/id of your application, if not explicitly specified in
:paramref:`~ConsoleApp.app_name`. other application environment vars/options (like e.g. the application startup folder
path and the current working directory path) will be automatically initialized and provided via the app instance.


configuration files, sections, variables and options
----------------------------------------------------

a config file consists of config sections, each section provides config variables and config options to parametrize your
application at run-time.

.. _config-files:

config files
^^^^^^^^^^^^

configuration files can be shared between apps or used exclusively by one app. the following file names are recognized
and loaded automatically on app initialization:

+----------------------------+---------------------------------------------------+
|  config file               |  used for .... config variables and options       |
+============================+===================================================+
| <any_path_name_and_ext>    |  application/domain specific                      |
+----------------------------+---------------------------------------------------+
| <app_name>.ini             |  application specific (read-/write-able)          |
+----------------------------+---------------------------------------------------+
| <app_name>.cfg             |  application specific (read-only)                 |
+----------------------------+---------------------------------------------------+
| .app_env.cfg               |  application/suite specific (read-only)           |
+----------------------------+---------------------------------------------------+
| .sys_env.cfg               |  general system (read-only)                       |
+----------------------------+---------------------------------------------------+
| .sys_env<SYS_ENV_ID>.cfg   |  the system with SYS_ID (read-only)               |
+----------------------------+---------------------------------------------------+

the above table is ordered by the preference to search/get the value of a config variable/option. so the values stored
in the domain/app specific config file will always precede/overwrite any application and system specific values.

app/domain-specific config files have to be specified explicitly, either on initialization of the :class:`ConsoleApp`
instance via the kwarg :paramref:`~ConsoleApp.__init__.additional_cfg_file`, or by calling the method
:meth:`~ConsoleApp.add_cfg_files`. they can have any file extension and can be placed into any accessible folder.

all the other config files have to have the specified name with a `.ini` or `.cfg` file extension, and get recognized in
the current working directory, in the user data directory (see :func:`ae.paths.user_data_path`) and in the application
installation directory.

.. _config-sections:

config sections
^^^^^^^^^^^^^^^

this module is supporting the `config file format <https://en.wikipedia.org/wiki/INI_file>`_ of Pythons built-in
:class:`~configparser.ConfigParser` class, extended by more complex config value types. the following examples shows a
config file with two config sections containing one config option (named `log_file`) and two config variables
(`configVar1` and `configVar2`)::

    [aeOptions]
    log_file = './logs/your_log_file.log'
    configVar1 = ['list-element1', ('list-element2-1', 'list-element2-2', ), {}]

    [YourSectionName]
    configVar2 = {'key1': 'value 1', 'key2': 2222, 'key3': datetime.datetime.now()}

.. _config-main-section:

the config section `aeOptions` (defined by :data:`MAIN_SECTION_NAME`) is the default or main section, storing the values
of any pre-defined :ref:`config option <config-options>` and of some :ref:`config variables <config-variables>`.

.. _config-variables:

config variables
^^^^^^^^^^^^^^^^

config variables can store complex data types. in the example config file above the config variable `configVar1` holds a
list with 3 elements: the first element is a string, the second element a tuple, and the third element an empty dict.

all the values, of which its `repr` string can be evaluated with the built-in :func:`eval` function, can be stored in
a config variable, by calling the :meth:`~ConsoleApp.set_variable` method. to read/fetch their value, call the method
:meth:`~ConsoleApp.get_variable` with the name and section names of the config variable. you can specify the type of an
config variable via the value passed into :paramref:`~ConsoleApp.add_option.value` argument or by the
see :attr:`special encapsulated strings <ae.literal.Literal.value>`, respectively the config value literal.

the following config variables are pre-defined in the :ref:`main config section <config-main-section>` and recognized by
:mod:`this module <.console>`, some of them also by the module/portion :mod:`ae.core`:

* `debug_level`: debug logging verbosity level :ref:`config option <config-options>`
* `log_file`: ae logging file name (this is also a :ref:`config option <config-options>` - set-able as command line arg)
* `logging_params`: :meth:`general ae logging configuration parameters (py and ae logging) <.core.AppBase.init_logging>`
* `py_logging_params`: `python logging configuration
  <https://docs.python.org/3.6/library/logging.config.html#logging.config.dictConfig>`_
* `registered_users`: list of registered user names/ids (extended by calls of :meth:`ConsoleApp.register_user` method)
* `user_id`: id of the app user (default is the `operating system user name <ae.base.os_user_name>`)
* `user_specific_cfg_vars`: list of config variables storing an individual value for each registered user (see
  section :ref:`user-specific-config-variables`)

.. note::
  the value of a config variable can be overwritten by defining an OS environment variable with a name that is equal to
  the :func:`snake+upper-case converted names <ae.base.env_str>` of the config-section and -variable. e.g. declare an OS
  environment variable with the name `AE_OPTIONS_LOG_FILE` to overwrite the value of the
  :ref:`pre-defined config option/variable <pre-defined-config-options>` `log_file`.


.. _config-options:

config options
^^^^^^^^^^^^^^

config options are config variables, defined persistently in the config section :data:`aeOptions <MAIN_SECTION_NAME>`.
specifying them on the command line, preceding the option name with two leading hyphen characters, and using an equal
character between the name and the option value, overwrites the value stored in the config file::

    $ your_application --log_file='your_new_log_file.log'

the default value of a not specified config option gets searched first in the config files (the exact search order is
documented in the doc-string of the method :meth:`~ConsoleApp.add_cfg_files`), or if not found then the default value
will be used, that is specified in the definition of the config option (the call of :meth:`~ConsoleApp.add_option`).

the method :meth:`~ConsoleApp.get_option` determines the value of a config option::

    my_log_file_name = ca.get_option('log_file')

use the :meth:`~ConsoleApp.set_option` if you want to change the value of a configuration option at run-time. to read
the default value of a config option or variable directly from the available configuration files use the method
:meth:`~ConsoleApp.get_variable`. the default value of a config option or variable can also be set or changed directly
from within your application by calling the :meth:`~ConsoleApp.set_variable` method.

.. _pre-defined-config-options:

pre-defined configuration options
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

for a more verbose logging to the console output specify, either on the command line or in a config files, the config
option `debug_level` (or as short option `-D`) with a value of 2 (for verbose). the supported config option values are
documented :data:`here <.core.DEBUG_LEVELS>`.

the value of the second pre-defined config option `log_file` specifies the log file path/file_name. also this option can
be abbreviated on the command line with the short `-L` option id.

.. note::
    after an explicit definition of the optional config option `user_id` via :meth:`~ConsoleApp.add_option` it will be
    automatically used to initialize the :attr:`~ConsoleApp.user_id` attribute.

.. _user-specific-config-variables:

user specific config variables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

config variables specified in the set :attr:`~ConsoleApp.user_specific_cfg_vars` get automatically recognized as
user-specific. override the method :meth`~ConsoleApp._init_default_user_cfg_vars` in your main app instance to define or
revoke which config variables the app is storing individually for each user.

.. hint::
    to permit individual sets of user-specific config variables for a user (or group) add the config variable
    `user_specific_cfg_vars` in the user-specific config file section(s). don't forget in this special case to also add
    there also this config variable, e.g. as `('aeOptions', 'user_specific_cfg_vars')`.
"""
import os
import datetime
import shlex
import subprocess
import threading

from typing import Any, Callable, Iterable, Optional, Sequence, Type, Union
from configparser import ConfigParser, NoSectionError
from argparse import ArgumentParser, ArgumentError, HelpFormatter, Namespace

from ae.base import (                                                                       # type: ignore
    CFG_EXT, DATE_TIME_ISO, DATE_ISO, INI_EXT, UnsetType, UNSET,
    dummy_function, env_str, instantiate_config_parser, norm_name, os_path_isfile, os_path_join,
    os_user_name, sys_env_dict, sys_env_text)
from ae.paths import PATH_PLACEHOLDERS, normalize, Collector  # type: ignore
# noinspection PyProtectedMember
from ae.core import (                                                                       # type: ignore  # for mypy
    DEBUG_LEVEL_VERBOSE, DEBUG_LEVELS, main_app_instance, ori_std_out, _LOGGER as APP_LOGGER, AppBase)
from ae.literal import Literal                                                              # type: ignore


__version__ = '0.3.80'


MAIN_SECTION_NAME: str = 'aeOptions'            #: default name of main config section

STDERR_BEG_MARKER = "vvv   STDERR   vvv"        #: begin of stderr lines in :paramref:`ae.console.sh_exec.lines_output`
STDERR_END_MARKER = "^^^   STDERR   ^^^"        #: end of stderr lines in :paramref:`ae.console.sh_exec.lines_output`

USER_NAME_MAX_LEN = 12                          #: maximum length of a `username/id <ae.console.ConsoleApp.user_id>`


config_lock = threading.RLock()                 # lock to prevent errors in config var value changes and reloads/reads


def config_value_string(value: Any) -> str:
    """ convert passed value to a string to store them in a config/ini file.

    :param value:               value to convert to ini variable string/literal.
    :return:                    ini variable literal string.

    .. note::
        :class:`~ae.literal.Literal` converts the returned string format back into the representing value.
    """
    if isinstance(value, datetime.datetime):
        str_val = value.strftime(DATE_TIME_ISO)
    elif isinstance(value, datetime.date):
        str_val = value.strftime(DATE_ISO)
    else:
        str_val = repr(value)
    return str_val.replace('%', '%%')


def sh_exec(command_line: str, extra_args: Sequence = (), console_input: str = "",
            lines_output: Optional[list[str]] = None, cae: Optional[Any] = None, shell: bool = False,
            env_vars: Optional[dict[str, str]] = None) -> int:
    """ execute command in the current working directory of the OS console/shell.

    :param command_line:        command line string to execute on the console/shell. could contain command line args
                                separated by whitespace characters (alternatively use :paramref:`~sh_exec.extra_args`).
    :param extra_args:          optional sequence of extra command line arguments.
    :param console_input:       optional string to be sent to the stdin stream of the console/shell.
    :param lines_output:        optional list to be extended with the lines printed to stdout/stderr on execution.
                                by passing an empty list the stdout and stderr streams/pipes will be separated,
                                resulting in having the stderr output lines at the end of the list, enclosed by
                                the list items :data:`STDERR_BEG_MARKER` and :data:`STDERR_END_MARKER`.
    :param cae:                 optional :class:`~ae.console.ConsoleApp` instance, only used for logging. to suppress
                                any logging output pass :data:`~ae.base.UNSET`.
    :param shell:               pass True to execute command in the default OS shell (see :meth:`subprocess.run`).
    :param env_vars:            OS shell environment variables to be used instead of the console/bash defaults.
    :return:                    return code of the executed command or 126 if execution raised any other exception.
    """
    args = command_line + " " + " ".join(extra_args) if shell else shlex.split(command_line) + list(extra_args)
    ret_out = lines_output is not None  # == isinstance(lines_output, list)
    merge_err = bool(lines_output)      # == -''- and len(lines_output) > 0
    print_out = cae.po if cae else print if cae is None else dummy_function
    debug_out = cae.dpo if cae else dummy_function
    debug_out(f"    # executing at {os.getcwd()}: {args}")

    result: Union[subprocess.CompletedProcess, subprocess.CalledProcessError]   # having: stdout/stderr/returncode
    try:
        result = subprocess.run(args,
                                stdout=subprocess.PIPE if ret_out else None,
                                stderr=subprocess.STDOUT if merge_err else subprocess.PIPE if ret_out else None,
                                input=console_input.encode(),
                                check=True,
                                shell=shell,
                                env=env_vars)
    except subprocess.CalledProcessError as ex:                                             # pragma: no cover
        debug_out(f"****  subprocess.run({args=}) returned non-zero exit code {ex.returncode}; {ex=}")
        result = ex
    except Exception as ex:
        print_out(f"****  subprocess.run({args}) raised exception {ex}")
        return 126

    if ret_out:
        assert isinstance(lines_output, list), "silly mypy doesn't recognize ret_out"
        if result.stdout:
            lines_output.extend([line for line in result.stdout.decode().split(os.linesep) if line])
        if not merge_err and result.stderr:
            lines_output.append(STDERR_BEG_MARKER)
            lines_output.extend([line for line in result.stderr.decode().split(os.linesep) if line])
            lines_output.append(STDERR_END_MARKER)

    return result.returncode


class ConsoleApp(AppBase):
    """ provides command line arguments and options, config options, logging and debugging for your application.

    most applications only need a single instance of this class. each instance is encapsulating a ConfigParser and
    a ArgumentParser instance. so only apps with threads and different sets of config options for each
    thread could create a separate instance of this class.

    instance attributes (ordered alphabetically - ignoring underscore characters):

    * :attr:`_arg_parser`           ArgumentParser instance.
    * :attr:`cfg_opt_choices`       valid choices for pre-/user-defined options.
    * :attr:`cfg_opt_eval_vars`     additional dynamic variable values that are getting set via
      the :paramref:`~.ConsoleApp.cfg_opt_eval_vars` argument of the method :meth:`ConsoleApp.__init__`
      and get then used in the evaluation of :ref:`evaluable config option values <evaluable-literal-formats>`.
    * :attr:`_cfg_files`            iterable of config file names that are getting loaded and parsed (specify
      additional configuration/INI files via the :paramref:`~ConsoleApp.additional_cfg_files` argument).
    * :attr:`cfg_options`           pre-/user-defined options (dict of :class:`~.literal.Literal` instances defined
      via :meth:`~ConsoleApp.add_option`).
    * :attr:`_cfg_opt_val_stripper` callable to strip option values.
    * :attr:`_cfg_parser`           ConfigParser instance.
    * :attr:`_main_cfg_fnam`        main config file name.
    * :attr:`_main_cfg_mod_time`    last modification datetime of main config file.
    * :attr:`_parsed_arguments`     ArgumentParser.parse_args() return.
    """
    def __init__(self, app_title: str = '', app_name: str = '', app_version: str = '', sys_env_id: str = '',
                 debug_level: int = DEBUG_LEVEL_VERBOSE, multi_threading: bool = False, suppress_stdout: bool = False,
                 cfg_opt_eval_vars: Optional[dict] = None, additional_cfg_files: Iterable = (),
                 cfg_opt_val_stripper: Optional[Callable] = None,
                 formatter_class: Optional[Any] = None, epilog: str = "",
                 **logging_params):
        """ initialize a new :class:`ConsoleApp` instance.

        :param app_title:               application title/description to set the instance attribute
                                        :attr:`~ae.core.AppBase.app_title`.

                                        if not specified then the docstring of your app's main module will
                                        be used (see :ref:`example <app-title>`).

        :param app_name:                application instance name to set the instance attribute
                                        :attr:`~ae.core.AppBase.app_name`.

                                        if not specified then base name of the main module file name will be used.

        :param app_version:             application version string to set the instance attribute
                                        :attr:`~ae.core.AppBase.app_version`.

                                        if not specified then value of a global variable with the name __version__` will
                                        be used (:ref:`if declared in the actual call stack <app-version>`).

        :param sys_env_id:              system environment id to set the instance attribute
                                        :attr:`~ae.core.AppBase.sys_env_id`.

                                        this value is also used as file name suffix to load all
                                        the system config variables in sys_env<suffix>.cfg. pass e.g. 'LIVE'
                                        to init this ConsoleApp instance with config values from sys_envLIVE.cfg.

                                        the default value of this argument is an empty string.

                                        .. note::
                                          if the argument value results as empty string then the value of the
                                          optionally defined OS environment variable `AE_OPTIONS_SYS_ENV_ID`
                                          will be used as default.

        :param debug_level:             default debug level to set the instance attribute
                                        :attr:`~ae.core.AppBase.debug_level`.

                                        the default value of this argument is :data:`~ae.core.DEBUG_LEVEL_DISABLED`.

        :param multi_threading:         pass True if instance is used in multi-threading app.

        :param suppress_stdout:         pass True (for wsgi apps) to prevent any python print outputs to stdout.

        :param cfg_opt_eval_vars:       dict of additional application specific data values that are used in eval
                                        expressions (e.g. AcuSihotMonitor.ini).

        :param additional_cfg_files:    iterable of additional CFG/INI file names (opt. incl. abs/rel. path).

        :param cfg_opt_val_stripper:    callable to strip/reformat/normalize the option choices values.

        :param formatter_class:         alternative formatter class passed onto ArgumentParser instantiation.

        :param epilog:                  optional epilog text for command line arguments/options help text (passed
                                        onto ArgumentParser instantiation).

        :param logging_params:          all other kwargs are interpreted as logging configuration values - the
                                        supported kwargs are all the method kwargs of
                                        :meth:`~.core.AppBase.init_logging`.
        """
        self._user_id = ''
        if not sys_env_id:
            sys_env_id = env_str(MAIN_SECTION_NAME + '_sys_env_id', convert_name=True) or ''

        super().__init__(app_title=app_title, app_name=app_name, app_version=app_version, sys_env_id=sys_env_id,
                         debug_level=debug_level, multi_threading=multi_threading, suppress_stdout=suppress_stdout)

        with config_lock:       # prepare config parser and the config files, including the main config file to write to
            self._cfg_parser = instantiate_config_parser()                  #: ConfigParser instance
            self.cfg_options: dict[str, Literal] = {}                       #: all config options
            self.cfg_opt_choices: dict[str, Iterable] = {}                  #: all valid config option choices
            self.cfg_opt_eval_vars: dict = cfg_opt_eval_vars or {}          #: app-specific vars for init of cfg options

            self._cfg_files: list = []                                      #: specified/added INI/CFG file paths
            self._main_cfg_fnam: str = os_path_join(os.getcwd(), self.app_name + INI_EXT)
            """ default main config file <app_name>.INI in the cwd (possibly overwritten by :meth:`.load_cfg_files) """
            self._main_cfg_mod_time: float = 0.0                            #: main config file modification datetime
            warn_msg = self.add_cfg_files(*additional_cfg_files)
            if warn_msg:
                self.dpo(f"ConsoleApp.__init__(): config files collection warning: {warn_msg}")
            self._cfg_opt_val_stripper: Optional[Callable] = cfg_opt_val_stripper
            """ callable to strip or normalize config option choice values """

            self._parsed_arguments: Optional[Namespace] = None
            """ storing returned namespace of ArgumentParser.parse_args() call, used to retrieve command line args """

        self.load_cfg_files()

        self.registered_users: list[str] = []
        self.user_specific_cfg_vars: set[tuple[str, str]] = set()
        self._init_default_user_cfg_vars()
        self.load_user_cfg()

        self._debug_level = self.get_var('debug_level', default_value=debug_level)

        log_file_name = self._init_logging(logging_params)

        self.dpo(self.app_name, "      startup", self.startup_beg, self.app_title, logger=APP_LOGGER)
        self.dpo(f"####  {self.app_key} initialization......  ####", logger=APP_LOGGER)

        # prepare argument parser
        if not formatter_class:
            formatter_class = HelpFormatter
        self._arg_parser: ArgumentParser = ArgumentParser(
            description=self.app_title, epilog=epilog, formatter_class=formatter_class)   #: ArgumentParser instance
        # changed to pass mypy checks (current workarounds are use setattr or add type: ignore:
        # self.add_argument = self._arg_parser.add_argument       #: redirect this method to our ArgumentParser instance
        setattr(self, 'add_argument', self._arg_parser.add_argument)

        # create pre-defined config options
        self.add_option('debug_level', "Verbosity of debug messages send to console and log files",
                        self._debug_level, 'D', choices=DEBUG_LEVELS.keys())
        if log_file_name is not None:
            self.add_option('log_file', "Log file path", log_file_name, 'L')

    def _init_default_user_cfg_vars(self):
        """ init user default config variables.

        override this method to add module-/app-specific config vars that can be set individually per user.
        """
        self.user_specific_cfg_vars |= {(MAIN_SECTION_NAME, 'debug_level')}

    def _init_logging(self, logging_params: dict[str, Any]) -> Optional[str]:
        """ determine and init logging config.

        :param logging_params:      logging config dict passed as args by user that will be amended with cfg values.
        :return:                    None if py logging is active, log file name if ae logging is set in cfg or args
                                    or empty string if no logging got configured in cfg/args.

        the logging configuration can be specified in several alternative places. the precedence
        on various existing configurations is (the highest precedence first):

        * :ref:`log_file  <pre-defined-config-options>` :ref:`configuration option <config-options>` specifies
          the name of the used ae log file (will be read after initialisation of this app instance)
        * `logging_params` :ref:`configuration variable <config-variables>` dict with a `py_logging_params` key
          to activate python logging
        * `logging_params` :ref:`configuration variable <config-variables>` dict with the ae log file name
          in the key `log_file_name`
        * `py_logging_params` :ref:`configuration variable <config-variables>` to use the python logging module
        * `log_file` :ref:`configuration variable <config-variables>` specifying ae log file
        * :paramref:`~_init_logging.logging_params` dict passing the python logging configuration in the
          key `py_logging_params` to this method
        * :paramref:`~_init_logging.logging_params` dict passing the ae log file in the logging
          key `log_file_name` to this method

        """
        log_file_name = ""

        cfg_logging_params = self.get_var('logging_params')
        if cfg_logging_params:
            logging_params = cfg_logging_params
            if 'py_logging_params' not in logging_params:                   # .. there then cfg py_logging params
                log_file_name = logging_params.get('log_file_name', '')     # .. then cfg logging_params log file

        if 'py_logging_params' not in logging_params and not log_file_name:
            lcd = self.get_var('py_logging_params')
            if lcd:
                logging_params['py_logging_params'] = lcd                   # .. then cfg py_logging params directly
            else:
                log_file_name = self.get_var('log_file', default_value=logging_params.get('log_file_name'))
                logging_params['log_file_name'] = log_file_name             # .. finally cfg log_file / log file arg

        if logging_params.get('log_file_name'):                             # if log file path: replace placeholders
            logging_params['log_file_name'] = normalize(logging_params['log_file_name'])

        super().init_logging(**logging_params)

        return None if 'py_logging_params' in logging_params else log_file_name

    def __del__(self):
        """ deallocate this app instance by calling :func:`ae.core.AppBase.shutdown`. """
        self.shutdown(exit_code=None)

    @AppBase.debug_level.setter
    def debug_level(self, debug_level):
        """ overwriting AppBase setter to update also the `debug_level` config option. """
        self._debug_level = debug_level
        if self.get_opt('debug_level') != debug_level:
            self.set_opt('debug_level', debug_level)

    # methods to process command line options and config files

    def add_cfg_files(self, *additional_cfg_files: str) -> str:
        """ extend list of available and additional config files (in :attr:`~ConsoleApp._cfg_files`).

        :param additional_cfg_files:    domain/app-specific config file names to be defined/registered additionally.
        :return:                        empty string on success else line-separated list of error message text.

        underneath the search order of the config files variable value - the first found one will be returned:

        #. the domain/app-specific :ref:`config files <config-files>` added in your app code by this method. these files
           will be searched for the config option value in reversed order - so the last added
           :ref:`config file <config-files>` will be the first one where the config value will be searched.
        #. :ref:`config files <config-files>` added via :paramref:`~ConsoleApp.additional_cfg_files` argument of
           :meth:`ConsoleApp.__init__` (searched in the reversed order).
        #. <app_name>.INI file in the <app_dir>
        #. <app_name>.CFG file in the <app_dir>
        #. <app_name>.INI file in the <usr_dir>
        #. <app_name>.CFG file in the <usr_dir>
        #. <app_name>.INI file in the <cwd>
        #. <app_name>.CFG file in the <cwd>
        #. .sys_env.cfg in the <app_dir>
        #. .sys_env<sys_env_id>.cfg in the <app_dir>
        #. .app_env.cfg in the <app_dir>
        #. .sys_env.cfg in the <usr_dir>
        #. .sys_env<sys_env_id>.cfg in the <usr_dir>
        #. .app_env.cfg in the <usr_dir>
        #. .sys_env.cfg in the <cwd>
        #. .sys_env<sys_env_id>.cfg in the <cwd>
        #. .app_env.cfg in the <cwd>
        #. .sys_env.cfg in the parent folder of the <cwd>
        #. .sys_env<sys_env_id>.cfg in the parent folder of the <cwd>
        #. .app_env.cfg in the parent folder of the <cwd>
        #. .sys_env.cfg in the parent folder of the parent folder of the <cwd>
        #. .sys_env<sys_env_id>.cfg in the parent folder of the parent folder of the <cwd>
        #. .app_env.cfg in the parent folder of the parent folder of the <cwd>
        #. value argument passed into the add_opt() method call (defining the option)
        #. default_value argument passed into this method (only if :class:`~ConsoleApp.add_option` didn't get called)

        **legend of the placeholders in the above search order lists** (see also :data:`ae.paths.PATH_PLACEHOLDERS`):

        * *<cwd>* is the current working directory of your application (determined with :func:`os.getcwd`)
        * *<app_name>* is the base app name without extension of your main python code file.
        * *<app_dir>* is the application data directory (APPDATA/<app_name> in Windows, ~/.config/<app_name> in Linux).
        * *<usr_dir>* is the user data directory (APPDATA in Windows, ~/.config in Linux).
        * *<sys_env_id>* is the specified argument of :meth:`ConsoleApp.__init__`.

        """
        std_search_paths = ("{cwd}", "{usr}", "{ado}", )    # reversed - latter config file var overwrites former
        coll = Collector(main_app_name=self.app_name)
        coll.collect("{cwd}/../..", "{cwd}/..", *std_search_paths,
                     append=(".app_env" + CFG_EXT,
                             ".sys_env" + CFG_EXT,
                             ".sys_env" + (self.sys_env_id or "TEST") + CFG_EXT,),
                     only_first_of=())
        coll.collect(*std_search_paths, append=("{app_name}" + CFG_EXT, "{app_name}" + INI_EXT), only_first_of=())
        if additional_cfg_files:
            coll.collect(*std_search_paths, select=additional_cfg_files, only_first_of=())

        self._cfg_files.extend(coll.files)

        return "\n".join(f"config file {fnam} not found ({count} times)!" for fnam, count in coll.suffix_failed.items())

    def cfg_section_variable_names(self, section: str, cfg_parser: Optional[ConfigParser] = None) -> tuple[str, ...]:
        """ determine current config variable names/keys of the passed config file section.

        :param section:         config file section name.
        :param cfg_parser:      ConfigParser instance to use (def=self._cfg_parser).
        :return:                tuple of all config variable names.
        """
        try:                                # quicker than asking before with: if cfg_parser.has_section(section):
            with config_lock:
                return tuple((cfg_parser or self._cfg_parser).options(section))
        except NoSectionError:
            self.vpo(f"   ## ConsoleApp.cfg_section_variable_names: ignoring missing config file section {section}")
            return tuple()

    def _get_cfg_parser_val(self, name: str, section: str,
                            default_value: Optional[Any] = None,
                            cfg_parser: Optional[ConfigParser] = None) -> Any:
        """ determine thread-safe the value of a config variable from the config file.

        :param name:            name/option_id of the config variable.
        :param section:         name of the config section.
        :param default_value:   default value to return if config value is not specified in any config file.
        :param cfg_parser:      ConfigParser instance to use (def=self._cfg_parser).
        :return:                config var value. str values enclosed in single high commas will be returned without
                                high commas. code block and multiline-strings enclosed in tripple high-commas will be
                                returned with the high-commas.
        """
        with config_lock:
            cfg_parser = cfg_parser or self._cfg_parser
            val = cfg_parser.get(section, name, fallback=default_value)
            if isinstance(val, str):
                val = val.replace('%%', '%')            # revert mask of %-char done in :func:`config_value_str`
        return val

    def load_cfg_files(self, config_modified: bool = True):
        """  (re)load and parse all config files.

        :param config_modified:     pass False to prevent the refresh/overwrite the initial config file modified date.
        """
        with config_lock:
            for cfg_fnam in reversed(self._cfg_files):
                if cfg_fnam.endswith(INI_EXT) and os_path_isfile(cfg_fnam):
                    self._main_cfg_fnam = cfg_fnam
                    if config_modified:
                        self._main_cfg_mod_time = os.path.getmtime(cfg_fnam)
                    break

            self._cfg_parser = instantiate_config_parser()      # new instance needed in case of renamed config var
            self._cfg_parser.read(self._cfg_files, encoding='utf-8')

    def is_main_cfg_file_modified(self) -> bool:
        """ determine if main config file got modified.

        :return:    True if the content of the main config file got modified/changed.
        """
        with config_lock:
            return os.path.getmtime(self._main_cfg_fnam) > self._main_cfg_mod_time \
                if self._main_cfg_fnam and self._main_cfg_mod_time else False

    def get_variable(self, name: str, section: Optional[str] = None, default_value: Optional[Any] = None,
                     cfg_parser: Optional[ConfigParser] = None, value_type: Optional[Type] = None) -> Any:
        """ get value of :ref:`config option <config-options>`, OS environ or :ref:`config variable <config-variables>`.

        :param name:            name of a :ref:`config option <config-options>` or of an existing/declared
                                :ref:`config variable <config-variables>`.
        :param section:         name of the :ref:`config section <config-sections>`. defaulting to the app options
                                section (:data:`MAIN_SECTION_NAME`) if not specified or if None or empty string passed.
                                if :paramref:`~get_variable.name` specifies a user-specific config option then its
                                value will get retrieved from the user-specific section (section name gets then
                                extended with help of the :meth:`.user_section` method).
        :param default_value:   default value to return if config value is not specified in any config file.
        :param cfg_parser:      optional ConfigParser instance to use (def= :attr:`~ConsoleApp._cfg_parser`).
        :param value_type:      optional type of the config value. only used for :ref:`config-variables` and
                                ignored for :ref:`config-options`.
        :return:                variable value which will be searched in the :ref:`config-options`, the OS environment
                                and in the :ref:`config-variables` in the following order and manner:

                                * **config option** with a name equal to the :paramref:`~get_variable.name` argument
                                  (only if the passed :paramref:`~get_variable.section` value is either empty,
                                  None or equal to :data:`MAIN_SECTION_NAME`).
                                * **user-specific OS environment variable** with a matching snake+upper-cased name,
                                  compiled from the :paramref:`~get_variable.section` argument, the string 'usr_id',
                                  the :attr:`~ConsoleApp.user_id` and :paramref:`~get_variable.name` argument,
                                  and all four parts separated by an underscore character.
                                * **OS environment variable** with a matching snake+upper-cased name, compiled from
                                  the :paramref:`~get_variable.section` and :paramref:`~get_variable.name` arguments,
                                  separated by an underscore character.
                                * **config variable** with a name and section equal to the values passed into
                                  the :paramref:`~get_variable.name` and :paramref:`~get_variable.section` arguments.

                                if no variable could be found then a None value will be returned.

        this method has an alias named :meth:`get_var`.
        """
        section = section or MAIN_SECTION_NAME
        if name in self.cfg_options and section == MAIN_SECTION_NAME:
            val = self.cfg_options[name].value

        else:
            if name != 'user_id':
                sec = self.user_section(section, name)
                val = env_str(sec + '_' + name, convert_name=True)
            else:
                sec = section
                val = None
            if val is None:
                val = env_str(section + '_' + name, convert_name=True)

            if val is None:
                lit = Literal(literal_or_value=default_value, value_type=value_type, name=name)  # used for convert/eval
                lit.value = self._get_cfg_parser_val(name, section=sec, default_value=lit.value, cfg_parser=cfg_parser)
                val = lit.value

        return val

    get_var = get_variable      #: alias of method :meth:`.get_variable`

    def set_variable(self, name: str, value: Any, cfg_fnam: Optional[str] = None, section: Optional[str] = None,
                     old_name: str = '') -> str:
        """ set/change the value of a :ref:`config variable <config-variables>` and if exists the related config option.

        if the passed string in :paramref:`~set_variable.name` is the id of a defined
        :ref:`config option <config-options>` and :paramref:`~set_variable.section` is either empty or
        equal to the value of :data:`MAIN_SECTION_NAME` then the value of this
        config option will be changed too.

        if the section does not exist it will be created (in contrary to Pythons ConfigParser).

        :param name:            name/option_id of the config value to set.
        :param value:           value to assign to the config value, specified by the
                                :paramref:`~set_variable.name` argument.
        :param cfg_fnam:        file name (def= :attr:`~ConsoleApp._main_cfg_fnam`) to save the new option value to.
        :param section:         name of the :ref:`config section <config-sections>`. defaulting to the app options
                                section (:data:`MAIN_SECTION_NAME`) if not specified or if None or empty string passed.
        :param old_name:        old name/option_id that has to be removed (used to rename config option name/key).
        :return:                empty string on success else error message text.

        this method has an alias named :meth:`set_var`.
        """
        msg = f"****  ConsoleApp.set_variable({name=!r}, {value=!r}) "
        cfg_fnam = cfg_fnam or self._main_cfg_fnam
        section = section or MAIN_SECTION_NAME
        if section == MAIN_SECTION_NAME:
            self._change_option(name, value)
        if name != 'user_id':
            section = self.user_section(section, name)

        if not cfg_fnam or not os_path_isfile(cfg_fnam):
            return msg + f"INI/CFG file {cfg_fnam} not found." \
                         f" Please set the ini/cfg variable {section}/{name} manually to the value {value!r}"

        err_msg = ''
        with config_lock:
            try:
                cfg_parser = instantiate_config_parser()
                cfg_parser.read(cfg_fnam)

                if not cfg_parser.has_section(section):
                    cfg_parser.add_section(section)
                cfg_parser.set(section, name, config_value_string(value))
                if old_name:
                    cfg_parser.remove_option(section, old_name)
                with open(cfg_fnam, 'w') as configfile:
                    cfg_parser.write(configfile)

                # refresh self._config_parser cache in case the written var is in one of our already loaded config files
                # .. while keeping the initial modified date untouched
                self.load_cfg_files(config_modified=False)
                self.load_user_cfg()  # reload in case a user config variable got changed

            except Exception as ex:
                err_msg = msg + f"exception: {ex}"

        return err_msg

    set_var = set_variable  #: alias of method :meth:`.set_variable`

    def del_section(self, section: str, cfg_fnam: Optional[str] = None):
        """ delete section from the main or the specified config file.

        :param section:         name of the :ref:`config section <config-sections>` to delete/remove.
        :param cfg_fnam:        optional path/name of the config file (def= :attr:`~ConsoleApp._main_cfg_fnam`).
        :return:                empty string on success else error message text.
        """
        msg = f"****  ConsoleApp.del_section({section=}, {cfg_fnam=}) "
        cfg_fnam = cfg_fnam or self._main_cfg_fnam
        if not cfg_fnam or not os_path_isfile(cfg_fnam):
            return msg + f"INI/CFG file {cfg_fnam} not found."

        err_msg = ''
        with config_lock:
            try:
                cfg_parser = instantiate_config_parser()
                cfg_parser.read(cfg_fnam)

                assert cfg_parser.remove_section(section), f"{section=} not found in {cfg_fnam=}"

                with open(cfg_fnam, 'w') as configfile:
                    cfg_parser.write(configfile)
                self.load_cfg_files(config_modified=False)
                self.load_user_cfg()

            except Exception as ex:
                err_msg = msg + f"exception: {ex}"

        return err_msg

    def add_argument(self, *args, **kwargs):
        """ define new command line argument.

        original/underlying args/kwargs of :class:`argparse.ArgumentParser` are used - please see the
        description/definition of :meth:`~argparse.ArgumentParser.add_argument`.

        this method has an alias named :meth:`add_arg`.
        """
        # ### THIS METHOD DEF GOT CODED HERE ONLY FOR SPHINX DOCUMENTATION BUILD PURPOSES ###
        # .. this method get never called because gets overwritten with self._arg_parser.add_argument in __init__().
        self._arg_parser.add_argument(*args, **kwargs)  # pragma: no cover - will never be executed

    add_arg = add_argument      #: alias of method :meth:`.add_argument`

    def get_argument(self, name: str) -> Any:
        """ determine the command line parameter value.

        :param name:    argument id of the parameter.
        :return:        value of the parameter.

        this method has an alias named :meth:`get_arg`.
        """
        if not self._parsed_arguments:
            self.parse_arguments()
            self.vpo("ConsoleApp.get_argument call before explicit command line args parsing (run_app call missing)")
        return getattr(self._parsed_arguments, name)

    get_arg = get_argument      #: alias of method :meth:`.get_argument`

    def add_option(self, name: str, desc: str, value: Any,
                   short_opt: Union[str, UnsetType] = '', choices: Optional[Iterable] = None, multiple: bool = False):
        """ defining and adding a new config option for this app.

        :param name:        string specifying the option id and short description of this new option.
                            the name value will also be available as long command line argument option (case-sens.).
        :param desc:        description and command line help string of this new option.
        :param value:       default value and type of the option. returned by :meth:`.get_option` if this option
                            is not specified as command line argument nor exists as config variable in any config file.
                            pass `UNSET` to define a boolean flag option, specified without a value on the command line.
                            the resulting value will be `True` if the option will be specified on the command line, else
                            `False`. specifying a value on the command line results in a `SystemExit` on parsing.
        :param short_opt:   short option character. if not passed or passed as '' then the first character of the name
                            will be used. passing `UNSET` or `None` prevents the declaration of a short option. please
                            note that the short options 'h', 'D' and 'L' are already used internally by the classes
                            :class:`~argparse.ArgumentParser` and :class:`ConsoleApp`.
        :param choices:     list of valid option values (optional, default=allow all values).
        :param multiple:    True if option can be added multiple times to command line (optional, default=False).

        the value of a config option can be of any type and gets represented by an instance of the
        :class:`~.literal.Literal` class. supported value types and literals are documented
        :attr:`here <.literal.Literal.value>`.

        this method has an alias named :meth:`add_opt`.
        """
        if self._parsed_arguments:
            self._parsed_arguments = None        # request (re-)parsing of command line args
            self.vpo("ConsoleApp.add_option call after parse of command line args parsing (re-parse requested)")
        if short_opt == '':
            short_opt = name[0]

        args = []
        if short_opt and len(short_opt) == 1:
            short_opt = '-' + short_opt
            # noinspection PyProtectedMember
            assert short_opt not in self._arg_parser._option_string_actions, f"short_opt {short_opt} already exists"
            args.append(short_opt)
        args.append('--' + name)

        # determine config value to use as default for command line arg
        option = Literal(literal_or_value=False if value is UNSET else value, name=name)
        # alt: cfg_val = self._get_cfg_parser_val(name, self.user_section(MAIN_SECTION_NAME, name), default_value=value)
        cfg_val = self.get_variable(name, section=MAIN_SECTION_NAME, default_value=False if value is UNSET else value)
        option.value = cfg_val
        kwargs = dict(help=desc, default=cfg_val)
        if value is UNSET:
            kwargs['action'] = 'store_true'
        else:
            kwargs.update(type=option.convert_value, choices=choices, metavar=name)
            if multiple:
                kwargs['type'] = option.append_value
                if choices:
                    kwargs['choices'] = None    # for multiple options this instance need to check the choices
                    self.cfg_opt_choices[name] = choices

        self._arg_parser.add_argument(*args, **kwargs)

        self.cfg_options[name] = option

    add_opt = add_option    #: alias of method :meth:`.add_option`

    def _change_option(self, name: str, value: Any):
        """ change config option and the instance shortcut|property to the specified value. """
        if name in self.cfg_options:
            self.cfg_options[name].value = value
        if hasattr(self, name) and getattr(self, name) != value:    # name in ('debug_level', 'user_id', ...)
            setattr(self, name, value)  # self.debug_level = value | self.user_id = value (both are @property!)

    def get_option(self, name: str, default_value: Optional[Any] = None) -> Any:
        """ determine the value of a config option specified by its name (option id).

        :param name:            name/id of the config option.
        :param default_value:   default value of the option (if not defined with :class:`~ConsoleApp.add_option`).
        :return:                first found value of the option identified by :paramref:`~ConsoleApp.get_option.name`.
                                the returned value has the same type as the value specified in the :meth:`.add_option`
                                call. if not given on the command line, then it gets search next in default config
                                section (:data:`MAIN_SECTION_NAME`) of the collected config files (the exact search
                                order is documented in the doc-string of the method :meth:`~ConsoleApp.add_cfg_files`).
                                if not found in the config file then the default value specified of the option
                                definition (the :meth:`.add_option` call) will be used. the other default value,
                                specified in the :paramref:`~get_option.default_value` kwarg of this method, will be
                                returned only if the option name/id never got defined.

        this method has an alias named :meth:`get_opt`.
        """
        if not self._parsed_arguments:
            self.parse_arguments()
            self.vpo("ConsoleApp.get_option call before explicit command line args parsing (run_app call missing)")
        return self.cfg_options[name].value if name in self.cfg_options else default_value

    get_opt = get_option    #: alias of method :meth:`.get_option`

    def set_option(self, name: str, value: Any, cfg_fnam: Optional[str] = None, save_to_config: bool = True) -> str:
        """ set or change the value of a config option.

        :param name:            id of the config option to set.
        :param value:           value to assign to the option, identified by :paramref:`~set_option.name`.
        :param cfg_fnam:        config file name to save new option value. if not specified then the
                                default file name of :meth:`~ConsoleApp.set_variable` will be used.
        :param save_to_config:  pass False to prevent to save the new option value also to a config file.
                                the value of the config option will be changed in any case.
        :return:                ''/empty string on success else error message text.

        this method has an alias named :meth:`set_opt`.
        """
        if save_to_config:
            return self.set_variable(name, value, cfg_fnam)     # store in config file and call self._change_option()
        self._change_option(name, value)
        return ""

    set_opt = set_option    #: alias of method :meth:`.set_option`

    def parse_arguments(self):
        """ parse all command line args.

        this method get normally only called once and after all the options have been added with :meth:`add_option`.
        :meth:`add_option` will then set the determined config file value as the default value and then the
        following call of this method will overwrite it with command line argument value, if given.
        """
        self.vpo("ConsoleApp.parse_arguments()")
        self._parsed_arguments = self._arg_parser.parse_args()

        for name, cfg_opt in self.cfg_options.items():
            cfg_opt.value = getattr(self._parsed_arguments, name)
            if name in self.cfg_opt_choices:
                for given_value in cfg_opt.value:
                    if self._cfg_opt_val_stripper:
                        given_value = self._cfg_opt_val_stripper(given_value)
                    allowed_values = self.cfg_opt_choices[name]
                    if given_value not in allowed_values:
                        raise ArgumentError(None, f"'{name}' option has wrong {given_value=}; {allowed_values=}")

        is_main_app = main_app_instance() is self
        if is_main_app and not self.py_log_params and 'log_file' in self.cfg_options:
            self._log_file_name = self.cfg_options['log_file'].value
            if self._log_file_name:
                self.log_file_check()

        # finished argument parsing - now print chosen option values to the console
        self.startup_end = datetime.datetime.now()
        self.po(f"####  {self.app_name}  V {self.app_version}  args parsed at {self.startup_end}", logger=APP_LOGGER)

        self.debug_level = self.cfg_options['debug_level'].value

        if 'user_id' in self.cfg_options:
            self.user_id = self.cfg_options['user_id'].value
            self.cfg_options['user_id'].value = self.user_id    # update if user_id property got normalized

        if self.debug:
            debug_levels = ", ".join([str(k) + "=" + v for k, v in DEBUG_LEVELS.items()])
            self.po(f"  ##  debug level({debug_levels}): {self.debug_level}", logger=APP_LOGGER)
            if self._log_file_name:
                self.po(f"   #  log file: {self._log_file_name}", logger=APP_LOGGER)
            if self.user_id:
                self.po(f"   #  user id: {self.user_id}", logger=APP_LOGGER)
            self.po(f"  ##  {self.app_key} system environment:", logger=APP_LOGGER)
            self.po(sys_env_text(extra_sys_env_dict=self.app_env_dict()), logger=APP_LOGGER)

    # app user related properties and methods

    @property
    def user_id(self):
        """ id of the user of this app. """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: str):
        """ set id of user of this app. """
        checked_id = norm_name(user_id)
        if checked_id != user_id:
            self.po(f"  **  removed invalid characters in user id '{user_id}', resulting in '{checked_id}'")
        self._user_id = checked_id

    def load_user_cfg(self):
        """ load users configuration. """
        with config_lock:
            if not self.user_id:
                self.user_id = self.get_variable('user_id', default_value=os_user_name())

            self.registered_users = self.get_var('registered_users', default_value=[])
            self.user_specific_cfg_vars = self.get_var('user_specific_cfg_vars',
                                                       default_value=self.user_specific_cfg_vars)

    def register_user(self, new_user_id: str = "", reset_cfg_vars: bool = False, set_as_default: bool = True) -> bool:
        """ register/reset the specified or current user, creating/copying a new set of user specific config vars.

        :param new_user_id:     username/id to register. if not specified then register current os user (self.user_id).
        :param reset_cfg_vars:  pass True to reset the user-specific-variables to the default values.
        :param set_as_default:  pass False to not set the specified user id as default for next app start.
        :raises AssertionError: if specified/current user id/name is empty, too long or contains invalid characters.
        :return:                True if the specified or the current os user id/name was not registered, else False.
        """
        user_id = new_user_id or self.user_id
        assert user_id, f" ***  cannot register user with empty user name/id; {self.user_id=} {new_user_id=}"
        assert len(user_id) <= USER_NAME_MAX_LEN, f" ***  user id/name {user_id} too long ({USER_NAME_MAX_LEN=})"
        inv_chars = "".join(ch for ch in user_id if ch not in norm_name(user_id))
        assert not inv_chars, f" ***  spaces or invalid characters '{inv_chars}' not allowed in user id/name {user_id}"

        registered = user_id in self.registered_users

        with config_lock:
            if not registered:
                self.registered_users.append(user_id)
                self.set_var('registered_users', self.registered_users)

            if not registered or reset_cfg_vars:
                current_user_id = self.user_id
                for section, var_name in self.user_specific_cfg_vars:
                    self.user_id = ''
                    value = self.get_var(var_name, section)
                    self.user_id = user_id
                    self.set_var(var_name, value, section=section)
                self.user_id = current_user_id

            if set_as_default:
                self.set_option('user_id', user_id)  # save to app config file, to be also used/set on next app start

        return not registered

    def user_section(self, section: str, name: str = "") -> str:
        """ return the user section name if the passed (section, name) setting id is user-specific.

        :param section:         section name.
        :param name:            config variable name. if specified then this variable has to be a user-specific one.
                                if not specified and the user is registered then return always the user section.
        :return:                passed section name or user-specific section name.
        """
        if self.user_id in self.registered_users and (not name or (section, name) in self.user_specific_cfg_vars):
            section = section + '_usr_id_' + self.user_id
        return section

    # optional helper and extra feature methods

    def app_env_dict(self) -> dict[str, Any]:
        """ collect run-time app environment data and settings - for app logging and debugging.

        :return:                dict with app environment data/settings.
        """
        app_env_info: dict[str, Any] = {"main config": self._main_cfg_fnam, "sys env id": self.sys_env_id}
        if self.debug:
            app_data = dict(app_key=self.app_key)
            if self.verbose:
                app_data['app_name'] = self.app_name
                app_data['app_path'] = self.app_path
                app_data['app_title'] = self.app_title
                app_data['app_version'] = self.app_version
            app_env_info["app data"] = app_data

            cfg_data: dict[str, Any] = dict(_cfg_files=self._cfg_files, cfg_options=self.cfg_options)
            if self.verbose:
                cfg_data['cfg_opt_choices'] = self.cfg_opt_choices
                cfg_data['cfg_opt_eval_vars'] = self.cfg_opt_eval_vars
                cfg_data['is_main_cfg_file_modified'] = self.is_main_cfg_file_modified()
            app_env_info["cfg data"] = cfg_data

            log_data = dict(_log_file_name=self._log_file_name)
            if self.verbose:
                log_data['_last_log_line_prefix'] = self._last_log_line_prefix
                log_data['_log_file_index'] = self._log_file_index
                log_data['_log_file_size_max'] = self._log_file_size_max
                log_data['_log_with_timestamp'] = self._log_with_timestamp
                log_data['py_log_params'] = self.py_log_params
                log_data['suppress_stdout'] = self.suppress_stdout
            app_env_info["log data"] = log_data

            app_env_info['PATH_PLACEHOLDERS'] = PATH_PLACEHOLDERS
            if self.verbose:
                app_env_info["sys env data"] = sys_env_dict()
                app_env_info["sys env data"]['user name'] += "/" + self.user_id

        return app_env_info

    def run_app(self):
        """ prepare app run. call after definition of command line arguments/options and before run of app code. """
        if not self._parsed_arguments:
            self.parse_arguments()

    def show_help(self):
        """ print help message, listing defined command line args and options, to console output/stream.

        includes command line args defined with :meth:`.add_argument`, options defined with :meth:`.add_option` and the
        args/kwargs defined with the respective :class:`~argparse.ArgumentParser` methods (see description/definition of
        :meth:`~argparse.ArgumentParser.print_help` of :class:`~argparse.ArgumentParser`).
        """
        self._arg_parser.print_help(file=ori_std_out)
