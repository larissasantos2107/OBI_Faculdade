# soma dos dígitos de um número
def soma_digitos(n):
    return sum(map(int, str(n)))

S = int(input())
A = int(input())
B = int(input())

menor = None
maior = None

for i in range(A, B+1):
    if soma_digitos(i) == S:
        if menor is None:
            menor = i
        maior = i

print(menor)
print(maior)
