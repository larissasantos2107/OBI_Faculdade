n = int(input(""))
pilha = []

for _ in range(n):
    x = int(input())
    if x == 0 and pilha:
        pilha.pop()
    else:
        pilha.append(x)

print(sum(pilha))
