import matplotlib.pyplot as plt
from entities.beam import Ray
from entities.source import *
from entities.optical_elements import PlaneMirror, BeamSplitter
from entities.optical_table import OpticalTable
from entities.geometry import Box

table = OpticalTable(5,5,gridspacing=0.2,scale=5)

source_verdi = BoxSource(table,x=0.4,y=0.4,
                      length=0.50,width=0.25,orientation=0,
                      wavelength=1000,divergence=0,
                      color="green",n_rays=0)

source_ir = BoxSource(table,x=3.7,y=3.9,
                      length=1.0,width=0.15,orientation=-90,
                      wavelength=1000,divergence=0,
                      color="red",n_rays=1)

spectrometer = Box(table,x=0.3,y=2.5,
                   length=1.0,width=0.25,orientation=90)

spectrometer2 = Box(table,x=4.6,y=1.8,
                    length=1.0,width=0.75,orientation=90)

camera = Box(table,x=4.8,y=0.9,
            length=0.75,width=0.25,orientation=90)

dac = Box(table,x=2.1,y=4.9,
            length=0.1,width=0.1,orientation=90)




mirror0 = PlaneMirror(table,1.4,0.40,-120,0.1)
mirror1 = PlaneMirror(table,1.1,0.9,60,0.2)
mirror2 = PlaneMirror(table,1.9,0.9,-135,0.2)
mirror3 = PlaneMirror(table,1.9,4.9,45,0.1)
mirror4 = PlaneMirror(table,2.3,4.9,-45,0.1)
mirror5 = PlaneMirror(table,2.3,3.3,-45,0.2)
mirror6 = PlaneMirror(table,3.3,3.3,135,0.2)
mirror7 = PlaneMirror(table,3.3,1.7,-45,0.2)
mirror8 = PlaneMirror(table,3.7,1.7,45,0.2)


for source in table.sources:
    for ray in source.generate_rays():
        ray.trace()
        ray.draw()

table.draw()