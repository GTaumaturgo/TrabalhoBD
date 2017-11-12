import mysql.connector
from mysql.connector import errorcode

DBUsername = input('Type your database username: ')
DBPassword = input('Type your database password: ')
#Checa conexao
try:
	cnx = mysql.connector.connect(user = DBUsername, password = DBPassword,
				host = '127.0.0.1',
				database = 'bd_enem_2015')
except mysql.connector.Error as err:
	if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("Bad username or password")
	elif err.errno == errorcode.ER_BAD_DB_ERROR:
		print("Database does not exist or invalid name")
	else:
		print(err)
else:
	print("Connection estabilished successfuly")
#executa query
	cursor = cnx.cursor()
	query = ("SELECT idCandidato FROM Candidato "
		  "WHERE idade > 25")
	cursor.execute(query)
	for (idCandidato) in cursor:
		print("{}".format(idCandidato))
	cursor.close()
#fecha conexao
	cnx.close()
