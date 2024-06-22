from math import fabs, cos, sin, exp
import matplotlib.pyplot as plt
import numpy as np

omega = 4
k = 0.7


def f(x):
    return 9 * np.exp(-k * x) * np.cos(omega * x) - 3.5


def df(x):
    return 9 * np.exp(-k * x) * (k * np.cos(omega * x) - omega * np.sin(omega * x))


def newtown_raphson(f, df, x0, tolerance, maxIter):
    x_list = np.array([])
    y_list = np.array([])

    x = x0
    while maxIter > 0:
        fx = f(x)
        x_new = x - fx / df(x)
        err = fabs(x_new - x) / x_new * 100.0

        x_list = np.append(x_list, x)
        y_list = np.append(y_list, fx)
        x = x_new
        if err < tolerance:
            break
        else:
            --maxIter
    return x, x_list, y_list


if __name__ == "__main__":
    x0 = 0.5
    root, x_list, y_list = newtown_raphson(f, df, x0, 0.01, 10)

    print("Root finding with newtown raphson method")
    print("f(x) = 9 * exp(-k * x) * cos(omega * x) - 3.5")
    print("omega = {}, k = {}".format(omega, k))
    print("=============================================")
    print("Starts with x0 = {}".format(x0))
    print("root is {}".format(root))

    plt.ylabel("newtown_raphson")
    x = np.linspace(0, 10, 1000)
    plt.plot(x, f(x))
    plt.plot(x_list, y_list, "o")
    plt.plot(x0, f(x0), 'ro')
    plt.show()
