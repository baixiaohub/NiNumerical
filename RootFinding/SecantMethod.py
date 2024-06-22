from math import fabs, cos, sin, exp
import matplotlib.pyplot as plt
import numpy as np

omega = 4
k = 0.7


def f(x):
    return 9 * np.exp(-k * x) * np.cos(omega * x) - 3.5


def secant(f, x0, x1, tolerance, maxIter):
    x_list = np.array([])
    y_list = np.array([])

    while maxIter > 0:
        fx0 = f(x0)
        fx1 = f(x1)
        df = (fx0 - fx1) / (x0 - x1)
        x_new = x1 - fx1 / df
        err = fabs(x_new - x1) / x_new * 100.0

        x_list = np.append(x_list, x1)
        y_list = np.append(y_list, fx1)
        x0, x1 = x1, x_new
        if err < tolerance:
            break
        else:
            --maxIter
    return x1, x_list, y_list


if __name__ == "__main__":
    x0 = 0.5
    x1 = 0.6
    root, x_list, y_list = secant(f, x0, x1, 0.01, 10)

    print("Root finding with secant method")
    print("f(x) = 9 * exp(-k * x) * cos(omega * x) - 3.5")
    print("omega = {}, k = {}".format(omega, k))
    print("=============================================")
    print("Starts with x0 = {}, x1 = {}".format(x0, x1))
    print("root is {}".format(root))

    plt.ylabel("secant method")
    x = np.linspace(0, 10, 1000)
    plt.plot(x, f(x))
    plt.plot(x_list, y_list, "o")
    plt.plot([x0, x1], [f(x0), f(x1)], 'ro')
    plt.show()
