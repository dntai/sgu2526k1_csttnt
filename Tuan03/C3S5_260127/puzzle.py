# print("Hello, World!")

FI = "puzzle.inp"

class State:
    def __init__(self, key, parent = None, cost = 0):
        self.key = [[c for c in rows] for rows in key]
        self.parent = parent
        self.cost = cost
        pass

    def convertKey(key):
        return tuple([tuple([c for c in rows]) for rows in key])
        pass

    def tokey(self):
        return State.convertKey(self.key)
        pass
    
    pass

def test1(fpath = FI, **kwargs):
    with open(fpath, 'rt') as file:
        content = file.readlines()

    start = [
        [int(ci.replace('\n','')) for ci in row.split(' ')] 
        for row in content[:3]
    ]

    goal = [
        [int(ci.replace('\n','')) for ci in row.split(' ')] 
        for row in content[3:]
    ]

    print('Start: ', State(start).tokey())
    print('Goal: ', State(goal).tokey())
        
    kwargs.get('debug',{}).update(locals())
    pass

if __name__ == "__main__":
    test1()
    pass