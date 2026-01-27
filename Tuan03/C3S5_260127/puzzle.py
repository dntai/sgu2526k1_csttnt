# print("Hello, World!")

FI = "puzzle.inp"

def bfs(startk, goalk):
    frontier = []
    states = dict({})

    sNode = State(startk, parent = None, cost = 0)
    
    frontier.append(startk)
    states[sNode.tokey()] = sNode

    while len(frontier)>0:
        curk = frontier[0]
        frontier.pop(0)
        if State.compareKey(curk, goalk):
            break
        curNode = states[State(curk).tokey()]
        for childk in curNode.expand():
            if states.get(State.convertKey(childk)) is None:
                childNode = State(childk)
                childNode.parent = curNode
                childNode.cost = curNode.cost + 1
                states[childNode.tokey()] = childNode
                frontier.append(childk)
                pass
            pass
        pass

    return states
    pass

class State:
    actions = [(-1,0),(1,0),(0,-1),(0,1)]
    
    def __init__(self, key, parent = None, cost = 0):
        self.key = [[c for c in rows] for rows in key]
        self.pos0 = State.find0(self.key)
        self.parent = parent
        self.cost = cost
        pass

    def find0(key):
        for i in range(3):
            for j in range(3):
                if key[i][j] == 0:
                    return i, j
        return -1, -1
        pass

    def compareKey(k1, k2):
        for i in range(3):
            for j in range(3):
                if k1[i][j] != k2[i][j]:
                    return False
        return True
        pass

    def convertKey(key):
        return tuple([tuple([c for c in rows]) for rows in key])
        pass

    def tokey(self):
        return State.convertKey(self.key)
        pass

    def expand(self):
        d0, c0 = self.pos0
        for i in range(4):
            dm, cm = d0 + State.actions[i][0], c0 + State.actions[i][1]
            if dm>=0 and dm<3 and cm>=0 and cm<3:
                keym = [[c for c in rows] for rows in self.key]
                keym[d0][c0], keym[dm][cm] = keym[dm][cm], keym[d0][c0]
                yield keym
                pass
            pass
        pass

    def pprint(self, title='State'):
        print('-'*5, title, '-'*5)
        for i in range(3):
            for j in range(3):
                print(self.key[i][j], end = " ")
                pass
            print()
        print()
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

    startNode = State(start)
    startNode.pprint('Start')

    goalNode = State(goal)
    goalNode.pprint('Goal')


    states = bfs(start, goal)
    
    kwargs.get('debug',{}).update(locals())
    pass

if __name__ == "__main__":
    test1(debug = globals())
    pass