import logging
# from logging import ERROR, WARN, INFO, DEBUG

def init_log():
    logger = logging.getLogger("arxiv")
    stream_handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s[%(levelname)s] %(message)s")
    logger.setLevel(logging.DEBUG)

    stream_handler.setLevel(logging.DEBUG)

    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)

    return logger


arxiv_logger = init_log()