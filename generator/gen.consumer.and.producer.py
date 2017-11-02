# -*- coding:utf-8 -*-
# 协程 -- 使用生成器 , 实现生产者和消费者
# 避免多线程带来的上下文切换消耗 , 无锁 , 也可共享内存
# yield           -- 挂起
# next() / send() -- 唤醒
# 一个消费者 , 一个生产者
def gen_producer(consumer, n):
    print('product ready')

    consumer.send(None)

    for i in range(n):
        result = i
        consumer.send(result)  # 将控制权交给consumer , product挂起
        print('product continue')

    consumer.close()


def gen_consumer():
    print('consumer ready')

    while True:
        result = yield
        if result is not None:
            print('consumer receival', result)


consumer = gen_consumer()
product = gen_producer(consumer, 10)
