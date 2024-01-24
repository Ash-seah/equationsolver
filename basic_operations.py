def add(a, b):
    i = 0
    addition = []
    while i < len(a):
        addition.append(a[i] + b[i])
        i += 1
    return addition

def subtract(a, b):
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
        while j < len(j):
            multiply[i+j] += a[i] * b[j]
            j += 1
        i += 1
    return multiply

def divide(a, b):
    pass