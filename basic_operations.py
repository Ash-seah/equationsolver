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
        print(len(a), len(b))
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

# add a normalization function that matches the lengths of 2 polynomials
def divide(a, b):
    curr_poly = a
    quotient = []
    i = 0
    while i < len(a) - len(b) + 1:
        temp = [0] * (len(a) - len(b) + 1)
        temp[i] += int(curr_poly[i]/b[0])
        curr_poly = subtract(curr_poly, multiply(temp, b))
        quotient.append(int(curr_poly[i]/b[0]))
        i += 1
    
    return quotient

def trim(a):
    while a[0] == 0:
        a.pop(0)
    return a

print(divide([2,9,14,5], [2,1]))