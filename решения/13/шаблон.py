
from itertools import *

count_num = 0
count_all_num = 1

for word in product("АЛГОРИТМ", repeat=5):

    if (word.count("И") >= 2) and (word[0] != 'Г') and (count_all_num % 2 != 0):
        count_num += 1

    count_all_num += 1

print(count_num)

