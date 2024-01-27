def ready_input(a):
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

def find_sign(a):
    if a >= 0:
        return '+'
    else:
        return '-'

def ready_output(a):
    i = 0
    tex_str = ''
    while i < len(a):
        if a[i] == 0:
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

print(ready_output([4, 7, 9, 10, 0, 6 ,2]))

import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['text.usetex'] = True

txte = '$' + ready_output([4, 7, 9, 10, 0, 6 ,2]) + '$'


plt.text(0.5, 0.5, txte, fontsize=14, ha='center', va='center')
ax = plt.gca()
ax.axes.get_xaxis().set_visible(False)
ax.axes.get_yaxis().set_visible(False)

plt.show()