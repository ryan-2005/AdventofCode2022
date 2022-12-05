from itertools import permutations,combinations
item_lst=[i.strip() for i in open('input/input_day_2.txt')]



list_1=['A','B','C','X','Y','Z']

comb_list=list(combinations(list_1,2))

possible_score = {('A X'):3,
('A Y'):6,
('A Z'):0,
('B X'):0,
('B Y'):3,
('B Z'):6,
('C X'):6,
('C Y'):0,
('C Z'):3}

my_own_score = {'X':1,'Y':2,'Z':3}

score  = 0 
for i in item_lst : 
    print(i)
    opp,me=i.split()
    score += my_own_score[me]
    score += possible_score[(i)]
print(score)


possible_score = {('A X'):3,
('A Y'):1,
('A Z'):2,
('B X'):1,
('B Y'):2,
('B Z'):3,
('C X'):2,
('C Y'):3,
('C Z'):1}

my_own_score = {'X':0,'Y':3,'Z':6}
score2 = 0 
for i in item_lst : 
    print(i)
    opp,me=i.split()
    score2 += my_own_score[me]
    score2 += possible_score[(i)]
print(score2)