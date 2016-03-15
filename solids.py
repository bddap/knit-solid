from tools import *

def dome(vec):
    r = distance(vec, (0,0,0))
    return 1 > r and 0.9 < r

def cube(vec):
    return not any(abs(v) > 0.8 for v in vec)

def ground(vec):
    return vec[1] <= 0


def sand(*solids):
    return lambda x: all(s(x) for s in solids)

def snot(*solids):
    return lambda x: not any(s(x) for s in solids)

def sor(*solids):
    return lambda x: any(s(x) for s in solids)

def sxor(*solids):
    return lambda x: len(() for s in solid if s(x)) == 1
