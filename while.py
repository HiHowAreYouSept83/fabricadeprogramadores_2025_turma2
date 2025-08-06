"""x=1
while x<=3:
    print(x)
    x = x + 1"""

"""x=1
while x<=50000:
    print(x)
    x = x + 1"""

"""x=1
while x<=100:
    print(x)
    x = x + 1"""

"""x=50
while x<=100:
    print(x)
    x = x + 1"""


"""def exercicio_3():
    x = 10
    while x >= 0: 
        print(x)
        x = x - 1
    print('fogo') 
exercicio_3()"""

"""
fim=int(input("digite o ultimo numero a imprimir:"))
x=0
while x <= fim:
    if x % 2 == 0:
        print(x) 
    x = x + 1"""

"""def numero_par():
    fim=int(input("digite o ultimo numero a imprimir:"))
    x=0
    while x <= fim:
        if x % 2 == 0:
            print(x) 
        x = x + 1
numero_par()"""

"""def numero_impar():
    fim=int(input("digite o ultimo numero a imprimir:"))
    x=0
    while x <= fim:
        if x % 2 == 1:
            print(x) 
        x = x + 1
numero_impar()"""

"""def arvore_de_natal():
    linha = 1
    while linha <= 10:
        coluna = 1
        while coluna <= linha:
            coluna = coluna + 1
            if coluna % 2 == 1: 
                print('❤️', end="")
            else: 
                print('💚', end="")
        print()
        linha = linha + 1
arvore_de_natal()"""
            
"""def arvore_de_natal():
    linha = 1
    while linha <= 10:
        coluna = 1
        while coluna <= linha: 
            if (linha + coluna) % 2 ==0:
                print('💚', end=="")
            else:
                print('❤️', end=="")
            coluna = coluna + 1
        print()
        linha = linha + 1
arvore_de_natal()"""

n = int(input("tabuada de"))
x = 1
while x <= 10:
     print(n+x)
     x+x+1