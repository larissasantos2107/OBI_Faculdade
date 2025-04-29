n = int(input(""))
lista = list(map(int, input().split()))

esquerda = 0
direita = n - 1

operacoes = 0

while esquerda < direita:
    if lista[esquerda] == lista[direita]:
        esquerda += 1
        direita -= 1
    elif lista[esquerda] < lista[direita]:
        lista[esquerda + 1] += lista[esquerda]
        esquerda += 1
        operacoes += 1
    else:
        lista[direita - 1] += lista[direita]
        direita -= 1
        operacoes += 1

print(operacoes)
