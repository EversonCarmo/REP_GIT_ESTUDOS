import cx_Oracle

# Conectar ao banco de dados Oracle
conexao = cx_Oracle.connect('SYSTEM/Oracle123@192.168.0.9:1521/XE') 

# Criar um cursor
cursor = conexao.cursor()

# Executar uma consulta para listar os registros da tabela TESTE
cursor.execute('SELECT * FROM TESTE')

# Recuperar e imprimir os registros
for registro in cursor:
    print(registro)

# Fechar cursor e conexão
cursor.close()
conexao.close()