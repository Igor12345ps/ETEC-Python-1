horas = input(‘Digite o numero de horas trabalhadas: ‘)
ghoras = input(‘Digite o ganho por horas: ‘)

bruto = ghoras * horas

cinco = (5 / 100.0) * bruto
dez = (10 / 100.0) * bruto
vinte = (20 / 100.0) * bruto
onze = (11 / 100.0) * bruto

if bruto <= 900:
       print ‘Seu salário bruo é de:’,bruto – cinco
       print ‘(-) IR (5%) :’,’ R$’,cinco
       print ‘(-) INSS ( 10%):’,’ R$’,dez
       print ‘FGTS (11%): ‘,’ R$’,onze
       print ‘Total de descontos:’,’R$’,cinco + dez + onze
       print ‘Salário Liquido :’,’ R$’,bruto – (cinco + dez + onze)
elif bruto >= 900 and bruto <= 1500:
       print ‘Seu salário bruo é de:’,bruto – dez
       print ‘(-) IR (5%) :’,’ R$’,cinco
       print ‘(-) INSS ( 10%):’,’ R$’,dez
       print ‘FGTS (11%): ‘,’ R$’,onze
       print ‘Total de descontos:’,’R$’,cinco + dez + onze
elif bruto > 1500:
       print ‘Seu salário bruo é de:’,bruto – vinte
       print ‘(-) IR (5%) :’,’ R$’,cinco
       print ‘(-) INSS ( 10%):’,’ R$’,dez
       print ‘FGTS (11%): ‘,’ R$’,onze
       print ‘Total de descontos:’,’R$’,cinco + dez + onze