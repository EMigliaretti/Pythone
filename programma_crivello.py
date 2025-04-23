# Numeri primi fino a "n"

def crivello(n):
    l = set(range(2, n+1))
    for i in range(2, int(n**0.5) + 1):
        l = l.difference({i * x for x in range(2, n + 1)})
    return l
