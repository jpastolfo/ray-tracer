import matplotlib.pyplot as plt
from entities.beam import Ray
from entities.source import *
from entities.optical_elements import PlaneMirror, Dicroic, BeamSplitter
from entities.optical_table import OpticalTable
from entities.geometry import Box

import utils.stl_exporter as stl_exporter

table = OpticalTable(dimension=(2.7,1.5),
                     gridspacing=0.025,
                     scale=10)

### INFRA RED 0
ir_0 = BoxSource(table,
                       position=(0.55,1.3),
                       dimension=(0.2,0.05),
                       orientation=-90,
                       wavelength=1064,divergence=0,
                       color="red",
                       max_collisions=40,
                       n_rays=1)

mirror_ir0_0 = PlaneMirror(table,
                            position=(0.55,0.8),
                            orientation=-45,
                            size=0.05)

mirror_ir0_1 = PlaneMirror(table,
                            position=(0.65,0.8),
                            orientation=45,
                            size=0.05)

pishaper_0 = Box(table,
                 position=(0.65,1.0),
                 orientation=90,
                 dimension=(0.1,0.025))

beamexpander_0 = Box(table,
                 position=(0.65,1.15),
                 orientation=90,
                 dimension=(0.05,0.025))

mirror_ir0_1 = PlaneMirror(table,
                            position=(0.65,1.4),
                            orientation=-135,
                            size=0.05)

### INFRA RED 1
ir_1 = BoxSource(table,
                position=(1.95,1.3),
                dimension=(0.2,0.05),
                orientation=-90,
                wavelength=1064,divergence=0,
                color="red",
                max_collisions=40,
                n_rays=1)

mirror_ir0_0 = PlaneMirror(table,
                            position=(1.95,0.8),
                            orientation=45,
                            size=0.05)

mirror_ir0_1 = PlaneMirror(table,
                            position=(1.85,0.8),
                            orientation=-45,
                            size=0.05)

pishaper_1 = Box(table,
                 position=(1.85,1.0),
                 orientation=90,
                 dimension=(0.1,0.025))

beamexpander_1 = Box(table,
                 position=(1.85,1.15),
                 orientation=90,
                 dimension=(0.05,0.025))

mirror_ir0_1 = PlaneMirror(table,
                            position=(1.85,1.4),
                            orientation=-45,
                            size=0.05)

### RGB Lasers
laser_green = BoxSource(table,
                       position=(0.5,0.6),
                       dimension=(0.1,0.05),
                       orientation=0,
                       wavelength=500,divergence=0,
                       color="green",
                       max_collisions=40,
                       n_rays=1)

laser_blue = BoxSource(table,
                       position=(0.5,0.5),
                       dimension=(0.1,0.05),
                       orientation=0,
                       wavelength=1064,divergence=0,
                       color="blue",
                       max_collisions=2,
                       n_rays=1)

laser_red = BoxSource(table,
                       position=(0.5,0.4),
                       dimension=(0.1,0.05),
                       orientation=0,
                       wavelength=1064,divergence=0,
                       color="red",
                       max_collisions=2,
                       n_rays=1)

### LED 0
led_0 = BoxSource(table,
                    position=(0.9,1.05),
                    dimension=(0.1,0.025),
                    orientation=0,
                    wavelength=1070,divergence=0,
                    color="yellow",
                    max_collisions=5)

pellicle_0 = Dicroic(table,
                    position=(1.2,1.05),
                    orientation=-45,
                    size=0.05,
                    wavelength_range=[1069,1070])

pellicle_1 = Dicroic(table,
                    position=(1.2,0.95),
                    orientation=45,
                    size=0.05,
                    wavelength_range=[1069,1070])

red_filters_1 = Dicroic(table,
                    position=(0.95,0.95),
                    orientation=90,
                    size=0.05,
                    wavelength_range=[1068,1069])

filter_0 = Box(table,
               position=(0.85,0.925),
               orientation=0,
               dimension=(0.025,0.1))

