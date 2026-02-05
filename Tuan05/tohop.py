def docTapTin(fpath = "TOHOP.INP"):
    with open(fpath, "rt") as file:
        content = file.readlines()
        # print(content)
        n, k = [int(si.replace('\n','')) for si in content[0].split(' ')[:2]]
        th = [si[0] for si in content[1:]]
        pass
    return n, k, th
    pass

def InDapAn(tohop, th):
    for i in range(1, len(tohop)):
        print(th[tohop[i]-1], end = ' ')
    print()
    pass

def LietKeToHop(n, k, th):
    tohop = [-1]*(k+1) # [1..k] = -1
    tohop[0] = 0
    info = dict(tohop = tohop, cnt = 0, n = n, k = k, th = th, isprint = False)
    TryToHop(1, info)
    print(info['cnt'])

    tohop = [-1]*(k+1) # [1..k] = -1
    tohop[0] = 0
    info = dict(tohop = tohop, cnt = 0, n = n, k = k, th = th, isprint = True)
    TryToHop(1, info)
    pass

def TryToHop(t, info):
    tohop, k, n = info["tohop"], info["k"], info["n"]
    for vt in range(tohop[t-1]+1, n - k + t + 1):
        tohop[t] = vt
        if t == k:
            info["cnt"] = info["cnt"] + 1
            if info['isprint'] is True:
                InDapAn(tohop, info["th"])
            pass
        else:
            TryToHop(t+1, info)
        tohop[t] = -1
        pass
    pass

def main(sfile, **kwargs):
    n, k, th = docTapTin(sfile)
    LietKeToHop(n, k, th)
    kwargs.get("debug",{}).update(locals())
    pass

def test1(**kwargs):
    n, k, th = docTapTin("TOPHOP.INP")

    print('-'*5, 'DOC FILE', '-'*5)
    print(f'n = {n}, k = {k}, th = {th}')
    print('Ket qua: ')
    LietKeToHop(n, k, th)
    
    kwargs.get("debug",{}).update(locals())
    pass
    
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--action', type=str, default="help", help='test1, main')
    parser.add_argument('--file', type=str, default="TOHOP.INP", help='file path')
    args, _ = parser.parse_known_args()
    params  = vars(args)
    
    if params['action'] == "test1":
        test1(debug = globals())
    elif params['action'] == "main":
        main(sfile = params['file'], debug = globals())
    else:
        parser.print_help()
    pass