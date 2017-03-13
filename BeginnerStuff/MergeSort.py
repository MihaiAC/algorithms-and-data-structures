class MergeSort:
    @staticmethod
    def sort(array):
        if(array == None):
            print('Input array is empty')
        l = len(array)
        if(l >= 1):
            MergeSort.mergeSort(0,l-1,array)

    @staticmethod
    def mergeSort(i,j,array):
        if(i < j):
            mid = (i+j)/2
            MergeSort.mergeSort(i,mid,array)
            MergeSort.mergeSort(mid+1,j,array)
            MergeSort.merge(i,mid,j,array)

    @staticmethod
    def merge(i,mid,j,array):
        aux = []
        k = i
        m = mid + 1
        while(k <= mid and m <= j):
            if(array[k] <= array[m]):
                aux.append(array[k])
                k += 1
            else:
                aux.append(array[m])
                m += 1
        while(k <= mid):
            aux.append(array[k])
            k += 1
        while(m <= j):
            aux.append(array[m])
            m += 1
        array[i:j+1] = aux

if __name__ == '__main__':
    a = [3,4,5,1,2,10]
    MergeSort.sort(a)
    print(a)
