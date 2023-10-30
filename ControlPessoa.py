#Control Pessoa
from ModelPessoa import ModelPessoa
class ControlPessoa:
    #Método construtor
    def __init__(self):
        self.pessoaUm = ModelPessoa#Criando uma chave para acessar os métodos da classe ModelPessoa
        self.opcao = -1
        self.atu   = 0

    def menu(self):
        print("\n\nEscolha uma das opções abaixo: " +
              "\n0. Sair"                           +
              "\n1. Cadastrar Pessoa"               +
              "\n2. Consultar Pessoa"               +
              "\n3. Atualizar Pessoa"               +
              "\n4. Excluir Pessoa")
        self.opcao = int(input())

    def cadastrar(self):
        cpf = int(input("Informe seu CPF: "))
        nome = input("Informe seu nome: ")
        telefone = int(input("Informe seu telefone: "))
        endereco = input("Informe seu endereço: ")
        email = input("Informe seu e-mail: ")
        #Chamar o método cadastrarPessoa
        self.pessoaUm.cadastrarPessoa(self, cpf,nome,telefone,endereco, email)

    def consultar(self):
        print(self.pessoaUm.consultarPessoa(self))

    def menuAtualizar(self):
        print("\nQual campo você deseja atualizar? " +
              "\n1. Nome" +
              "\n2. Telefone" +
              "\n3. Endereço" +
              "\n4. E-mail"
              )
        self.atu = int(input())

    def atualizar(self):
        self.menuAtualizar()
        if self.atu == 1:
            nome = input("Informe o novo nome: ")
            self.pessoaUm.atualizarPessoa(self,self.atu,nome)
        elif self.atu == 2:
            telefone = int(input("Informe o novo telefone: "))
            self.pessoaUm.atualizarPessoa(self,self.atu,telefone)
        elif self.atu == 3:
            endereco = input("Informe o novo endereço: ")
            self.pessoaUm.atualizarPessoa(self,self.atu,endereco)
        elif self.atu == 4:
            email = input("Informe o novo e-mail: ")
            self.pessoaUm.atualizarPessoa(self,self.atu,email)
        else:
            print("Escolha uma opção entre 1 e 4")

    def excluir(self):
        self.pessoaUm.excluirPessoa(self)
        print("Dados Excluídos com Sucesso!")

    def operacao(self):
        while self.opcao != 0:
            self.menu() #Mostrar as opções para o usuário
            if self.opcao == 1:
                self.cadastrar()
            elif self.opcao == 2:
                self.consultar()
            elif self.opcao == 3:
                self.atualizar()
            elif self.opcao == 4:
                self.excluir()
            elif self.opcao == 0:
                print("Obrigado!")
            else:
                print("Escolha uma opção entre 1 e 4")


