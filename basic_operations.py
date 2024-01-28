import numpy as np

# tabe be ezaye har eleman dar a, an ra ba haman eleman dar c jam mikonad 
# va hasel ra return mikonad
def add(a, c):
    b = c
    while len(a) != len(b):
        b = list(b[::-1])
        b.append(0)
        b = list(b[::-1])
    i = 0
    addition = []
    while i < len(a):
        addition.append(a[i] + b[i])
        i += 1
    return addition

# tabe be ezaye har eleman dar a, an ra ba haman eleman dar c tafriq mikonad 
# va hasel ra return mikonad
def subtract(a, c):
    b = c
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

# tabe be ezaye har eleman dar a, an ra ba haman eleman dar c zarb mikonad 
# va hasel ra dar har loop dar jaye khod dar list multiply gharar midahad
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

# in yek tabe komaki baraye tabe divide ast. yek float ra dar hame eleman haye 
# yek list zarb mikonad
def float_multiply(a, f):
    i = 0
    while i < len(a):
        a[i] *= f
        i += 1
    return a

# in code be ezaye tool maghsoom alaih maghsoom ra mipeymayad va dar har gam
# scale ra dar chand jomlei hal hazer zarb mikonad va an ra dar q zakhire mikonad
# q haman kharej ghesmat va r baghi mande ast
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


# in code baraye hazf kardan 0 haye aval tabe ast
def trim(a):
    while a[0] == 0:
        a.pop(0)
    return a

def add_np(a, b):
    return(np.polyadd(a, b))

def subtract_np(a, b):
    return(np.polysub(a, b))

def multiply_np(a, b):
    return(np.polymul(a, b))

def divide_np(a, b):
    return(np.polydiv(a, b))