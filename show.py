try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk
import json, math, threading, time, atexit

class Rendering(object):
    def __init__(s, filename):
        s.R = tk.Tk()
        s.C = tk.Canvas(bg='#555555'); s.C.pack(expand=True, fill='both')
        s.dat = json.load(open(filename))
        s.ls = [s.C.create_line(0,0,0,0) for _ in s.dat]
        s.xrot, s.yrot = 0, 0
        s.callbacks()

    def callbacks(s):
        s.C.bind('<Configure>', lambda _:s.show())

    def show(s):
        w, h = s.C.winfo_width()/2, s.C.winfo_height()/2
        sc = min(w,h)
        def to_canvas(vv):
            (x0,y0,_),(x1,y1,_) = vv
            return (sc*x0+w, -sc*y0+h, sc*x1+w, -sc*y1+h, )
        for line, loc in zip(s.ls, s.calc_rot()):
            s.C.coords(line, *to_canvas(loc))

    def calc_rot(s):
        def mult(m0,m1):
            return [[
                    sum(a*b for a, b in zip(ra, cb))
                for cb in zip(*m1)]
            for ra in m0]

        def rotation(angle, axis):
            c = math.cos(angle); s = math.sin(angle); t = 1 - c
            x,y,z = axis
            return [
                [t*x*x + c  ,   t*x*y - z*s,   t*x*z + y*s ],
                [t*x*y + z*s,	t*y*y + c  ,   t*y*z - x*s ],
                [t*x*z - y*s,	t*y*z + x*s,   t*z*z + c   ]
            ]

        m = mult( rotation(s.xrot, (1,0,0)), rotation(s.yrot, (0,1,0)) )
        def trans(vec):
            return [sum(v*r for v,r in zip(vec,ro)) for ro in m]

        return [[trans(v0), trans(v1)] for v0,v1 in s.dat]

r = Rendering("sweater.json")

start = time.time()
time.elapsed = lambda : time.time() - start

def upd():
    i = 0
    while True:
        r.xrot = 0.2
        r.yrot = time.elapsed() / 10
        r.show()
u = threading.Thread(target=upd); u.setDaemon(True); u.start()

tk.mainloop()
