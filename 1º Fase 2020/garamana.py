from collections import Counter

P = input().strip()
A = input().strip()

cont_P = Counter(P)
cont_A = Counter(c for c in A if c != '*')
curingas = A.count('*')

# Calcular quantas letras faltam em A para ser anagrama de P
faltando = 0
for letra in cont_P:
    qtd_P = cont_P[letra]
    qtd_A = cont_A.get(letra, 0)
    if qtd_A < qtd_P:
        faltando += qtd_P - qtd_A

# Verificar se o número de curingas cobre as letras faltantes
if faltando <= curingas:
    print("S")
else:
    print("N")