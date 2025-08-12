import matplotlib.pyplot as plt
import numpy as np

ages = np.array([0, 0.5, 1, 2, 3, 4, 5, 6, 7, 8])
proofs = np.array([104.6, 104.1, 104.4, 105.0, 106.0, 106.8, 107.7, 108.7, 110.6, 112.1])

n = len(ages)
xy_sum = sum([age * proofs[idx] for idx, age in enumerate(ages)])
x_sum = ages.sum()
y_sum = proofs.sum()
x_squared_sum = sum([age * age for age in ages])

print(f"{n=}")
print(f"{xy_sum=}")
print(f"{x_sum=}")
print(f"{y_sum=}")
print(f"{x_squared_sum=}")

b, a = np.polyfit(ages, proofs, deg=1)

y = a + b * ages 

plt.scatter(ages, proofs)
plt.plot(ages, y, label=f"Least Squares Line (y = {a:.2f} + {b:.2f}x)")

plt.xlabel("Age in years")
plt.ylabel("Proof")
plt.title("Age in years vs Proof")
plt.legend()
plt.grid(True)
plt.show()