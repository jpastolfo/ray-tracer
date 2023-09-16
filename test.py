import matplotlib.pyplot as plt
from entities.beam import Beam
from entities.entities import Source
from entities.optical_elements import Mirror

plt.figure()

beam = Beam("red")
source = Source(0,0,0)
mirror = Mirror(2,0,45,2)
mirror1 = Mirror(2,2,15,1)
mirror2 = Mirror(-2,-5,-60,4)

path = [source,mirror,mirror1,mirror2]
beam.append_to_path(*path)
beam.trace()

plt.show()