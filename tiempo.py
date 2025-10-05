import random
import time
import matplotlib.pyplot as plt

def min_operations(colors):
    n = len(colors)
    if n == 0:
        return 0
    memo = [[-1]*n for _ in range(n)]

    def dp(l, r):
        if l > r:
            return 0
        if l == r:
            return 1
        if memo[l][r] != -1:
            return memo[l][r]

        # Caso 1
        best = 1 + dp(l+1, r)

        # Caso2
        for k in range(l+1, r+1):
            if colors[l] == colors[k]:
                if k == l+1:
                    best = min(best, 1 + dp(k+1, r))
                else:
                    best = min(best, dp(l+1, k-1) + dp(k+1, r))

        memo[l][r] = best
        return best

    return dp(0, n-1)

sizes = [10, 50, 100, 150, 200, 250, 300]
times = []

for n in sizes:
    colors = [random.randint(1, n) for _ in range(n)]
    start = time.time()
    min_operations(colors)
    end = time.time()
    times.append(end - start)

plt.figure(figsize=(8,5))
plt.plot(sizes, times, marker='o')
plt.title('Tiempo de ejecución vs Tamaño de entrada (Top-Down)')
plt.xlabel('Tamaño de entrada (n)')
plt.ylabel('Tiempo (s)')
plt.grid(True)
plt.show()