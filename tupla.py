tupla =("28/07/2025", "nascido em sp")
tupla

L=[4,6,8,10,2,12,14,2,22,18]
for x, e in enumerate(L):
    print("[%d] %d" % (x,e))
    print("[%d] X %d= %d" % (x,e, x*e)) #multiplicação
    print("[%d] + %d= %d" % (x,e, x+e)) #adição
    print("[%d] - %d= %d" % (x,e, x-e)) #subtração
    print("[%d] / %d = %f" % (x,e, x/e)) #divisão
