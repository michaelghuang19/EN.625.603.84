import numpy as np
from scipy import stats

dates = [1543, 1600, 1665, 1746, 1774, 1830, 1858, 1864, 1896, 1901, 1905, 1926]
ages = [40, 34, 23, 40, 31, 33, 49, 33, 34, 43, 26, 39]

print(f"{len(ages)=}")

ages_mean = np.mean(ages)
ages_sd = np.std(ages, ddof=1)

print(f"{ages_mean=}")
print(f"{ages_sd=}")

ages_t_value = stats.t.ppf(0.05 / 2, 11)

print(f"{ages_t_value=}")

import matplotlib.pyplot as plt

plt.scatter(dates, ages)
plt.xlabel("Dates")
plt.ylabel("Ages")
plt.title("Dates vs Ages for Scientific Breakthroughs")
plt.grid(True)
plt.show()