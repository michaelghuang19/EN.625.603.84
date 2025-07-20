from scipy import stats

k_t_value = stats.t.ppf(0.05 / 2, 10)

print(f"{k_t_value=}")