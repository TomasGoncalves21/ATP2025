import random

soma=21
print("Jogo dos fósforos: tem 21 fósforos. Cada jogador pode retirar entre 1 a 4 fósforos. Quem tirar o ultimo perde.")

inicio=int(input("Quem começa? (1 - jogador , 2 - computador): "))

if inicio == 1 :
    while soma>1 :
        n = int(input("Retira um número de fósforos: "))
        while n<1 or n>4 or n>soma :
            print("Número inválido! Escolhe um número entre 1 e 4, e não maior que o número de fósforos restantes.")
            n = int(input("Retira um número de fósforos: "))

        soma -= n
        print(f"Tiraste {n} fósforos. Restam {soma} fósforos.")

        if soma==1 :
            print("O Jogador ganhou! O computador perdeu.")
            break

        comp=min(5-n, soma-1)
        soma -= comp
        print(f"O computador retirou {comp} fósforos. Faltam {soma} fósforos.")

        if soma == 1 :
            print("O computador ganhou!")
            break

else :
    comp=random.randint(1,4)
    soma -= comp
    print(f"O computador tirou {comp} fósforos. Restam {soma} fósforos.")

    while soma>1 :
        n=int(input("Retira um número de fósforos: "))
        while n<1 or n>4 or n>soma :
            print("Número inválido! Escolhe um número entre 1 e 4, e não maior que o número de fósforos restantes.")
            n=int(input("Retira um número de fósforos: "))

        soma -= n
        print(f"Tiraste {n} fósforos. Restam {soma} fósforos.")

        if soma==1 :
            print("O Jogador ganhou! O computador perdeu.")
            break

        if soma % 5 != 1 :
            comp=(soma-1)%5
            if comp == 0 :
                comp=random.randint(1,min(4,soma-1))
        
        else:
            comp=random.randint(1,min(4,soma-1))

        soma -= comp
        print(f"O computador tirou {comp} fósforos. Restam {soma} fósforos.")

        if soma == 1 :
            print("O computador ganhou!")
            break