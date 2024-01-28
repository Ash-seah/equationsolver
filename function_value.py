import numpy as np

# in tabe yek adad ra be jaye x dar yek chand jomlei jagozari mikonad
def evaluate(a, n):
    val = 0
    i = 0
    while i < len(a):
        val += n**(len(a) - i - 1) * a[i]
        i += 1

    return int(val)

def evaluate_np(a, n):
    return(np.polyval(a, n))
