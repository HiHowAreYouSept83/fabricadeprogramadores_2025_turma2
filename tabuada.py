"""n = int(input("tabuada de:"))
x = 1
while x <= 10:
     print(n+x)
     x=x+1"""


"""def tabuada():
    numero = int(input("digite um número:"))
    x=1
    while x <=10:
        print(numero,"x",x,"=", x*numero)
        x=x+1 
tabuada()"""

"""def tabuada():
    numero = int(input("digite um número:"))
    fim = int(input("digite o numero final: "))
    x=1
    while x <= fim:
        print(numero,"x",x,"=", x*numero)
        x=x+1 
tabuada()"""

"""s=0
while True:
    v=int(input("digite um numero a somar ou 0 para sair:"))
    if v==0:
        break
    s = s+v
print(s)"""

#socorro Deus

s = 0
c = 0
while True:
    v=int(input("digite um número a somar ou 0 para sair: "))
    if v==0:
        break
    s += v
    c += 1
if c > 0:
     media = s / c
     print("soma:", s)
     print("quantidade de valores", c)
     print("media dos valores:", media)
else:
    print("nenhum numero informado")