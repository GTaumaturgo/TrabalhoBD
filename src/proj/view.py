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
		self.menu_estrutura += ['| 10 - Ver colunas da tabela 10      |']
		self.menu_estrutura += ['| 11 - Voltar                        |']
		self.menu_estrutura += [' ==================================== ']
		

	def print_menu(self,menu):
		system('clear') # limpa a tela
		for line in menu:
			print(line)

	def print_main_menu(self):
		self.print_menu(self.main_menu)	

	def print_menu_estrutura(self):
		self.print_menu(self.menu_estrutura)

	def getInput(self):
		return input()







