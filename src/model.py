import csv
import mysql.connector
import pdb

class Model():

	def __init__(self):
		self.cnx = None
		try:
			self.cnx = mysql.connector.connect(user = 'root', password = '',
			host = '127.0.0.1',
			database = 'bd_enem_2015')
		except:
			print("\n \n Banco não existe ou usuário/senha errados \n \n")
			exit(0)
		else:
			pass
			# print("Connection estabilished successfuly")

	def __del__(self):
		try:
			self.cnx.close()
		except:
			exit(0)

	def select_all_from(self, entity):
		# prepare a cursor object using cursor() method
		cursor = self.cnx.cursor()

		sql = "SELECT * FROM " + entity
		try:
			# Execute the SQL command
			cursor.execute(sql)
			# Fetch all the rows in a list of lists.
			results = cursor.fetchall()
			return results

		except:
			print( "Error: unable to fecth data")

	def get_column_names(self, entity):
		c = self.get_column_info(entity)
		res = [a[0] for a in c]
		return res

	def get_tables(self):
		cursor = self.cnx.cursor()

		sql = 'show tables'
		try:
			cursor.execute(sql)
			results = cursor.fetchall()
			return results
		except:
			print("Error: unable to fetch data")

	def get_column_info(self, entity):
		# prepare a cursor object using cursor() method
		cursor = self.cnx.cursor()

		sql = "desc " + entity
		try:
			# Execute the SQL command
			cursor.execute(sql)
			results = cursor.fetchall();

			# Fetch all the rows in a list of lists.
			return results
		except:
			print( "Error: unable to fecth data")

	def run_query(self,sql):
		# prepare a cursor object using cursor() method
		cursor = self.cnx.cursor()

		try:
			if 'call' in sql.lower():
				procedure_name = sql.lower().split('call ')[1].split('(')[0]
				procedure_args = self.procedure_arguments(sql)
				cursor.callproc(procedure_name, procedure_args)
				cursor.execute("select * from " + procedure_name)
			else:
				cursor.execute(sql)
			if 'update' in sql.lower():
				results = None
			else:
				results = cursor.fetchall();


			# Fetch all the rows in a list of lists.
			return results
		except:
			print( "Error: unable to fecth data")

	def procedure_arguments(self, sql):
		args = sql.lower().split('call ')[1].split('(')[1].split(')')[0].split(',')
		for index, arg in enumerate(args):
			if not "'" in arg:
				args[index] = int(arg)
			else:
				args[index] = arg.replace("'","")
		return tuple(args)
