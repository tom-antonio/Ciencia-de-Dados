"""
Conexao_Pyhton_BD.py

Este script realiza a conexão com um banco de dados PostgreSQL utilizando as configurações armazenadas em um dicionário externo (DB_CONFIG).
O objetivo principal é testar a conexão e exibir a versão do PostgreSQL em uso.

Funcionalidades:
- Adiciona o caminho da pasta "Arquivos" ao sys.path para importar configurações externas.
- Importa as configurações de conexão do arquivo db_config.py.
- Estabelece conexão com o banco de dados PostgreSQL usando psycopg2.
- Executa uma consulta para obter a versão do PostgreSQL.
- Exibe a versão do PostgreSQL no console.
- Fecha o cursor e a conexão ao final da execução.

Pré-requisitos:
- O arquivo db_config.py deve estar localizado em /Users/luanmorais/Desktop/Arquivos e conter o dicionário DB_CONFIG com as informações de conexão.
- O pacote psycopg2 deve estar instalado no ambiente Python.

Exemplo de uso:
$ python Conexao_Pyhton_BD.py

Autor: Luan
Data de criação: 28/09/2025
"""