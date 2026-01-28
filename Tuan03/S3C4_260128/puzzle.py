# print("Hello, World!")

FI = "puzzle.inp"

def bfs(startk, goalk):

    frontier = []
    states = dict({})

    states[State._tokey(startk)] = State(startk, parent = None, cost = 0) 
    frontier.append(startk)

    while len(frontier)>0:
        curk = frontier[0]
        frontier.pop(0)

        if State._is_equal(curk, goalk) is True:
            break

        curNode = states[State._tokey(curk)]
        for child in curNode.expand():
            childk = State._tokey(child)
            if states.get(childk) is None:
                childNode = State(child)
                childNode.parent = curNode
                childNode.cost = curNode.cost + 1
                states[childk] = childNode
                frontier.append(child)
                pass
            pass
        
        pass

    return states
    pass # bfs

class State:
    actions = [(-1,0),(1,0),(0,-1),(0,1)]
    def __init__(self, key, parent = None, cost = 0):
        self.key = [[ci for ci in row] for row in key]
        self.pos0 = State.find0(self.key)
        self.parent = parent
        self.cost = cost
        pass # __init__

    def _is_equal(k1, k2):
        for i in range(3):
            for j in range(3):
                if k1[i][j] != k2[i][j]:
                    return False
        return True
        pass

    def find0(key):
        for i in range(3):
            for j in range(3):
                if key[i][j] == 0:
                    return i, j
        return -1, -1
        pass

    def _tokey(key):
        return tuple([tuple([ci for ci in row]) for row in key])
        pass

    def tokey(self):
        return State._tokey(self.key)
        pass

    def pprint(self, title='State'):
        print('*'*10,title,'*'*10)
        for i in range(3):
            for j in range(3):
                print(self.key[i][j], end = ' ')
            print()
        print()
        pass

    def expand(self):
        d0, c0 = self.pos0
        for ai in range(len(State.actions)):
            dm, cm = d0 + State.actions[ai][0], c0 + State.actions[ai][1]
            if dm>=0 and dm<=2 and cm>=0 and cm<=2:
                keym = [[ci for ci in row] for row in self.key]
                keym[d0][c0], keym[dm][cm] = keym[dm][cm], keym[d0][c0]
                yield keym
                pass
            pass
        pass
    
    pass # State

def test1(**kwargs):
    with open(FI,"rt") as file:
        content = file.readlines()
        pass # with

    start = [
        [int(ci.replace('\n','')) for ci in row.split(' ')] for row in content[:3]
    ]

    goal = [
        [int(ci.replace('\n','')) for ci in row.split(' ')] for row in content[3:]
    ]

    print(content)
    print(start)
    print(goal)
    print("-"*10)
    print(State._tokey(start))

    startNode = State(start)
    print(startNode.__dict__)

    startNode.pprint('Start')

    print("-"*10, 'YIELD',"*"*10)
    it = startNode.expand()
    print(it)
    
    key = next(it)
    State(key).pprint()

    key = next(it)
    State(key).pprint()

    key = next(it)
    State(key).pprint()

    # key = next(it)
    # State(key).pprint()

    print('debug for')
    for keym in startNode.expand():
        State(keym).pprint('Node')
        pass

    print("-"*10, 'BFS',"*"*10)
    states = bfs(start, goal)
    
    kwargs.get("debug",{}).update(**locals())
    pass # test1

if __name__ == "__main__":
    test1(debug = globals())
    pass