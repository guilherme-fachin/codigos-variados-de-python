produtos = ["pc gamer","xbox series","playstation 5","nitendo switch","notebook gamer","teste"]
valores = [8000,3000,4500,2500,6000]

#percorrendo duas listas ao mesmo tempo

#zip()
for produto, valor in zip(produtos, valores):
    print("o valor de {} é R${}".format(produto, valor))

#range()
#for i in range(len(produtos)):
#   print("o valor de {} é R${}".format(produtos[i], valores[i]))

#enumerate()
#for i, produto in enumerate(produtos):
#   print("o valor de {} é R${}".format(produto, valores[i]))