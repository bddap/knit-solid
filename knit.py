import json
from tools import *
from primitives import *
import solids as s

def knit(solid):
    a = range(-10,10)

    a = everycombo(a,a,a)

    a = [(b,a,c) for a,b,c in a]

    a = [transforms( octahedron(), add(v) ) for v in a]

    a = sum_l(a)

    a = transforms(a, mul(0.1))


    a = filter(line_in(solid), a)

    return list(a)

if __name__ == '__main__':

    #sky = s.snot( s.ground )

    #anticube = s.snot( s.cube )

    #shape = s.sand( s.dome, sky, s.cube, s.ground )

    sky = s.snot(s.ground)

    shape = s.sand( s.dome, s.cube, sky )

    json.dump(knit(shape), open("sweater.json", 'w'), indent=1)
