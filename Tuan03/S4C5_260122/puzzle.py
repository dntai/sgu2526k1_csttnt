FI = "puzzle.inp"

class State:
    actions = [(-1,0),(1,0),(0,-1),(0,1)]
    
    def __init__(self, key, parent = None, cost = 0):
        self.key = [[v for v in row] for row in key]
        self.pos0 = State.find0(self.key)
        self.parent = parent
        self.cost = cost
        pass

    @staticmethod
    def tokey(key):
        return tuple([tuple([v for v in row]) for row in key])
        pass

    def tokey(self):
        return State.tokey(self.key)
        pass

    @staticmethod
    def find0(key):
        for i in range(3):
            for j in range(3):
                if key[i][j] == 0:
                    return (i,j)
        return (-1,-1)
        pass
    
    
    pass

def solve(**kwargs):
    with open(FI,"rt") as file:
        content = file.readlines()
        pass

    # start
    start = [
        [int(v.replace('\n', '')) for v in row.split(' ')] 
        for row in content[0:3]
    ]

    # goal
    goal = [
        [int(v.replace('\n', '')) for v in row.split(' ')] 
        for row in content[3:6]
    ]

    print(State(start).tokey())
    
    kwargs.get('debug', {}).update(**locals())
    pass # solve

if __name__ == "__main__":
    solve(debug = globals())
    pass