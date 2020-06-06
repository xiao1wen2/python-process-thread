import queue
import time
import threading
import random
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
nums = queue.Queue()

# 生产数字队列 先进先出
def gen(q:queue.Queue):
    num = 1
    while True:
        q.put(num)
        num += 1
        time.sleep(1)

# 消费 队列
def worker(q:queue.Queue, frontcolor=37):
    head = '\x1b[{}m'.format(frontcolor)
    tail = '\x1b[m' # 重置颜色
    while True:
        data = q.get()
        output = "{}\t{}num = {} {} ".format(
            threading.current_thread().ident,
            head,
            data,
            tail
        )
        print (output)


# 第一种方式
# 消费者
try:
    for i in range(20):
        t = threading.Thread(
            target=worker,
            name='worker-{}'.format(i + 1),
            args=(nums, random.randint(30, 37))
        )
        t.start()

    # 生产者
    threading.Thread(target=gen, name='gen', args=(nums, )).start()
except KeyboardInterrupt as e:
    print(e)
# 第二种方式
# 生产者
# threading.Thread(target=gen, name='gen', args=(nums, )).start()
# 消费者
# executor = ThreadPoolExecutor(4)
# with executor:
#
#     for i in range(4):
#
#         executor.submit(worker, nums, random.randint(30, 37))

