# coding=utf-8
from collections import deque

# declare
class Queue:
    def __init__(self):
        self._queue = deque()

    def enqueue(self,x):
        self._queue.append(x)

    def dequeue(self):
        return self._queue.popleft()

    def to_string(self):
        return ''.join(self._queue)


# call
queue = Queue()

queue.enqueue('o')
queue.enqueue('n')
queue.enqueue('p')
queue.enqueue('y')
queue.enqueue('t')
queue.enqueue('h')

queue.enqueue(queue.dequeue())
queue.enqueue(queue.dequeue())

# => python
print(queue.to_string())


