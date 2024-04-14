from emoji import emojize as em   # Biblioteco de emoji para dar um charme na apresentação do programa hehe...
import textwrap


def inicio(x): #Função de Título do Programa
    print("-"*50)
    print(f"\033[3;34m{x:^50}\033[m")
    print("-"*50)
    
def menu(): #Função da tela de menu do Programa
    print("""
FAVOR, SELECIONE A OPERAÇÃO QUE DESEJA ABAIXO:
          
[5] CRIAR USUÁRIO
[6] NOVA CONTA
[7] LISTAR CONTAS
[0] DEPOSITAR
[1] SACAR
[3] EXTRATO
[9] SAIR

""")

def linha(): #Função de separação de linhas
    print("-"*50)

def depositar(saldo, valor, extrato, /): #Função de deposito do Programa
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R${valor:.2f}\n"
        print("\nDepositado com sucesso!")
    
    else:
        print("\n\033[3;31mACESSO NEGADO! VALOR INFORMADO INVÁLIDO!\033[m\n")
            
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saque, limite_saque): #Função de saque do Programa
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
    
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato): #Função de extrato do Programa
    inicio("EXTRATO")
    if not extrato:
        print("\033[3;33mNÃO FORAM REALIZADAS MOVIMENTAÇÕES.")
    else:
        print(f"\n{extrato}")
        linha()
        print(f"\033[3;34mSaldo: R${saldo:.2f}\033[m")
        linha()

def criar_usuario(usuarios): #Função de criação de novo usuário do Programa
    cpf = int(input("Informe o CPF (somente núemros): "))
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\n\033[3;31mJÁ EXISTE UM USUÁRIO CADASTRADO NESTE CPF\033[m")
        return

    nome = str(input("Informe o nome completo: "))
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    
    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})
    
    print("\n\033[3;34mUSUÁRIO CRIADO COM SUCESSO!\033[m")

def filtrar_usuario(cpf, usuarios): #Função de filtragem de usuário caso aponte duplicidade de CPF no Programa
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios): #Função de criação de conta para novo usuário no Programa
    cpf = int(input("Informe o CPF do usuário: "))
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\n\033[3;34mCONTA CRIADA COM SUCESSO!\033[m")
        return

    print("\n\033[3;31mUSUÁRIO NÃO ENCONTRADO, FLUXO DE CRIAÇÃO DE CONTA ENCERRADO!\033[m")

def listar_contas(contas): #Função de listagem de contas
   for conta in contas:
       resulta = f"""
           Agência: {conta['agencia']}
           C/C: {conta['numero_conta']}
           Titular: {conta['usuario']['nome']}
        """
                

def main(): #Função de execução do programa

# Variáveis base para o funcionamento do programa
    LIMITE_SAQUE = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saque = 0
    usuarios = []
    contas = []

    # Início do Programa
    inicio(em("🏦 BEM-VINDO(A) AO BANCO X 🏦"))
    while True:
        
        menu()
        opcao = int(input("OPÇÃO: "))
        linha()
        
        if opcao == 0: # Condição se for acionado o botão 0 [Depósito]
            valor = float(input("Informe o valor de depósito: R$"))

            saldo, extrato = depositar(saldo, valor, extrato)
            linha()
                
        elif opcao == 1: # Condição se for acionado o botão 1 [Saque]
            valor = float(input("Informe o valor de saque: R$"))
            
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saque=numero_saque,
                limite_saque=LIMITE_SAQUE,
                )
            numero_saque += 1
                
            linha()
        
        elif opcao == 3: # Condição se for acionado o botão 3 [Extrato]
            exibir_extrato(saldo, extrato=extrato)
          
        elif opcao == 5: # Condição se for acionado o botão 5 [Criar Usuário]
            criar_usuario(usuarios)
        
        elif opcao == 6:  # Condição se for acionado o botão 6 [Criação de Contas]
            numero_conta = len(contas) + 1 
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            
            if conta:
                contas.append(conta)
        
        elif opcao == 7: # Condição se for acionado o botão 7 [Listar Contas]
            listar_contas(contas)
                   
        elif opcao == 9: # Condição se for acionado o botão 9 [Sair da Aplicação]
            print("\033[3;34mMUITO OBRIGADO POR USAR NOSSOS SERVIÇOS!\033[m")
            linha()
            break
         
        else: # Condição se for acionado botão inválido
            print("\033[3;31mACESSO NEGADO! FAVOR REPETIR PROCESSO\033[m")
            linha()

#Inicialização do Programa:
main()