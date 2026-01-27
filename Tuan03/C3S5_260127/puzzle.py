# print("Hello, World!")

FI = "puzzle.inp"

def DocFile(fpath = FI, **kwargs):
    with open(fpath, 'rt') as file:
        content = file.readlines()
    kwargs.get('debug',{}).update(locals())
    pass

def test1():
    DocFile(debug = globals())
    kwargs.get('debug',{}).update(locals())
    pass

if __name__ == "__main__":
    test1()
    pass