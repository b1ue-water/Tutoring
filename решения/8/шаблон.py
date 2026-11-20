
from itertools import *

x = product('АЗКМУЫ', repeat=6)
n = 0

for word in x:
    n += 1
    word = ''.join(word)
    
    if n % 2 != 0 and word[0] != 'У' and word.count('Ы') == 1:
        print(n, word)


"""
   product(iterable, n) - когда есть повторения
   set(product())
   """