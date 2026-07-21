aluno1 = ("a", 15, "1°b")
aluno2 = ("b", 11, "2°b")
aluno3 = ("c", 55, "1°a")
notas_alunos1 = (7.5, 20, 2, 0)
notas_alunos2 = (9, 8, 7, 6)
notas_alunos3 = (1, 3, 4, 5)

nome1, idade1, turma1 = aluno1
print(f"nome : {nome1}, idade: {idade1}, turma: {turma1}")

nome2, idade2, turma2 = aluno2
print(f"nome : {nome2}, idade: {idade2}, turma: {turma2}")

nome3, idade3, turma3 = aluno3
print(f"nome : {nome3}, idade: {idade3}, turma: {turma3}")

nota1_1, nota1_2, nota1_3, nota1_4 = notas_alunos1
print(f"notas de {nome1}: {nota1_1}, {nota1_2}, {nota1_3} {nota1_4}")

nota2_1, nota2_2, nota2_3, nota2_4 = notas_alunos2
print(f"notas de {nome2}: {nota2_1}, {nota2_2}, {nota2_3} {nota2_4}")

nota3_1, nota3_2, nota3_3, nota3_4 = notas_alunos3
print(f"notas de {nome3}: {nota3_1}, {nota3_2}, {nota3_3} {nota3_4}")

print(f"menor nota do aluno {nome1}:{min(notas_alunos1)}")
print(f"maior nota do aluno {nome2}:{max(notas_alunos2)}")
print(f"soma das notas do aluno {nome3}:{sum(notas_alunos3)}")

#o "f" nos prints servem, para o "{}" funcionar
#tive que colocar o comando detro de "{}" e nao "()" porque se nao da erro pois eu usei outra "{}" antes