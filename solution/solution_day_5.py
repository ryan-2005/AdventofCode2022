import copy

def main():
    #Reading file part was hard
    with open('input/input_day_5.txt') as file:
            file=file.readlines()
    indexOfSplit = file.index("\n")
    numColumns = len(file[indexOfSplit-2].split(" "))
    crates_lists = [[] for x in range(numColumns)]
    for i in range (indexOfSplit-2,-1,-1):
        index=0
        for j in range(indexOfSplit):
            obj = file[i][index+1]
            if obj != " ":
                cratesColumn = crates_lists[j]
                cratesColumn.append(obj)
                crates_lists[j] = cratesColumn
            index+=4

    crates_lists_1 = copy.deepcopy(crates_lists)
        
    for line in file[indexOfSplit+2:]:
        action = line.rstrip()
        _,a,_,b,_,c=action.split(" ")
        from_column = crates_lists_1[int(b)-1]
        if len(from_column) == 0:
            print(action)
            break
        to_column = crates_lists_1[int(c)-1]
        for i in range(int(a)):
            to_column.append(from_column.pop())
        crates_lists_1[int(b)-1] = from_column
        crates_lists_1[int(c)-1] = to_column
        
    top=[]
    for i in range(len(crates_lists_1)):
        top.append(crates_lists_1[i][-1])
    print(top)

    crates_lists_2 = copy.deepcopy(crates_lists)

    for line in file[indexOfSplit+2:]:
        action = line.rstrip()
        _,a,_,b,_,c=action.split(" ")
        from_column = crates_lists_2[int(b)-1]
        to_column = crates_lists_2[int(c)-1]
        temp_list =[]
        for i in range(int(a)):
            temp_list.append(from_column.pop())
        temp_list=temp_list[::-1]
        crates_lists_2[int(b)-1] = from_column
        crates_lists_2[int(c)-1] = to_column+temp_list
    top=[]
    for i in range(len(crates_lists_2)):
        top.append(crates_lists_2[i][-1])
    print(top)

if __name__ == "__main__":
    main()


# # different way of reading file
# input = []
# instructions = [[]]
# crates = []
# crate_stacks = []
# procedure = []

# # read input file
# with open('Day_5.txt', 'r') as file:
#     for line in file:
#         input.append(line)

# # split instructions in half into drawing & procedure
# delimiter = '\n'
# for line in input:
#     if line == delimiter:
#         instructions.append([])
#     elif line != delimiter:
#         instructions[-1].append(line.split('\n')[0])

# drawing = instructions[0]
# for line in drawing:
#     crates.append([line[containers * 4 + 1] for containers in range(len(line) // 4 + 1)])
# # transpose rows into columns (stacks)
# crate_stacks = [list("".join(stack_column).strip()[::-1]) for stack_column in zip(*crates)]