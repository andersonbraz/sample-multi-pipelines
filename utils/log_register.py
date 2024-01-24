import logging


class LogRegister:

    logging.basicConfig(filename='files/logs/apps.log', level=logging.DEBUG)

    def __init__(self, app_name: str):
        self.app_name = app_name

    @staticmethod
    def record(self, message: str):
        logging.info(message, self.app_name)
