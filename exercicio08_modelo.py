usuarios = ["Luiz", "Felipe", "Tiago", "Ricardo"]
opcoes = ["C - cadastrar usuario", "R - Leitura de usuários", "U - atualizar usuario", "D - deletar usuario"]

print("Escolha uma opção:")

for i, opcao in enumerate(opcoes, start=1):
    print(f"{i}. {opcao}")

opcao = int(input("Digite o número da opção desejada: "))

while opcao > 0 and opcao < 5: 
    if opcao == 1:
        print("Você escolheu a opção cadastro.")
        novo_usuario = input("digite o nome do novo usuario: ")
        usuarios.append(novo_usuario)
        print(f"usuario {novo_usuario} cadastro com sucesso!")

    elif opcao == 2:
        print("Você escolheu a opção Leitura.")  
        for usuario in usuarios:
            print(usuario) 

    elif opcao == 3:
        print("Você escolheu a opção atualização.")
        for i, usuario in enumerate(usuarios, start=1):
            print(f"{i}. {usuario}")
        indice = int(input("digite o numero do usuario que deseja atualizar: ")) - 1
        if 0 <= indice and indice < len(usuarios):
            novo_nome = input(f"digite o novo nome para {usuarios[indice]}: ")
            usuarios[indice] = novo_nome
            print(f"usuarios atualizados para {novo_nome} com sucesso!")
        else:
            print("usuario invalido.")

    elif opcao == 4:
        print("Você escolheu a opção exclusão.")
        for i,usuario in enumerate(usuarios, start=1):
            print(f"{i}. {usuario}")
        indice = int(input("digite o numero do usuario que deseja excluir: ")) - 1
        if 0 <= indice and indice < len(usuarios):
            removido = usuarios.pop(indice)
            print(f"usuario {removido} excluido com sucesso!")
        else:
            print("usuario invalido")

    opcao = int(input("Digite o número da opção desejada: "))

print("Opção inválida. Tente novamente.")
print("Encerrando o sistema")




