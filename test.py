import matplotlib.pyplot as plt
from entities.beam import Ray
from entities.source import *
from entities.optical_elements import PlaneMirror, BeamSplitter
from entities.optical_table import OpticalTable

table = OpticalTable(3,2,gridspacing=0.2,scale=5)

divSource = PointSource(table,0,1,0,100,5,color="red",n_rays=11)
mirror0 = PlaneMirror(table,0.5,1,45,0.2)
mirror1 = PlaneMirror(table,0.5,1.5,-135,0.2)
mirror2 = PlaneMirror(table,1.5,1.5,135,0.2)
mirror3 = PlaneMirror(table,1.5,1,-45,0.2)

for ray in divSource.generate_rays():
    ray.trace()
    ray.draw()

table.draw()