def differentiate(a):
    a = a[::-1]
    i = 0
    differentiated = []

    while i < len(a):
        differentiated.append(i * a[i])
        i += 1

    differentiated = differentiated[::-1]
    differentiated.pop()
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

print(integrate([45, 3, 2, 1]))