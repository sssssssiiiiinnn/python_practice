import logging
import queue
import threading
import time

logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)s; %(message)s')


def worker1(queue):
    logging.debug('start')
    while True:
        item = queue.get()
        if item is None:
            break
        logging.debug(item)
        queue.task_done()
    logging.debug('longggggggggggggggggggggggggggg')
    logging.debug('end')


def worker2(queue):
    logging.debug('start')
    logging.debug(queue.get())
    logging.debug(queue.get())
    logging.debug('end')


if __name__ == '__main__':
    logging.debug('start')
    queue = queue.Queue()
    for i in range(100):
        queue.put(i)
    ts = []
    for _ in range(3):
        t1 = threading.Thread(target=worker1, args=(queue, ))
        t1.start()
        ts.append(t1)
    logging.debug('tasks are not done')
    [t.join for t in ts]
    queue.join()
    logging.debug('tasks are done')
    for _ in range(len(ts)):
        queue.put(None)

    [t.join() for t in ts]
    logging.debug('Done')