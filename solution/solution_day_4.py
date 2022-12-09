def main():
    item_lst=[i.strip() for i in open('input/input_day_4.txt')]

    counter = 0
    for i in item_lst:
        a,b=i.split(',')
        a1,a2=a.split('-')
        b1,b2=b.split('-')
        list_1 = [i for i in range (int(a1),int(a2)+1,1)]
        list_2 = [i for i in range(int(b1),int(b2)+1,1)]
        if set(list_1).issubset(set(list_2)) or set(list_2).issubset(set(list_1)):
            counter+=1
    print(counter)

    counter_2 = 0
    for i in item_lst:
        a,b=i.split(',')
        a1,a2=a.split('-')
        b1,b2=b.split('-')
        a1,a2,b1,b2=int(a1),int(a2),int(b1),int(b2)
        list_1 = [i for i in range (int(a1),int(a2)+1,1)]
        list_2 = [i for i in range(int(b1),int(b2)+1,1)]
        if set(list_1).intersection(set(list_2)) or set(list_2).intersection(set(list_1)):
            counter_2+=1

    print (counter_2)

if __name__ == "__main__":
    main()