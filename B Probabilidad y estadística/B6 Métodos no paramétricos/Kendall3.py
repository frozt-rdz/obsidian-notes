from scipy.stats import kendalltau

años = [2015, 2016, 2017, 2018, 2019,
        2020, 2021, 2022, 2023, 2024]

temperatura = [22.1, 22.3, 22.2, 22.5, 22.7,
               22.8, 23.0, 22.9, 23.2, 23.4]



tau, p = kendalltau(años, temperatura)

print(f"Tau = {tau:.3f}")
print(f"p = {p:.4f}")


temperatura2 = [
    22.1, 22.3, 22.3, 22.5, 22.5,
    22.8, 22.8, 22.9, 23.2, 23.4
]

tau2, p2 = kendalltau(años, temperatura2)

print(f"Tau2 = {tau2:.3f}")
print(f"p2 = {p2:.4f}")