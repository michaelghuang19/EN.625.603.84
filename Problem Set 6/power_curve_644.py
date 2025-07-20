import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

curve_z_value = stats.norm.ppf(0.05 / 2)

print(f"{curve_z_value=}")

mean_values = np.linspace(50, 70, 200)
beta_values = stats.norm.cdf(58.04 - mean_values) + (1 - stats.norm.cdf(61.96 - mean_values))

plt.plot(mean_values, beta_values)
plt.xlabel("Mean")
plt.ylabel("Power")
plt.title("6.4.4 Power Curve")
plt.grid(True)
plt.show()