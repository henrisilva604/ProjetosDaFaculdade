class Produto:
    def __init__(self, codigo, nome, quantidade, preco):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def __str__(self):
        return f"Código: {self.codigo} | Produto: {self.nome} | Quantidade: {self.quantidade} | Preço: R$ {self.preco:.2f}"

class ControleEstoque:
    def __init__(self):
        self.produtos = {} 

    def adicionar_produto(self):
        codigo = input("Código do produto: ").strip()
        if codigo in self.produtos:
            print("Produto já cadastrado. Use a opção de atualizar quantidade.")
            return
        nome = input("Nome do produto: ").strip()
        try:
            quantidade = int(input("Quantidade inicial: "))
            preco = float(input("Preço unitário: R$ "))
        except ValueError:
            print("Quantidade e preço devem ser números válidos.")
            return

        self.produtos[codigo] = Produto(codigo, nome, quantidade, preco)
        print("Produto adicionado com sucesso.")

    def listar_estoque(self):
        if not self.produtos:
            print("Estoque vazio.")
            return
        print("\n=== Estoque Atual ===")
        for produto in self.produtos.values():
            print(produto)
        print("====================\n")

    def atualizar_quantidade(self):
        codigo = input("Código do produto para atualizar: ").strip()
        if codigo not in self.produtos:
            print("Produto não encontrado.")
            return

        produto = self.produtos[codigo]
        try:
            ajuste = int(input("Informe a quantidade para adicionar (positivo) ou retirar (negativo): "))
        except ValueError:
            print("Quantidade inválida.")
            return

        if produto.quantidade + ajuste < 0:
            print("Não é possível retirar mais do que o estoque disponível.")
            return

        produto.quantidade += ajuste
        print(f"Quantidade atualizada. Novo estoque de {produto.nome}: {produto.quantidade}")

    def remover_produto(self):
        codigo = input("Código do produto para remover: ").strip()
        if codigo in self.produtos:
            del self.produtos[codigo]
            print("Produto removido com sucesso.")
        else:
            print("Produto não encontrado.")

    def buscar_produto(self):
        nome_busca = input("Digite o nome do produto para buscar: ").strip().lower()
        encontrados = [p for p in self.produtos.values() if nome_busca in p.nome.lower()]
        if encontrados:
            print("\nProdutos encontrados:")
            for p in encontrados:
                print(p)
        else:
            print("Nenhum produto encontrado com esse nome.")

def menu():
    controle = ControleEstoque()

    while True:
        print("""
Sistema de Controle de Estoque - Loja de Eletrônicos
1 - Adicionar Produto
2 - Listar Estoque
3 - Atualizar Quantidade
4 - Remover Produto
5 - Buscar Produto
0 - Sair
        """)
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            controle.adicionar_produto()
        elif opcao == "2":
            controle.listar_estoque()
        elif opcao == "3":
            controle.atualizar_quantidade()
        elif opcao == "4":
            controle.remover_produto()
        elif opcao == "5":
            controle.buscar_produto()
        elif opcao == "0":
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()