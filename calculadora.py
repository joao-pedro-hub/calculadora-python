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
def verificacao_menu():
    while True:
        try:
            return int(input('escolha uma opção: '))
        except ValueError:
            #caso der erro por o valor não for do tipo float
            print ('somente numeros ')

def verificacao_de_numero():
    while True:
        try:
            return float(input('Digite um número: '))
        except ValueError:
            #caso der erro por o valor não for do tipo int
            print ('somente numeros ')
            
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
    opcao_calculadora = verificacao_menu()
    #recebe a opção digitadaexcept ValueError:
    match opcao_calculadora:        
        case 1:
                somar (verificacao_de_numero(),verificacao_de_numero())
        case 2:
                subtrair (verificacao_de_numero(),verificacao_de_numero())
        case 3:
                mutiplicar (verificacao_de_numero(),verificacao_de_numero())
        case 4:
                dividir (verificacao_de_numero(),verificacao_de_numero())
        case 5:
                print ('saindo da caculadora')
                break
        case _:
                print ('opção invalida')
        
        

# --Próximas melhorias--


# Melhorar validação de entrada
# Criar versão com interface gráfica