import numpy as np
import time
import matplotlib.pyplot as plt
def f(x, N):
    return np.sin(np.pi * x / N)

N = 11

x_values = np.linspace(-10, 10, 1000)

start_time_numpy = time.time()
y_values_numpy = f(x_values, N)
end_time_numpy = time.time()

y_values_part1 = np.sin(np.pi * x_values / N)

print("NumPy result (first 5 values):", y_values_numpy[:5])
print("Results from Part 1 (first 5 values):", y_values_part1[:5])

comparison = np.allclose(y_values_numpy, y_values_part1)
print("Results match:", comparison)

print("NumPy execution time:", end_time_numpy - start_time_numpy, "seconds")

plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values_part1, label="Results from Part 1")
plt.plot(x_values, y_values_numpy, label="NumPy")
plt.title("Comparison of NumPy and Part 1 Results")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.show()