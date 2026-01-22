FI = "puzzle.inp"

class State:
    actions = [(-1,0),(1,0),(0,-1),(0,1)]
    
    def __init__(self, key, parent = None, cost = 0):
        self.key = [[v for v in row] for row in key]
        self.pos0 = State.find0(self.key)
        self.parent = parent
        self.cost = cost
        pass

    def convert_key(key):
        return tuple([tuple([v for v in row]) for row in key])
        pass

    def tokey(self):
        return State.convert_key(self.key)
        pass

    def find0(key):
        for i in range(3):
            for j in range(3):
                if key[i][j] == 0:
                    return (i,j)
        return (-1,-1)
        pass

    def expand(self):
        d, c = self.pos0
        for i in range(len(State.actions)):
            dn, cn = d + State.actions[i][0], c + State.actions[i][1]
            if dn>=0 and dn<=2 and cn>=0 and cn<=2:
                staten = [[v for v in row] for row in self.key]
                staten[d][c], staten[dn][cn] = staten[dn][cn], staten[d][c]

                yield staten
                pass
            pass
        pass
    
    def pprint(self, title = ''):
        print('-'*10, title, '-'*10)
        for i in range(3):
            for j in range(3):
                print(self.key[i][j], ' ', end="")
            print()
        print()
        pass
    pass

def test1(**kwargs):
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
    print(State(start).__dict__)

    startNode = State(start)
    startNode.pprint('Start')

    goalNode = State(goal)
    goalNode.pprint('Goal')
    
    
    kwargs.get('debug', {}).update(**locals())
    pass # solve

if __name__ == "__main__":
    test1(debug = globals())
    pass