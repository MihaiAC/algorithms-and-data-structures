from InsertionSort import insertionSort
import random

#// = for integer result of division.
#Returns the Median of the array in Theta(n) time.
def findMedian(array):
    length = len(array)
    if(length < 6):
        #If the length of the array is smaller than 6, then sort the array and return its median.
        insertionSort(array)
        return array[(length - 1)//2]
    else:
        nrOfMedians = 0
        medians = []
        #Calculate number of medians.
        if(length % 5 == 0):
            nrOfMedians = length//5;
        else:
            nrOfMedians = length//5 + 1;
        #Split the array in subarrays of maximum 5 elements and add the median.
        for i in range(0,nrOfMedians):
            if(i*5 + 4 > length):
                insertionSort(array[(i*5):(length-1)])
                medians.append(array[(i*5 + length - 1)//2])
            else:
                insertionSort(array[(i*5):(i*5+4)])
                medians.append(array[(10*i+4)//2])
        if(nrOfMedians > 5):
            findMedian(medians)
        return medians[(nrOfMedians - 1)//2]

if __name__ == '__main__':
    arr = random.sample(range(1,1000),100)
    print(arr)
    #arr = [2, 5, 9, 19, 24, 5, 9, 10, 54, 87, 2, 13, 21, 32, 44, 4, 16, 18, 19, 26, 25, 39, 47, 56, 71]
    print(findMedian(arr))
        
