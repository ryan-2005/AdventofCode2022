# Failed on this one 

def main ():

    grid = [list(map(int,x)) for x in open('input/input_day_8.txt').read().splitlines()]
    counter = 0 
    for r in range(len(grid)):
        for t in range(len(grid[r])):
            k = grid[r][t]
            if all(grid[r][x]<k for x in range(t)) or all(grid[r][x]<k for x in range(t+1,len(grid[r]))) or all(grid[x][t]<k for x in range(r))or all(grid[x][t]<k for x in range(r+1,len(grid))):
               counter+=1
    # part 1 
    print(counter)     

    left =0
    right =0
    top = 0
    bottom = 0
    score_list = []
    for r in range(len(grid)):
        for t in range(len(grid[r])):
            k = grid[r][t]
            for a in range(t-1,-1,-1 ):
                left+=1
                if grid[r][a]>=k:
                    break
            for b in range(t+1,len(grid[r])):
                right +=1
                if grid[r][b]>=k :
                    break
            for c in range(r-1,-1,-1):
                top +=1
                if grid[c][t]>=k:
                    break
            for d in range(r+1,len(grid)):
                bottom +=1
                if grid[d][t]>=k:
                    break
            score_list.append(left*right*top*bottom)
            left=right=top=bottom=0
    print(max(score_list))

if __name__ == "__main__":
        main()



# Another solition online neat
# with open('../input/input_day_8.txt') as file :
#     text=file.read()
# grid = np.array([list(map(int, line)) for line in text.splitlines()])

# def distance(line, tree):
#     i = 0
#     for i, x in enumerate(line, 1):
#         if x >= tree:
#             break
#     return i

# visible = 0
# score = 0
# for y, x in np.ndindex(grid.shape):
#     tree = grid[y, x]
#     visible += int(
#         all(grid[y, :x] < tree) or 
#         all(grid[y, x + 1:] < tree) or
#         all(grid[y + 1:, x] < tree) or
#         all(grid[:y, x] < tree))
#     score = max((distance(reversed(grid[y, :x]), tree) *
#             distance(grid[y, x + 1:], tree) * 
#             distance(reversed(grid[:y, x]), tree) * 
#             distance(grid[y + 1:, x], tree)), score)

# visible, score