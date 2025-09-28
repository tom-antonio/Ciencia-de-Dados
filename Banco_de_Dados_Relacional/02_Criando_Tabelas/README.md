"""
Criacao_Tabelas.py

Este script realiza a criação da tabela 'clientes' em um banco de dados PostgreSQL, insere registros de exemplo e exibe todos os clientes cadastrados.

Funcionalidades:
- Adiciona o caminho da pasta "Arquivos" ao sys.path para importar configurações externas.
- Importa as configurações de conexão do arquivo db_config.py.
- Cria a tabela 'clientes' caso ela ainda não exista.
- Verifica se a tabela foi criada com sucesso e exibe mensagem correspondente.
- Insere três registros de clientes na tabela.
- Consulta e exibe todos os clientes cadastrados no banco de dados.
- Fecha o cursor e a conexão ao final da execução.

Pré-requisitos:
- O arquivo db_config.py deve estar localizado em /Users/luanmorais/Desktop/Arquivos e conter o dicionário DB_CONFIG com as informações de conexão.
- O pacote psycopg2 deve estar instalado no ambiente Python.

Exemplo de uso:
$ python Criacao_Tabelas.py

Autor: Luan
Data de criação: 28/09/2025
"""