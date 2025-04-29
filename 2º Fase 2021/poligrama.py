N = int(input())
P = input()

def eh_anagrama(base, palavra):
    return sorted(base) == sorted(palavra)

for tamanho in range(1, N//2 + 1):
    if N % tamanho != 0:
        continue  
    raiz = P[:tamanho]
    ok = True
    for i in range(0, N, tamanho):
        pedaço = P[i:i+tamanho]
        if sorted(pedaço) != sorted(raiz):
            ok = False
            break
    if ok:
        print(raiz)
        break
else:
    print('*')
