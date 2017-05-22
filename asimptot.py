import matplotlib.pyplot as plt
import numpy as np
import math
x = [x for x in range(3, 5)]
y = [math.factorial(i**2) for i in x]
plt.plot(x, y)
plt.show()