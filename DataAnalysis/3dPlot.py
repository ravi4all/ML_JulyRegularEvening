import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pandas as pd

x = np.array([i for i in range(1,301)])
y = np.random.randint(1,1000,300)
z = np.random.randint(500,1000,300)

figure = plt.figure(figsize=(10,6))
axes = Axes3D(figure)
axes.scatter(x,y,z)
plt.show()

