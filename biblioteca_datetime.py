from datetime import datetime

def calcular_idade(data_nascimento):
    #obter a data atual
    data_atual = datetime.now()

    #calcular a idade
    idade = data_atual.year - data_nascimento.year

    #verificar se a pessoa ja fez aniversario este ano
    if (data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day):
        idade -= 1
    
    return idade

def main():
    data_str = input("digite sua data de nascimento (no formato DD/MM/AAAA): ")

#converter a tring para uma data usando o formato especificado
    data_nascimento = datetime.strptime(data_str, "%d/%m/%Y")

#calcular e exibir a idade
    idade = calcular_idade(data_nascimento)
    print(f"voce tem {idade} anos.")

if __name__ == "__main__":
    main()