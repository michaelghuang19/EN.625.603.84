import matplotlib.pyplot as plt
import numpy as np

chirps = np.array([20.0, 16.0, 19.8, 18.4, 17.1, 15.5, 14.7, 17.1, 15.4, 16.2, 15.0, 17.2, 16.0, 17.0, 14.4])
temperatures = np.array([88.6, 71.6, 93.3, 84.3, 80.6, 75.2, 69.7, 82.0, 69.4, 83.3, 79.6, 82.6, 80.6, 83.5, 76.3])

b, a = np.polyfit(chirps, temperatures, deg=1)

y = a + b * chirps 

plt.scatter(chirps, temperatures)
plt.plot(chirps, y)

plt.xlabel("Chirps per second")
plt.ylabel("Temperature")
plt.title("Chirps per second vs Temperature")
plt.legend()
plt.grid(True)
plt.show()