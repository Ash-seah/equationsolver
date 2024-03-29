import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['text.usetex'] = True

# in tabe voroodi GUI ra baraye dade shodan be tavabe digar amade mikonad
# voroodi ra bar asas + va x joda mikonad sepas etelaat ra parse mikonad
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

# in tabe baraye peyda kardan alamat estefade mishavad. yek tabe
# komaki baraye ready_output ast
def find_sign(a):
    if a == 'c' or a > 0:
        return '+'
    elif a == 0:
        return ''
    else:
        return '-'

# in tabe yek bordar zarayeb ra baraye dade shodan be latex amade mikonad
def ready_output(a):
    i = 0
    tex_str = ''
    while i < len(a):
        if a[i] == 'c':
            tex_str += ' c'
            break
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

# in tabe ba estefade as latex dakhel ketabkhane matplotlib voroodi
# ra dar latex neshan midahad 
def output(a):
    txte = '$' + str(a) + '$'


    plt.text(0.5, 0.5, txte, fontsize=14, ha='center', va='center')
    ax = plt.gca()
    ax.axes.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)

    plt.show()