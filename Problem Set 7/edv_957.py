import numpy as np
from scipy import stats

normal_data = [62, 60, 78, 62, 49, 67, 80, 48]
constrictive_data = [24, 56, 42, 74, 44, 28]
alpha = 0.05
normal_df = len(normal_data) - 1
constrictive_df = len(constrictive_data) - 1

normal_sample_var = np.var(normal_data, ddof=1)
constrictive_sample_var = np.var(constrictive_data, ddof=1)

var_ratio = normal_sample_var / constrictive_sample_var

f_lower_value = stats.f.ppf(alpha / 2 , normal_df, constrictive_df)
f_upper_value = stats.f.ppf(1 - (alpha / 2), constrictive_df, normal_df)

ci_lower_value = var_ratio * f_lower_value
ci_upper_value = var_ratio * f_upper_value

print(f"{normal_sample_var=}")
print(f"{constrictive_sample_var=}")
print(f"{var_ratio=}")

print(f"{ci_lower_value=}")
print(f"{ci_upper_value=}")