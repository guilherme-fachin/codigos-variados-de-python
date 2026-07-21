tupla = (1, 2, 3, 2, 4, 5)

#contando a ocorrencia do numero 2
print(tupla.count(2)) #saida: 2

#encontrando o indice da primeira ocorrencia do numero 2
print(tupla.index(2)) #saida: 1

#obtendo o comprimento da tupla
print(len(tupla)) # saida: 6

#encontrado o maior elemento da tupla
print(max(tupla)) #saida: 5

#encontrando o menor elemento da tupla
print(min(tupla)) # saida: 1

#calculando a soma de todos os elementos da tupla
print(sum(tupla)) #saida: 17

#verificando se algum elemento é verdadeiro
print(any(tupla)) #saida: true(pois ha numeros diferentes de zero)

#verificando se todos os elementos sao verdadeiros
print(all(tupla)) #saida:true(pois todos sao diferentes de zero)

# ordenando a tupla (retorna uma lista)
print(sorted(tupla)) # saida: [1, 2, 2, 3, 4, 5]

#revertendo a tupla (retorna um interador)
print(list(reversed(tupla))) #saida: [5, 4, 2, 3, 2, 1] #iterador: e um objeto que percorre uma sequecia de elemento(como uma lista, tupla, conjunto, etc.) um de cada vez. ele nao armazena os elementos; em vez disso, gera cada elemento sob demanda.

