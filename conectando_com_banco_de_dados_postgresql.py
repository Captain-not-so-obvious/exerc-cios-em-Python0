import psycopg2
conn = psycopg2.connect(database = "postgres", user = "postgres", password = "123", host = "127.0.0.1", port = "5432")
print("Conexão com o Banco de Dados aberta com sucesso!")
cur = conn.cursor()
cur.execute('''CREATE TABLE Agenda(ID INT PRIMARY KEY NOT NULL,Nome TEXT NOT NULL,Telefone CHAR(12));''')
print("Tabela criada com sucesso!")
conn.commit()
conn.close()
