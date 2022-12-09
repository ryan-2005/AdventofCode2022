import copy

def main():
    with open('input/input_day_6.txt') as file:
            file=file.read()

    occur =[]
    for i in range(len(file)-1):
        temp_list = list(file[i:i+4])
        if len(set(temp_list)) != 4:
            pass
        else :
            occur.append(i)
    print(occur[1] + 3)

    occur =[]
    for i in range(len(file)-1):
        temp_list = list(file[i:i+14])
        if len(set(temp_list)) != 14:
            pass
        else :
            occur.append(i)
    print(occur[0] + 14)

if __name__ == "__main__":
    main()