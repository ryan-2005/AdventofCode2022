import string


def main():
    item_lst=[i.strip() for i in open('input/input_day_3.txt')]
    all_alphabet = string.ascii_lowercase+string.ascii_uppercase
    all_list = [i for i in all_alphabet]
    dict_alp={}
    for i, j in enumerate(all_list):
        dict_alp[j]=i+1

    dict_counter = {}
    for i in item_lst:
        mid_point = len(i)//2
        first, second=i[:mid_point], i[mid_point:]
        same_elements = set(first).intersection(set(second))
        for i in same_elements:
            if i in dict_counter:
                dict_counter[i] = dict_counter[i]+1
            else:
                dict_counter[i] = 1
    points_1=0
    for i,_ in dict_counter.items():
        points_1 = points_1+(dict_alp[i]*dict_counter[i])


    dict_counter = {}
    for i in range(0,len(item_lst),3):
        temp_list = item_lst[i:i+3]
        common=set(temp_list[0])&set(temp_list[1])&set(temp_list[2])
        common = next(iter(common))
        if common in dict_counter:
            dict_counter[common] = dict_counter[common]+1
        else:
                dict_counter[common] = 1
        
    points_2=0
    for i,_ in dict_counter.items():
        points_2 = points_2+(dict_alp[i]*dict_counter[i])
    
    print(points_1, points_2)

if __name__ == "__main__":
    main()