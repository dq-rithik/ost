import numpy as np 
import matplotlib.pyplot as plt

x = np.linspace(0,2 * np.pi,100)
y = np.sin(x)

plt.plot(x,y,'bo')
plt.xlabel('X')
plt.ylabel('Y')
plt.title("Sine curve")
plt.show()