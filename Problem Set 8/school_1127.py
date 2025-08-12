import matplotlib.pyplot as plt
import numpy as np

spendings = np.array([10.0, 10.2, 10.2, 10.3, 10.3, 10.8, 11.0, 11.0, 11.2, 11.6, 12.1, 12.3, 12.6, 12.7, 12.9, 13.0, 13.9, 14.5, 14.7, 15.5, 16.4, 17.5, 18.1, 20.8, 22.4, 24.0 ])
rates = np.array([88.7, 93.2, 95.1, 94.0, 88.3, 89.9, 67.7, 90.2, 95.5, 75.2, 84.6, 85.0, 94.8, 56.1, 54.4, 97.9, 83.0, 94.0, 91.4, 94.2, 97.2, 94.4, 78.6, 87.6, 93.3, 92.3])

b, a = np.polyfit(spendings, rates, deg=1)

y = a + b * spendings 

plt.scatter(spendings, rates)
plt.plot(spendings, y, label=f"Least Squares Line (y = {a:.2f} + {b:.2f}x)")

plt.xlabel("Spending per pupil, in 1000s")
plt.ylabel("Graduation rate")
plt.title("Spending per pupil vs Graduation rate")
plt.legend()
plt.grid(True)
plt.show()