import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s; %(message)s')

def worker1():
    logging.debug('start')
    time.sleep(5)
    logging.debug('end')


def worker2(x, y=1):
    logging.debug('start')
    logging.debug(x)
    logging.debug(y)

    time.sleep(2)
    logging.debug('end')


if __name__ == '__main__':
    logging.debug('start')
    t = threading.Timer(3, worker1)
    t.start()


    # for _ in range(5):
    #     t = threading.Thread(name='test', target=worker1)
    #     t.setDaemon(True)
    #     t.start()
    #     # threads.append(t)
    # print(threading.enumerate())
    # for thread in threading.enumerate():
    #     if thread is threading.current_thread():
    #         print(thread)
    #         continue
    #     thread.join()


    # logging.debug('start')
    # t1 = threading.Thread(name='rename worker1', target=worker1)
    # # Daemon thread
    # t1.setDaemon(True)
    # t2 = threading.Thread(target=worker2, args=(100, ), kwargs={'y':200})
    # t1.start()
    # t2.start()
    # print('started')
    # # スレッドの終了を待ってから終了する
    # t1.join()