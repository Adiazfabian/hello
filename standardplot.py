import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 100) #Crea una lista
plt.plot(x, np.sin(x))
plt.show()
