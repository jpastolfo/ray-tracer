from entities.optical_table import OpticalTable
from entities.source import PointSource, BoxSource
from entities.geometry import Box

from entities.optical_elements import PlaneMirror,Dicroic


table = OpticalTable(length=1.2,
                     width=1.2,
                     gridspacing=0.1,
                     scale=10)

## SOURCES
source_ir0 = BoxSource(table,
                       x=0.2,y=0.7,
                       length=0.1,width=0.025,orientation=-90,
                       wavelength=1064,divergence=0,
                       color="red",
                       max_collisions=6)

source_ir1 = BoxSource(table,
                       x=1.0,y=0.7,
                       length=0.1,width=0.025,orientation=-90,
                       wavelength=1064,divergence=0,
                       color="red",max_collisions=6)

source_verdi = BoxSource(table,
                         x=0.1,y=0.1,
                         length=0.2,width=0.05,orientation=0,
                         wavelength=450,divergence=0,
                         color="green",max_collisions=5)

point_source = PointSource(table,x=0.65,y=1.1,
                           divergence=0,
                           orientation=180,
                           color="green",wavelength=400,
                           max_collisions=4)

point_source = PointSource(table,x=0.6,y=1.1,
                           divergence=0,
                           orientation=0,
                           color="red",wavelength=400,
                           max_collisions=4,linestyle="dashed")


## GEOMETRY
spectrometer = Box(table,x=0.05,y=0.4,
                   length=0.1,width=0.2,orientation=0)

spectrometer2 = Box(table,x=1.1,y=0.2,
                    length=0.15,width=0.2,orientation=0)

camera = Box(table,x=1.15,y=0.075,
            length=0.05,width=0.05,orientation=90)

dac = Box(table,x=0.6,y=1.1,
            length=0.03,width=0.03,orientation=90)



### OPTICAL ELEMENTS
mirror0 = PlaneMirror(table,
                      x=0.3,
                      y=0.1,
                      orientation=60,
                      size=0.05)

mirror1 = Dicroic(table,
                      x=0.24,
                      y=0.2,
                      orientation=-120,
                      size=0.05,
                      wavelength_range=[450,500])

mirror2 = PlaneMirror(table,
                      x=0.55,
                      y=0.2,
                      orientation=45,
                      size=0.05)

mirror3 = PlaneMirror(table,x=0.55,
                      y=1.1,
                      orientation=-135,
                      size=0.05)

mirror4 = PlaneMirror(table,x=0.65,
                      y=1.1,
                      orientation=135,
                      size=0.05)

# SPRECTOMETER MIRROR
mirror5 = PlaneMirror(table,x=0.05,
                      y=0.2,
                      orientation=-45,
                      size=0.05)

mirror6 = PlaneMirror(table,x=0.05,
                      y=0.3,
                      orientation=0,
                      size=0.001)

mirror3 = PlaneMirror(table,x=0.65,
                      y=0.2,
                      orientation=-45,
                      size=0.05)

mirror6 = PlaneMirror(table,x=1.1,
                      y=0.2,
                      orientation=90,
                      size=0.001)

### INFRA-RED MIRRORS
mirror_ir0_0 = PlaneMirror(table,x=0.2,
                         y=0.4,
                         orientation=-45,
                         size=0.05)

mirror_ir0_1 = PlaneMirror(table,x=0.3,
                         y=0.4,
                         orientation=45,
                         size=0.05)

mirror_ir0_2 = PlaneMirror(table,
                           x=0.3,
                           y=0.7,
                           orientation=-135,
                           size=0.05)

mirror_ir0_3 = Dicroic(table,
                       x=0.55,
                       y=0.7,
                       orientation=45,
                       wavelength_range=[1000,1100],
                       size=0.05)

mirror_ir1_0 = PlaneMirror(table,
                           x=1.0,
                           y=0.4,
                           orientation=45,
                           size=0.05)

mirror_ir1_1 = PlaneMirror(table,
                           x=0.9,
                           y=0.4,
                           orientation=-45,
                           size=0.05)

mirror_ir1_2 = PlaneMirror(table,
                           x=0.9,
                           y=0.7,
                           orientation=135,
                           size=0.05)

mirror_ir1_3 = Dicroic(table,
                       x=0.65,
                       y=0.7,
                       orientation=-45,
                       wavelength_range=[1000,1100],
                       size=0.05)


### RAY-TRACING
for source in table.sources:
    rays = source.generate_rays()
    for ray in rays:
        ray.trace()
        ray.draw()

table.draw()