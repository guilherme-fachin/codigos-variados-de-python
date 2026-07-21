#este codigo solicita ao usuario uma resposta e continua execuando
#enquanto a resposta for "sim"
resposta = input("deseja continuar?(digite 'sim' para continuar):")

#a funcao lower() transforma toda a string em letras minusculas
while resposta.lower() == "sim":
    resposta = input("deseja continuar?(digite 'sim' para continuar): ")