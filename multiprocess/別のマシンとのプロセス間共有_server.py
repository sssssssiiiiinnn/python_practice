import logging
import queue
from multiprocessing.managers import BaseManager


logging.basicConfig(level=logging.DEBUG, format='%(processName)s; %(message)s')


queue = queue.Queue()


class QueueManager(BaseManager):
    pass


# 呼び出せる関数を登録
QueueManager.register(
    'get_queue', callable=lambda: queue
)


manager = QueueManager(
    address= ('127.0.0.1', 50000),
    authkey=b'abrakatabura'
)
server = manager.get_server()
logging.debug('server is running')
server.serve_forever()
