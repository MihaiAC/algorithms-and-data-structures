from matplotlib import pyplot
from functools import partial
import timeit
#Want to figure out how committing works.
@staticmethod
class Plotter:
    #generator = generates a list of appropiate arguments for the function, based on the previous list of arguments
    #func = function of which the runtime will be measured
    #n = number of plot points (executions of function func)
    def plotter(func,generator,n):
        x = range(1,n)
        y = []
        argss = []
        for i in x:
            argss = generator(argss)
            #By increasing "number", the plot gets smoother, but takes longer to generate.
            #"number" = number of times the timing is repeated.
            y.append(timeit.timeit(partial(func,argss), number = 20))

        #Plot the graph:
        pyplot.plot(x,y)
        pyplot.show()
