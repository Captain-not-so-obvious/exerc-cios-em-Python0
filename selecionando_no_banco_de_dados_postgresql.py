import psycopg2
conn = psycopg2.connect(database = " postgres", user="postgres" , password=" senha123" , host="127.0.0.1", port="5432" ) 
print ("Conexão com o Banco de Dados aberta com sucesso!") 
cur=conn.cursor() 
cur.execute("""select * from public."AGENDA" where "id"=1""") 
registro=cur.fetchone() 
print(registro) 
conn.commit()
print("Seleção realizada com sucesso!"); 
conn.close()
