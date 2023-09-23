import logging

logging.basicConfig(level=logging.DEBUG,
                    filename="para8_log.log",
                    filemode='w',
                    format="We have nex logging message: %(asctime)s:%(levelname)s:%(message)s")

try:
    print(10/0)
except Exception:
    logging.exception('Excepction')