# Ler os valores
A = int(input())
B = int(input())
C = int(input())
D = int(input())

# Calcular todas as possíveis diferenças
diferenca1 = abs((A + B) - (C + D))
diferenca2 = abs((A + C) - (B + D))
diferenca3 = abs((A + D) - (B + C))

# A menor diferença
menor_diferenca = min(diferenca1, diferenca2, diferenca3)

# Mostrar o resultado
print(menor_diferenca)
