import matplotlib.pyplot as plt
from entities.beam import Ray
from entities.source import *
from entities.optical_elements import PlaneMirror, Dicroic, BeamSplitter
from entities.optical_table import OpticalTable
from entities.geometry import Box

table = OpticalTable(dimension=(1.2,1.2),
                     gridspacing=0.1,
                     scale=10)


for source in table.sources:
    for ray in source.generate_rays():
        ray.trace()
        ray.draw()

table.draw()