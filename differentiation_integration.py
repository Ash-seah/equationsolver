import numpy as np

# in tabe tavan har adad ra dar khod zarb mikonad va dar akhar
# yek 0 as enteha pak mikonad
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


# in tabe 1/1+tavan har adad ra dar khod zarb mikonad va dar akhar
# yek c be enteha ezafe mikonad 
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

def differentiate_np(a, n):
    return(np.polyder(a, n))

def integrate_np(a, n):
    return(np.polyint(a, n))