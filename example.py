from entities.optical_table import OpticalTable
from entities.source import PointSource

from entities.optical_elements import PlaneMirror,Dicroic


table = OpticalTable(length=1.2,
                     width=1.2,
                     gridspacing=0.1,
                     scale=10)

## SOURCES
source_ir0 = PointSource(table,
                         x=0.2,
                         y=0.7,
                         orientation=-90,
                         wavelength=1064,
                         divergence=0,
                         color="red")

source_ir1 = PointSource(table,
                         x=1.0,
                         y=0.7,
                         orientation=-90,
                         wavelength=1064,
                         divergence=0,
                         color="red",
                         n_rays=1)

source_verdi = PointSource(table,
                           x=0.1,
                           y=0.1,
                           orientation=0,
                           wavelength=450,
                           divergence=0,
                           color="green")

### OPTICAL ELEMENTS
mirror0 = PlaneMirror(table,
                      x=0.3,
                      y=0.1,
                      orientation=60,
                      size=0.05)

mirror1 = PlaneMirror(table,
                      x=0.24,
                      y=0.2,
                      orientation=-120,
                      size=0.05)

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