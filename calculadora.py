#objetivo: calculadora simples

def menu_calculadora ():
    print ('     calculadora              ')
    print ('+------------------------+')
    print ('| (1) somar              |')
    print ('| (2) subtrair           |')
    print ('| (3) mutiplicar         |')
    print ('| (4) dividir            |')
    print ('| (5) sair               |')
    print ('|                        |')
    print ('+------------------------+') 
def somar (numero1,numero2):
    resposta = numero1 + numero2
    print (f'A soma entre {numero1} e {numero2} é iqual a {resposta}')

def subtrair (numero1,numero2):
    resposta = numero1 - numero2
    print (f'A subtração de {numero1} e {numero2} é iqual a {resposta}')

def mutiplicar (numero1,numero2):
    resposta = numero1 * numero2
    print (f'A mutiplicão de {numero1} e {numero2} é iqual a {resposta}')

def dividir (numero1,numero2):
    if numero2 == 0:
        print ('não é possivel dividir com zero')
    else:
        resposta = numero1 / numero2
        print (f'A divisão de {numero1} e {numero2} é iqual a {resposta}')

while True:
    #repete o codigo até que digite 5 como opção
    menu_calculadora ()    
    opcao_calculadora = int (input ('escolha uma opção '))
    #recebe a opção digitada
    match opcao_calculadora:        
        case 1:
                somar (int (input ('digite um numero ')),int (input ('digite outro numero ')))
        case 2:
                subtrair (int (input ('digite um numero ')),int (input ('digite outro numero ')))
        case 3:
                mutiplicar (int (input ('digite um numero ')),int (input ('digite outro numero ')))
        case 4:
                dividir (int (input ('digite um numero ')),int (input ('digite outro numero ')))
        case 5:
                print ('saindo da caculadora')
                break
        case _:
                print ('opção invalida')

# --Próximas melhorias--

# Aceitar números decimais
# Melhorar validação de entrada
# Criar versão com interface gráfica