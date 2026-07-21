#solicitar os anos de experiencia do profissional
anos_experiencia = int(input("digite quantos anos de experiencia o profissional possui: "))

#verificar a classificação do profissional com base nos nos de experiencia
if anos_experiencia < 5:
    print("profissional em incio de carreira - junior")
elif anos_experiencia >= 5 and anos_experiencia < 10:
    print("profissional pleno")
elif anos_experiencia >= 10 and anos_experiencia < 15:
    print("profissional senior")
elif anos_experiencia >= 15:
    print("profissional master")