import logging
import queue
from multiprocessing.managers import BaseManager


logging.basicConfig(level=logging.DEBUG, format='%(processName)s; %(message)s')


queue = queue.Queue()


class QueueManager(BaseManager):
    pass


# 呼び出せる関数を登録
QueueManager.register('get_queue')


manager = QueueManager(
    address= ('127.0.0.1', 50000),
    authkey=b'abrakatabura'
)
manager.connect()
queue = manager.get_queue()
queue.put('hello')