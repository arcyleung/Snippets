def gcd(a, b):
    if (b == 0):
        return a
    if (b < a):
        return gcd(b, a % b)
    else:
        return gcd(a, b % a)

print(gcd(23756, 32))