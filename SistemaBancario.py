from decimal import Decimal
import os

menu = """
selecione uma opção de movimento
[d]  Depositar
[s]  Sacar
[e]  Extrato
[q]  Sair
>>"""


saldo = 0.0
limite = 500 
extrato = ""

numero_saques= 0
LIMITE_SAQUES = 3 

def somavetores(recebido):
    for x in recebido:
      soma += x 
    return soma
        
def salvaDeposito( deposito ,saldo  ):
        saldo = float(saldo) + float( deposito)       
        return saldo,"depositou " + deposito + " \n"
       
def realizaSaque( saque = 0.0,saldo = 0):        
        if numero_saques >= 3 :
            print("ultrapassou a quantidade de saques diarios" )
            return saldo,0,""
        if saldo < saque:
            print("vc não tem saldo suficiente para essa transação")        
            return saldo,0,""
        else:
            saldo =  saldo - saque
            return saldo, 1 , "sacou " + str( saque) + " \n "   

def imprimeExtrato( saldo):
    print("----------------------")
    print("inicio extrato")
    print("----------------------")
    print(extrato)
    print("----------------------")
    print("seu saldo é " + str(saldo))
    print("----------------------")
    print("           fim extrato")
    
    input("")  
    
while True:  
    opcao = input(menu)    
    
    if opcao == "d":
        deposito = input ("digite o valor deposito.")
        saldo,msg = salvaDeposito(deposito,saldo) 
        extrato = extrato +  msg        
        input("")  
        
    if opcao == "s":
        if saldo >=0 and limite >=0 :
            saque = float(input ("digite o valor saque."))
            saldo,numero,msg = realizaSaque(saque,saldo )
            numero_saques += numero
            extrato = extrato + msg 
        input("")              
    if opcao == "e":
        imprimeExtrato(saldo)

    if opcao == "q":
        print("sair")
        break
            
    else:
        print("\n")
        print("Favor digitar um valor valído no menu!")
   
        
        


   