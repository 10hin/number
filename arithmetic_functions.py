def gcd(a, b):
    if a == 0 or b == 0:
        raise ArithmeticError('gcd of zero')
    p = a
    q = b
    if p < q:
        p = b
        q = a
    r = p % q
    while r != 0:
        p = q
        q = r
        r = p % q
    return q