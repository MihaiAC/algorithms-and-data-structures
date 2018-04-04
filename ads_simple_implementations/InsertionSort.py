#Must add some failsafe mechanisms.

def insertionSort(array):
    for j in range(1,len(array)):
        aux = array[j]
        i = j-1
        while(i>=0 and array[i] > aux):
            array[i+1] = array[i]
            i = i - 1
        array[i+1] = aux


if __name__ == '__main__':
    a = [6,2,1,10,7]
    print(a)
    insertionSort(a)
    print(a)
