#criando uma lista de numeros
numeros = [1,3,5,7,9]

#acessando elementos da lista
print("primeiro elemento:",numeros[0])
print("ultimo elemento:",numeros[-1])

#modificando um elemento da lista
numeros[0] = 10
print("lista apos a modificacao",numeros)

#adicionando um novo elemento a listas
numeros.append(6)
print("lista apos a adicao:", numeros)

#removendo o ultimo elemento da lista
ultimo_elemento = numeros.pop()
print("elemento removido:", ultimo_elemento)
print("lista apos a remoção:", numeros)

#removendo um elemento especifico da lista
numeros.remove(5) #remove o numero 5 da lista
print("lista apos a remoção:", numeros)

#removendo um elemento especifico pelo indice da lista
print("elemento que sera removido:",numeros[2])
del numeros[2] #remove o elemento de indice 2 da lista
print("lista apos a remoção", numeros)