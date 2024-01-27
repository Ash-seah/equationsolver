def ready_input(a):
    print(a.split('+')[2].split('x'))
    i = 0
    split_poly = a.split('+')[::-1]
    coefficients = []
    prev_power = 0
    highest_power = int(split_poly[len(split_poly)-1].split('x')[1].replace(' ', '').replace('^', ''))
    if 'x' not in split_poly[0]:
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
