FI = "puzzle.inp"

class State:
    def __init__(self):
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
    
    kwargs.get('debug', {}).update(**locals())
    pass # solve

if __name__ == "__main__":
    solve(debug = globals())
    pass