import datetime
import logging
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

FORMAT = "%(processName)s %(thread)d %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)

start = datetime.datetime.now()

def calc():
    sum = 0
    for i in range(200000000):
        sum += 1
    logging.info('finished')


if __name__ == '__main__':
    # executor = ThreadPoolExecutor(4) # 开4个工作线程
    executor = ProcessPoolExecutor(4) # 开4个工作进程
    fs = []
    with executor:
        for i in range(4):
            future = executor.submit(calc) # 异步提交任务， 返回future对象
            fs.append(future)
        print(*fs, sep='\n')
    # 退出with时，任务全部执行完成
    print('-'*30)
    print(*fs, sep='\n')

    delta = (datetime.datetime.now() - start)
    logging.info(delta)