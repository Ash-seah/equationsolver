def add(a, b):
    i = 0
    addition = []
    while i < len(a):
        addition.append(a[i] + b[i])
        i += 1
    return addition

def subtract(a, c):
    b = c
    print(len(a), len(b))
    while len(a) != len(b):
        b = list(b[::-1])
        b.append(0)
        b = list(b[::-1])
    i = 0
    subtraction = []
    while i < len(a):
        subtraction.append(a[i] - b[i])
        i += 1
    return subtraction

def multiply(a, b):
    a, b = a[::-1], b[::-1]
    multiply = [0] * (len(a) + len(b))
    i = 0
    while i < len(a):
        j = 0
        while j < len(b):
            multiply[i+j] += a[i] * b[j]
            j += 1
        i += 1
    return trim(list(multiply[::-1]))

def float_multiply(a, f):
    i = 0
    while i < len(a):
        a[i] *= f
        i += 1
    return a

# add a normalization function that matches the lengths of 2 polynomials
def divide(a, b):
    i = 0
    m = len(a) - 1
    n = len(b) - 1
    scale = 1. / b[0]
    q = [0] * max(m - n + 1, 1)
    r = a
    while i < m - n + 1:
        d = scale * r[i]
        q[i] = d
        r[i:i+n+1] = subtract(r[i:i+n+1],float_multiply(b, d))
        i += 1

    return [q, r]

def trim(a):
    while a[0] == 0:
        a.pop(0)
    return a

