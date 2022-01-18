opção=0
while opção != 4:
    print('''    [1] Matutino
    [2] Vespertino
    [3] Noturno
    [4] Sair do programa''')
    opção = int(input('Qual é sua opção? '))
    if opção == 1:
        print('Bom dia!')
    elif opção == 2:
        print('Boa tarde!')
    elif opção == 3:
        print('Boa noite!')
print('Fim do programa...')