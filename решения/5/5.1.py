max_r = 0

for n in range(2, 10001):
    
    n_b = bin(n)[2:]
    
    if n % 2 == 0:
        n_b = "11" + n_b[2:] + "11"
    else:
        n_b = "1" + n_b[2:] + "00"
        
    r = int(n_b, 2)
    
    if r <= 113:
        max_r = max(r, max_r)

print(max_r)