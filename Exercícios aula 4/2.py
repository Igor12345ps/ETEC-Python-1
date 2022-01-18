n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))

media = n1 + n2 / 2

if media < 7:
    print("Reprovado")
elif media >= 7 :
    print("Aprovado")
elif media == 10:
    print("Aprovado com Distinção")