import logging


class Logger:
    @staticmethod
    def setup_logger(name):
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                            handlers=[
                                logging.FileHandler("../test_log.log"),
                                logging.StreamHandler()
                            ])
        logger = logging.getLogger(name)
        # Set googleapiclient logging level to WARNING to filter out INFO messages
        logging.getLogger('googleapiclient.discovery_cache').setLevel(logging.WARNING)
        return logger
