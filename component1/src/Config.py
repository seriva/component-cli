import os
from os.path import expanduser

class Config:
    class __ConfigBase:
        def __init__(self):
            self._debug = 0
            self._auto_approve = False
            self._output_dir = os.environ.get('E_OUTPUT_DIR')
            self._log_file = 'log.log'
            self._log_format = '%(asctime)s %(levelname)s %(name)s - %(message)s'
            self._log_date_format = '%H:%M:%S'
            self._log_count = 10
            self._log_type = 'plain'

        @property
        def output_dir(self):
            if self._output_dir == None:
                self._output_dir = os.path.join(os.getcwd(), 'output')
                if not os.path.exists(self._output_dir):
                    os.makedirs(self._output_dir)
            return self._output_dir

        @output_dir.setter
        def output_dir(self, output_dir):
            if not output_dir is None:
                self._output_dir = output_dir

        @property
        def log_file(self):
            return self._log_file

        @log_file.setter
        def log_file(self, log_file):
            if not log_file is None:
                self._log_file = log_file

        @property
        def log_format(self):
            return self._log_format

        @log_format.setter
        def log_format(self, log_format):
            if not log_format is None:
                self._log_format = log_format

        @property
        def log_date_format(self):
            return self._log_date_format

        @log_date_format.setter
        def log_date_format(self, log_date_format):
            if not log_date_format is None:
                self._log_date_format = log_date_format

        @property
        def log_count(self):
            return self._log_count

        @log_count.setter
        def log_count(self, log_count):
            if not log_count is None:
                self._log_count = log_count

        @property
        def log_type(self):
            return self._log_type

        @log_type.setter
        def log_type(self, log_type):
            if not log_type is None:
                self._log_type = log_type

        @property
        def debug(self):
            return self._debug

        @debug.setter
        def debug(self, debug):
            if not debug is None:
                self._debug = debug

        @property
        def auto_approve(self):
            return self._auto_approve

        @auto_approve.setter
        def auto_approve(self, auto_approve):
            if not auto_approve is None:
                self._auto_approve = auto_approve

    instance = None

    def __new__(cls):
        if Config.instance is None:
            Config.instance = Config.__ConfigBase()
        return Config.instance