mirror_led_0 = PlaneMirror(table,
                            position=(0.8,0.95),
                            orientation=45,
                            size=0.05)

end_led_0 = PlaneMirror(table,
                            position=(0.8,0.85),
                            orientation=0,
                            size=0.0001)

camera_0 = Box(table,
               position=(0.8,0.85),
               orientation=0,
               dimension=(0.05,0.05))


### LED 1
led_1 = BoxSource(table,
                    position=(1.6,1.05),
                    dimension=(0.1,0.025),
                    orientation=180,
                    wavelength=1070,divergence=0,
                    color="yellow",
                    max_collisions=5)

pellicle_0 = Dicroic(table,
                    position=(1.3,1.05),
                    orientation=45,
                    size=0.05,
                    wavelength_range=[1069,1070])

pellicle_1 = Dicroic(table,
                    position=(1.3,0.95),
                    orientation=-45,
                    size=0.05,
                    wavelength_range=[1069,1070])

red_filters_1 = Dicroic(table,
                    position=(1.55,0.95),
                    orientation=90,
                    size=0.05,
                    wavelength_range=[1068,1069])

filter_1 = Box(table,
               position=(1.65,0.925),
               orientation=0,
               dimension=(0.025,0.1))

mirror_led_0 = PlaneMirror(table,
                            position=(1.7,0.95),
                            orientation=-45,
                            size=0.05)

end_led_0 = PlaneMirror(table,
                            position=(1.7,0.85),
                            orientation=0,
                            size=0.0001)

camera_0 = Box(table,
               position=(1.7,0.85),
               orientation=0,
               dimension=(0.05,0.05))


### 
mirror_g0 = PlaneMirror(table,
                      position=(0.7,0.6),
                      orientation=45,
                      size=0.05)

mirror_b0 = PlaneMirror(table,
                      position=(0.7,0.5),
                      orientation=45,
                      size=0.05)

mirror_r0 = PlaneMirror(table,
                      position=(0.7,0.4),
                      orientation=45,
                      size=0.05)

mirror_g1 = PlaneMirror(table,
                      position=(0.7,0.65),
                      orientation=-135,
                      size=0.05)

dicroic_g0 = Dicroic(table,
                     position=(1.2,0.65),
                     orientation=45,
                     size=0.05,
                     wavelength_range=[0,1000])



dicroic_g1 = Dicroic(table,
                    position=(1.2,1.4),
                    orientation=-135,
                    size=0.05,
                    wavelength_range=[1064,1070])

dicroic_g1 = Dicroic(table,
                    position=(1.3,1.4),
                    orientation=-45,
                    size=0.05,
                    wavelength_range=[1064,1070])


### SPECTROMETER
spectrometer = Box(table,
                   position=(0.2,1.0),
                   orientation=0,
                   dimension=(0.3,0.25))

spectrometer_camera = Box(table,
                          position=(0.4,1.05),
                          orientation=0,
                          dimension=(0.1,0.1))

filter_wheel_0 = Box(table,
                   position=(0.175,0.8),
                   orientation=90,
                   dimension=(0.025,0.15))

filter_wheel_1 = Box(table,
                   position=(0.175,0.75),
                   orientation=90,
                   dimension=(0.025,0.15))


mirror_0 = PlaneMirror(table,
                position=(0.2,0.2),
                orientation=-45,
                size=0.05)

mirror_1 = PlaneMirror(table,
                position=(1.2,0.2),
                orientation=45,
                size=0.05)

end_spectrometer = PlaneMirror(table,
                position=(0.2,1.0),
                orientation=0,
                size=0.00001)

source_1 = PointSource(table,
                       position=(1.2,0.65),
                       divergence=0,
                       orientation=-90,
                       color="green",
                       max_collisions=4)




for source in table.sources:
    rays = source.generate_rays()
    for ray in rays:
        ray.trace()
        ray.draw()
        #stl_exporter.create(ray,n_vertices=4,radius=0.01)


table.draw()