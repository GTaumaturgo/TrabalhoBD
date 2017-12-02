import csv
import mysql.connector

class Model():

	def __init__(self):
		self.cnx = None
		try:
			self.cnx = mysql.connector.connect(user = 'root', password = 'root',
			host = '127.0.0.1',
			database = 'bd_enem_2015')
		except mysql.connector.Error as err:
			if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
				print("Bad username or password")
				exit(0)
			elif err.errno == errorcode.ER_BAD_DB_ERROR:
				print("Database does not exist or invalid name")
				exit(0)
			else:
				print(err)
				exit(0)
		else:
			pass
			# print("Connection estabilished successfuly")

	def __del__(self):
		self.cnx.close()

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
			# Execute the SQL command
			cursor.execute(sql)
			results = cursor.fetchall();

			# Fetch all the rows in a list of lists.
			return results
		except:
			print( "Error: unable to fecth data")
