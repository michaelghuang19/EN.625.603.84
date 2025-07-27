import numpy as np
from scipy import stats

normal_data = [8, 4, 6, 3, 1, 4, 4, 6, 4, 2, 2, 1, 1, 4, 3, 3, 2, 6, 3, 4]
schizophrenic_data = [2, 1, 1, 3, 2, 7, 2, 1, 3, 1, 0, 2, 4, 2, 3, 3, 0, 1, 2, 2]
alpha = 0.05
normal_df = len(normal_data) - 1
schizophrenic_df = len(schizophrenic_data) - 1

normal_sample_var = np.var(normal_data, ddof=1)
schizophrenic_sample_var = np.var(schizophrenic_data, ddof=1)

print(f"{normal_sample_var=}")
print(f"{schizophrenic_sample_var=}")

f_lower_value = stats.f.ppf(alpha / 2, schizophrenic_df, normal_df)
f_upper_value = stats.f.ppf(1 - (alpha / 2), schizophrenic_df, normal_df)

print(f"{f_lower_value=}")
print(f"{f_upper_value=}")

normal_sample_mean = np.mean(normal_data)
schizophrenic_sample_mean = np.mean(schizophrenic_data)

t_critical_value = stats.t.ppf(0.025,38)

print(f"{normal_sample_mean=}")
print(f"{schizophrenic_sample_mean=}")
print(f"{t_critical_value=}")