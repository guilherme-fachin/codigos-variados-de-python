#solicitar a noita do aluno em uma disciplina
nota = float(input("digite a nota do aluno: "))

#verificar a situação do aluno com base na nota
if nota >= 9.0:
    print("conceito A - excelente")
if nota >= 7.0 and nota < 9.0:
    print("conceito B - bom")
if nota >= 5.0 and nota < 7.0:
    print("conceito C - regular")
if nota < 5.0:
    print("conceito D - insuficiente")