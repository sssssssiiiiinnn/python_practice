import threading
import time
import logging


format = '%(threadName)s;%(message)s'
logging.basicConfig(level=logging.DEBUG, format=format)


def worker1(barrier):
    with barrier:
        barrier.wait()
        logging.debug('start')
        time.sleep(3)
        logging.debug('end')


def worker2(barrier):
    with barrier:
        barrier.wait()
        logging.debug('start')
        time.sleep(3)
        logging.debug('end')


def worker3(barrier):
    with barrier:
        logging.debug('start')
        time.sleep(3)
        logging.debug('end')
        barrier.notifyAll()


if __name__ == '__main__':
    barrier = threading.Barrier()
    t1 = threading.Thread(target=worker1, args=(barrier, ))
    t2 = threading.Thread(target=worker2, args=(barrier, ))
    t3 = threading.Thread(target=worker3, args=(barrier, ))
    t1.start()
    t2.start()
    t3.start()