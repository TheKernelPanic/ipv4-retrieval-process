import logging


def get_file_formatter():
    """
    example: 2020-11-10 14:39:20,541 - Reader-gps-tracking - ERROR - message
    return Formatter object
    """
    return logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def get_stream_formatter():
    """
    example: INFO - SOMETHING...
    return Formatter object
    """
    return logging.Formatter('%(levelname)s - %(message)s')


class Logger:

    def __init__(self, log_directory):
        """
        Configure logger instance
        """
        self.logger = logging.getLogger('ipv4_retrieval_process')
        self.logger.setLevel(logging.DEBUG)

        self.file_handler = logging.FileHandler(filename=f'{log_directory}/app.log')
        self.file_handler.setLevel(logging.DEBUG)
        self.file_handler.setFormatter(get_file_formatter())

        self.stream_handler = logging.StreamHandler()
        self.stream_handler.setLevel(logging.ERROR)
        self.stream_handler.setFormatter(get_stream_formatter())

        self.logger.addHandler(self.stream_handler)
        self.logger.addHandler(self.file_handler)

    def get_logger(self) -> logging.Logger:
        """
        return configured logger instance
        """
        return self.logger
