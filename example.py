def g(x):
    return h(x)

def h(x):
    return x * 7

def f(x):
    r = g(x)
    s = h(r)
    return s
