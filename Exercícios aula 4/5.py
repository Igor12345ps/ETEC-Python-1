salario = input('Digite o salário: ')

if salario <= 280:
    salarior = ((salario/100)*20) + salario
    reajp = '20%'
    reajv = (salario/100)*20
elif salario > 280 and salario <= 700:
    salarior = salario + (salario/100)*15
    reajp = '15%'
    reajv = (salario/100)*15
elif salario > 700 and salario <= 1500:
    salarior = salario + (salario/100)*10
    reajp = '10%'
    reajv = (salario/100)*10
else:
    salarior = salario + (salario/100)*5
    reajp = '5%'
    reajv = (salario/100)*5

print 'Salário antes do reajuste: ', salario
print 'Salário reajustado: ', salarior
print 'Valor do reajuste: ', reajv
print 'Porcentagem do reajuste: ', reajp