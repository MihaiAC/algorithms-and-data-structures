import os
import time
import matplotlib.pyplot as plt
from typing import Callable, Generator, List, Any
from functools import partial

class Plotter:
    """
    Attempts to plot the time complexity for the provided function.
    The function should have only one input whose size variation we're interested in.
    """
    def __init__(self, 
                 func: Callable[..., Any], 
                 generator: Generator[List[Any], None, None], 
                 get_size: Callable[..., int],
                 save_path: str,
                 fig_name: str):
        """
        func      = function whose time complexity we want to plot;
        generator = a generator that generates inputs for func;
                    consequent inputs should linearly grow in size;
        get_size  = function that takes in a function input and returns an int signifying its size;
        save_path = directory in which the plot should be saved;
        fig_name  = output file name
        """
        self.func = func
        self.generator = generator
        self.get_size = get_size
        self.save_path = save_path
        self.fig_name = fig_name

        # Run every input REPEATS times + take the average time.
        self.REPEATS = 1

    def plot(self):
        input_sizes = []
        run_times = []
        for curr_args in self.generator():
            total_time = 0
            for _ in range(self.REPEATS):
                start_time = time.time()
                self.func(*curr_args)
                total_time += time.time() - start_time
            total_time = total_time/self.REPEATS

            run_times.append(total_time)
            input_sizes.append(self.get_size(*curr_args))
        
        # Create save_dir if it doesn't exist.
        if not os.path.isdir(self.save_path):
            os.makedirs(self.save_path)

        # Generate + save the plot.
        plt.figure(figsize=(10, 10))
        plt.scatter(input_sizes, run_times, color='black')
        plt.title('Time complexity for ' + self.func.__name__)
        plt.xlabel('Input size')
        plt.ylabel('Time')
        plt.savefig(self.save_path + self.fig_name)

# Example usage
if __name__ == '__main__':
    import numpy as np
    # Function to be timed
    func = sorted

    # Generator
    def gen():
        for size in range(100, 100000, 500):
            func_input = list(np.random.randint(low=0, high=size, size=size))
            yield [func_input]

    get_size = len
    save_path = './'
    fig_name = 'Simple plot'

    plotter = Plotter(func, gen, get_size, save_path, fig_name)
    plotter.plot()
    
