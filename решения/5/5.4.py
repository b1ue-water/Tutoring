def tri(n):
    tri_ostatki = []
    
    while n > 0:
        ostatok = n % 3
        tri_ostatki.append((str(ostatok)))
        
        n //= 3

    return ''.join(reversed(tri_ostatki))

for n in range(2, 10001):
    n_tri = tri(n)
    
    if n % 3 == 0:
        n_tri = n_tri + n_tri[-2:]
    else:
        sum = (n_tri.count('1') + n_tri.count('2') * 2) * 2
        sum_tri = tri(sum)
        n_tri = n_tri + sum_tri

    r = int(n_tri, 3)
    
    if (r > 520) and (r % 2 != 0):
        print(r)
        break
    
"""Ответ: 631

tri_ostatki = [0, 2, 1, 1, 1]

reversed(tri_ostatki) = ["1", "1", "1", "2", "0"]

''.join([1, 1, 1, 2, 0]) -> "11120" - str

n -> int
"""