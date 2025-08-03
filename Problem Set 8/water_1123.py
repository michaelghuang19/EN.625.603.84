import matplotlib.pyplot as plt
import numpy as np

temperatures = np.array([0, 4, 10, 15, 21, 29, 36, 51, 68])
parts = np.array([66.7, 71.0, 76.3, 80.6, 85.7, 92.9, 99.4, 113.6, 125.1])

b, a = np.polyfit(temperatures, parts, deg=1)

y = a + b * temperatures 

residuals = parts - y

plt.scatter(temperatures, residuals)
plt.xlabel("Temperature")
plt.ylabel("Residuals")
plt.title("Residual plot for Temperature vs Parts Dissolved")
plt.legend()
plt.grid(True)
plt.show()