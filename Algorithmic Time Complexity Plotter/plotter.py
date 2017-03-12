from matplotlib import pyplot
from functools import partial
import timeit
import random

#pyplot.plot(x,y)
#pyplot.show()
#generator = generates a list of arguments of size i for function func
#func = function of which the runtime will be measured
def plotter(func,generator,n):
    x = []
    y = []
    argss = []
    for i in range(1,n):
        argss = generator(argss)
        x.append(i)
        y.append(timeit.timeit(partial(func,argss)))
    
    #Plot the graph:
    pyplot.plot(x,y)
    pyplot.show()

def gen(lst):
    lst.append(random.randint(1,1000))
    return lst

#Selection sort:
def func(lst):
    for i in range(0,len(lst) - 1):
        minim = i
        for j in range(i+1,len(lst) - 1):
            if(lst[j] < lst[minim]):
                minim = j
        if(minim != i):
            aux = lst[i]
            lst[i] = lst[minim]
            lst[minim] = aux
    




def main():
    plotter(func,gen,25)

if __name__ == '__main__':
    main()
