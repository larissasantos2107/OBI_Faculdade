from collections import deque

N, F = map(int, input("").split())
matriz = [list(input("")) for _ in range(N)]

# Direções: cima, baixo, esquerda, direita
direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Verificação se a célula pode ser invadida
def pode_invadir(x, y):
    return (0 <= x < N and 0 <= y < N and
            matriz[x][y] != '*' and int(matriz[x][y]) <= F)

fila = deque()

if int(matriz[0][0]) <= F:
    fila.append((0, 0))
    matriz[0][0] = '*'

while fila:
    x, y = fila.popleft()
    for dx, dy in direcoes:
        nx, ny = x + dx, y + dy
        if pode_invadir(nx, ny):
            matriz[nx][ny] = '*'
            fila.append((nx, ny))

for linha in matriz:
    print(''.join(linha))