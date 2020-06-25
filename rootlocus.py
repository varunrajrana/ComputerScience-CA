import numpy as np
from matplotlib import pyplot as plt 
import control

G = control.TransferFunction((1,1), (1,5,6,0))

rlist, klist = control.rlocus(G, kvect=np.linspace(100.0, -100.0, num=1000))

plt.show()
