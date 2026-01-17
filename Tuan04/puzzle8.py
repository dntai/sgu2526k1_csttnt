def docTapTin(file_path, **kwargs):
    start, goal = None, None
    
    with open(file_path, 'rt') as file:
        content = file.readlines()
    
    start = tuple([tuple([int(si.replace('\n', '')) for si in ci.split(' ')])
             for ci in content[0:3]])
    goal = tuple([tuple([int(si.replace('\n', '')) for si in ci.split(' ')])
             for ci in content[3:6]])

    kwargs.get('debug', {}).update(**locals())
    return start, goal
    pass

class State:
    actions = [(-1, 0),(1,0),(0,-1),(0,1)] # Up, Down, Left, Right (Pos 0)
    def __init__(self, key):
        self.key = key
        self.pos0 = self.find0(key)
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

    def expand(self, state, action):
        d0, c0 = self.pos0
        for dd, cc in State.actions:
            dm, cm = d0 + dd, c0 + cc
            if dm>=0 and dm <3 and cm>=0 and cm<3: # valid
                yield dm, cm
            pass
        pass
    pass


def test1(**kwargs):
    start, goal = docTapTin('puzzle8.inp', debug = kwargs.get('debug', {}))
    print(f'start = {start}')
    print(f'goal = {goal}')

    startNode = State(start)
    print('Start: ', startNode.__dict__)
    goalNode = State(goal)
    print('Goal: ', goalNode.__dict__)

    kwargs.get('debug', {}).update(**locals())
    pass

if __name__ == "__main__":
    test1(debug = globals())
    pass