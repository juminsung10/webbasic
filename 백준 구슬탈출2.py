import numpy as np

x = np.array([list("##########"), list("#R#...##B#") ,list("#...#.##.#"), list("#####.##.#"), list("#......#.#"), list("#.######.#"), list("#.#....#.#"), list("#.#.#.#..#"), list("#...#.O#.#"), list("##########")])
#print(np.where(x == "R"), np.where(x == "O"), x)

goal = np.where(x == "O")

class marble():
    def __init__(self):
        marble.r = np.where(x == 'R')
        marble.b = np.where(x == 'B')
        marble.goal = np.where(x == "O")
        marble.rlist = list([marble.r[0][0], marble.r[1][0]])
        marble.blist = list([marble.b[0][0], marble.b[1][0]])
        marble.goallist = list([marble.goal[0][0], marble.goal[1][0]])

    def up(self):
        if [marble.rlist[0]-1, marble.rlist[1]] == marble.blist:
            while x[marble.blist[0]-1, marble.blist[1]] == '.':
                marble.blist = [marble.blist[0]-1, marble.blist[1]]
                marble.rlist = [marble.rlist[0]-1, marble.rlist[1]]
        elif [marble.blist[0]-1, marble.blist[1]] == marble.rlist:
            while x[marble.rlist[0]-1, marble.rlist[1]] == '.':
                marble.rlist = [marble.rlist[0]-1, marble.rlist[1]]
                marble.blist = [marble.blist[0]-1, marble.blist[1]]
        else:
            while x[marble.rlist[0]-1, marble.rlist[1]] == '.' or x[marble.blist[0]-1, marble.blist[1]] == '.':
                if x[marble.rlist[0]-1, marble.rlist[1]] == '.':
                    marble.rlist = [marble.rlist[0]-1, marble.rlist[1]]
                if x[marble.blist[0]-1, marble.blist[1]] == '.':
                    marble.blist = [marble.blist[0]-1, marble.blist[1]]
    
    def down(self):
        if [marble.rlist[0]+1, marble.rlist[1]] == marble.blist:
            while x[marble.blist[0]+1, marble.blist[1]] == '.':
                marble.blist = [marble.blist[0]+1, marble.blist[1]]
                marble.rlist = [marble.rlist[0]+1, marble.rlist[1]]
        elif [marble.blist[0]+1, marble.blist[1]] == marble.rlist:
            while x[marble.rlist[0]+1, marble.rlist[1]] == '.':
                marble.rlist = [marble.rlist[0]+1, marble.rlist[1]]
                marble.blist = [marble.blist[0]+1, marble.blist[1]]
        else:
            while x[marble.rlist[0]+1, marble.rlist[1]] == '.' or x[marble.blist[0]+1, marble.blist[1]] == '.':
                if x[marble.rlist[0]+1, marble.rlist[1]] == '.':
                    marble.rlist = [marble.rlist[0]+1, marble.rlist[1]]
                if x[marble.blist[0]+1, marble.blist[1]] == '.':
                    marble.blist = [marble.blist[0]+1, marble.blist[1]]

    def right(self):
        if [marble.rlist[0], marble.rlist[1]+1] == marble.blist:
            while x[marble.blist[0], marble.blist[1]+1] == '.':
                marble.blist = [marble.blist[0], marble.blist[1]+1]
                marble.rlist = [marble.rlist[0], marble.rlist[1]+1]
        elif [marble.blist[0], marble.blist[1]+1] == marble.rlist:
            while x[marble.rlist[0], marble.rlist[1]+1] == '.':
                marble.rlist = [marble.rlist[0], marble.rlist[1]+1]
                marble.blist = [marble.blist[0], marble.blist[1]+1]
        else:
            while x[marble.rlist[0], marble.rlist[1]+1] == '.' or x[marble.blist[0], marble.blist[1]+1] == '.':
                if x[marble.rlist[0], marble.rlist[1]+1] == '.':
                    marble.rlist = [marble.rlist[0], marble.rlist[1]+1]
                if x[marble.blist[0], marble.blist[1]+1] == '.':
                    marble.blist = [marble.blist[0], marble.blist[1]+1]
    def left(self):
        if [marble.rlist[0], marble.rlist[1]-1] == marble.blist:
            while x[marble.blist[0], marble.blist[1]-1] == '.':
                marble.blist = [marble.blist[0], marble.blist[1]-1]
                marble.rlist = [marble.rlist[0], marble.rlist[1]-1]
        elif [marble.blist[0], marble.blist[1]-1] == marble.rlist:
            while x[marble.rlist[0], marble.rlist[1]-1] == '.':
                marble.rlist = [marble.rlist[0], marble.rlist[1]-1]
                marble.blist = [marble.blist[0], marble.blist[1]-1]
        else:
            while x[marble.rlist[0], marble.rlist[1]-1] == '.' or x[marble.blist[0], marble.blist[1]-1] == '.':
                if x[marble.rlist[0], marble.rlist[1]-1] == '.':
                    marble.rlist = [marble.rlist[0], marble.rlist[1]-1]
                if x[marble.blist[0], marble.blist[1]-1] == '.':
                    marble.blist = [marble.blist[0], marble.blist[1]-1]
                

        
y = marble()

y.down()
y.right()
y.up()
y.right()

print([marble.rlist[0], marble.rlist[1]], [marble.blist[0], marble.blist[1]])