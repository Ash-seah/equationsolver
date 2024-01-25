import function_value
import differentiation_integration

def find_root(a):

    i = 0
    acc = 0.001
    error = 1
    x1 = 3.5

    diff_function = differentiation_integration.differentiate(a, 1)

    while error > acc:
        x2 = x1 - function_value.evaluate(a, x1)/function_value.evaluate(diff_function, x1)
        error = abs(x2 - x1)
        x1 = x2
    
    if abs(x2 - round(x2)) < acc:
        return int(round(x2))
    else:
        return x2
    