from bib import *

usuarios = []

while True:
        print("Selecione uma opção:")
        print("1. Criar uma conta")
        print("2. Conectar-se à conta")
        print("3. Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            criar_conta(usuarios)
        elif opcao == "2":
            conectar_conta(usuarios)
        elif opcao == "3":
            print("Obrigado por utilizar o programa!")
            break
        else:
            print("Opção inválida, tente novamente.")

        with open('usuarios.txt', 'a') as arquivo:
            for usuario in usuarios:
                arquivo.write(f"Nome: {usuario['nome']}\n")
                arquivo.write(f"CPF: {usuario['cpf']}\n")
                arquivo.write(f"Senha: {usuario['senha']}\n")
                arquivo.write("\n")

planos_loc=["1) 30 dias - R$ 180,00", "2) 15 dias - R$ 90,00", "3) 7 dias - R$ 45,00", "0) Sair da escolha de planos"]

mostrar_planos(planos_loc)
escolha_plano()
        