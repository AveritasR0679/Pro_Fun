def gcd(a,b):
    """Return the greatest common factor of integers a and b.
    """
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a % b != 0:
        return gcd(b, a % b)
    else:
        return min(a, b)

if __name__ == '__main__':
    print('hello')
