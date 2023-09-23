import logging

logging.basicConfig(level=logging.DEBUG,
                    filename="para8_log.log",
                    filemode='w',
                    format="We have nex logging message: %(asctime)s:%(levelname)s:%(message)s")
logging.debug("debug")
logging.info("info log")
logging.warning("warning! Aaaa!")
logging.error("error :(")
logging.critical("critical, System Dead!")