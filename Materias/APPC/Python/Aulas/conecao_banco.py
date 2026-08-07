import mysql.connector

def obtemConexao (servidor,usuario,senha, bd):
    if obtemConexao.conexao == None:
        obtemConexao.conexao = mysql.connector.connect(host=f"{servidor}", user=f"{usuario}", password=f"{senha}",database=f"{bd}")

    return obtemConexao.conexao
obtemConexao.conexao=None