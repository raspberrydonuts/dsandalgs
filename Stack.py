# implementation of Stack with only queues
from queue import Queue
class Stack:

    def __init__(self):
        # newly entered element always put in front of q1
        # so pop will always dequeue first element of q1
        self.q1 = Queue()
        # q2 is used to put every new element in front of q1
        self.q2 = Queue()
        self.size = 0

    def push(self, x):
        self.size += 1
        # enqueue x to q2
        self.q2.put(x)
        # dequeue everything from q1 to q2
        while (not self.q1.empty()):
            self.q2.put(self.q1.get())
        # swap names q1 and q2
        temp = self.q1
        self.q1 = self.q2
        self.q2 = temp

    def pop(self):
        # dequeue from q1 and return it
        if self.size == 0:
            return
        self.size -= 1
        return self.q1.get() # .get() removes and returns from queue


if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)

    print("size ", s.size)
    print()
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print("size ", s.size)
