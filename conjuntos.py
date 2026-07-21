#criando um conjunto
frutas = {"banana", "maça", "laranja"}

print(frutas)

#adicionando um item ao conjunto
frutas.add("abacaxi")
print(frutas)

#removendo um item do conjunto
frutas.remove("maça")
print(frutas)

#tentando adicionar um item ja existente(na caus erro, mas o item nao e duplicado) #nao permite duplicacao nem se coloca direto no conjunto
frutas.add("banana")
print(frutas)

#verificando se um item esta no conjunto
print("abacaxi" in frutas)