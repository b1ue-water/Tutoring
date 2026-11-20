from itertools import *

count_num = 0
count_all_num = 1

for i in product("АЛГОРИТМ", repeat=5):

    if (i.count("И") >= 2) and (i[0] != 'Г') and (count_all_num % 2 != 0):
        count_num += 1

    count_all_num += 1

print(count_num)
