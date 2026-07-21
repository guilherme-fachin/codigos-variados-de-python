#criando uma tupla
carros = ("fusca","civic","corolla")

#acessando elementos
print(carros[0]) #fusca

#tentar modificar uma tupla gera erro
#carros[0] = "ferrari" #isso causará um erro!

#para adicionar ou remover elementos, é nescessario criar uma nova tupla
carros = carros + ("ferrari",)
print(carros)

#slicing(possivel em listas, tuplas e strings)
print(carros[2:]) #'corolla','ferrari' #tupla + [algum numero e os dois pontos] faz ela falar todos os valores a partir daquele valor