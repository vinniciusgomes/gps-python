# -*- coding: utf-8 -*-
import os
# O NetworkX é um pacote Python para a criação, manipulação e estudo da estrutura, dinâmica e funções de redes complexas.
import networkx as nx
def limpar_tela():
    os.system('clear')

class GPS(object):
	grafo 	= None
	origem 	= None
	destino = None

	def ler_mapa(self, arquivo_mapa):
		# Grafos
		self.grafo = nx.convert.convert_to_undirected(nx.read_gml(arquivo_mapa))

	def setar_origem(self, origem):
		# Origem
		self.origem = int(origem)

	def setar_destino(self, destino):
		# Destino
		self.destino = int(destino)

	def processar(self):
		# Gerando todos os caminhos simples no Grafo da origem ao destino
		rotas = nx.all_simple_paths(self.grafo, self.origem, self.destino, cutoff=None)
		limpar_tela()		
		print '\n________________________________ GPS ________________________________'
		print '                                                                     '
		print '                           Sistema de GPS                            '
		print '_____________________________________________________________________'

    	# Obter atributos de nó do gráfico com o parametro "nx.get_node_attributes"			
		print u'\nCalculando rota de [%s]%s até [%s]%s:' % (str(self.origem), nx.get_node_attributes(self.grafo,'label')[self.origem], str(self.destino), nx.get_node_attributes(self.grafo,'label')[self.destino])
		
		# Contar numero de rotas
		conta_rota = 1
		
		# Exibindo rotas no terminal
		for rota in rotas:
			print '\nRota número %s:' % (str(conta_rota))
			conta_rota += 1
			caminho = ''
			cidade_anterior = False
			for cidade in rota:
				if caminho:
					caminho += ' - '
					if cidade_anterior:
						try:
							# Obter atributos de borda do gráfico com o parametro "nx.get_edge_attributes"
							caminho += nx.get_edge_attributes(self.grafo,'label')[cidade_anterior, cidade]
						except:
							caminho += nx.get_edge_attributes(self.grafo,'label')[cidade, cidade_anterior]
					caminho += ' --> '
				caminho += nx.get_node_attributes(self.grafo,'label')[cidade]
				cidade_anterior = cidade
			print caminho