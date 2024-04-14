def texto(txt):
    """\033[3;33mFunção informada para gerar um texto formatada com linhas de separação PADRÃO;\033[m

    Args:
        \033[3;33mtxt (_type_): Inserir a string para realizar a formação\033[m
    """
    print("=-"*20)
    print(txt)
    print("=-"*20)
    
def linha():
    """\033[3;33mLinha padrão para utilizar no Programa Principal;\033[m
    """
    print("=-"*20)
    
def aumentar(preco = 0, taxa = 0, formato = False):
    """\033[3;34mFunção para conversão de valor de cunho aumentativo, informando o valor, a taxa e, se\033[m
    \033[3;34mpreferir, exibindo a formatação como moeda ou não;\033[m

    Args:
        \033[3;34mpreco (int, optional): Preço informado pelo usuário;\033[m
        \033[3;34mtaxa (int, optional): Taxa em % informada pelo usuário;\033[m
        \033[3;34mformato (bool, optional):\033[m
        \033[3;34mSe informada como True: Exibição formatada como moeda;\033[m
        \033[3;34mSe informada como False: apenas o preço final convertido;\033[m

    Returns:
        \033[3;34m_type_: Valor que será retornado para o usuário final.\033[m
    """
    res =  preco + (preco * taxa/100)
    return res if formato is False else moeda(res)

def diminuir(preco = 0, taxa = 0, formato = False):
    """\033[3;37mFunção para conversão de valor de cunho diminutivo, informando o valor, a taxa e, se\033[m
    \033[3;37mpreferir, exibindo a formatação como moeda ou não;\033[m

    Args:
        \033[3;37mpreco (int, optional): Preço informado pelo usuário;\033[m
        \033[3;37mtaxa (int, optional): Taxa em % informada pelo usuário;\033[m
        \033[3;37mformato (bool, optional):\033[m
        \033[3;37mSe informada como True: Exibição formatada como moeda;\033[m
        \033[3;37mSe informada como False: apenas o preço final convertido;\033[m

    Returns:
        \033[3;37m_type_: Valor que será retornado para o usuário final.\033[m
    """
    res = preco - (preco * taxa/100)
    return res if formato is False else moeda(res)

def dobro(preco = 0, formato = False):
    """\033[3;35mFunção para conversão de valor de cunho multiplicativo(dobro), informando o valor e, se\033[m
    \033[3;35mpreferir, exibindo a formatação como moeda ou não;\033[m

    Args:
        \033[3;35mpreco (int, optional): Preço informado pelo usuário;\033[m
        \033[3;35mformato (bool, optional): \033[m
        \033[3;35mSe informada como True: Exibição formatada como moeda;\033[m
        \033[3;35mSe informada como False: apenas o preço final convertido;\033[m

    Returns:
        \033[3;35m_type_: Valor que será retornado para o usuário final.\033[m
    """
    res = preco * 2
    return res if formato is False else moeda(res)

def metade(preco = 0, formato = False):
    """\033[3;36mFunção para conversão de valor de cunho de divisão(metade), informando o valor e, se\033[m
    \033[3;36mpreferir, exibindo a formatação como moeda ou não;\033[m

    Args:
        \033[3;36mpreco (int, optional): Preço informado pelo usuário;\033[m
        \033[3;36mformato (bool, optional):\033[m
        \033[3;36mSe informada como True: Exibição formatada como moeda;\033[m
        \033[3;36mSe informada como False: apenas o preço final convertido;\033[m

    Returns:
        \033[3;36m_type_: Valor que será retornado para o usuário final.\033[m
    """
    res = preco / 2
    return res if formato is False else moeda(res)

def moeda(preco = 0, moeda = "R$"):
    """\033[3;32mFunção informada para conversão do valor para moeda em real (R$);\033[m

    Args:
        \033[3;32mpreco (int, optional): preço informado pelo usuário;\033[m
        \033[3;32mmoeda (str, optional): Se não informada, será automaticamente informada como real(R$);\033[m

    Returns:
        \033[3;32m_type_: Valor convertido retornado para o usuário.\033[m
    """
    return f"{moeda}{preco:.2f}".replace(".", ",")

def ajuda():
    texto("\033[3;33mMANUAL DE INSTRUÇÕES DO MÓDULO \033[3;34mM109\033[m CRIADO\033[m")
    while True:
        while True:
            print("""
        [0] - LINHA
        [1] - TEXTO
        [2] - AUMENTAR
        [3] - DIMINUIR
        [4] - DOBRO
        [5] - METADE
        [6] - SAIR
                """)
            choice = int(input("OPÇÃO: "))
            if choice > 6:
                print("\033[3;31mRESPOSTA NEGADA! FAVOR INFORMAR A RESPOSTA CONFORME LISTADA ACIMA!\033[m")
            elif choice < 0:
                print("\033[3;31mRESPOSTA NEGADA! FAVOR INFORMAR A RESPOSTA CONFORME LISTADA ACIMA!\033[m")
            else:
                break
        linha()
        if choice == 0:
            help(linha)
            linha()
        elif choice == 1:
            help(texto)
            linha()
        elif choice == 2:
            help(aumentar)
            linha()
        elif choice == 3:
            help(diminuir)
            linha()
        elif choice == 4:
            help(dobro)
            linha()
        elif choice == 5:
            help(metade)
            linha()
        else:
            break
    texto("\033[3;32mMUITO OBRIGADO! VOLTE SEMPRE\033[m")