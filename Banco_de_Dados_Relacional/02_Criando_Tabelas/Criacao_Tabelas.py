import sys
import os

# Adiciona o caminho da pasta "Arquivos" à lista de caminhos de importação
sys.path.append('/Users/luanmorais/Desktop/Arquivos')

from db_config import DB_CONFIG
import psycopg2

# Usa o dicionário de configuração
conn = psycopg2.connect(**DB_CONFIG)
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id_cliente SERIAL PRIMARY KEY,
        nome CHARACTER VARYING(100) NOT NULL,
        CPF CHARACTER VARYING(11) NOT NULL,
        telefone CHARACTER VARYING(15) NOT NULL
    );
""")
cur.execute("SELECT to_regclass('public.clientes');")
result = cur.fetchone()

if result[0] is None:
    print("Tabela 'clientes' ainda não existe.")
else:
    print("Tabela 'clientes' já existe.")
conn.commit()

cur.execute("""
    INSERT INTO clientes (id_cliente, nome, CPF, telefone) VALUES
        (1, 'Luan', '12345678901', '11999999999'),
        (2, 'Maria', '10987654321', '21988888888'),
        (3, 'João', '11122233344', '31977777777');""")
conn.commit()

cur.execute("SELECT * FROM clientes;")
clientes = cur.fetchall()
for cliente in clientes:
    print(cliente)
conn.commit()

cur.close()
conn.close()