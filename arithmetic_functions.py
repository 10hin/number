def gcd(a, b):
    if a == 0 or b == 0:
        raise ArithmeticError('gcd of zero')
    p = abs(a)
    q = abs(b)
    if p < q:
        p = abs(b)
        q = abs(a)
    r = p % q
    while r != 0:
        p = q
        q = r
        r = p % q
    return q

def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a) * abs(b) // gcd(a, b)

def quadres(p, q):
    for x in range(0, (p - 1) // 2):
        if (x * x - q) % p == 0:
            return 1
    return -1
