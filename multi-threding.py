import datetime
import threading
import logging

# 伪多线程，在不同时间片时交替执行
FORMAT = "%(thread)s %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)
start = datetime.datetime.now()
def calc():
    sum = 0
    for i in range(2000000):
        sum+=1
    logging.info("finshed")
tasks = []
for i in range(4):
    t = threading.Thread(target=calc, name="c-{}".format(i+1)) #线程对象
    tasks.append(t)
    t.start() #启动线程
for t in tasks:
    t.join() # 调用线程join方法，知道调用线程结束，否者一直等待
delta = (datetime.datetime.now() - start).total_seconds()
logging.info(delta)
