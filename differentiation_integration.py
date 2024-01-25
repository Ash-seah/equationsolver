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
    # differentiated.pop()
    return differentiated

def integrate(a):
    a = a[::-1]
    i = 0
    integrated = []
    while i < len(a):
        integrated.append((1/(i+1)) * a[i])
        i += 1
    
    integrated = integrated[::-1]
    integrated.append('c')
    return integrated

print(differentiate([4, 3, 2, 1], 7))