import math

def polyarea(n, s):
    return 0.25 * n * s**2 / math.tan(math.pi / n )

def polyper(n, s):
    return n * s

def polysum(n, s):
    return round(polyarea(n, s) + polyper(n, s)**2, 4)
    