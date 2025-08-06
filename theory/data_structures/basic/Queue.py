#Basic queue class.
class Queue:
    class Node:
        def __init__(self,value = None, nextNode = None):
            self.value = value
            self.nextNode = nextNode

        def getNextNode(self):
            return self.nextNode

        def setNextNode(self,node):
            self.nextNode = node

        def getValue(self):
            return self.value

    def __init__(self, value = None):
        if(value == None):
            self.elements = 0
        else:
            self.dequeueNode = self.Node(value)
            self.enqueueNode = self.dequeueNode
            self.elements = 1

    def enqueue(self, val):
        if(self.elements == 0):
            self.dequeueNode = self.Node(val)
            self.enqueueNode = self.dequeueNode
            self.elements = 1
        else:
            newNode = self.Node(val)
            self.enqueueNode.nextNode = newNode
            self.enqueueNode = newNode
            self.elements += 1

    def dequeue(self):
        if(self.elements == 0):
            raise IndexError('Cannot dequeue an element from an empty queue.')
        else:
            returnVal = self.dequeueNode.getValue()
            self.dequeueNode = self.dequeueNode.nextNode
            self.elements -= 1
            return returnVal

    def isEmpty(self):
        return self.elements == 0

if(__name__ == '__main__'):
    q = Queue()
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(5)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())