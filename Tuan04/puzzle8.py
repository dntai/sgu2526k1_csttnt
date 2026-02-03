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
    def __init__(self, key, parent = None, cost = 0):
        self.key = [[ci for ci in row]for row in key]
        self.pos0 = State._find0(self.key)
        self.parent = parent
        self.cost = cost
        self.info = dict({}) # cac thong tin khac
        pass

    def tokey(self):
        return State._tokey(self.key)
        pass

    def _tokey(key):
        return tuple([tuple([ci for ci in row]) for row in key])
        pass

    def _find0(key):
        for i in range(3):
            for j in range(3):
                if key[i][j] == 0:
                    return (i,j)
        return (-1,-1)
        pass

    def _heuristic1(key, target):
        cnt = 0
        for i in range(3):
            for j in range(3):
                if key[i][j]!=0 and key[i][j] != target[i][j]:
                    cnt = cnt + 1
        return cnt
        pass

    def _heuristic2(key, target):
        info = {}
        for i in range(3):
            for j in range(3):
                info[target[i][j]] = (i,j)
        cnt = 0
        for i in range(3):
            for j in range(3):
                if key[i][j] != 0:
                    dt, ct = info[key[i][j]]
                    cnt = cnt + abs(dt - i) + abs(ct - j) - 1 
        return cnt
        pass

    def _is_same(k1, k2):
        for i in range(3):
            for j in range(3):
                if k1[i][j] != k2[i][j]:
                    return False
        return True
        pass

    def is_same(self, key):
        return State._is_same(self.key, key)
        pass

    def expand(self):
        d0, c0 = self.pos0
        for dd, cc in State.actions:
            dm, cm = d0 + dd, c0 + cc
            if dm>=0 and dm <3 and cm>=0 and cm<3: # valid
                keym = [[ci for ci in row]for row in self.key]
                keym[dm][cm], keym[d0][c0] = keym[d0][c0], keym[dm][cm]
                yield keym
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

def bfs(skey, gkey):
    info = {}

    frontier = [] # queue
    states = dict({}) # reached states

    sNode = State(skey, parent = None, cost = 0)
    # for debug
    sNode.info['depth'] = 0
    
    states[State._tokey(skey)] = sNode
    frontier.append(skey)

    # for debug
    info['cnt'], info['depth'], info['max_depth'] = 1, 0, 0
    
    while len(frontier)>0:
        curk = frontier[0]      # queue
        frontier.pop(0)
        
        if State._is_same(curk, gkey) is True:
            info['depth'] = states[State._tokey(gkey)].info['depth']
            break
            pass

        curNode = states[State._tokey(curk)]

        for childk in curNode.expand():
            if states.get(State._tokey(childk)) is None:
                childNode = State(childk)
                childNode.parent = curNode
                childNode.cost = curNode.cost + 1
                # for debug
                childNode.info['depth'] = curNode.info['depth']+1

                states[State._tokey(childk)] = childNode

                # for debug
                info['cnt'] = info['cnt'] + 1
                info['max_depth'] = max(childNode.info["depth"], info['max_depth'])

                frontier.append(childk)
                pass
            pass
        pass

    return states, info
    pass

def astar(skey, gkey, fnEval = State._heuristic1):
    from heapq import heappush, heappop

    info = {}

    frontier = [] # heap_min (f=g+h,key)
    states = dict({}) # reached states

    sNode = State(skey, parent = None)
    sNode.info = {'g': 0, 'h': fnEval(skey, gkey)}
    sNode.cost = sNode.info['g'] + sNode.info['h']

    # for debug
    sNode.info['depth'] = 0
    info['cnt'], info['depth'], info['max_depth'] = 1, 0, 0

    states[State._tokey(skey)] = sNode
    heappush(frontier, (sNode.cost, skey))
    
    while len(frontier)>0:
        costk, curk = heappop(frontier)      # priority queue
        
        if State._is_same(curk, gkey) is True:
            info['depth'] = states[State._tokey(gkey)].info['depth']
            break
            pass

        curNode = states[State._tokey(curk)]
        # print(curNode.__dict__)

        for childk in curNode.expand():
            gg = curNode.info['g'] + 1 
            hh = fnEval(childk, gkey)
            childf = gg + hh

            if states.get(State._tokey(childk)) is None or states[State._tokey(childk)].cost>childf:
                childNode = State(childk)
                childNode.parent = curNode
                childNode.info['g'] = gg
                childNode.info['h'] = hh
                childNode.cost = childf

                # for debug
                childNode.info['depth'] = curNode.info['depth']+1

                states[State._tokey(childk)] = childNode

                # for debug
                info['cnt'] = info['cnt'] + 1
                info['max_depth'] = max(childNode.info["depth"], info['max_depth'])

                heappush(frontier, (childNode.cost, childk))
                pass
            pass
        pass

    return states, info
    pass

