# GoodWallet

Gerenciador de gastos pessoais em Python.

## Problema:

Muitas pessoas têm dificuldade em controlar seus gastos mensais de forma simples e organizada. 
Sem um controle adequado, é comum ultrapassar o orçamento e perder a noção de onde o dinheiro está sendo gasto.

Este projeto busca resolver esse problema oferecendo uma aplicação simples em linha de comando para registrar,
organizar e visualizar despesas pessoais.

## Público-alvo:

Este projeto é voltado para pessoas que desejam controlar seus gastos pessoais de forma simples,
como estudantes, trabalhadores autônomos ou qualquer pessoa que queira organizar suas despesas mensais.

Descrição:
- Aplicação em Python para gerenciamento de gastos pessoais, permitindo cadastrar, editar, remover, filtrar e visualizar despesas de forma simples.

Funcionalidades:
- Cadastro de gastos
- Classificação por categoria
- Listagem de despesas
- Controle de gastos mensais
- Edição e remoção de gastos
- Filtro por categoria
- Filtro por mês
- Definição de limite mensal
- Gráfico de gastos por categoria
- Adicionar gastos
- Listar gastos
- Editar gastos
- Remover gastos
- Verificar limite mensal

Tecnologias utilizadas:
- Python
- JSON
- Git
- GitHub
- Matplotlib

Estrutura do Projeto:
- app/: lógica principal
- data/: banco de dados
- docs/: documentação
- assets/: imagens
- `app/main.py` → menu principal da aplicação
- `app/services.py` → lógica do sistema
- `app/storage.py` → leitura e gravação em JSON
- `data/gastos.json` → armazenamento dos gastos
- `data/config.json` → configuração do limite mensal

Necessário para executar o projeto:
- pip install -r requirements.txt

Como executar o projeto:
1. Clone o repositório - git clone https://github.com/seu-usuario/GoodWallet.git
2. Entre na pasta - cd GoodWallet
3. Instale as dependências - python -m pip install -r requirements.txt
4. Execute o programa no python app/main.py - python -m app.main

## Testes automatizados:

Para executar os testes do projeto:
- python -m pytest
Para verificar a qualidade do código utilizando Ruff:
- python -m ruff check .

Demonstração:
### Menu principal
![Menu principal](assets/menu.png)

### Lista de gastos
![Lista de gastos](assets/listar-gastos.png)

### Gráfico por categoria
![Gráfico por categoria](assets/gastos-categoria.png)


Versão: 1.0.0

Autor:
Vinícius Martins
