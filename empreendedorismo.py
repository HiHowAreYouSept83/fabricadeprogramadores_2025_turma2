estoque = {"strat": [10, 1500.0],
           "telecaster": [14, 1243.92],
           "mustang": [8, 4687.23],
           "jaguar": [19, 3347.55],
           "jagstang": [5, 8764.32],
           "thinline": [12, 2670.44],
           "les-paul": [31, 990.99],
           "LPS": [10, 1100.00],
           "vip": [13, 2590.52],
           "SG": [10, 2200.12], 
           "Soloist": [2, 3350.59],
           "Mockingbird": [5, 2460.63],
           "warlock":[12, 3210.43],
           "flying V":[24, 3124.10],
           "Starcaster":[1, 6466.56],
           "iceman":[22, 1000.00],
           "Firebird":[17, 2219],
           "jazzmaster":[29, 1541.99],
           "hollow":[12, 4500.99],
           "explorer":[3, 5656.65]}

produto = input("digite o produto selecionado:")
quantidade = int(input("digite a quantidade:"))
venda = [ [produto, quantidade]]
total = 0
if produto in estoque:
  print("Vendas:\n")
  for operação in venda:
    produto, quantidade = operação 
    preço = estoque[produto][1] 
    custo = preço * quantidade
    print("%12s: %3d x %6.2f = %6.2f" %
		(produto, quantidade,preço,custo))
    estoque[produto][0] -= quantidade 
    total+=custo
else:
   print ("nao temos esse produto em estoque") 
print(" Custo total: %21.2f\n" % total)
print("Estoque:\n")
for chave, dados in estoque.items(): 
    print("Descrição: ", chave)
    print("Quantidade: ", dados[0])
    print("Preço: %6.2f\n" % dados[1])