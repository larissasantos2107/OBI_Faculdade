N, K, U = map(int, input("").split())

cartelas = []
for _ in range(N):
    cartelas.append(list(map(int, input().split())))

sorteados = list(map(int, input().split()))

# posição em que foi sorteado 
posicao_sorteio = {}
for rodada, numero in enumerate(sorteados):
    posicao_sorteio[numero] = rodada

tempos_para_completar = []

for cartela in cartelas:
    tempo = max(posicao_sorteio[num] for num in cartela)
    tempos_para_completar.append(tempo)

menor_tempo = min(tempos_para_completar)

# Encontrar cartelas que foram completadas
vencedoras = [i + 1 for i, t in enumerate(tempos_para_completar) if t == menor_tempo]

print(' '.join(map(str, sorted(vencedoras))))