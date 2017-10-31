# coding=utf-8
# declare
class Stack(list):
    def __init__(self):
        list.__init__(self)

    def push(self,x):
        self.append(x)



# call
stack = Stack()

stack.push('p')
stack.push('y')
stack.push('t')
stack.push('h')
stack.push('n')
stack.push('o')

stack.pop()
stack.pop()

stack.push('o')
stack.push('n')

# => python
print(''.join(stack))


