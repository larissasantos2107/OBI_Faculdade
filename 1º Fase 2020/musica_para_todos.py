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