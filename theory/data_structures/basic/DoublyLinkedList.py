#Maybe another time :)

class DLL:
    class Node:
        def __init__(self,value,nextNode = None, prevNode = None):
            self.value = value
            self.nextNode = nextNode
            self.prevNode = prevNode

    def __init__(self, value):
        n = Node(value)
        self.first = n
        self.last = n
        self.length = 1
