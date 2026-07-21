lista_de_carros = []

quantidade = int(input("quantos carros voce deseja adicionar a lista? "))

for i in range(quantidade):
    carro = input(f"digite o nome do carro {i}: ")
    lista_de_carros.append(carro)

print("lista de carros criada: ", lista_de_carros)

#precisa ter a "quantidade" para poder falar pro for qnts veses tem q repetir

#cria um loop para exibir a posição e o carro na lista
for index,carro in enumerate(lista_de_carros):
    print(f"na posicao {index} esta o carro: {carro}")

#solicita o indice para excluir
indice_exclusao = int(input(f"digite o indice de 0 a {len(lista_de_carros) - 1} para excluir um carro: "))

#verifica se o indice esta dentro do intervalo valido
if 0 <= indice_exclusao < len(lista_de_carros):
    carro_removido = lista_de_carros.pop(indice_exclusao)
    print(f"carro '{carro_removido}' foi removido da lista.")
else:
    print("erro: indice invalido.")