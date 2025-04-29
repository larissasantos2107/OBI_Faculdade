def pode_formar_retangulo(N, L):
    perimetro = sum(L)
    
    # Se perímetro ímpar, nunca vai dividir exatamente
    if perimetro % 2 != 0:
        return 'N'
    
    pos = [0]
    for l in L:
        pos.append(pos[-1] + l)
    
    pos_set = set(pos[:-1])  

    count = 0
    for p in pos[:-1]:
        if (p + perimetro // 2) in pos_set:
            count += 1
    
    if count >= 2:
        return 'S'
    else:
        return 'N'

N = int(input())
L = list(map(int, input().split()))
print(pode_formar_retangulo(N, L))
