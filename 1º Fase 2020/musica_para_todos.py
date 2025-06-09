def musica_para_todos(n, m, c, preferencias):
    # Mapear música detestada para lista de amigos que a detestam
    detestam = {}
    adora = [0] * n

    for i, (a, d) in enumerate(preferencias):
        adora[i] = a
        detestam.setdefault(d, []).append(i)

    atual = c
    tocadas = set()
    trocas = 0

    while True:
        if atual in tocadas:
            return -1  
        tocadas.add(atual)

        if atual not in detestam:
            return trocas  

        amigo = detestam[atual][0]  
        nova = adora[amigo]

        if nova == atual:
            return -1  

        atual = nova
        trocas += 1



n, m, c = map(int, input().split())
preferencias = [tuple(map(int, input().split())) for _ in range(n)]


print(musica_para_todos(n, m, c, preferencias))
