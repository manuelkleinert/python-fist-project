# -*- coding: utf-8 -*-

import logging
import threading
import time

def thread_function(name, sleep):
    logging.info("Thread %s: starting", name)
    time.sleep(sleep)
    logging.info("Thread %s: finishing", name)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")

    x1 = threading.Thread(target=thread_function, args=(1,4))
    x2 = threading.Thread(target=thread_function, args=(2,3))

    logging.info("Main    : before running thread")

    x1.start()
    x2.start()

    logging.info("Main    : wait for the thread to finish")
    # x.join()
    logging.info("Main    : all done")
