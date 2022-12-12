import numpy as np   
 #Failed to crack it   
    
    
def main():   
    with open("../input/input_day_9.txt") as fin:
        lines = fin.read().strip().split("\n")


    knots = [[0,0] for i in range(10)]

    def touching(x1, y1, x2, y2):
        return abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1


    def move(dx, dy):
        global knots
        
        knots[0][0] += dx
        knots[0][1] += dy
        
        for i in range(1,10):
            hx,hy = knots[i-1]
            tx,ty = knots[i]

            if not touching(hx, hy, tx, ty):
                sign_x = 0 if hx == tx else (hx - tx) / abs(hx - tx)
                sign_y = 0 if hy == ty else (hy - ty) / abs(hy - ty)

                tx += sign_x
                ty += sign_y
            knots[i] = [tx,ty]


    dd = {
        "R": [1, 0],
        "U": [0, 1],
        "L": [-1, 0],
        "D": [0, -1]
    }

    tail_visited = set()
    tail_visited.add(tuple(knots[-1]))


    for line in lines:
        op, amount = line.split(" ")
        amount = int(amount)
        dx, dy = dd[op]

        for _ in range(amount):
            move(dx, dy)
            tail_visited.add(tuple(knots[-1]))

    print(len(tail_visited))

    # another solution to part 2
    k = np.zeros((10,2))
    visited = set()
    for line in lines:
        d, n = line.split(' ')
    for i in range(int(n)):
        k[0] += dd[d]
        for j in range(1,10):
            if np.max(np.abs(k[j] - k[j-1])) > 1: # if distance of a knot between previous knot > 1: then
                k[j] += np.sign(k[j-1] - k[j]) # np. sign <0, move-1; ==0, no movment; >1 move 1
        visited.add(tuple(k[-1]))
    print(len(visited))

if __name__ == "__main__":
        main()