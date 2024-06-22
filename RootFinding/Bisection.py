from math import fabs, cos, sin, exp, log
import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return np.log(x**4) - 0.7


def bisection(f, xl, xr, tolerance, maxIter):
    if(f(xl) * f(xr)) > 0 :
        print("Besection search failed!")
        return None

    x_list = np.array([xl, xr])
    y_list = np.array([f(xl), f(xr)])

    xm = 0
    while maxIter > 0:
        xm_old = xm
        xm = 0.5 * (xl + xr)
        fxl = f(xl)
        fxr = f(xr)
        fxm = f(xm)

        if(fxm * fxl) > 0: xl = xm
        else: xr = xm
        err = fabs(xm - xm_old) / xm * 100.0

        x_list = np.append(x_list, xm)
        y_list = np.append(y_list, fxm)
        if err < tolerance:
            break
        else:
            maxIter-=1
    return xm, x_list, y_list


if __name__ == "__main__":
    xl = 0.5
    xr = 2.0
    root, x_list, y_list = bisection(f, xl, xr, 0.0001, 1000)

    print("Root finding with bisection method")
    print("f(x) log(x**4) - 0.7")
    print("Starts with xl = {}, xr = {}".format(xl, xr))
    print("root is {}".format(root))

    plt.ylabel("bisection method")
    x = np.linspace(-10, 10, 1000)
    plt.plot(x, f(x))
    plt.axhline(y = 0.0, color = 'orange', linestyle = '-') 
    plt.plot(x_list, y_list, "o")
    plt.plot([xl, xr], [f(xl), f(xr)], 'ro')
    plt.show()
