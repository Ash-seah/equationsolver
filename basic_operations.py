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
    return multiply[::-1]

# add a normalization function that matches the lengths of 2 polynomials
def divide(a, b):
    curr_poly = a
    quotient = []
    while len(b) <= len(curr_poly):
        quotient.append(curr_poly[0]/b[0])
        curr_poly= trim(subtract(curr_poly, int(round(curr_poly[0]/b[0])) * b))
    remainder = curr_poly
    
    return [quotient, remainder]

def trim(a):
    while a[0] == 0:
        a.pop(0)
    return a

print(divide([4,0,2,0], [2,1]))