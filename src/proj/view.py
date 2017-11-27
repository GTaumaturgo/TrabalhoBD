from os import system

class View():



	def __init__(self):
		self.init_menus()

	def init_menus(self):
		self.main_menu = []
		self.main_menu += [' ============================== ']
		self.main_menu += ['| 1 - Ver a estrutura do banco |']
		self.main_menu += ['| 2 - Fazer buscas no banco    |']
		self.main_menu += ['| 3 - Sair do programa         |']
		self.main_menu += [' ============================== ']

		self.menu_estrutura = []
		self.menu_estrutura += [' ==================================== ']
		self.menu_estrutura += ['| 1 - Ver colunas da tabela AreaConhecimento  |']
		self.menu_estrutura += ['| 2 - Ver colunas da tabela CadernoProva      |']
		self.menu_estrutura += ['| 3 - Ver colunas da tabela Candidato         |']
		self.menu_estrutura += ['| 4 - Ver colunas da tabela CorProva          |']
		self.menu_estrutura += ['| 5 - Ver colunas da tabela Escola            |']
		self.menu_estrutura += ['| 6 - Ver colunas da tabela Municipio         |']
		self.menu_estrutura += ['| 7 - Ver colunas da tabela Prova             |']
		self.menu_estrutura += ['| 8 - Ver colunas da tabela UnidadeFederativa |']
		self.menu_estrutura += ['| 9 - Ver colunas da tabela TipoProva         |']
		self.menu_estrutura += ['| 10 - Ver colunas da tabela Redacao		   |']
		self.menu_estrutura += ['| 11 - Voltar               			       |']
		self.menu_estrutura += [' ==================================== ']


		self.menu_busca = []
		self.menu_busca += [' ==================================== ']
		self.menu_busca += ['| 1 - Ver Dados de AreaConhecimento  |']
		self.menu_busca += ['| 2 - Ver Dados de CadernoProva      |']
		self.menu_busca += ['| 3 - Ver Dados de Candidato         |']
		self.menu_busca += ['| 4 - Ver Dados de CorProva          |']
		self.menu_busca += ['| 5 - Ver Dados de Escola            |']
		self.menu_busca += ['| 6 - Ver Dados de Municipio         |']
		self.menu_busca += ['| 7 - Ver Dados de Prova             |']
		self.menu_busca += ['| 8 - Ver Dados de UnidadeFederativa |']
		self.menu_busca += ['| 9 - Ver Dados de TipoProva         |']
		self.menu_busca += ['| 10 - Ver Dados de Redacao	      |']
		self.menu_busca += ['| 11 - Fazer query personalizada     |']
		self.menu_busca += ['| 12 - Voltar                        |']
		self.menu_busca += [' ==================================== ']


	def print_menu(self,menu):
		system('clear') # limpa a tela
		for line in menu:
			print(line)

	def print_main_menu(self):
		self.print_menu(self.main_menu)

	def print_menu_estrutura(self):
		self.print_menu(self.menu_estrutura)

	def print_menu_busca(self):
		self.print_menu(self.menu_busca)

	def getInput(self):
		return input()

	def mostrar_estrutura(self, ):
		print (' ==================================== ')
		print (' ==================================== ')

	def show_select_result(self, results):
		i = 1
		for row in results:
			for field in row:
				print (field, "\t", end="")
			print( '\n')
            # Imprime de 50 em 50
			if (i % 50 == 0):
				self.wait_user_consent()
			i+=1

	def show_column_names(self, result):
		for columns in result:
			print (columns[0], "\t", end="")
		print( '\n')

	def wait_user_consent(self):
		input("Precione enter")

	def print_query_input_description(self):
		print("Digite a query desejada na liguagem sql:")
