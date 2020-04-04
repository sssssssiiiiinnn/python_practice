import logging
import threading


logging.basicConfig(level=logging.DEBUG, format='%(threadName)s; %(message)s;')


def test1(d):
    logging.debug('Start')
    logging.info(d)
    i = d['x']
    d['x'] = 100
    logging.debug('End')
    logging.info(d)


def test2(d):
    logging.debug('Start')
    logging.info(d)
    i = d['x']
    d['x'] = i + 1
    logging.info(d)
    logging.debug('End')


if __name__ == '__main__':
    logging.debug('Start')
    d = {'x': 0}
    t1 = threading.Thread(target=test1, args=(d, ))
    t2 = threading.Thread(target=test2, args=(d, ))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    logging.debug(d)
    logging.debug('End')
