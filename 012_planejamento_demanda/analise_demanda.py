import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('./demanda/demanda.sql')
cursor = conn.cursor()

# Executar a consulta
cursor.execute("SELECT * FROM demanda")

# Recuperar todos os registros
registros = cursor.fetchall()

# Exibir os registros
for registro in registros:
    print(registro)

# Fechar a conexão
conn.close()
