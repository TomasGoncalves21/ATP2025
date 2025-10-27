def listar(cinema):
    lista=[]
    for sala in cinema:
        lista.append(sala[2])
    return lista
def disponivel (cinema, filme, lugar):
    res=False
    for sala in cinema:
        if filme == sala [1]:
            if lugar not in sala [1]:
                res=True
    return res
def venderbilhete (cinema, filme, lugar):
     if disponivel(cinema, filme, lugar):
        for sala in cinema:
            if filme==sala[2]:
                sala[1].append(lugar)
     return cinema
def listardisponibilidades(cinema):
    l=[]
    for sala in cinema:
        info=(sala[2],sala[0]-len(sala[1]))
        l.append(info)
    return l
def insersala(cinema, sala):
    if sala not in cinema:
        cinema.append(sala[2])
    return cinema
def menu():
    print('''\n=== Gestão de Cinema ===
1. Inserir Sala
2. Listar Filmes
3. Vender Bilhete
4. Verificar Disponibilidade
5. Listar Disponibilidades
6. Remover Sala
0. Sair''')
    
    num=int(input("Escolha uma opção: "))
    if num ==1:
        lista=listar(cinema)
        for filmes in lista:
         print(filmes)
    if num==2:
        cinema=str(input("Escolha o cinema"))
        filme=str(input("Qual é o filme que quer ver"))
        lugar=str(input("Escolha o lugar"))
        cond=disponivel(cinema, filme, lugar)
        if cond:
            print("O seu lugar está disponével")
        else:
            print("Não está")
    if num ==3:
        cinema=str(input("Escolha o cinema"))
        filme=str(input("Qual é o filme que quer ver"))
        lugar=str(input("Escolha o lugar"))
        venderbilhete(cinema, filme, lugar)
    if num==4:
        print(listardisponibilidades(str(input("Escolha o cinema"))))

    if num ==5:
        cinema=str(input("Escolha o cinema"))
        num_lugares=int(input("Insira o número de lugares"))

        n=int(input("Insira o número de lugares"))
        lista=[]
        for i in range(n):
            num=int(input("Qual o num do lugar"))
            lista.append(num)

        filme=str(input("Insira o filme"))
        sala=(num_lugares, lista, filme)
        insersala(cinema, sala)

menu()
