import sys, time
sys.setrecursionlimit(10000)

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

tests = [
    ([1, 2, 1], 1),
    ([1, 2, 3], 3),
    ([1, 4, 4, 2, 3, 2, 1], 2)
]

print("=== Pruebas ===")
for i, (colors, expected) in enumerate(tests, 1):
    t0 = time.time()
    res = min_operations(colors)
    t1 = time.time()
    status = "OK" if res == expected else "FAIL"
    print(f"Prueba {i}: {colors} => resultado: {res} (esperado: {expected}) [{status}]")
