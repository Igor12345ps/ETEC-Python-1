combustivel = str(input("Digite o tipo de combustível que você colocou:")). strip().capitalize() 
litro = float(input ("Digite a quantidade de litros que você colocou:")) 

if combustivel == "A": 
    alcool = 3.5 
    custo = litro * alcool 

if litro <= 20: 
    desconto1 = (custo * 3)/100 
    print("O desconto de combustível foi de : {} e o preço agora é {}".format(desconto1,custo-desconto1)) 

elif litro > 20: 
    desconto2 = (custo * 5)/100 
    print("O desconto de combustível foi de : {} e o preço agora é {}".format(desconto2,custo-desconto2)) 

elif combustivel == "G": 
    gasolina = 4.6 
    custo = litro * gasolina 

if litro <= 20: 
    desconto3 = (custo * 4)/100 
    print("O desconto de combustível foi de : {} e o preço agora é {}".format(desconto3,custo-desconto3)) 

elif litro > 20: 
    desconto4 = (custo * 6)/100 
    print("O desconto de combustível foi de : {} e o preço agora é {}".format(desconto4,custo-desconto4)) 