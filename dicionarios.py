#criando um dicionario
precos = {"banana": 3.50, "maca": 4.00,"laranja": 2.75}
print(precos)

#adicionando um novo par chave-valor
precos["abacaxi"] = 5.50
print(precos)

#removendo um item do dicionario
del precos["maca"]
print(precos)

#modificando o valor de uma chave existente
precos["banana"] = 2.90
print(precos)

#precos["banana"] = ["abacate"]
#print(precos)

#verificando se uma chave esta no dicionario
print("abacaxi" in precos)

#escrevendo o valor de uma chave especifica
print(precos["abacaxi"])

