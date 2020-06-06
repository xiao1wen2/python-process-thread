import multiprocessing
import logging
import datetime

FORMAT = "%(processName)s %(thread)d %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)
start = datetime.datetime.now()
def calc():
    sum = 0
    for i in range(200000000):
        sum += 1
    logging.info('finished')

if __name__ == '__main__':
    tasks = []
    for i in range(4):
        t = multiprocessing.Process(target=calc, name="c-{}".format(i+1))
        tasks.append(t)
        t.start()
    for t in tasks:
        t.join() # 主进程的主线程等待工作进程的线程执行完成
    delta = (datetime.datetime.now() - start).total_seconds()
    logging.info(delta)
