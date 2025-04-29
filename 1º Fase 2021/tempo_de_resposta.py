n = int(input())
eventos = [input().split() for _ in range(n)]

tempo_atual = 0
aguardando = {}  # tempo de recebimento
tempo_total = {}  # tempo de resposta total

i = 0
while i < n:
    evento, x = eventos[i][0], int(eventos[i][1])

    if evento == 'T':
        tempo_atual += x
        i += 1
        continue

    if i > 0 and eventos[i-1][0] != 'T':
        tempo_atual += 1

    if evento == 'R':
        aguardando[x] = tempo_atual
        if x not in tempo_total:
            tempo_total[x] = 0

    elif evento == 'E':
        if x in aguardando:
            tempo_total[x] += tempo_atual - aguardando[x]
            del aguardando[x] 
    i += 1

# processa todos eventos
for amigo in tempo_total.keys():
    if amigo in aguardando:
        tempo_total[amigo] = -1

# Imprimir em ordem 
for amigo in sorted(tempo_total.keys()):
    print(amigo, tempo_total[amigo])
