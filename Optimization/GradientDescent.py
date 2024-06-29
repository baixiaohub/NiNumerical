from math import fabs


def f(x):
    return x*x + 3*x - 1

def df(x):
    return 2*x + 3


def gradient_descent(f, df, x0, k):
    x = x0
    epsilon = 1e-4
    max_iter = 100
    while fabs(df(x)) >= epsilon and max_iter > 0:
        x = x - k*df(x)
        max_iter -= 1
    return x, f(x)

if __name__ == '__main__':
    x, fx = gradient_decent(f, df, 300, 0.1)
    print('min f(x) = x*x + 3*x - 1,  at x:{}, f(x):{}'.format(x, fx))
