import datetime
import multiprocessing
import logging

FORMAT = "%(processName)s %(thread)d %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)

start = datetime.datetime.now()

def calc():
    sum = 0
    for i in range(20000000):
        sum += 1
    logging.info('finished')

if __name__ == '__main__':
    pool = multiprocessing.Pool(4) # 创建4个工作进程

    for i in range(4):
        pool.apply_async(calc)  # 异步提交任务到进程池
    pool.close() #等待⼯作进程全部结束后，清理池，然后关闭
    pool.join() # 阻塞到close之后

    delta = (datetime.datetime.now() - start).total_seconds()
    logging.info(delta)