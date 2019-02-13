from scipy.fftpack import dst, idst
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1.0, 2.0, 1.0, -1.0, 1.5])
 # scaling factor 2*N = 10
idst(dst(x, type=2), type=2)

 # no scaling factor
idst(dst(x, type=2, norm='ortho'), type=2, norm='ortho')

 # scaling factor 2*N = 10
idst(dst(x, type=3), type=3)

 # no scaling factor
idst(dst(x, type=3, norm='ortho'), type=3, norm='ortho')

 # scaling factor 2*(N+1) = 8
idst(dst(x, type=1), type=1)