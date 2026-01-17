def docTapTin(file_path, **kwargs):
    start, goal = None, None
    
    with open(file_path, 'rt') as file:
        content = file.readlines()
    
    start = [[int(si.replace('\n', '')) for si in ci.split(' ')]
             for ci in content[0:3]]
    goal =  [[int(si.replace('\n', '')) for si in ci.split(' ')]
             for ci in content[3:6]]

    kwargs.get('debug', {}).update(**locals())
    return start, goal
    pass

class State:
    actions = [(-1, 0),(1,0),(0,-1),(0,1)] # Up, Down, Left, Right (Pos 0)
    def __init__(self, key):
        self.key = [[ci for ci in row]for row in key]
        self.pos0 = self.find0(key)
        self.parent = None
        self.checked = False
        pass

    def tokey(self):
        return tuple([tuple([ci for ci in row]) for row in self.key])
        pass

    def find0(self, key):
        row, col = None, None
        for i in range(3):
            for j in range(3):
                if key[i][j] == 0:
                    row, col = i, j
                    return row, col
                pass
        return row, col
        pass

    def is_same(self, key):
        flag = True
        for i in range(3):
            for j in range(3):
                if key[i][j] != self.key[i][j]:
                    flag = False
                    return flag
        return flag
        pass

    def expand(self):
        d0, c0 = self.pos0
        for dd, cc in State.actions:
            dm, cm = d0 + dd, c0 + cc
            if dm>=0 and dm <3 and cm>=0 and cm<3: # valid
                keym = [[ci for ci in row]for row in self.key]
                keym[dm][cm], keym[d0][c0] = keym[d0][c0], keym[dm][cm]
                yield State(keym)
            pass
        pass

    def print(self):
        print()
        for i in range(3):
            for j in range(3):
                print(self.key[i][j], ' ', end='')
            print()
        pass
    pass

def bfs_alg(start, goal):

    startNode = State(start)
    goalNode = State(goal)

    states = { startNode.tokey(): startNode }

    if startNode.is_same(goal):
        return True, states

    open = [startNode.tokey()]
    while len(open)>0:
        curKey = open[0]
        # print(curKey)
        curNode = states[curKey]
        open.pop(0)
        if curNode.is_same(goal):
            return True, states
        curNode.checked = True

        for childNode in curNode.expand(): # transition
            if states.get(childNode.tokey()) is None:
                states[childNode.tokey()] = childNode
                childNode.parent = curNode
                open.append(childNode.tokey())
                pass
            pass

        pass

    return False, states
    pass

def test2(**kwargs):
    start, goal = docTapTin('puzzle8.inp', debug = kwargs.get('debug', {}))
    print(f'start = {start}')
    print(f'goal = {goal}')

    is_found, states = bfs_alg(start, goal)
    kwargs.get('debug', {}).update(**locals())
    pass

def test1(**kwargs):
    start, goal = docTapTin('puzzle8.inp', debug = kwargs.get('debug', {}))
    print(f'start = {start}')
    print(f'goal = {goal}')

    startNode = State(start)
    print('Start: ', startNode.__dict__)

    nextNodeIter = startNode.expand()
    for nextNode in nextNodeIter: 
        print(nextNode.__dict__)
        print("--")

    goalNode = State(goal)
    print('Goal: ', goalNode.__dict__)

    kwargs.get('debug', {}).update(**locals())
    pass

if __name__ == "__main__":
    # test1(debug = globals())
    test2(debug = globals())
    pass