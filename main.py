cardapio = []
proximo_codigo_item = 1
todos_os_pedidos = []
proximo_codigo_pedido = 1
fila_pedidos_pendentes = []
fila_pedidos_aceitos = []
fila_pedidos_prontos = []
# lista de clientes
clientes = []
proximo_codigo_cliente = 1


# --- Loop Principal do Programa ---
while True:
    print("\n" * 3)
    print("="*40)
    print("   Sistema de Pedidos Tia Lu Delivery")
    print("="*40)
    print("1. Gerenciar Menu de Itens")
    print("2. Gerenciar Menu de Pedidos")
    print("3. Consultas e Relatórios")
    print("4. Cadastrar Cliente")
    print("5. Sair do Sistema")
    print("="*40)
    
    opcao_principal = input("Escolha uma opção: ")

    # === MÓDULO 1: GERENCIAR MENU DE ITENS =========
    if opcao_principal == '1':
        print("\n" * 3)
        print("--- Gerenciar Menu de Itens ---")
        print("1. Cadastrar Item")
        print("2. Consultar Itens")
        print("3. Atualizar Item")
        print("4. Voltar ao Menu Principal")
        opcao_itens = input("Escolha uma opção: ")

        # --- Cadastrar Item ---
        if opcao_itens == '1':
            print("\n" * 3)
            print("-- Cadastro de Novo Item --")
            nome = input("Nome do item: ")
            descricao = input("Descrição do item: ")
            try:
                preco = float(input("Preço (ex: 45.50): "))
                estoque = int(input("Quantidade em estoque: "))
                
                # Cria o item
                novo_item = {
                    'código': proximo_codigo_item,
                    'nome': nome,
                    'descrição': descricao,
                    'preço': preco,
                    'estoque': estoque
                }
                cardapio.append(novo_item)
                proximo_codigo_item += 1
                print(f"\nItem '{nome}' cadastrado com sucesso! Código: {novo_item['código']}")
            except ValueError:
                print("\nERRO: Preço e estoque devem ser números. Operação cancelada.")
            input("Pressione Enter para continuar...")

        # --- Consultar Itens ---
        elif opcao_itens == '2':
            print("\n" * 3)
            print("-- Cardápio Completo --")
            if not cardapio:
                print("Cardápio vazio.")
            else:
                for item in cardapio:
                    print(f"Cód: {item['código']} | {item['nome']} | R${item['preço']:.2f} | Estoque: {item['estoque']} | Desc: {item['descrição']}")
            input("\nPressione Enter para continuar...")

        # --- 1.3 Atualizar Item (Funcionalidade Adicionada) ---
        elif opcao_itens == '3':
            print("\n" * 3)
            print("-- Atualização de Item --")
            if not cardapio:
                print("Cardápio vazio.")
            else:
                for item in cardapio:
                    print(f"Cód: {item['código']} | Nome: {item['nome']} | Estoque: {item['estoque']}")
                try:
                    cod_atualizar = int(input("Digite o código do item para atualizar: "))
                    item_encontrado = None
                    for item in cardapio:
                        if item['código'] == cod_atualizar:
                            item_encontrado = item
                            break
                    
                    if item_encontrado:
                        
                        print(f"\nAtualizando item: {item_encontrado['nome']}")
                        novo_nome = input(f"Novo nome (deixe em branco para manter '{item_encontrado['nome']}'): ")
                        novo_preco_str = input(f"Novo preço (deixe em branco para manter R${item_encontrado['preço']:.2f}): ")
                        novo_estoque_str = input(f"Novo estoque (deixe em branco para manter {item_encontrado['estoque']}): ")

                        try:

                            if novo_nome: item_encontrado['nome'] = novo_nome
                            if novo_preco_str: item_encontrado['preço'] = float(novo_preco_str)
                            if novo_estoque_str: item_encontrado['estoque'] = int(novo_estoque_str)
                            print("\nItem atualizado com sucesso!")
                        except ValueError:
                            print("\nERRO: Preço ou estoque inválido. A atualização foi cancelada.")
                    else:
                        print("\nCódigo do item não encontrado.")
                except ValueError:
                    print("\nERRO: O código deve ser um número. Operação cancelada.")
            input("Pressione Enter para continuar...")

        # --- Voltar ---
        elif opcao_itens == '4':
            pass
        else:
            input("Opção inválida. Pressione Enter para continuar...")

    # === MÓDULO 2: GERENCIAR MENU DE PEDIDOS =======
    elif opcao_principal == '2':
        print("\n" * 3)
        print("--- Gerenciar Menu de Pedidos ---")
        print("1. Criar Pedido")
        print("2. Processar Pedido Pendente (Aceitar/Rejeitar)")
        print("3. Atualizar Status de Pedido em Preparo")
        print("4. Voltar ao Menu Principal")
        opcao_pedidos = input("Escolha uma opção: ")

        # --- Criar Pedido ---
        if opcao_pedidos == '1':
            print("\n" * 3)
            print("-- Criação de Novo Pedido --")
            if not cardapio:
                print("Não é possível criar pedidos, pois o cardápio está vazio.")
            else:
                novo_cliente = input("Nome do cliente: ")
                itens_do_pedido = []
                subtotal = 0.0
                
                while True:
                    print("\n-- Cardápio --")
                    for item in cardapio:
                        print(f"Cód: {item['código']} | {item['nome']} | R${item['preço']:.2f} | Estoque: {item['estoque']}")
                    
                    codigo_str = input("Digite o código do item para adicionar (ou 'F' para finalizar): ").upper()
                    if codigo_str == 'F':
                        break
                    
                    try:
                        cod_item_pedido = int(codigo_str)
                        item_selecionado = None
                        for item in cardapio:
                            if item['código'] == cod_item_pedido:
                                item_selecionado = item
                                break
                        
                        if item_selecionado:
                            qtd = int(input(f"Quantidade de '{item_selecionado['nome']}': "))
                            if 0 < qtd <= item_selecionado['estoque']:
                                itens_do_pedido.append({
                                    'código': item_selecionado['código'],
                                    'nome': item_selecionado['nome'],
                                    'quantidade': qtd,
                                    'preco_unitario': item_selecionado['preço']
                                })
                                subtotal += item_selecionado['preço'] * qtd
                                item_selecionado['estoque'] -= qtd # Abate do estoque
                                print(f"-> {qtd}x {item_selecionado['nome']} adicionado(s).")
                            else:
                                print("Quantidade inválida ou estoque insuficiente.")
                        else:
                            print("Código do item não encontrado.")
                    except ValueError:
                        print("Entrada inválida. Por favor, digite um número ou 'F'.")
                
                if not itens_do_pedido:
                    print("\nNenhum item adicionado. Pedido cancelado.")
                else:
                    total = subtotal # Lógica de desconto pode ser adicionada aqui
                    
                    # Cria o pedido como um dicionário
                    novo_pedido = {
                        'código': proximo_codigo_pedido,
                        'cliente': novo_cliente,
                        'itens': itens_do_pedido,
                        'total': total,
                        'status': 'AGUARDANDO APROVACAO'
                    }
                    
                    fila_pedidos_pendentes.append(novo_pedido)
                    todos_os_pedidos.append(novo_pedido) # Adiciona na lista mestre
                    proximo_codigo_pedido += 1
                    
                    print(f"\nPedido Cód: {novo_pedido['código']} criado com sucesso!")
            input("Pressione Enter para continuar...")

        # --- Processar Pedido Pendente ---
        elif opcao_pedidos == '2':
            print("\n" * 3)
            print("-- Processamento de Pedidos Pendentes --")
            if not fila_pedidos_pendentes:
                print("Não há pedidos pendentes para processar.")
            else:
                # Pega o primeiro pedido da fila (FIFO)
                pedido_a_processar = fila_pedidos_pendentes[0]
                
                print(f"Processando Pedido Cód: {pedido_a_processar['codigo']} | Cliente: {pedido_a_processar['cliente']}")
                for item_p in pedido_a_processar['itens']:
                    print(f"- {item_p['quantidade']}x {item_p['nome']}")
                print(f"Total: R${pedido_a_processar['total']:.2f}")
                
                decisao = input("\nDigite (A) para Aceitar ou (R) para Rejeitar o pedido: ").upper()
                
                if decisao == 'A':
                    # Remove da fila de pendentes e adiciona na de aceitos
                    pedido_aceito = fila_pedidos_pendentes.pop(0)
                    pedido_aceito['status'] = 'ACEITO'
                    fila_pedidos_aceitos.append(pedido_aceito)
                    print("Pedido Aceito e movido para a fila de preparo.")
                elif decisao == 'R':
                    pedido_rejeitado = fila_pedidos_pendentes.pop(0)
                    pedido_rejeitado['status'] = 'REJEITADO'
                    # Restaura o estoque
                    for item_pedido in pedido_rejeitado['itens']:
                        for item_cardapio in cardapio:
                            if item_pedido['código'] == item_cardapio['código']:
                                item_cardapio['estoque'] += item_pedido['quantidade']
                                break
                    print("Pedido Rejeitado. Estoque dos itens foi restaurado.")
                else:
                    print("Decisão inválida. O pedido permanece na fila.")
            input("Pressione Enter para continuar...")

        # --- Atualizar Status ---
        elif opcao_pedidos == '3':
            print("\n" * 3)
            print("-- Iniciar Preparo de Pedido --")
            if not fila_pedidos_aceitos:
                print("Nenhum pedido na fila de preparo.")
            else:
                pedido_a_preparar = fila_pedidos_aceitos.pop(0)
                pedido_a_preparar['status'] = 'FAZENDO'
                print(f"Pedido Cód {pedido_a_preparar['código']} iniciou o preparo (status: FAZENDO).")
                
                # Simulação de finalização do preparo
                input("Pressione ENTER quando o pedido estiver pronto...")
                pedido_a_preparar['status'] = 'FEITO'
                fila_pedidos_prontos.append(pedido_a_preparar)
                print(f"Pedido Cód {pedido_a_preparar['código']} está pronto e aguardando entregador.")
            input("Pressione Enter para continuar...")

        elif opcao_pedidos == '4':
            pass
        else:
            input("Opção inválida. Pressione Enter para continuar...")

    # === MÓDULO 3: CONSULTAS E RELATÓRIOS ==========
    elif opcao_principal == '3':
        print("\n" * 3)
        print("--- Consultas e Relatórios ---")
        print("1. Exibir todos os pedidos")
        print("2. Filtrar pedidos por status")
        print("3. Voltar ao Menu Principal")
        opcao_consultas = input("Escolha uma opção: ")

        # --- Exibir Todos os Pedidos ---
        if opcao_consultas == '1':
            print("\n" * 3)
            print("-- Todos os Pedidos Registrados --")
            if not todos_os_pedidos:
                print("Nenhum pedido foi criado ainda.")
            else:
                for p in todos_os_pedidos:
                    print(f"Cód: {p['código']} | Cliente: {p['cliente']} | Total: R${p['total']:.2f} | Status: {p['status']}")
            input("\nPressione Enter para continuar...")

        # --- Filtrar por Status  ---
        elif opcao_consultas == '2':
            print("\n" * 3)
            status_filtro = input("Digite o status para filtrar (ex: FAZENDO, ACEITO): ").upper()
            print(f"\n-- Pedidos com Status: {status_filtro} --")
            encontrados = False
            for p in todos_os_pedidos:
                if p['status'] == status_filtro:
                    print(f"Cód: {p['código']} | Cliente: {p['cliente']} | Total: R${p['total']:.2f}")
                    encontrados = True
            if not encontrados:
                print(f"Nenhum pedido encontrado com o status '{status_filtro}'.")
            input("\nPressione Enter para continuar...")
        
        # --- Voltar ---
        elif opcao_consultas == '3':
            pass
        else:
            input("Opção inválida. Pressione Enter para continuar...")
    
    # === MÓDULO 4: CADASTRAR CLIENTE ===============
    # --- Cadastrar Cliente
    elif opcao_principal == '4':
        print("\n" * 3)
        print("-- Cadastro de Novo Cliente --")
        print("1. Cadastrar novo cliente")
        print("2. Listar todos os clientes")
        print("3. Voltar ao Menu Principal")
        opcao_clientes = input("Escolha uma opção: ")

        if opcao_clientes == '1':
            nome = input("Nome do cliente: ")
            telefone = input("Telefone do cliente: ")
            endereco = input("Endereço do cliente: ")
            
            # Cria o cliente
            novo_cliente = {
                'código': proximo_codigo_cliente,
                'nome': nome,
                'telefone': telefone,
                'endereco': endereco
            }

            clientes.append(novo_cliente)
            print(f"\nCliente '{nome}' cadastrado com sucesso! Código: {novo_cliente['código']}")
            proximo_codigo_cliente += 1
        
        elif opcao_clientes == '2':
            print("\n" * 3)
            print("-- Lista de Clientes Cadastrados --")
            if not clientes:
                print("Nenhum cliente cadastrado.")
            else:
                for cliente in clientes:
                    print(f"cód: {cliente['código']} | Nome: {cliente['nome']} | Telefone: {cliente['telefone']}")

        elif opcao_clientes == '3':
            pass

        else:
            input("Opção inválida. Pressione Enter para continuar...")


    # === SAÍDA DO SISTEMA
    elif opcao_principal == '5':
        print("Saindo do sistema. Obrigado por usar o Tia Lu Delivery!")
        break
    else:
        input("Opção principal inválida. Pressione Enter para continuar...")