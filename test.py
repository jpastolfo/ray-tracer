import sys,os

import matplotlib.pyplot as plt
from entities.beam import Ray
from entities.source import *
from entities.optical_elements import PlaneMirror
from entities.optical_table import OpticalTable


table = OpticalTable(3,2,gridspacing=0.2,scale=5)

divSource = DivergentSource(0,1,0.1,"red",n_rays=5)
mirror0 = PlaneMirror(0.5,1,45,0.1)
mirror1 = PlaneMirror(0.5,1.5,-135,0.1)
mirror2 = PlaneMirror(1.5,1.5,135,0.1)
mirror3 = PlaneMirror(1.5,1,-45,0.1)

objects = [mirror0,mirror1,mirror2,mirror3]

for ray in divSource.generate_rays():
    ray.trace(objects)
    ray.draw()

table.draw()