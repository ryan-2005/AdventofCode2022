import numpy as np
# Didn't crack it

def main():
    actions = open('../input/input_day_9.txt').read().split()

    actions = [(d, int(s)) for d, s in zip(actions[::2], actions[1::2])]
    dirs = {    'R': np.array([1, 0]), 'L': np.array([-1, 0]), 
                'U': np.array([0, 1]), 'D': np.array([0, -1]) }
    head, tail = [np.array([0,0])], [np.array([0,0])]
    for dr,dd in actions:
        for _ in range(dd):
            temp_pos=dirs.get(dr)+head[-1]
            dif = temp_pos-tail[-1]
            if abs(dif[0]) > 1 or abs(dif[1]) > 1:
                tail.append(head[-1])
            head.append(temp_pos)
    a=[]
    for i in tail:
        a.append((i[0],i[1]))  
    print(len(set(a)))



    with open("../input/input_day_9.txt") as fin:
        lines = fin.read().strip().split("\n")


    hx, hy = 0, 0
    tx, ty = 0, 0


    def touching(x1, y1, x2, y2):
        return abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1


    def move(dx, dy):
        global hx, hy, tx, ty

        hx += dx
        hy += dy

        if not touching(hx, hy, tx, ty):
            sign_x = 0 if hx == tx else (hx - tx) / abs(hx - tx)
            sign_y = 0 if hy == ty else (hy - ty) / abs(hy - ty)

            tx += sign_x
            ty += sign_y


    dd = {
        "R": [1, 0],
        "U": [0, 1],
        "L": [-1, 0],
        "D": [0, -1]
    }

    tail_visited = set()
    tail_visited.add((tx, ty))

    for line in lines:
        op, amount = line.split(" ")
        amount = int(amount)
        dx, dy = dd[op]

        for _ in range(amount):
            move(dx, dy)
            tail_visited.add((tx, ty))

    print(len(tail_visited))

if __name__ == "__main__":
        main()
    