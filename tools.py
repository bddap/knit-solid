import math
from functools import reduce

def add(vec):
    return lambda bv: [a+b for a,b in zip(vec,bv)]

def mul(scalar):
    return lambda bv: [b*scalar for b in bv]

def rot(axis, angle):
    c = math.cos(angle); s = math.sin(angle); t = 1 - c
    x,y,z = axis
    return lambda v : (
        v[0]*(t*x*x + c  ) + v[1]*(t*x*y - z*s) + v[2]*(t*x*z + y*s) ,
        v[0]*(t*x*y + z*s) + v[1]*(t*y*y + c  ) + v[2]*(t*y*z - x*s) ,
        v[0]*(t*x*z - y*s) + v[1]*(t*y*z + x*s) + v[2]*(t*z*z + c  )
    )

def distance(a,b):
    return sum((a-b)**2 for a,b in zip(a,b)) ** 0.5

def line_in(solid):
    return lambda line:all(map(solid, line))

def transforms(line_list, *vertex_transforms):
    f = reduce(lambda fa,fb:lambda x:fb(fa(x)), vertex_transforms)
    return [[f(a),f(b)] for a,b in line_list]

def everycombo(*iterables):
    if len(iterables) == 1: return [(a,) for a in iterables[0]]
    return [(a,) + b for a in iterables[0] for b in everycombo(*iterables[1:])]

def sum_l(iter_iter): #generalize the sum function to lists and tuples
    return reduce(lambda a,b:a+b, iter_iter)
