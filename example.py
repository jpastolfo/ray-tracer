from entities.optical_table import OpticalTable
from entities.source import PointSource, BoxSource
from entities.geometry import Box

from entities.optical_elements import PlaneMirror,Dicroic


table = OpticalTable(dimension=(1.2,1.2),
                     gridspacing=0.1,
                     scale=10)

## SOURCES
source_ir0 = BoxSource(table,
                       position=(0.2,0.7),
                       dimension=(0.1,0.025),
                       orientation=-90,
                       wavelength=1064,divergence=0,
                       color="red",
                       max_collisions=6,
                       n_rays=1)

source_ir1 = BoxSource(table,
                       position=(1.0,0.7),
                       dimension=(0.1,0.025),
                       orientation=-90,
                       wavelength=1064,divergence=0,
                       color="red",max_collisions=6,n_rays=1)

source_verdi = BoxSource(table,
                         position=(0.1,0.1),
                         dimension=(0.2,0.05),
                         orientation=-0,
                         wavelength=450,divergence=0,
                         color="green",max_collisions=5,
                         n_rays=1)

point_source = PointSource(table,
                           position=(0.65,1.1),
                           divergence=0,
                           orientation=180,
                           color="green",wavelength=400,
                           max_collisions=4)

point_source = PointSource(table,
                           position=(0.6,1.1),
                           divergence=0,
                           orientation=0,
                           color="red",wavelength=400,
                           max_collisions=4,linestyle="dashed")


## GEOMETRY
spectrometer = Box(table,
                   position=(0.05,0.4),
                   dimension=(0.1,0.2),
                   orientation=0)

spectrometer2 = Box(table,
                    position=(1.1,0.2),
                    dimension=(0.15,0.2),
                    orientation=0)

camera = Box(table,
             position=(1.15,0.075),
             dimension=(0.05,0.05),
             orientation=90)

dac = Box(table,
          position=(0.6,1.1),
          dimension=(0.03,0.03),
          orientation=90)

### OPTICAL ELEMENTS
mirror0 = PlaneMirror(table,
                      position=(0.3,0.1),
                      orientation=60,
                      size=0.05)

mirror1 = Dicroic(table,
                  position=(0.24,0.2),
                  orientation=-120,
                  size=0.05,
                  wavelength_range=[450,500])

mirror2 = PlaneMirror(table,
                      position=(0.55,0.2),
                      orientation=45,
                      size=0.05)

mirror3 = PlaneMirror(table,
                      position=(0.55,1.1),
                      orientation=-135,
                      size=0.05)

mirror4 = PlaneMirror(table,
                      position=(0.65,1.1),
                      orientation=135,
                      size=0.05)

# SPRECTOMETER MIRROR
mirror5 = PlaneMirror(table,
                      position=(0.05,0.2),
                      orientation=-45,
                      size=0.05)

mirror6 = PlaneMirror(table,
                      position=(0.05,0.3),
                      orientation=0,
                      size=0.001)

mirror3 = PlaneMirror(table,
                      position=(0.65,0.2),
                      orientation=-45,
                      size=0.05)

mirror6 = PlaneMirror(table,
                      position=(1.1,0.2),
                      orientation=90,
                      size=0.001)

### INFRA-RED MIRRORS
mirror_ir0_0 = PlaneMirror(table,
                           position=(0.2,0.4),
                           orientation=-45,
                           size=0.05)

mirror_ir0_1 = PlaneMirror(table,
                           position=(0.3,0.4),
                           orientation=45,
                           size=0.05)

mirror_ir0_2 = PlaneMirror(table,
                           position=(0.3,0.7),
                           orientation=-135,
                           size=0.05)

mirror_ir0_3 = Dicroic(table,
                       position=(0.55,0.7),
                       orientation=45,
                       wavelength_range=[1000,1100],
                       size=0.05)

mirror_ir1_0 = PlaneMirror(table,
                           position=(1.0,0.4),
                           orientation=45,
                           size=0.05)

mirror_ir1_1 = PlaneMirror(table,
                           position=(0.9,0.4),
                           orientation=-45,
                           size=0.05)

mirror_ir1_2 = PlaneMirror(table,
                           position=(0.9,0.7),
                           orientation=135,
                           size=0.05)

mirror_ir1_3 = Dicroic(table,
                       position=(0.65,0.7),
                       orientation=-45,
                       wavelength_range=[1000,1100],
                       size=0.05)

from utils import stl_exporter
### RAY-TRACING
for source in table.sources:
    rays = source.generate_rays()
    for ray in rays:
        ray.trace()
        ray.draw()
        stl_exporter.create(ray,n_vertices=11,radius=0.01)


table.draw()