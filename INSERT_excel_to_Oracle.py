import pandas as pd
import cx_Oracle
from pathlib import Path

# Defina as credenciais do banco de dados Oracle
oracle_username = 'SYSTEM'
oracle_password = 'Oracle123'
oracle_host = '192.168.0.9'
oracle_port = '1521'
oracle_service = 'XE'

# Caminho para o arquivo da planilha na área de trabalho do Windows
caminho_planilha = Path("C:\Users\Everson Carmo\Desktop\mailling\Everson_AP_08_07.xlsx")

# Função para carregar dados da planilha para o banco de dados Oracle
def carregar_para_oracle(planilha_path, oracle_username, oracle_password, oracle_host, oracle_port, oracle_service, tabela_oracle):
    # Carregar dados da planilha para um DataFrame do pandas
    dados_planilha = pd.read_excel(planilha_path)
    
    # Conectar ao banco de dados Oracle
    dsn_tns = cx_Oracle.makedsn(oracle_host, oracle_port, service_name=oracle_service)
    conexao = cx_Oracle.connect(user=oracle_username, password=oracle_password, dsn=dsn_tns)

    # Criar um cursor para executar comandos SQL
    cursor = conexao.cursor()

    # Loop através das linhas do DataFrame e inserir os dados na tabela Oracle
    for indice, linha in dados_planilha.iterrows():
        num_cpf = linha['CPF']
        cod_agencia = linha['agencia']
        num_conta = linha['conta']
        nm_cliente = linha['nome_cliente']
        cod_uf = linha['UF']
        dat_nasc = linha['data_nascimento']
        ind_sexo = linha['ind_sexo']
        num_fone1 = linha['FONE1']
        num_fone2 = linha['FONE2']
        num_fone3 = linha['FONE3']
        num_fone4 = linha['FONE4']

        comando_sql = f"INSERT INTO {tabela_oracle} (NUM_CPF, COD_AGENCIA, NUM_CONTA, NOME_CLIENTE, COD_UF, DAT_NASC, IND_SEXO, NUM_FONE1, NUM_FONE2, NUM_FONE3, NUM_FONE4) VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11)"
        cursor.execute(comando_sql, (num_cpf, cod_agencia, num_conta, nm_cliente, cod_uf, dat_nasc, ind_sexo, num_fone1, num_fone2, num_fone3, num_fone4))

    # Commit para salvar as mudanças
    conexao.commit()

    # Fechar o cursor e a conexão
    cursor.close()
    conexao.close()

# Nome da tabela Oracle para carregar os dados
tabela_oracle = 'CLIENTE'

# Chamar a função para carregar os dados da planilha para a tabela Oracle
carregar_para_oracle(caminho_planilha, oracle_username, oracle_password, oracle_host, oracle_port, oracle_service, tabela_oracle)

print("Dados carregados com sucesso para a tabela Oracle!")