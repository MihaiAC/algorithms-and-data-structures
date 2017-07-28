import random
import Plotter
import MergeSort

#Must implement a comparator for all sort methods.
class Sort:
    @staticmethod
    def generator(argss):
        argss.append(random.randInt(1,1000))
        return argss


if __name__ == '__main__':
    Plotter.plotter(MergeSort.sort,Sort.generator,100)
