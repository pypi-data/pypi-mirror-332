import logging
# import dotenv
from threading import Thread
import os
from Server_3_free_threads.load_app import load_app
from Server_3_free_threads.parser_args import ParserCommandLineArgs
from Server_3_free_threads.server_actions import ServerActions
from Server_3_free_threads.parser_config import ParserConfigFile
import importlib


def main():
    # dotenv.load_dotenv()
    logging.basicConfig(level=logging.INFO, format='[%(asctime)s] [%(filename)s:%(funcName)s] %(message)s')
    log = logging.getLogger(__name__)

    host = '127.0.0.1'
    port_default = 8888
    connection_queue = 200

    module = None
    pars_args = ParserCommandLineArgs(port_default)
    pars_args.find_args()
    port, path_app, configfile = int(pars_args.port), pars_args.app, pars_args.configfile

    if configfile:
        pars_config = ParserConfigFile(configfile)
        pars_config.open_file()
        host, port, path_app, connection_queue = pars_config.host, int(pars_config.port), pars_config.app, int(pars_config.connection_queue)

    if path_app:
        if load_app(path_app):
            module = importlib.import_module(path_app)
            importlib.invalidate_caches()
    else:
        log.info("относительный путь к приложению не указан, сервер запущен в тестовом режиме")
    serv_act = ServerActions(host=host, port=port, connection_queue=connection_queue)
    threads = (Thread(target=serv_act.accepting_connections),
               Thread(target=serv_act.reading_from_socket),
               Thread(target=serv_act.sending_to_socket, args=(module, )),
               Thread(target=serv_act.close_client_sock),)

    for elem in threads:
        elem.start()
    for elem in threads:
        elem.join()
