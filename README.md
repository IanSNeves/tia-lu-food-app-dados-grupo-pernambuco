1. FUNCIONALIDADES FALTANTES

Gerenciamento de Clientes
- [ ] Cadastrar Cliente: Criar uma nova seção no menu para gerenciar clientes, permitindo, no mínimo, cadastrá-los (com código, nome, etc.).
- [ ] Listar Clientes: Implementar uma forma de consultar os clientes já cadastrados.

### Gerenciamento de Itens
- [ ] Atualizar Item: Adicionar ao menu a opção "Atualizar Item" para modificar nome, descrição, preço e estoque.

### Gerenciamento de Pedidos
- [ ] Associar Cliente a um Pedido: Ao criar um pedido, o sistema deve perguntar e associar um cliente cadastrado.
- [ ] Aplicar Cupom de Desconto: Implementar a lógica para aplicar um cupom de desconto na criação do pedido.
- [ ] Atualizar Status de Pedido: Criar uma função no menu para permitir a alteração manual do status de um pedido existente.
- [ ] Cancelar Pedido: Implementar a opção para cancelar um pedido, seguindo a regra de que só é possível se o status for "AGUARDANDO APROVACAO" ou "ACEITO".

### Fluxo de Pedidos
- [ ] Gestão da Fila de Pedidos Prontos: Implementar a lógica para mover os pedidos, após o preparo, para a "fila_pedidos_prontos".

### Consultas
- [ ] Filtrar Pedidos por Status: Implementar a funcionalidade de filtrar pedidos por status.

# 2. CORREÇÕES E INCONSISTÊNCIAS

### Fluxo de Status dos Pedidos
- [ ] Corrigir Status Incorretos: Ao aceitar um pedido, o status deve mudar para "ACEITO" e depois para "FAZENDO", em vez de ir direto para "EM PREPARO".
- [ ] Implementar Status Faltantes: Garantir que todos os status definidos no documento sejam utilizados no fluxo do programa (ACEITO, FEITO, ESPERANDO ENTREGADOR, SAIU PARA ENTREGA, ENTREGUE, CANCELADO, REJEITADO).
- [ ] Implementar Lógica de Rejeição: Quando um pedido pendente não é confirmado, seu status deve ser alterado para "REJEITADO" e ele deve ser tratado adequadamente, em vez de apenas permanecer na fila.

### Estrutura e Lógica do Código
- [ ] Melhorar Processamento de Pedidos: Considerar um loop ou outra forma de permitir que o atendente processe vários pedidos pendentes em sequência, sem precisar voltar ao menu principal a cada pedido processado.





# 🍔 Sistema de Gerenciamento de Pedidos

## Documentação
- [Clique aqui para acessar.](https://bold-fireplant-8eb.notion.site/Documenta-o-2688254211a2803b97d9e71366eed8a1)

---

## 👥 Equipe
- Membro 1: Ian Neves
- Membro 2: David Cairo
- Membro 3: Paulo Soares
- Membro 4: Pedro Silveira
- Membro 5: Jefte Santos

---

## 📖 Descrição
Este projeto é um **sistema de gerenciamento de pedidos** desenvolvido em Python.  
O objetivo é simular o funcionamento básico de um restaurante utilizando **estruturas de dados nativas** para representar filas de pedidos e operações de gerenciamento de itens e pedidos.

O sistema é operado por meio de um **menu interativo em linha de comando**, oferecendo funcionalidades para manipulação do **menu de itens** e do **fluxo de pedidos**.

---

## ⚙️ Estrutura e Funcionalidades

### 🔹 Gerenciar Menu de Itens
- **Cadastrar Item**: Adiciona um novo produto ao menu.  
- **Atualizar Item**: Modifica informações de um item existente (nome, descrição, preço, quantidade em estoque).  
- **Consultar Itens**: Exibe todos os itens disponíveis.  

Cada item é armazenado com as seguintes informações:
- `código`: Identificador único (gerado automaticamente).
- `nome`: Nome do produto.
- `descrição`: Detalhes sobre o item.
- `preço`: Valor monetário.
- `estoque`: Quantidade em estoque.

---

### 🔹 Gerenciar Menu de Pedidos
- **Criar Pedido**:  
  - Deve conter no mínimo **um item**.  
  - Pode ter um **cupom de desconto** aplicado.  
  - Ao ser criado, o pedido é considerado **pago** e recebe o status inicial `AGUARDANDO APROVACAO`.  

- **Processar Pedidos Pendentes**:  
  - Permite **aceitar ou rejeitar** pedidos na ordem em que foram criados.  

- **Atualizar Status de Pedido**:  
  - Altera o status de um pedido existente de acordo com o fluxo definido.  

- **Cancelar Pedido**:  
  - Só é possível se o status for `AGUARDANDO APROVACAO` ou `ACEITO`.

---

### 🔹 Fluxo de Pedidos e Filas
O sistema usa **filas (FIFO)** para gerenciar os pedidos:

1. **Fila de Pedidos Pendentes**  
   - Todos os novos pedidos são adicionados aqui.  
   - Processados na ordem de chegada.  

2. **Fila de Pedidos Aceitos**  
   - Pedidos aceitos são movidos para cá com status `FAZENDO`.  

3. **Fila de Pedidos Prontos**  
   - Após o preparo, recebem status `FEITO` e ficam aguardando entregador (`ESPERANDO ENTREGADOR`).  

---

### 🔹 Fluxo de Status do Pedido
Os pedidos podem assumir os seguintes status:

- `AGUARDANDO APROVACAO`
- `ACEITO`
- `FAZENDO`
- `FEITO`
- `ESPERANDO ENTREGADOR`
- `SAIU PARA ENTREGA`
- `ENTREGUE`
- `CANCELADO`
- `REJEITADO`

---

### 🔹 Consultas
O sistema permite:
- Exibir **todos os pedidos**.  
- Filtrar pedidos por **status**.  

---

## 🛠️ Tecnologias Utilizadas
- **Python 3.x**  
- Estruturas de dados nativas (`list`, `queue`)  
- Menu interativo no terminal  

---

## ▶️ Como Executar
1. Clone o repositório:
   ```bash
   git clone https://github.com/usuario/repositorio.git
   cd repositorio
