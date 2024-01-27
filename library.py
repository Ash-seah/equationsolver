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

def differentiate(a, n):
    if n > len(a):
        return 'invalid'
    elif n == len(a):
        return [0]
    
    a = a[::-1]
    j = 0
    differentiated = []

    while j < n:
        i = 0
        while i < len(a):
            differentiated.append(i * a[i])
            i += 1
        differentiated.pop(0)
        a = differentiated
        differentiated = []
        j += 1

    differentiated = a[::-1]
    return differentiated


def integrate(a, n):
    print(a)
    a = a[::-1]
    j = 0
    integrated = []

    while j < n:

        i = 0
        while i < len(a):
            if a[i] == 'c':
                i += 1
                integrated.append('c')
                continue
            integrated.append((1/(i+1)) * a[i])
            i += 1
        
        integrated = integrated[::-1]
        integrated.append('c')
        a = integrated[::-1]
        integrated = []
        j += 1

    integrated = a[::-1]
    return integrated

def evaluate(a, n):
    val = 0
    i = 0
    while i < len(a):
        val += n**(len(a) - i - 1) * a[i]
        i += 1

    return int(val)

def ready_input(a):
    i = 0
    split_poly = a.split('+')[::-1]
    coefficients = []
    prev_power = 0
    
    if 'x^' in split_poly[0]:
        lowest_power = split_poly[0].split('x')[1].replace(' ', '').replace('^', '')
        i = 0
        while i < int(lowest_power):
            coefficients.append(0)
            i += 1
    elif 'x' in split_poly[0] and 'x^' not in split_poly[0]:
        coefficients.append(0)
    else:
        coefficients.append(int(split_poly[0].replace(' ', '')))
        split_poly.pop(0)
        

    while i < len(split_poly):
        coe = split_poly[i].split('x')[0].replace(' ', '')
        power = split_poly[i].split('x')[1].replace(' ', '').replace('^', '')
        if power == '':
            coefficients.append(int(coe))
            prev_power += 1
        elif int(power) - prev_power != 1:
            coefficients.append(0)
            prev_power += 1
            continue
        else:
            coefficients.append(int(coe))
            prev_power += 1
        i += 1
    return coefficients[::-1]

def find_sign(a):
    if a > 0:
        return '+'
    elif a == 0:
        return ''
    else:
        return '-'

def ready_output(a):
    i = 0
    tex_str = ''
    while i < len(a):
        if a[i] == 0 and i != len(a) - 1:
            tex_str += f' {find_sign(a[i + 1])} '
            i += 1
            continue
        elif i == len(a) - 1:
            tex_str += f'{abs(a[i])}'
            i += 1
            continue
        elif i == len(a) - 2:
            tex_str += f'{abs(a[i])}x {find_sign(a[i + 1])} '
            i += 1
        elif i == 0:
            tex_str += f'{a[i]}x^{len(a) - i - 1} {find_sign(a[i + 1])} '
            i += 1
        else:
            tex_str += f'{abs(a[i])}x^{len(a) - i - 1} {find_sign(a[i + 1])} '
            i += 1
    return tex_str

def find_root(a):

    i = 0
    acc = 0.001
    error = 1
    x1 = 3.5

    diff_function = differentiate(a, 1)

    while error > acc:
        if evaluate(diff_function, x1) == 0:
            x1 += 1
        x2 = x1 - evaluate(a, x1)/evaluate(diff_function, x1)
        error = abs(x2 - x1)
        x1 = x2
    
    if abs(x2 - round(x2)) < acc:
        return int(round(x2))
    else:
        return x2