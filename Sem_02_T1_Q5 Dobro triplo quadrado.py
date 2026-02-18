# ATIVIDADE SEMANA 02 - T1 - Q5

#Crie um programa em que o usuário insira um número inteiro X e você devolva o dobro, triplo e o quadrado de X.

while True:
    valor = input('Digite um valor para ver o dobro, triplo e o quadrado desse valor: ')
    try:
        valor = int(valor)
        break
    except:
        print('Não é Permitido "letras" nem numeros com "Ponto" ou "virgula"')
        print('Tente novamente!\n')
        
dobro = valor * 2
triplo = valor * 3
quadrado = valor ** 2

print(f'O dobro de {valor} é {dobro}, o triplo é {triplo} e o quadrado é {quadrado}')