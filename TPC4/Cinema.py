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
    print(
        '''1. `listar( cinema )` - que lista no monitor todos os filmes que estão em exibição nas salas do cinema passado como argumento;
        2. `disponivel( cinema, filme, lugar )` - que dá como resultado **False** se o lugar lugar já estiver ocupado na sala onde o filme está a ser exibido e dará como resultado **True** se o inverso acontecer;
        3. `vendebilhete( cinema, filme, lugar )` - que dá como resultado um novo cinema resultante de acrescentar o lugar à lista dos lugares ocupados, na sala onde está a ser exibido o filme;
        4. `listardisponibilidades( cinema )` - que, para um dado cinema, lista no monitor para cada sala, o filme que está a ser exibido e o total de lugares disponíveis nessa sala (número de lugares na sala menos o número de lugares ocupados);
        5. `inserirSala( cinema, sala )` - que acrescenta uma sala nova a um cinema (devendo verificar se a sala já existe);
        6. Acrescente todas as outras funcionalidades que achar necessárias;
        7. À semelhança do exercício 3, construa uma aplicação com um menu de interface para as operações.
        '''
    )
    num=int(input("Escreve a tua opção"))
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
