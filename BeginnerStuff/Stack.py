#Basic Stack (will add stuff when I'll become more proficient in Python)
class Stack:
    class Node:
        def __init__(self,value,nextNode = None):
            self.value = value
            self.nextNode = nextNode

        def getNextNode(self):
            return self.nextNode

        def setNextNode(self,node):
            self.nextNode = node

        def getValue(self):
            return self.value

    def __init__(self,value):
        self.topNode = self.Node(value)
        self.elements = 1

    def push(self, val):
        newNode = self.Node(val,self.topNode)
        self.topNode = newNode
        self.elements += 1

    def pop(self):
        if(self.elements == 0):
            raise IndexError('Cannot pop() from an empty stack')
        else:
            returnVal = self.topNode.getValue()
            self.topNode = self.topNode.nextNode
            self.elements -= 1
            return returnVal

    def isEmpty(self):
        return self.elements == 0

if(__name__ == '__main__'):
    s = Stack(2)
    s.push(3)
    s.push(5)
    print(s.pop())
    print(s.pop())
    print(s.pop())
