from view import View
from model import Model
import sys

class Controller():

	def init_arr(self):
		self.main_menu_events = []
		self.main_menu_events += [self.estrutura]
		self.main_menu_events += [self.buscar]
		self.main_menu_events += [self.exit]

		self.db_entities = []
		self.db_entities += ["AreaConhecimento"]
		self.db_entities += ["CadernoProva"]
		self.db_entities += ["Candidato"]
		self.db_entities += ["CorProva"]
		self.db_entities += ["Escola"]
		self.db_entities += ["Municipio"]
		self.db_entities += ["Prova"]
		self.db_entities += ["UnidadeFederativa"]
		self.db_entities += ["TipoProva"]
		self.db_entities += ["Redacao"]

		self.eventos_busca = []
		self.eventos_busca += [self.fazer_query]

		self.estrutura_queries = []
		self.estrutura_queries += ['']


	def __init__(self):
		self.mView  =  View()
		self.mModel = Model()

		self.init_arr()


	def estrutura(self):
		while(True):
			try:
				self.mView.print_menu_estrutura()
				inp = int(self.mView.getInput())
			except:
				pass
			if(inp == 11):
				return

	def buscar(self):
		while(True):
			self.mView.print_menu_busca()
			try:
				inp = int(self.mView.getInput())
	            # As buscas pre feitas de todos os dados de tabelas estão abaixo de 11
				if (inp < 11):
					column_names = self.mModel.get_column_names(self.db_entities[inp-1])
					results = self.mModel.select_all_from(self.db_entities[inp-1])

					self.mView.show_column_names(column_names)
					self.mView.show_select_result(results)
					self.mView.wait_user_consent();
				else:
					self.eventos_busca[inp-11]()
			except:
				pass
			if(inp == 12):
				return

	def exit(self):
		sys.exit(0)

	def start(self):
		while(True):
			self.mView.print_main_menu()
			try:
				inp = int(self.mView.getInput())
				self.main_menu_events[inp-1]()
			except:
                # Gambiarra
				if (inp == 3):
					exit(1)
				pass

	def fazer_query(self):
		self.mView.print_query_input_description()
		sql = self.mView.getInput()
		results = self.mModel.run_query(sql)
		self.mView.show_select_result(results)
