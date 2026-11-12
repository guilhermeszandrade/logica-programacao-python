nomeConta = "guijeitoso"
senhaConta = "Guizin.20"
tentativas = 0

while True:

    conta = input("Digite o nome da conta: ")
    senha = input("Digite a senha da conta: ")

    if nomeConta == conta and senhaConta == senha:
        print("Login com sucesso")
        break
    else:
        print("Senha ou Usuario errados! Tente novamente")
        tentativas += 1
        if tentativas >= 5:
            print(
                "Tentativa execedidadas! Sua conta foi bloqueada, entre em contanto com o suporte "
            )
            break
