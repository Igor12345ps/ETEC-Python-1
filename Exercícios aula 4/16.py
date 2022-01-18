num1 = input("Digite o primeiro numero: ")
num2 = input("Digite o segundo numero: ")
operacao = input("Qual operacao voce deseja? (+, -, *, /): ")

if operacao == '+':
	resultado = num1 + num2
	if resultado % 2 == 0:
		print("O numero %d e par!" % resultado)
	else:
		print("O numero %d e impar." % resultado)
	if resultado >= 0:
		print("O numero %d e Positivo!" % resultado)
	else:
		print("O numero %d e negativo." % resultado)
	if round(resultado) == resultado:
		print("O numero %d e inteiro!" % resultado)
	else:
		print("O numero %.1f e decimal." % resultado)

if operacao == '-':
	resultado = num1 - num2
	if resultado % 2 == 0:
		print("O numero %d e par!" % resultado)
	else:
		print("O numero %d e impar." % resultado)
	if resultado >= 0:
		print("O numero %d e Positivo!" % resultado)
	else:
		print("O numero %d e negativo." % resultado)
	if round(resultado) == resultado:
		print("O numero %d e inteiro!" % resultado)
	else:
		print("O numero %.1f e decimal." % resultado)

if operacao == '*':
	resultado = num1 * num2
	if resultado % 2 == 0:
		print("O numero %d e par!" % resultado)
	else:
		print("O numero %d e impar." % resultado)
	if resultado >= 0:
		print("O numero %d e Positivo!" % resultado)
	else:
		print("O numero %d e negativo." % resultado)
	if round(resultado) == resultado:
		print("O numero %d e inteiro!" % resultado)
	else:
		print("O numero %.1f e decimal." % resultado)

if operacao == '/':
	resultado = num1 / num2
	if resultado % 2 == 0:
		print("O numero %d e par!" % resultado)
	else:
		print("O numero %d e impar." % resultado)
	if resultado >= 0:
		print("O numero %d e Positivo!" % resultado)
	else:
		print("O numero %d e negativo." % resultado)
	if round(resultado) == resultado:
		print("O numero %d e inteiro!" % resultado)
	else:
		print("O numero %.1f e decimal." % resultado)