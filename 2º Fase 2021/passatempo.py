def passatempo():
    from collections import defaultdict

    L, C = map(int, input().split())
    
    grid = []
    linha_soma = []
    for _ in range(L):
        *linha, soma = input().split()
        grid.append(linha)
        linha_soma.append(int(soma))
    
    coluna_soma = list(map(int, input().split()))
    
    valores = dict()

    while True:
        encontrou = False

        for i in range(L):
            contagem = defaultdict(int)
            soma_conhecida = 0
            for j in range(C):
                var = grid[i][j]
                if var in valores:
                    soma_conhecida += valores[var]
                else:
                    contagem[var] += 1
            
            if len(contagem) == 1:
                var, freq = next(iter(contagem.items()))
                valor = (linha_soma[i] - soma_conhecida) // freq
                valores[var] = valor
                encontrou = True
                break

        if encontrou:
            continue

        for j in range(C):
            contagem = defaultdict(int)
            soma_conhecida = 0
            for i in range(L):
                var = grid[i][j]
                if var in valores:
                    soma_conhecida += valores[var]
                else:
                    contagem[var] += 1

            if len(contagem) == 1:
                var, freq = next(iter(contagem.items()))
                valor = (coluna_soma[j] - soma_conhecida) // freq
                valores[var] = valor
                encontrou = True
                break

        if not encontrou:
            break

    for var in sorted(valores):
        print(var, valores[var])

passatempo()
