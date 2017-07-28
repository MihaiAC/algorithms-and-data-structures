class MaxHeap(object):
    def __init__(self,compare):
        if(compare == None):
            raise Exception("A comparator must be provided.")
        self.compare = compare
        self.arr = []
        self.nrElem = 0
    
    def isEmpty(self):
        return len(self.arr) == 0
    
    def maxElement(self):
        if(self.isEmpty()):
            raise Exception("Cannot return max element because the heap is empty.")
        else:
            return self.arr[0]

    def insertItem(self,item):
        (self.arr).append(item)
        i = self.nrElem
        self.nrElem += 1
        if(i == 0):
            self.arr[0] = item
        else:
            while(i != 0 and self.compare(item,self.arr[int(i/2)]) == 1):
                self.arr[i] = self.arr[int(i/2)]
                self.arr[int(i/2)] = item
                i = int(i/2)
    
    def heapify(self,i):
        if(self.isEmpty()):
            pass
        if(i * 2 > self.nrElem - 1):
            pass
        elif(i * 2 + 1 > self.nrElem - 1):
            if(self.compare(self.arr[i],self.arr[2*i]) == -1):
                aux = self.arr[i]
                self.arr[i] = self.arr[2*i]
                self.arr[2*i] = aux
        else:
            ieven = 2*i
            iodd = 2*i + 1
            compareL = self.compare(self.arr[i],self.arr[ieven])
            compareR = self.compare(self.arr[i],self.arr[iodd])
            compareLR = self.compare(self.arr[ieven],self.arr[iodd])
            if(compareL == -1 or compareR == -1):
                if(compareLR == -1):
                    aux = self.arr[i]
                    self.arr[i] = self.arr[iodd]
                    self.arr[iodd] = aux
                    self.heapify(iodd)
                else:
                    aux = self.arr[i]
                    self.arr[i] = self.arr[ieven]
                    self.arr[ieven] = aux
                    self.heapify(ieven)

    def removeMax(self):
        if(self.isEmpty()):
            raise Exception("Cannot removeMax because the heap is empty.")
        self.arr[0] = self.arr[self.nrElem - 1]
        del(self.arr[self.nrElem - 1])
        self.nrElem -= 1
        self.heapify(0)

    def displayList(self):
        print(self.arr)

    def buildHeap(array,compare):
        newHeap = MaxHeap(compare)
        for elem in array:
           newHeap.insertItem(elem)
        return newHeap
        
#Testing the Heap:
def compare(x,y):
    if(x < y):
        return -1
    elif(x == y):
        return 0
    else:
        return 1

if __name__ == "__main__":
    mH = MaxHeap.buildHeap([4,2,10],compare)
    mH.displayList()
    mH.removeMax()
    mH.displayList()