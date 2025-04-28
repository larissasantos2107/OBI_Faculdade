entrada = input()

# Guardar as cartas que aparecem em cada naipe
cartas_copas = set()
cartas_espadas = set()
cartas_ouros = set()
cartas_paus = set()

# checa se tem repetição
repeticoes = {
    'C': set(),
    'E': set(),
    'U': set(),
    'P': set()
}

# Processar a entrada (de 3 em 3 caracteres)
erro = {
    'C': False,
    'E': False,
    'U': False,
    'P': False
}

for i in range(0, len(entrada), 3):
    numero = entrada[i:i+2]  # dígitos da carta
    naipe = entrada[i+2]     # letra do naipe

    if numero in repeticoes[naipe]:
        erro[naipe] = True
    else:
        repeticoes[naipe].add(numero)

    if naipe == 'C':
        cartas_copas.add(numero)
    elif naipe == 'E':
        cartas_espadas.add(numero)
    elif naipe == 'U':
        cartas_ouros.add(numero)
    elif naipe == 'P':
        cartas_paus.add(numero)


def verificar(cartas, naipe):
    if erro[naipe]:
        print('erro')
    else:
        faltando = 13 - len(cartas)
        print(faltando)

verificar(cartas_copas, 'C')
verificar(cartas_espadas, 'E')
verificar(cartas_ouros, 'U')
verificar(cartas_paus, 'P')

