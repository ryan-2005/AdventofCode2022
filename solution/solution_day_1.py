
with open('input/input_day_1.txt') as file :
    f1=file.read()

f1=f1.strip().split("\n\n")

temp_list = [[int(x) for x in y.split("\n")] for y in f1]

list_1 = []
for z in temp_list:
    temp = sum(z)
    list_1.append(temp)
list_1.sort()
print(list_1[-1])
print(sum(list_1[-3:]))

