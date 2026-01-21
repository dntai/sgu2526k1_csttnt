print(f'Loading __name__: {__name__}')

def giaitptbac2(a, b, c):
    """
    Giai phuong trinh bac 2
    """
    import math
    
    sn, x1, x2 = None, None, None

    if a==0: # bx + c = 0
        if b==0: # c = 0
            if c == 0:
                sn = -1 # vo so nghiem
            else:
                sn = 0  # vo nghiem
            pass
        else:
            sn = 1
            x1 = -b / c
        pass
    else:
        delta = b**2 - 4*a*c
        if delta<0:
            sn = 0
        elif delta == 0:
            sn = 1
            x1 = -b / (2*a)
        else:
            sn = 2
            x1 = (-b - math.sqrt(delta)) / (2*a)
            x2 = (-b + math.sqrt(delta)) / (2*a)
            if x1>x2:
                x1, x2 = x2, x1
        pass
    
    return sn, x1, x2
    pass # giaitptbac2

if __name__ == "__main__":
    line = input()
    a, b, c = [int(x) for x in line.split(' ')]
    # print(f'a = {a}, b = {b}, c = {c}')
    
    sn, x1, x2 = giaitptbac2(a, b, c)
    # print(f'sn = {sn}, x1 = {x1}, x2 = {x2}')
    if sn == -1:
        print(f'Phuong trinh {a}x^2+{b}x+{c}=0: vo so nghiem')
    elif sn == 0:
        print(f'Phuong trinh {a}x^2+{b}x+{c}=0: vo nghiem')
    elif sn == 1:
        print(f'Phuong trinh {a}x^2+{b}x+{c}=0: 1 nghiem, x1 = {x1}')
    else:
        print(f'Phuong trinh {a}x^2+{b}x+{c}=0: 2 nghiem, x1 = {x1}, x2 = {x2}')

    