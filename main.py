import pandas as pd 
import mysql.connector as mysql


mensagem_select = "SELECT * FROM namedatabase.users;"

conexao_mysql = mysql.connect(host="localhost", user="root", database="", port=3306)

cursor = conexao_mysql.cursor()
cursor.execute(mensagem_select)
result = cursor.fetchall()

count_result = len(result)

ids = []
nomes = []
cidades = []


for x in range(0, count_result):
    ids.append(result[x][0])
    nomes.append(result[x][1])
    cidades.append(result[x][2])

df = pd.DataFrame(columns=["ID","NOMES","CIDADES"], data=zip(ids,nomes,cidades))

df.to_excel("dadosmysql.xlsx", index=False)

cursor.close()
conexao_mysql.close()
