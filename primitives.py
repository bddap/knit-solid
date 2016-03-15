import json
import random

b,t,c = -0.5,0.5,0  #botom top center (also a crypto currency)

rp = lambda : [random.random()*2-1 for _ in range(3)]
rl = lambda : [rp(), rp()]

def cube():
    return [
        [[t,t,t],[b,t,t]],
        [[b,t,t],[b,t,b]],
        [[b,t,b],[t,t,b]],
        [[t,t,b],[t,t,t]],
        [[t,b,t],[b,b,t]],
        [[b,b,t],[b,b,b]],
        [[b,b,b],[t,b,b]],
        [[t,b,b],[t,b,t]],
        [[t,b,t],[t,t,t]],
        [[b,b,t],[b,t,t]],
        [[b,b,b],[b,t,b]],
        [[t,b,b],[t,a,b]],
    ]

def pyramid():
    return [
        [[t,c,t],[b,c,t]],
        [[b,c,t],[b,c,b]],
        [[b,c,b],[t,c,b]],
        [[t,c,b],[t,c,t]],
        [[c,t,c],[t,c,t]],
        [[c,t,c],[b,c,t]],
        [[c,t,c],[b,c,b]],
        [[c,t,c],[t,c,b]],
    ]

def octahedron():
    return [
        [[b,c,b],[t,c,b]],
        [[t,c,b],[t,c,t]],
        [[t,c,t],[b,c,t]],
        [[b,c,t],[b,c,b]],
        [[c,t,c],[b,c,b]],
        [[c,t,c],[t,c,b]],
        [[c,t,c],[t,c,t]],
        [[c,t,c],[b,c,t]],
        [[c,b,c],[b,c,b]],
        [[c,b,c],[t,c,b]],
        [[c,b,c],[t,c,t]],
        [[c,b,c],[b,c,t]],
    ]