def test3(heuristic = "h1", **kwargs):
    print('-'*10, "THUAT TOAN A*", '-'*10)

    print('+ Doc tap tin...')
    start, goal = docTapTin('puzzle8.inp', debug = kwargs.get('debug', {}))
    
    State(start).pprint('Start Node')
    State(goal).pprint('Goal Node')

    print('+ Thuat toan A*...')
    
    fnEval = State._heuristic1
    if heuristic == "h2":
        fnEval = State._heuristic2

    states, info = astar(start, goal, fnEval)
    if states.get(State._tokey(goal)) is None:
        print('--> Khong tim thay dap an')
    else:
        curNode = states[State._tokey(goal)]
        listPath = []
        while curNode is not None:
            listPath.append(curNode)
            curNode = curNode.parent 
        listPath.reverse()

        print(f'--> So trang thai da mo: {info["cnt"]}')
        print(f'--> Do sau toi goal: {info["depth"]}')
        print(f'--> Do sau cay tim kiem: {info["max_depth"]}')

        print(f"--> So buoc di: {len(listPath)}")
        print(f'--> Liet ke cac buoc di: ')
        for pos, node in enumerate(listPath):
            node.pprint(f"Buoc {pos+1}")
        print('')
        pass
    print()
    
    kwargs.get('debug', {}).update(**locals())
    pass

def test2(**kwargs):
    print('-'*10, "THUAT TOAN BFS", '-'*10)

    print('+ Doc tap tin...')
    start, goal = docTapTin('puzzle8.inp', debug = kwargs.get('debug', {}))
    
    State(start).pprint('Start Node')
    State(goal).pprint('Goal Node')

    print('+ Thuat toan BFS...')
    states, info = bfs(start, goal)
    if states.get(State._tokey(goal)) is None:
        print('--> Khong tim thay dap an')
    else:
        curNode = states[State._tokey(goal)]
        listPath = []
        while curNode is not None:
            listPath.append(curNode)
            curNode = curNode.parent 
        listPath.reverse()

        print(f'--> So trang thai da mo: {info["cnt"]}')
        print(f'--> Do sau toi goal: {info["depth"]}')
        print(f'--> Do sau cay tim kiem: {info["max_depth"]}')

        print(f"--> So buoc di: {len(listPath)}")
        print(f'--> Liet ke cac buoc di: ')
        for pos, node in enumerate(listPath):
            node.pprint(f"Buoc {pos+1}")
        print('')
        pass
    print()
    
    kwargs.get('debug', {}).update(**locals())
    pass

def test1(**kwargs):
    print('-'*10, "XAY DUNG TRANG THAI", '-'*10)

    print('+ Doc tap tin...')
    start, goal = docTapTin('puzzle8.inp', debug = kwargs.get('debug', {}))
    print(f'start = {start}')
    print(f'goal = {goal}')
    print()

    print('+ Trang thai node...')
    startNode = State(start)
    print('Start: ', startNode.__dict__)
    goalNode = State(goal)
    print('Goal: ', goalNode.__dict__)
    print()

    print('+ Duyet node...')
    startNode.pprint('Start Node')
    nextNodeIter = startNode.expand()
    for curk in nextNodeIter: 
        State(curk).pprint('Child Node')
    print()
    
    kwargs.get('debug', {}).update(**locals())
    pass

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--action', type=str, default="help", help='test1, test2')
    parser.add_argument('--heuristic', type=str, default="h1", help='h1, h2')
    args, _ = parser.parse_known_args()
    params  = vars(args)
    
    if params['action'] == "test1":
        test1(debug = globals())
    elif params['action'] == "test2":
        test2(debug = globals())
    elif params['action'] == "test3":
        test3(heuristic=params["heuristic"], debug = globals())
    else:
        parser.print_help()
    pass