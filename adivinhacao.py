from random import randint

while True:
    numx = randint(1, 100)

    numr = int(input('Qual número o programa pensou? de 1 a 100: '))
    tentativas = 1
    while numr != numx:
        if numx > numr:
            print('-'*10)
            print('O número que o programa pensou é maior que {}'.format(numr))
            numr = int(input('Digite um outro número '))
            tentativas = tentativas + 1
        else:
            print('-'*10)
            print('O número que o programa pensou é menor que {}!'.format(numr))
            numr = int(input('Digite um outro número '))
            tentativas = tentativas + 1

    print('-'*10)
    print('Parabéns, você acertou em {} tentativas, o número que o programa pensou era {}!'.format(tentativas, numx))
    
    continuar = input('Deseja jogar outra partida?? (s/n) ')
    pergunta = ['sim', 's', 'yes']
    if continuar not in pergunta:
        break
