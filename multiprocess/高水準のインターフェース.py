import threading
import multiprocessing


import concurrent.futures
import logging
import time


logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)s; %(message)s'
)


def worker(x, y):
    logging.debug('start')
    r = x * y
    time.sleep(3)
    logging.debug('end')
    return r


def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
        f1 = executor.submit(worker, 2, 5)
        f2 = executor.submit(worker, 3, 5)
        logging.debug(f1.result())
        logging.debug(f2.result())

if __name__ == '__main__':
    main()