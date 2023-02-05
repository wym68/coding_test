import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def func(x, a, b, c):
    return a * np.exp(-b * x) + c

if __name__ == "__main__":
    x = np.linspace(0, 4, 50)
    y = func(x, 2.5, 1.3, 0.5)
    y_noise = 0.2 * np.random.normal(size=x.size)
    ydata = y + y_noise
    popt, pcov = curve_fit(func, x, ydata)
    plt.plot(x, ydata, 'bo', label='data with noise')
    plt.plot(x, func(x, *popt), 'r', label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))
    plt.legend()
    plt.show()

