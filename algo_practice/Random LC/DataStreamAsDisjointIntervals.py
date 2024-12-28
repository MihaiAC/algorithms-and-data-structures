from typing import List

class LinkedList:
    def __init__(self, value: int):
        self.val = [value, value]
        self.next = None
    
    # No need for recursion => can eliminate it.
    def add_val(self, value: int):
        if value < self.val[0]:
            if value == self.val[0] - 1:
                self.val[0] = value
            else:
                new_second_node = LinkedList(-1)
                new_second_node.val = self.val
                new_second_node.next = self.next
                self.next = new_second_node
                self.val = [value, value]
        
        elif value <= self.val[1]:
            return

        elif value == (self.val[1] + 1):
            self.val[1] += 1
            if self.next is not None and self.next.val[0] == (self.val[1]+1):
                self.val[1] = self.next.val[1]
                self.next = self.next.next
            
            return
        else:
            if self.next is None:
                self.next = LinkedList(value)
            else:
                self.next.add_val(value)
    
    def to_list(self) -> List[List[int]]:
        curr_node = self
        accum = []
        while curr_node is not None:
            accum.append(curr_node.val)
            curr_node = curr_node.next
        
        return accum
        
        

class SummaryRanges:
    def __init__(self):
        self.ll = None

    def addNum(self, value: int) -> None:
        if self.ll is None:
            self.ll = LinkedList(value)
        else:
            self.ll.add_val(value)

    def getIntervals(self) -> List[List[int]]:
        return self.ll.to_list()
        

if __name__ == '__main__':
    sr = None
    actions = ["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"]
    values = [[], [1], [], [3], [], [7], [], [2], [], [6], []]

    for ii, action in enumerate(actions):
        if action == "SummaryRanges":
            sr = SummaryRanges()
        elif action == "addNum":
            sr.addNum(values[ii][0])
        else:
            print(sr.getIntervals())
# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()