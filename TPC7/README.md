TPC7: Teste de aferição

Resolva os problemas apresentados a seguir.
### tpc-1. Especifique as seguintes listas em compreensão:
a) Lista formada pelos elementos que não são comuns às duas listas:
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]  
ncomuns = [x for x in lista1 if x not in lista2]+ [x for x in lista2 if x not in lista1]
print(ncomuns)
# Resultado esperado: [1,2,3,7,8]

b) Lista formada pelas palavras do texto compostas por mais de 3 letras:
texto = """Vivia há já não poucos anos algures num concelho do Ribatejo 
    um pequeno lavrador e negociante de gado chamado Manuel Peres Vigário"""
lista = [pal for pal in texto.split() if len(pal)>3]
print(lista)
# Resultado esperado: ['Vivia', 'poucos', 'anos', 'algures', 'concelho', ...]

c) Lista formada por pares do tipo (índice, valor) com os valores da lista dada:
lista = ['anaconda', 'burro', 'cavalo', 'macaco']
listaRes = [(id+1,pal) for (id,pal) in enumerate(lista)]
print(listaRes)
# Resultado esperado: [(1,'anaconda'), (2,'burro'), (3,'cavalo'), (4,'macaco')]

### tpc-2. À semelhança do que foi feito nas aulas, realize as seguintes tarefas:
a) Especifique uma função que dada uma string e uma substring não vazia, calcula  o número de vezes em que a substring aparece na string, sem que haja sobreposição de substrings:
def strCount(s, subs):
    cont=0
    i=0
    while i<len(s):
        pedaco=s[i:i+len(subs)]
        if pedaco==subs:
            cont+=1
            i+=len(subs)
        else:
            i+=1

    return cont

print(strCount("catcowcat", "cat")) # --> 2
print(strCount("catcowcat", "cow")) # --> 1
print(strCount("catcowcat", "dog")) # --> 0

b) Especifique uma função que recebe uma lista de números inteiros positivos e devolve o menor produto que for possível calcular multiplicando os 3 menores inteiros da lista:
def produtoM3(lista):
    res=1
    menor=lista[0]
    a=0
    while a<3:
        for i in lista:
            if i<menor:
                menor=i
        res=res*menor
        lista.remove(menor)
        menor=lista[0]
        a+=1
    return res

print(produtoM3([12,3,7,10,12,8,9]))
# Resultado esperado: 168 = 3 * 7 * 8

c) Especifique uma função que dado um número inteiro positivo, repetidamente adiciona os seus dígitos até obter apenas um dígito que é retornado como resultado:
# Input: 38
# Output: 2
# Explicação: 3 + 8 = 11, 1 + 1 = 2.

# Input: 777
# Output: 3
# Explicação: 7 + 7 + 7 = 21, 2 + 1 = 3.

def reduxInt(n):
    soma=0
    a=str(n)
    while len(a)>1:
        for i in a:
            soma+=int(i)
        a=str(soma)
        soma=0
    return a

print(reduxInt(38))

d) Especifique uma função que recebe duas strings, `string1` e `string2`, e devolve o índice da primeira ocorrência de `string2` em `string1`, caso não ocorra nenhuma vez a função deverá retornar `-1`:
# Invocação: indexOf("Hoje está um belo dia de sol!", "belo")
# Resultado: 13

# Invocação: indexOf("Hoje está um belo dia de sol!", "chuva")
# Resultado: -1

def myIndexOf(s1, s2):
    modo=-1
    for i in s1.split():
        if i==s2:
            modo=s1.index(i)
    return modo

print(myIndexOf("Hoje está um belo dia de sol!", "belo"))
print(myIndexOf("Hoje está um belo dia de sol!", "chuva"))
### tpc-3. A Rede Social

Considere que a informação sobre uma rede social está armazenada numa lista de dicionários.

Cada dicionário, correspondente a um _post_ e tem chaves `id`, `conteudo`, `autor`, `dataCriacao` e `comentarios`.
Por sua vez, `comentarios` é uma lista de dicionários com chaves `comentario` e `autor`.

Considere o seguinte exemplo:

``` 
    MyFaceBook = [{
        'id': 'p1', 
        'conteudo': 'A tarefa de avaliação é talvez a mais ingrata das tarefas que um professor
    tem de realizar...', 
        'autor': 'jcr', 
        'dataCriacao': '2023-07-20', 
        'comentarios': [
            {
                'comentario': 'Completamente de acordo...',
                'autor': 'prh'
            },
            {
                'comentario': 'Mas há quem goste...',
                'autor': 'jj'
            }
        ]},
        {
            'id': 'p2',
            ...
        },
        ...
        ]
```
Defina as seguintes funções de manipulação e consulta da rede social:
#### a) `quantosPost`, que indica quantos posts estão registados:
def quantosPost(redeSocial):
    res=0
    for i in redeSocial:
        res+=1
    return res
    
b)  `postsAutor`, que devolve a lista de posts de um determinado autor:
def postsAutor(redeSocial, autor):
    p=[]
    for post in redeSocial:
        if post['autor']==autor:
            p.append(post)
            
    return p
    
c) `autores`, que devolve a lista de autores de posts ordenada alfabeticamente:
def autores(redeSocial):
    a=[]
    for post in redeSocial:
        if post['autor'] not in a:
            a.append(post['autor'])
    b=sorted(a) 
    return b
    
d) `insPost`, que acrescenta um novo post à rede social a partir dos parâmetros recebidos e devolve a nova rede social. 
    
O campo `id` devrá ser calculado a partir dos já existentes, por exemplo, se a rede tiver posts com id `p1`, `p2` e `p3`, o novo `id` deverá ser `p4`.
def insPost(redeSocial, conteudo, autor, dataCriacao, comentarios):
    res=len(redeSocial)
    i=f'p{res+1}'
    post={
        'id':i,
        'conteudo':conteudo,
        'autor':autor,
        'dataCriacao':dataCriacao,
        'comentarios':comentarios
    }
    redeSocial.append(post)
    return redeSocial
    
e)  `remPost`, que remove um post da rede, correspondente ao `id` recebido.
def remPost(redeSocial, id):
    novaRedeSocial=[post for post in redeSocial if post['id']!=id]
    return novaRedeSocial
    
f) `postsPorAutor`, que devolve uma distribuição de posts por autor (à semelhança do que foi feito nas aulas).
def postsPorAutor(redeSocial):
    cont=0
    rede={}
    for i in redeSocial:
        autor = i['autor']
        if autor in rede:
            rede[autor]+=1
        else:
            rede[autor]=1
    return rede
    
g) `comentadoPor`, que recebe um autor e devolve a lista de posts comentados por esse autor.
def comentadoPor(redeSocial, autor):
    res=[]
    for post in redeSocial:
        for comentario in post:
            if autor==comentario['autor']:
                res.append(post['comentarios'])
    return res
