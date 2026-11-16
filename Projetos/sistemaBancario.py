import os
from datetime import datetime



'''
validações:

nome, senha sem espaços em criar conta e entrar conta
validação: não pode ter 2 usuarios com o mesmo nome
'''


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


usuarios = []

sessao_ativa = False

while True:
    if sessao_ativa == True:
        break


    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("=-=-=SISTEMA BANCARIO=-=-=-")
    print("=-==-=1-CRIAR-CONTA=-==-==-")
    print("=-==2-ENTRAR NA CONTA==-==-")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("ESCREVA 'SAIR' A QUALQUER MOMENTO PARA ENCERRAR")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=")

    opcao = input("RESPOSTA: ")

    match opcao:
        case "1":
            while True:    
                print("=-=-=-=-=-=-=-=-=-=-=-=-=-==-=")
                print("=-==DIGITE O NOME DA CONTA-=--")
                print("=-=-=-=-=-=-=-=-=-=-=-=-=-==-=")

                nome_conta = input("RESPOSTA: ")
                if nome_conta.casefold() == "sair":
                    break

                limpar_tela()
                print("=-=-=-=-=-=-=-=-=-=-=-=-=-==-=")
                print("=-==DIGITE A SENHA DA CONTA-=-")
                print("=-=-=-=-=-=-=-=-=-=-=-=-=-==-=")


                senha_conta = input("RESPOSTA: ")
                if senha_conta.casefold() == "sair" :
                    print("Sessão encerrada")
                    break


                if senha_conta.isnumeric() and len(str(senha_conta)) == 6:
                    limpar_tela()
                    print("=-=-=-=-=-=-=-=-=-=-=-=-=-==-=")
                    print("=-=--=DIGITE A NOVAMENTE-=-=-=")
                    print("=-=-=-=-=-=-=-=-=-=-=-=-=-==-=")
                    
                    senha_confirmacao = input("RESPOSTA: ")

                    if senha_confirmacao.casefold() == "sair" :
                        limpar_tela()
                        print("=-==-=-SESSÃO ENCERRADA=--=-=-")
                        break

                    elif senha_conta == senha_confirmacao:
                        limpar_tela()
                        print("=-==-=-=-CONTA CRIADA=-=--=-=-")
                        usuarios.append({
                            'nome': nome_conta, 
                            'senha': senha_conta, 
                            'saldo_total': 0, 
                            'limite': 200, 
                            "data_criacao": datetime.now().strftime("%d/%m/%Y - %H:%M"), 
                            'extrato': []
                            })

                        break

                    else:
                        print("A Senha esta incorreta")
                else:
                    print("Digite uma senha composta somente por numeros, no maximo 6 digitos.")

        case '2':
            tentativas = 0
            while tentativas <= 3:
                if sessao_ativa == True:
                    break

                print("=-=-=-=-=-=-=-=-=-=-=-=-=-==-=")
                print("=-==DIGITE O NOME DA CONTA-=--")
                print("=-=-=-=-=-=-=-=-=-=-=-=-=-==-=")
                nome_conta = input("RESPOSTA: ")

                if nome_conta.casefold() == "sair":
                    break

                for indice, usuario in enumerate(usuarios):
                    if nome_conta == usuario['nome']:
                        limpar_tela()
                        print("=-=-=-=-=-=-=-=-=-=-=-=-=-==-=")
                        print("=-==DIGITE A SENHA DA CONTA-=-")
                        print("=-=-=-=-=-=-=-=-=-=-=-=-=-==-=")
                        senha_conta = input("RESPOSTA: ")
                        if senha_conta == usuario['senha']:
                            sessao_ativa = True

                            id_conta = str(indice)
                            nome_conta = usuario['nome']
                            senha_conta = usuario['senha']
                            saldo_total = usuario['saldo_total']
                            limite = usuario['limite']

                            break
                            

                        else:
                            print("Senha incorreta")
                    else:
                        print("Usuario não encontrado")

        case 'sair':
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-==-=")
            print("=-==-=-SESSÃO ENCERRADA=--=-=-")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-==-=")
            break

print(usuarios)

while sessao_ativa:
    
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-==-=")
    print(F"=-=BEM VINDO {nome_conta}=-=-")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-==-=")
    print("=-=-=-==-=1-EXTRATO=-=-=-==-=-")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-==-=")
    print("=-=-=-=2=TRANSFERENCIA=-=-=-=-")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-==-=")
    print("=-=-=-==-3-DEPOSITO=-=-=-=-=-=")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-==-=")
    print("=-=-=-==-4-PAGAMENTO=-=-=-=-=-")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-==-=")
    print("=-=-=-==-=-5-SAQUE=-=-=-=-=-=-")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-==-=")
    print("-=-=-=-=-=-6-BOLETO-=-=-=-==-=")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-==-=")
    print("=-=-=-=-=-=7=CÂMBIO-=-=-=-=-=-")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-==-=")
    print("=-=-=-=-=-8-CARTÕES-=-=-=-==-=")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-==-=")
    print("-=-=-=-=-=9=SUPORTE-=-=-=-=-=-")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-==-=")
    print("=-=-=-=-10-INVESTIMENTO=-=-==-")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-==-=")
    print("=-=-11=SEGUROS-E-PLANOS-=-=-=-")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-==-=")
    print("=-=-=-=-=-12=PERFIL-=-=-=-=-=-")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-==-=")
    print("=-=-=-=-=-=13-SAIR=-=-=-=-=-=-")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-==-=")
    opcao = input("RESPOSTA: ")
    match opcao:
        case "1":
            print(f"SALDO TOTAL : {saldo_total}")
            if usuarios[int(id_conta)]["extrato"]:
                for transacao in usuarios[int(id_conta)]["extrato"]:
                    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=")
                    print(f"{transacao["tipo_extrato"]} - VALOR: R${transacao["valor"]:.2f} - CONTA ORIGEM: {transacao["conta_origem"]} - CONTA DESTINO: {transacao["conta_destino"]}")
            else:
                pass

            print("=-=-=-=-=-=-=-=-=-=-=-=-=-==-=")
            print("DIGITE QUALQUER TECLA PARA SAIR")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-==-=")
            sair =input("")
            
        case "2":
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-==-=")
            print("=404-AREA-EM-DESENVOLVIMENTO=-")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-==-=")
        case "3":
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-==-=")
            print("=404-AREA-EM-DESENVOLVIMENTO=-")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-==-=")
        case "4":
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-==-=")
            print("=404-AREA-EM-DESENVOLVIMENTO=-")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-==-=")
        case "5":
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-==-=")
            print("=404-AREA-EM-DESENVOLVIMENTO=-")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-==-=")
        case "6":
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-==-=")
            print("=404-AREA-EM-DESENVOLVIMENTO=-")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-==-=")
        case "7":
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-==-=")
            print("=404-AREA-EM-DESENVOLVIMENTO=-")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-==-=")
        case "8":
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-==-=")
            print("=404-AREA-EM-DESENVOLVIMENTO=-")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-==-=")
        case "9":
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-==-=")
            print("=404-AREA-EM-DESENVOLVIMENTO=-")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-==-=")
        case "11":
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-==-=")
            print("=404-AREA-EM-DESENVOLVIMENTO=-")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-==-=")
        case "12":
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-==-=")
            print("=404-AREA-EM-DESENVOLVIMENTO=-")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-==-=")
        case "13":
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-==-=")
            print("=-==-=-SESSÃO ENCERRADA=--=-=-")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-==-=")
            break