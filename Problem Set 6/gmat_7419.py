import numpy as np
from scipy import stats

gmat_y_i = [35, 37, 33, 34, 38, 40, 35, 36, 38, 33, 28, 34, 47, 42, 46]
gmat_y_i_squared = [1225, 1369, 1089, 1156, 1444, 1600, 1225,  1296, 1444, 1089, 784, 1156, 2209, 1764, 2116]

gmat_y_i_sum = np.sum(gmat_y_i)
gmat_y_i_squared_sum = np.sum(gmat_y_i_squared)

print(f"{gmat_y_i_sum=}")
print(f"{gmat_y_i_squared_sum=}")

gmat_y_i_mean = np.mean(gmat_y_i)
gmat_y_i_std = np.std(gmat_y_i, ddof = 1)

print(f"{gmat_y_i_mean=}")
print(f"{gmat_y_i_std=}")

gmat_t_value = stats.t.ppf(0.05 / 2, 14)

print(f"{gmat_t_value=}")

gmat_p_value = 2 * stats.t.sf(abs(-2.24997405871), df=14)

print(f"{gmat_p_value=}")