import cx_Oracle

# Configurações de conexão com o banco de dados Oracle
dsn_tns = cx_Oracle.makedsn('192.168.0.9', '1521', service_name='xe')
conn = cx_Oracle.connect(user='system', password='Oracle123', dsn=dsn_tns)

# Nome da tabela no banco de dados Oracle
table_name = 'TESTE'

# Criar o cursor
cursor = conn.cursor()

# Executar uma consulta na tabela Oracle
cursor.execute(f"SELECT * FROM {table_name}")

# Recuperar os resultados da consulta
rows = cursor.fetchall()

# Exibir os resultados
for row in rows:
    print(row)

# Fechar o cursor e a conexão com o banco de dados
cursor.close()
conn.close()