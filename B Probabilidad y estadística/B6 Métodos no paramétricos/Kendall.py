from scipy.stats import kendalltau

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

tau, p_value = kendalltau(x, y)

print("Tau:", tau)
print("p-value:", p_value)
