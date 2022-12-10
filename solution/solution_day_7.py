from collections import defaultdict
# failed on this one



def main():
     with open('input/input_day_7.txt') as file:
            file=file.read()
     lines = [x for x in file.split('\n')]

     path =[]
     dict_path_size =defaultdict(int)
     mem = 0
    for line in lines:
        print(path)
    directory=line.strip().split()
    if directory[1] == 'cd':
        if directory[2] == '..':
            path.pop()
        else:
            path.append(directory[2])
    elif directory[1] == 'ls':
        continue
    else :
        try: 
            mem=int(directory[0]) 
            print(path,mem)
            # This part appending mem to existing directory with the use of default dict
            for i in range(len(path)+1):
                dict_path_size['/'.join(path[:i])] += mem
        except:
            pass

    target_size=100000
    size_list=[j for i,j in filtered.items() if (j <= target_size) & (j!= None)]
    print(sum(size_list))
    
    #part 2 
    total_space = 70000000
    update_size = 30000000
    unused_target = 30000000
    free_space=total_space - dict_path_size['/'] 
    target = unused_target-free_space 
    options = []
    for key,value in dict_path_size.items():
        if(value > target):
            options.append(value)

    print(min(options))