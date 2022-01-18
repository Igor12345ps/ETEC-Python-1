def calcular_precos():
  
    #variável
    count = 0
    calculo_produto = 0
  
    #dados do produto.
    dados_produto = [("morango", 2.50, 2.20), ("maçã", 1.80, 1.50)]
    
    while True:

        #variavel
        finalizar = False
      
        #perguntar qual tipo de produto desejado.
        produto = input("Por favor, informe o produto desejado(Morango ou Maçã):")
        
        for x in range(2):
            #verificar se tem o produto desejado
            if produto.lower() == dados_produto[x][0]:
                #armazenar a posição do produto na variável count.
                count = x
                #Inserir o valor booleano True para a variável finalizar, para que possa interromper o loop while.
                finalizar = True
                #interromper o loop for caso tenha encontrado o determinado produto.
                break
        
            else:
                if x == 1:
                    #Informa que o valor esta invalido.
                    finalizar = False
                    print ("Valor inválido.", produto)
    
        if finalizar:
            break

    while True:
        
        try:
        
            #obter o peso do produto.
            peso = float(input("Por favor, informe o peso desejado:"))
        
            #verificar se o peso está acima de zero.
            if peso > 0:
                break
          
            else:
                continue

        except ValueError:
            print ("valor Invalido do peso.")
            continue

    #calculos do produto
    if peso <= 5 and peso > 0:
        #calculando o valor do produto com o peso.
        calculo_produto = dados_produto[count][1] * peso
        
    elif peso > 5:
        #calculando o valor do produto com o peso.
        calculo_produto = dados_produto[count][2] * peso
        #verificando se o peso é maior que 8kg ou o valor passa de R$25,00.
        if peso > 8 or calculo_produto > 25:
            calculo_produto = (dados_produto[count][2] * peso) - ((dados_produto[count][2] * peso) * 10 / 100)
            
    print ("Valor a pagar:R$%.2f" % calculo_produto)

calcular_precos()