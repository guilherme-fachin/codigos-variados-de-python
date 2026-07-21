#criando um arrary de tamanho 5
numeros = [0] * 5

#solicitando 5 inteiros ao usuario
for i in range(5):
    numeros[i] = int(input("digite o {}º numero inteiro: ".format(i+1)))

#imprimindo cada numero com sua posicao na lista
for i, numero in enumerate(numeros):
    print("o numero {} esta na posicao {} da lista.".format(numero,i))
