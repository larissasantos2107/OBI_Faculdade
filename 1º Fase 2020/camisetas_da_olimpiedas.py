N = int(input(""))
pedidos = list(map(int, input().split()))
P = int(input(""))  
M = int(input(""))  

# Conta quantos pediram cada tamanho
qtd_p = pedidos.count(1)
qtd_m = pedidos.count(2)

# Verifica se há camisetas suficientes de cada tamanho
if qtd_p <= P and qtd_m <= M:
    print('S')
else:
    print('N')