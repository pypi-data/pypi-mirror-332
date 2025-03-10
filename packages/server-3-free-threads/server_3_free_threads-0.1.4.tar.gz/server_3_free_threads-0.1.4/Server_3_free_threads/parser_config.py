from pathlib import Path
import os
import re


class ParserConfigFile:

    def __init__(self, path):
        self._path = path
        self._abs_path = Path(os.getcwd())
        self._full_path = None

        self._port = None
        self._host = None
        self._app = None
        self._connection_queue = None

        self._port_re = re.compile(r'PORT=(?P<port>\d{0,4})')
        self._app_re = re.compile(r'APP=(?P<app>.+)')
        self._conn_re = re.compile(r'CONNECTION_QUEUE=(?P<con_q>\d{0,4})')
        self._host_re = re.compile(r'HOST=(?P<host>.+)')

    def check_path(self):
        full_path = self._abs_path.joinpath(self._path)
        if full_path.exists():
            print("file config exist")
            self._full_path = full_path
            return True
        else:
            print("file config don't exist")

    def open_file(self):
        if self.check_path():
            with open(self._full_path, 'r') as file:
                for line in file.readlines():
                    print(line)
                    result_port = self.pars_func(param=line, group='port', re_pattern=self._port_re)
                    result_app = self.pars_func(param=line, group='app', re_pattern=self._app_re)
                    result_host = self.pars_func(param=line, group='host', re_pattern=self._host_re)
                    result_conn_q = self.pars_func(param=line, group='con_q', re_pattern=self._conn_re)

                    if result_port:
                        print(result_port)
                        self._port = result_port

                    if result_app:
                        print(result_app)
                        self._app = result_app

                    if result_host:
                        print(result_host)
                        self._host = result_host

                    if result_conn_q:
                        print(result_conn_q)
                        self._connection_queue = result_conn_q

    def pars_func(self, param, group, re_pattern):
        result = re_pattern.match(param)
        if result:
            arg = result.group(group)
            return arg

    @property
    def port(self):
        return self._port

    @property
    def host(self):
        return self._host

    @property
    def app(self):
        return self._app

    @property
    def connection_queue(self):
        return self._connection_queue






