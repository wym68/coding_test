import numpy as np
from scipy.optimize import minimize

def objective_function(x):
    # 定义目标函数
    return x[0]**2 + x[1]**2

initial_guess = [5, 5]
result = minimize(objective_function, initial_guess, method='Nelder-Mead')

print(result.x)

