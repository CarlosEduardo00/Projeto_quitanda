#Declarando variaveis

parcelas = 'Não'
msgParcela= 'O total são 2 parcelas de R$:'
msgTotal= 'O total a pagar é: R$'


#Escolha do produto

fruta= int(input('Qual fruta você deseja?\n'' 1 Morango\n'' 2 Abacaxi\n'' 3 Pera\n'' 4 Maca\n'))
peso= float (input ('Quantos kilos de fruta você deseja?\n'))

match fruta:
       case 1:
              if peso<=5:
                     preco=5
              elif peso>5 and peso<=10:
                     preco=3.50
              else:
                     preco=2  

       case 2:
              if peso<=5:
                     preco=10
              elif peso>5 and peso<=10:
                     preco=7.5
              else:
                     preco=6.80
       
       case 3:
              if peso<=5:
                     preco=8.50
              elif peso>5 and peso<=10:
                     preco=7
              else:
                     preco=5.50
       
       case 4:
              if peso<=5:
                     preco=6.50
              elif peso>5 and peso<=10:
                     preco=5
              else:
                     preco=3.75

gastofruta = peso*preco
pagamento= input('Qual é a forma de pagamento?\n1 Dinheiro\n2 Débito\n3 Crédito\n')
if pagamento=='1':
   desconto= (gastofruta*(10/100))
   print(gastofruta - desconto)
elif pagamento=='2':
   desconto= (gastofruta*(5/100))
   print(gastofruta - desconto)
elif pagamento== '3':
        desconto= 0
        parcelas= input('Deseja parcelar em 2 vezes?\n')
        if parcelas=='Sim':
            print('2 parcelas de R$:', str((gastofruta/2)))

entrega = input('Deseja entrega? Sim ou Não?\n')
endereco = input('Qual o endereço da entrega?')

if entrega == 'Sim':
    gastofruta = ((gastofruta - desconto) + 10)
    if parcelas == 'Sim':
       print(msgParcela, ((gastofruta-desconto)/2))
    else:
       print(msgTotal, (gastofruta-desconto))
else:
    gastofruta = ((gastofruta - desconto))
    if parcelas == 'Sim':
       print(msgParcela, ((gastofruta-desconto)/2))
    else:
       print(msgTotal, (gastofruta-desconto))

