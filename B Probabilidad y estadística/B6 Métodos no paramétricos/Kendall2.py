from scipy.stats import kendalltau

años = [2018, 2019, 2020, 2021, 2022, 2023, 2024]

ndvi = [0.45, 0.47, 0.46, 0.50, 0.51, 0.53, 0.54]

tau, p = kendalltau(años, ndvi)

print(f"Tau = {tau:.3f}")
print(f"p-value = {p:.4f}")