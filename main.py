import os
import time

# Classes de dados
class Item:
    """Representa um item do cardápio."""
    def __init__(self, codigo, nome, descricao, preco, estoque):
        self.codigo = codigo
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.estoque = estoque

    def __str__(self):
        return f"Código: {self.codigo} | Nome: {self.nome} | Preço: R${self.preco:.2f} | Estoque: {self.estoque}"
  
class Pedido:
    """Representa um pedido do cliente."""
    def __init__(self, codigo, itens):
        self.codigo = codigo
        self.itens = itens
        self.valor_total = sum(item.preco for item in itens)
        self.status = "AGUARDANDO APROVACAO"  # Status inicial do pedido [cite: 75, 96]

    def __str__(self):
        nomes_itens = ", ".join([item.nome for item in self.itens])
        return f"Pedido {self.codigo} | Status: {self.status} | Total: R${self.valor_total:.2f} | Itens: {nomes_itens}"

# Simulação de estruturas de dados para o sistema
itens_cardapio = []  # Lista para armazenar os itens do menu
fila_pedidos_pendentes = [] # Fila para novos pedidos [cite: 83]
fila_pedidos_aceitos = [] # Fila para pedidos aceitos [cite: 87]
fila_pedidos_prontos = [] # Fila para pedidos prontos [cite: 91]

# Variáveis para controle de códigos automáticos
proximo_codigo_item = 1
proximo_codigo_pedido = 1

def limpar_tela():
    """Limpa a tela do console."""
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_principal():
    """Exibe o menu principal e processa a escolha do usuário."""
    while True:
        limpar_tela()
        print("--- Sistema de Gerenciamento de Pedidos ---")
        print("1. Gerenciar Menu de Itens")
        print("2. Gerenciar Menu de Pedidos")
        print("3. Consultar Pedidos")
        print("4. Sair")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == '1':
            menu_gerenciar_itens()
        elif opcao == '4':
            print("Saindo do sistema...")
            break
        else:
            input("Opção inválida. Pressione Enter para continuar...")

def menu_gerenciar_itens():
    """Menu para gerenciar itens do cardápio."""
    global proximo_codigo_item
    while True:
        limpar_tela()
        print("--- Gerenciar Menu de Itens ---")
        print("1. Cadastrar Item")
        print("2. Consultar Itens")
        print("3. Voltar")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == '1':
            limpar_tela()
            print("--- Cadastrar Novo Item ---")
            nome = input("Nome do item: ")
            descricao = input("Descrição: ")
            
            while True:
                try:
                    preco = float(input("Preço: R$"))
                    estoque = int(input("Estoque: "))
                    break
                except ValueError:
                    print("Valores de preço ou estoque inválidos. Tente novamente.")
            
            novo_item = Item(proximo_codigo_item, nome, descricao, preco, estoque)
            itens_cardapio.append(novo_item)
            proximo_codigo_item += 1
            print("\nItem cadastrado com sucesso!")
            input("Pressione Enter para continuar...")
        
        elif opcao == '2':
            limpar_tela()
            print("--- Itens do Cardápio ---")
            if not itens_cardapio:
                print("Nenhum item cadastrado ainda.")
            else:
                for item in itens_cardapio:
                    print(item)
            input("\nPressione Enter para continuar...")
        
        elif opcao == '3':
            break
        else:
            input("Opção inválida. Pressione Enter para continuar...")



# Inicia o sistema
if __name__ == "__main__":
    menu_principal()