from view import View
from model import Model
import sys

class Controller():

	def init_arr(self):
		self.main_menu_events = []
		self.main_menu_events += [self.estrutura]
		self.main_menu_events += [self.buscar]
		self.main_menu_events += [self.exit]

		self.estrutura_queries = []
		self.estrutura_queries += ['']


	def __init__(self):
		self.mView  =  View()
		self.mModel = Model()

		self.init_arr()


	def estrutura(self):
		while(True):
			self.mView.print_menu_estrutura()
			inp = int(self.mView.getInput())
			if(inp == 11):
				return
		


	def buscar(self):
		pass

	def exit(self):
		sys.exit(0)

	def start(self):
		while(True):
			self.mView.print_main_menu()
			inp = int(self.mView.getInput())

			self.main_menu_events[inp-1]() 
