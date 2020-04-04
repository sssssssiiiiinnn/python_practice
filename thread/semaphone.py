import logging
import threading
import time

logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)s; %(message)s')


def worker1(semaphore):
    with semaphore:
        logging.debug('start')
        time.sleep(3)
        logging.debug('end')


def worker2(semaphore):
    with semaphore:
        logging.debug('start')
        time.sleep(10)
        logging.debug('end')


def worker3(semaphore):
    with semaphore:
        logging.debug('start')
        time.sleep(3)
        logging.debug('end')


if __name__ == '__main__':
    logging.debug('start')
    # 並列処理できる数を決める
    semaphore = threading.Semaphore(2)
    t1 = threading.Thread(target=worker1, args=(semaphore, ))
    t2 = threading.Thread(target=worker2, args=(semaphore, ))
    t3 = threading.Thread(target=worker3, args=(semaphore, ))
    t1.start()
    t2.start()
    t3.start()