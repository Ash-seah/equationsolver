def evaluate(a, n):
    val = 0
    i = 0
    while i < len(a):
        val += n**(len(a) - i - 1) * a[i]
        i += 1

    return int(val)
