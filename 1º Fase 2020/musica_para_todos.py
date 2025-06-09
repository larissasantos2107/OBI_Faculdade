<<<<<<< HEAD
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
=======
def musica_para_todos():
    import sys
    input = sys.stdin.readline

    N, M, C = map(int, input().split())
    amigos = [tuple(map(int, input().split())) for _ in range(N)]

    # Para cada música, lista dos amigos que detestam essa música (índices)
    detestam = [[] for _ in range(M+1)]

    for i, (A, D) in enumerate(amigos):
        detestam[D].append(i)

    musica_atual = C
    trocas = 0
    usadas = set([musica_atual])  # para detectar ciclos

    while True:
        if not detestam[musica_atual]:
            # Nenhum amigo detesta essa música, todos satisfeitos
            print(trocas)
            return
        
        # Amigo que detesta a música e é cliente mais antigo
        amigo_indice = detestam[musica_atual][0]
        musica_nova = amigos[amigo_indice][0]  # música que ele adora

        if musica_nova in usadas:
            # Ciclo infinito detectado
            print(-1)
            return

        musica_atual = musica_nova
        trocas += 1
        usadas.add(musica_atual)
>>>>>>> cc68966efa5a0b5d1fe8175c84c37ff1166fd5b2
