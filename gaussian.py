import numpy as np
import matplotlib.pyplot as plt

values= np.random.normal(90,2, 10000)
for i in range(len(values)):
    print(values[i])
plt.hist(values,50)
plt.show()
