from FindMedian import findMedian
import random

class QuickSort(object):
    
    @staticmethod
    def quickSort(array,compare):
        QuickSort.sort(0,len(array)-1,array,compare)
        
    @staticmethod
    def sort(i,j,array,compare):
        if(i < j):
            r = QuickSort.partition(i,j,array,compare)
            QuickSort.sort(i,r,array,compare)
            QuickSort.sort(r+1,j,array,compare)

    @staticmethod
    def partition(i,j,array,compare):
        pivot = findMedian(array[i:j])
        print(pivot)
        p = i
        q = j
        while(True):
            while(compare(array[q],pivot) == 1):
                q = q-1
            while(compare(array[p],pivot) == (-1)):
                p = p+1
            if(p<q):
                aux = array[q]
                array[q] = array[p]
                array[p] = aux
            else:
                return q

def compare(a,b):
    if(a<b):
        return -1
    elif(a == b):
        return 0
    else:
        return 1

if __name__ == '__main__':
    arr = random.sample(range(1,1000),100)
    QuickSort.partition(0,len(arr) - 1,arr,compare)
    print(arr)