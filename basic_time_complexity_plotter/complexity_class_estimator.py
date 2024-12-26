import numpy as np
from scipy.optimize import curve_fit
from typing import List
# TODO: Return the fit function.
# TODO: Implement the complexity estimator.
# TODO: Show the estimated time complexity under the graph title.

def constant_f(N: np.ndarray, a: float, b: float) -> float:
    return b

def logarithmic_f(N: np.ndarray, a: float, b: float) -> float:
    return a * np.log(N) + b

def linear_f(N: np.ndarray, a: float, b: float) -> float:
    return a * N + b

def NlogN_f(N: np.ndarray, a: float, b: float) -> float:
    return a * N * np.log(N) + b

def N2logN_f(N: np.ndarray, a: float, b: float) -> float:
    return a * (N**2) * np.log(N) + b

def quadratic_f(N: np.ndarray, a: float, b: float) -> float:
    return a * (N**2) + b

def cubic_f(N: np.ndarray, a: float, b: float) -> float:
    return a * (N**3) + b

def exponential_f(N: np.ndarray, a: float, b: float) -> float:
    return a * (2**N) + b

def factorial_f(N: np.ndarray, a: float, b: float) -> float:
    return a * np.sqrt(2*np.pi*N) * ((N/np.e)**N)


class ComplexityEstimator:
    '''
    Given a list of function input sizes and corresponding outputs,
    estimate the complexity of the function (closest fit from a 
    predefined list of complexities).
    '''

    CLASSES = {
        "O(1)": constant_f,
        "O(logN)": logarithmic_f,
        "O(N)": linear_f,
        "O(NlogN)": NlogN_f,
        "O(N^2logN)": N2logN_f,
        "O(N^2)": quadratic_f,
        "O(N^3)": cubic_f,
        "O(2**N)": exponential_f,
        "O(N!)": factorial_f
    }

    def __init__(self):
        pass

    @staticmethod
    def estimate_complexity(input_sizes: List[float], runtimes: List[float]) -> str:
        errors = dict()
        input_sizes = np.array(input_sizes)
        runtimes = np.array(runtimes)
        for compl_class, func in ComplexityEstimator.CLASSES.items():
            try:
                params, _ = curve_fit(func, input_sizes, runtimes)
                preds = func(input_sizes, *params)
                mean_squared_error = np.mean((preds-runtimes)**2)
                errors[compl_class] = mean_squared_error
            except Exception as e:
                print(e)
                errors[compl_class] = float('inf')
        return min(errors, key=errors.get)