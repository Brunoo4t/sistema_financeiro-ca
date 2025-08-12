# Sistema de Gestão Financeira para Centro Acadêmico

## Descrição do Projeto
Desenvolvi um sistema completo de gestão financeira para um Centro Acadêmico, com o objetivo de centralizar e automatizar o controle de receitas e despesas. A aplicação utiliza um banco de dados relacional para garantir a integridade e a segurança dos dados financeiros, permitindo o registro de transações, geração de relatórios de fluxo de caixa e o acompanhamento do saldo por ano.

Este sistema foi crucial para a elaboração do relatório final da gestão 2023-2024, oferecendo uma visão clara e organizada da saúde financeira do Centro. A implementação do projeto visa dar suporte às próximas gestões para que possam tomar decisões mais assertivas e estratégicas.

## Funcionalidades
- **Registro de Transações**: Permite adicionar receitas e despesas com descrição, valor e data (mês e ano).
- **Relatórios Financeiros**: Gera um relatório de fluxo de caixa detalhado para um ano específico, mostrando o total de receitas, despesas e o saldo atual.
- **Armazenamento de Dados**: Utiliza um banco de dados relacional para armazenar de forma segura e organizada todas as transações.

## Tecnologias Utilizadas
- **Python**: Linguagem principal para o desenvolvimento da lógica da aplicação.
- **SQLAlchemy**: ORM (Object-Relational Mapper) para interagir com o banco de dados de forma intuitiva, sem a necessidade de escrever SQL puro.
- **SQLite**: Banco de dados relacional leve e integrado ao projeto, ideal para o gerenciamento de dados locais.
- **Pandas** (opcional, para futuras implementações): Biblioteca poderosa para manipulação e análise de dados, que poderia ser utilizada para relatórios mais complexos.

## Como Executar o Projeto

Siga estes passos simples para rodar o sistema em sua máquina:

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/SEU-USUARIO/sistema-financeiro-ca.git](https://github.com/SEU-USUARIO/sistema-financeiro-ca.git)
    cd sistema-financeiro-ca
    ```
2.  **Crie e ative o ambiente virtual:**
    ```bash
    # No Windows
    python -m venv venv
    venv\Scripts\activate

    # Em macOS ou Linux
    python3 -m venv venv
    source venv/bin/activate
    ```
    *Se você encontrar um erro ao ativar o ambiente virtual no Windows, lembre-se de rodar o PowerShell como administrador e executar o comando `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process`.*

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Execute a aplicação:**
    ```bash
    python -m src.main
    ```

## Contribuições
Sinta-se à vontade para abrir uma issue para reportar bugs, sugerir melhorias ou enviar um pull request. Sua contribuição é bem-vinda!

## Autor
[Bruno Alves] - [(https://www.linkedin.com/in/bruno-alves-09715437a)]

## Licença
Este projeto é distribuído sob a Licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
# sistema_financeiro-ca
 Sistema de Gestão Financeira para Centro Acadêmico
