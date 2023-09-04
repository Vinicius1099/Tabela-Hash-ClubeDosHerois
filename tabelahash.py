#Vinicius Artuso(1131886) e Guilherme Franciosi(1131090)
import csv

class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class AgendaHeroes:
    def __init__(self):
        self.tamanho = 26
        self.tabela = [None] * self.tamanho

    def calcular_indice(self, letra):
        return ord(letra.upper()) - ord('A')

    def adicionar_contato(self, contato):
        indice = self.calcular_indice(contato.nome[0])
        if self.tabela[indice] is None:
            self.tabela[indice] = [contato]
        else:
            self.tabela[indice].append(contato)

    def buscar_contato_por_nome(self, nome):
        indice = self.calcular_indice(nome[0])
        if self.tabela[indice] is not None:
            for contato in self.tabela[indice]:
                if contato.nome == nome:
                    return contato
        return None

    def listar_contatos_por_letra(self, letra):
        indice = self.calcular_indice(letra)
        contatos_letra = []
        if self.tabela[indice] is not None:
            contatos_letra.extend(self.tabela[indice])
        return contatos_letra

    def remover_contato(self, nome):
        indice = self.calcular_indice(nome[0])
        if self.tabela[indice] is not None:
            for contato in self.tabela[indice]:
                if contato.nome == nome:
                    self.tabela[indice].remove(contato)

    def importar_contatos(self, arquivo_csv):
        with open(arquivo_csv, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                nome, telefone = row
                contato = Contato(nome, telefone)
                self.adicionar_contato(contato)

    def menu_interativo(self):
        while True:
            print("\nMenu:")
            print("1. Adicionar contato")
            print("2. Buscar contato por nome")
            print("3. Listar contatos por letra")
            print("4. Remover contato")
            print("5. Importar contatos do arquivo")
            print("6. Sair")
            escolha = input("Escolha uma opção: ")

            if escolha == '1':
                nome = input("Digite o nome do contato: ")
                telefone = input("Digite o telefone do contato: ")
                contato = Contato(nome, telefone)
                self.adicionar_contato(contato)
                print("Contato adicionado com sucesso!")

            elif escolha == '2':
                nome = input("Digite o nome do contato a ser buscado: ")
                contato = self.buscar_contato_por_nome(nome)
                if contato:
                    print(f"Nome: {contato.nome}, Telefone: {contato.telefone}")
                else:
                    print("Contato não encontrado!")

            elif escolha == '3':
                letra = input("Digite a letra para listar os contatos: ")
                contatos_letra = self.listar_contatos_por_letra(letra)
                if contatos_letra:
                    for contato in contatos_letra:
                        print(f"Nome: {contato.nome}, Telefone: {contato.telefone}")
                else:
                    print("Nenhum contato encontrado para esta letra!")

            elif escolha == '4':
                nome = input("Digite o nome do contato a ser removido: ")
                self.remover_contato(nome)
                print("Contato removido com sucesso!")

            elif escolha == '5':
                arquivo_csv = input("Digite o nome do arquivo CSV para importar os contatos: ")
                self.importar_contatos(arquivo_csv)
                print("Contatos importados com sucesso!")

            elif escolha == '6':
                break

            else:
                print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    agenda = AgendaHeroes()
    agenda.menu_interativo()

