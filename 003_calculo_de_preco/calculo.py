import modulo_calculo as m109
from time import sleep
m109.texto("\033[3;32mDesafio 108: Calculando Preços PT.02\033[m")
while True:
    while True:
        print("""
\033[3;32mBem-vindo(a) em nossa calculadora de preços!\033[m
\033[3;32mAntes de começar, deseja verificar o manual de nosso módulo?\033[m
""")
        choice1 = str(input("[S/N]: ")).upper()[0]
        print()
        if choice1 not in "SN":
            m109.linha()
            print("\033[3;31mRESPOSTA NEGADA! FAVOR RESPONDER [S] OU [N].\033[m")
            m109.linha()
        else:
            break
    if choice1 in "Ss":
        help(m109.ajuda())
    else:
        break
while True:
    m109.linha()
    p = float(input("Digite o preço: R$"))
    m109.linha()
    sleep(0.5)
    print("\033[3;33mPROCESSANDO\033[m", end="", flush=True)
    print("...", flush = True)
    sleep(0.5)
    m109.linha()
    print(f"\n\033[3;36mA metade do preço {m109.moeda(p)} é {m109.metade(p, formato = True)};\033[m\n")
    print(f"\033[3;36mO dobro do preço R${m109.moeda(p)} é {m109.dobro(p, formato = True)};\033[m\n")
    m109.linha()
    while True:
        choice = str(input("DESEJA INFORMAR TAXA PARA O CÁLCULO AUMENTO E DESCONTO? [S/N] ")).upper()[0]
        if choice not in "SN":
            print("\n\033[3;31mRESPOSTA NEGADA! FAVOR RESPONDER COM S OU N!\033[m\n")
        else:
            break
    if choice in "Ss":
        m109.linha()
        taxa = float(input("Favor, digite a taxa desejada: [%] "))
        sleep(0.5)
        print("\nPROCESSANDO...\n", flush=True)
        sleep(0.5)
        m109.linha()
        print(f"\n\033[3;33mO aumento do preço de {m109.moeda(p)} com taxa de {taxa}% é de: {m109.aumentar(p, taxa, formato = True)}\033[m\n")
        print(f"\033[3;33mA deminuição do preço de {m109.moeda(p)} com taxa de {taxa}% é de: {m109.diminuir(p, taxa, formato = True)}\033[m\n")
        m109.linha()
    while True:
        choice2 = str(input("DESEJA CONTINUAR? [S/N] ")).upper()[0]
        if choice2 not in "SN":
            print("\n\033[3;31mRESPOSTA NEGADA! FAVOR RESPONDER COMO [S] OU [N].\033[m\n")
        else:
            break
    if choice2 in "Nn":
        break
m109.texto("\033[3;35mMUITO OBRIGADO POR UTILIZAR O SERVIÇO!\033[m") 