import math

def giaipt_bac2(a, b, c):
    '''
    Giai phuong trinh bac 2
    sn = -1 (vsn), 0: vn, 1: x1, 2: x1, x2
    '''
    sn, x1, x2 = -1, None, None

    if a == 0: # bx + c = 0
        if b == 0: # c = 0
            if c == 0:
                sn = -1 # vo so nghiem
            else:
                sn = 0  #  vo nghiem
            pass
        else: # bx + c = 0
            sn = 1
            x1 = -c / b # phuong trinh 1 nghiem
        pass
    else:
        delta = b**2 - 4 * a * c
        if delta < 0:
            sn = -1
        elif delta == 0:
            sn = 1
            x1 = -b / (2*a)
        else:
            sn = 2
            x1 = (-b - math.sqrt(delta)) / (2*a)
            x2 = (-b + math.sqrt(delta)) / (2*a)
            if x1 > x2:
                x1, x2 = x2, x1
            pass
        pass

    return sn, x1, x2
    pass

if __name__ == "__main__":
    line = input()
    print(line)
    print([float(x) for x in line.split(' ')])

    a, b, c = [float(x) for x in line.split(' ')]
    print(f'a = {a}, b = {b}, c = {c}')

    sn, x1, x2 = giaipt_bac2(a, b, c)
    if sn == -1:
        print(f'Phuong trinh {a}x^2 + {b}x + {c} = 0 vo so nghiem!')
    elif sn == 0:
        print(f'Phuong trinh {a}x^2 + {b}x + {c} = 0 vo nghiem!')
    elif sn == 1:
        print(f'Phuong trinh {a}x^2 + {b}x + {c} = 0 co 1 nghiem, x1= {x1}!')
    else:
        print(f'Phuong trinh {a}x^2 + {b}x + {c} = 0 co 2 nghiem, x1= {x1} va x2 = {x2}!')