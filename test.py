import sys,os

import matplotlib.pyplot as plt
from entities.beam import Ray
from entities.source import *
from entities.optical_elements import PlaneMirror

sys.path.append("/home/astolfo/Projects/ray-tracer/test.py")


plt.figure()

#source = Source(-5,0,0,"red")
lamp = Lamp(-5,0,"red",100)
mirror0 = PlaneMirror(0,0,40,4)
mirror1 = PlaneMirror(0,5,-135,6)
mirror2 = PlaneMirror(5,5,135,10)
mirror3 = PlaneMirror(5,0,-45,4)

objects = [mirror0,mirror1,mirror2,mirror3]

for ray in lamp.generate_rays():
    ray.trace(objects)
    ray.draw()


plt.xlim(-10,10)
plt.ylim(-10,10)
plt.show()