import logging


# TODO: Create Logger for bot


class Logger:
    def __init__(self):
        # Create logger
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter("[%(levelname)s]: %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
