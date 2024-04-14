from emoji import emojize as em #Biblioteco de emoji para dar um charme na apresentação do programa hehe...

# Funções do corpo do programa
def inicio(x):
    print("-"*50)
    print(f"\033[3;34m{x:^50}\033[m")
    print("-"*50)
    
def menu():
    print("""
FAVOR, SELECIONE A OPERAÇÃO QUE DESEJA ABAIXO:
          
[0] DEPOSITAR
[1] SACAR
[3] EXTRATO
[9] SAIR
""")

def linha():
    print("-"*50)

# Variáveis base para o funcionamento do programa
saldo = 0
limite = 500
extrato = ""
numero_saque = 0
limite_saque = 3

# Início do Programa
inicio(em("🏦 BEM-VINDO(A) AO BANCO X 🏦"))
while True:
    
    menu()
    opcao = int(input("OPÇÃO: "))
    linha()
    
    # Condição se for acionado o botão 0 [Depósito]
    if opcao == 0:
        valor = float(input("Informe o valor de depósito: R$"))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"
            print("\nDepositado com sucesso!")
        
        else:
            print("\n\033[3;31mACESSO NEGADO! VALOR INFORMADO INVÁLIDO!\033[m\n")
            
        linha()
    
    # Condição se for acionado o botão 1 [Saque]    
    elif opcao == 1:
        valor = float(input("Informe o valor de saque: R$"))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saque >= limite_saque
        
        if excedeu_saldo:
            print("\n\033[3;31mACESSO NEGADO! SALDO INSUFICIENTE!\033[m")
            
        elif excedeu_limite:
            print("\n\033[3;31mACESSO NEGADO! LIMITE INSUFICIENTE!\033[m")
            
        elif excedeu_saques:
            print("\n\033[3;31mACESSO NEGADO! NÚMERO MÁXIMO DE SAQUE EXCEDIDO!\033[m")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saque += 1
            print("\nSacado com sucesso!\n")
        
        else:
            print("\033[3;31mACESSO NEGADO! VALOR INFORMADO INVÁLIDO!\033[m")
            
        linha()
    
    # Condição se for acionado o botão 3 [Extrato]
    elif opcao == 3:
        inicio("EXTRATO")
        if not extrato:
            print("\033[3;33mNÃO FORAM REALIZADAS MOVIMENTAÇÕES.")
        else:
            print(f"\n{extrato}")
        linha()
        print(f"\033[3;34mSaldo: R${saldo:.2f}\033[m")
        linha()
    
    # Condição se for acionado o botão 9 [Sair da Aplicação]
    elif opcao == 9:
        print("\033[3;34mMUITO OBRIGADO POR USAR NOSSOS SERVIÇOS!\033[m")
        linha()
        break
    
    # Condição se for acionado botão inválido
    else:
        print("\033[3;31mACESSO NEGADO! FAVOR REPETIR PROCESSO\033[m")
        linha()