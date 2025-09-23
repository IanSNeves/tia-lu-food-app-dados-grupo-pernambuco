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
        elif opcao == '2':
            menu_gerenciar_pedidos()
        elif opcao == '3':
            menu_consultar_pedidos()
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

def menu_gerenciar_pedidos():
    """Menu para gerenciar pedidos."""
    global proximo_codigo_pedido
    while True:
        limpar_tela()
        print("--- Gerenciar Pedidos ---")
        print("1. Criar Pedido")
        print("2. Processar Pedidos Pendentes")
        print("3. Voltar")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == '1':
            limpar_tela()
            print("--- Criar Novo Pedido ---")
            if not itens_cardapio:
                print("Não é possível criar um pedido. Nenhum item cadastrado.")
                input("Pressione Enter para continuar...")
                continue
            
            itens_pedido = []
            
            while True:
                print("\nItens disponíveis:")
                for item in itens_cardapio:
                    print(f"[{item.codigo}] {item.nome} - R${item.preco:.2f}")
                
                codigo_item = input("Digite o código do item (ou 'f' para finalizar o pedido): ")
                
                if codigo_item.lower() == 'f':
                    if itens_pedido:
                        novo_pedido = Pedido(proximo_codigo_pedido, itens_pedido)
                        fila_pedidos_pendentes.append(novo_pedido)  # Adiciona à fila de pendentes [cite: 83]
                        proximo_codigo_pedido += 1
                        print("\nPedido criado com sucesso! Aguardando aprovação.")
                    else:
                        print("Pedido não pode ser vazio. Adicione pelo menos um item.")
                    break
                
                try:
                    codigo_item = int(codigo_item)
                    item_encontrado = next((item for item in itens_cardapio if item.codigo == codigo_item), None)
                    if item_encontrado:
                        itens_pedido.append(item_encontrado)
                        print(f"Item '{item_encontrado.nome}' adicionado ao pedido.")
                    else:
                        print("Item não encontrado.")
                except ValueError:
                    print("Entrada inválida. Digite um código de item ou 'f'.")
            
            input("Pressione Enter para continuar...")
            
        elif opcao == '2':
            processar_pedidos_pendentes()

            
        elif opcao == '3':
            break
        else:
            input("Opção inválida. Pressione Enter para continuar...")

def menu_consultar_pedidos():
    """Menu para consultar pedidos."""
    limpar_tela()
    print("--- Consultar Pedidos ---")
    print("1. Exibir todos os pedidos")
    print("2. Filtrar por status")
    print("3. Voltar")
    
    opcao = input("\nEscolha uma opção: ")
    
    if opcao == '1':
        limpar_tela()
        print("--- Todos os Pedidos ---")
        todos_pedidos = fila_pedidos_pendentes + fila_pedidos_aceitos + fila_pedidos_prontos
        if not todos_pedidos:
            print("Nenhum pedido no sistema.")
        else:
            for pedido in todos_pedidos:
                print(pedido)
        input("\nPressione Enter para continuar...")
    
    elif opcao == '2':
        # Lógica de filtro será implementada em outra sprint
        print("\nFuncionalidade em desenvolvimento. Filtro por status será adicionado aqui.")
        input("Pressione Enter para continuar...")

    elif opcao == '3':
        return
    
    else:
        input("Opção inválida. Pressione Enter para continuar...")

def processar_pedidos_pendentes():
    limpar_tela()
    print("--- Processar Pedidos Pendentes ---")
    if not fila_pedidos_pendentes:
        print("Nenhum pedido pendente para processar.")
    else:
        Pedido_a_processar = fila_pedidos_pendentes[0]
        print(f"Pedido {Pedido_a_processar.codigo} selecionado para processamento.")

        confirmado = input("\nDeseja confirmar esse pedido? (s/n): ")
        if confirmado == 's':
            fila_pedidos_pendentes.remove(Pedido_a_processar)
            fila_pedidos_aceitos.append(Pedido_a_processar)
            Pedido_a_processar.status = "EM PREPARO"
        else:
            print("Pedido não confirmado. Ele permanece na fila de pendentes.")
    
    input("Pressione Enter para continuar...")


# Inicia o sistema
if __name__ == "__main__":
    menu_principal()