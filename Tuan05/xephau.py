def docTapTin(fpath = "XEPHAU.INP"):
    with open(fpath, "rt") as file:
        content = file.read()
        # print(content)
        n = int(content)
        pass
    return n
    pass

def LietKeHau(n, action = "list"):
    hau = [-1] * (n+1) # hau[i] = -1 (chua dat), j (hau o cot i dong j)
    dong = [0] * (n+1) # dong[i] = 0 (dong i chua khong che) / 1
    cheo1 = [0] * (2*n) # cheo1[d-c+n] = 0 / 1 (1 -> 2n-1)
    cheo2 = [0] * (2*n) # cheo1[d+c-1] = 0 / 1
    info = { "n": n, "hau": hau, "dong": dong, 
             "cheo1": cheo1, "cheo2": cheo2, 
             "coDapAn": False, "action": action, 
             "cnt": 0, "laInDapAn": True}
    # action: find, list
    TryHau(1, info)

    return info
    pass

def InDapAn(info):
    # print(info["hau"])
    print(info["cnt"])
    for i in range(1, info["n"]+1):
        for j in range(1, info["n"]+1):
            if info["hau"][i] == j:
                print("1", end = " ")
            else:
                print("0", end = " ")
        print()
    print()
    pass

def TryHau(k, info):
    if info["coDapAn"] is True and info["action"] == "find":
        return
    n, hau, dong, cheo1, cheo2 = [info[x] 
        for x in ["n", "hau", "dong", "cheo1", "cheo2"]]
    for vk in range(1, n+1): # xet tat ca cach dien
        if dong[vk]==0 and cheo1[vk-k+n]==0 and cheo2[vk+k-1]==0: # hop le
            # vao
            hau[k] = vk
            dong[vk], cheo1[vk-k+n], cheo2[vk+k-1] = 1, 1, 1
            # dien du trang thai?
            if k == n:
                info["coDapAn"] = True
                info["cnt"] = info["cnt"] + 1
                if info["laInDapAn"] is True:
                    InDapAn(info)
            else:
                TryHau(k+1, info)
            # quay lui
            hau[k] = -1
            dong[vk], cheo1[vk-k+n], cheo2[vk+k-1] = 0, 0, 0
            pass
        pass
    pass

def main(sfile, **kwargs):
    n = docTapTin(sfile)
    info = LietKeHau(n, action = "find")
    if info["coDapAn"] is False:
        print("0")
    kwargs.get("debug",{}).update(locals())
    pass

def test1(**kwargs):
    n = docTapTin("XEPHAU.INP")

    print('-'*5, 'DOC FILE', '-'*5)
    print(f'n = {n}')
    print('Ket qua: ')
    LietKeHau(n)
    
    kwargs.get("debug",{}).update(locals())
    pass
    
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--action', type=str, default="help", help='test1, main')
    parser.add_argument('--file', type=str, default="XEPHAU.INP", help='file path')
    args, _ = parser.parse_known_args()
    params  = vars(args)
    
    if params['action'] == "test1":
        test1(debug = globals())
    elif params['action'] == "main":
        main(sfile = params['file'], debug = globals())
    else:
        parser.print_help()
    pass