from MaxHeap import MaxHeap

def compare(x,y):
    if(x < y):
        return 1
    elif(x == y):
        return 0
    else:
        return -1

def HeapSort(array,compare):
    if(array == None):
        raise Exception("Cannot sort empty array.")
    mH = MaxHeap.buildHeap(array,compare)
    sortedArray = []
    while(not mH.isEmpty()):
        sortedArray.append(mH.maxElement())
        mH.removeMax()
    return sortedArray

if __name__ == '__main__':
    print(HeapSort([2,4,8,6,1,4,3,10],compare))