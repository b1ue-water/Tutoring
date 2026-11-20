for n in range(2, 1000):
    
    n_b = bin(n)[2:]
    
    if n_b.count('1') % 2 == 0:
        n_b = '11' + n_b[2:] + '1'
    else:
        n_b = '10' + n_b[2:] + '0'
        
    r = int(n_b, 2)
    
    if r > 150:
        print(r)
        break
    
"""Ответ: 195"""