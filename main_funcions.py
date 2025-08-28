import agenda 

"""Agenda de Contatos (Módulo Próprio + JSON)
Criar um módulo de manipulação de contatos (adicionar, listar, excluir).
Armazenar os contatos em um arquivo JSON.
Usar os para verificar se o arquivo já existe."""

def menu():
    while True:
        print("Qual ação deseja realizar?")
        print("1. Adicionar Contato")
        print("2. Listar contatos")
        print("3. Remover um contato")
        print("4. Sair")
        
        choice = input("> ")
        
        if choice == "1":
            print("Novo contato")
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            agenda.adicionar_contatos(nome, telefone, email)
            
        elif choice == "2":
            agenda.listar_contatos()
            
        elif choice == "3":
            nome = input("Escolha o nome do contato a ser removido: ")
            agenda.remover_contatos(nome)
                
        elif choice == "4":
            print("Até breve!")
            break
        else:
            print("Opção inválida. Tente novamente")

if __name__ =="__main__": menu()