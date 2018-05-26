# -*- coding: utf-8 -*-
import os
def limpar_tela():
    os.system('clear')
limpar_tela()

# Perguntar para o usuário a cidade de origem e a cidade de destino
def mostrar(grafo):
    print '________________________________ GPS ________________________________'
    print '                                                                     '
    print '                         DESTINOS POSSÍVEIS                          '
    print '_____________________________________________________________________\n'

    # Listando as cidades do mapa
    for n,d in grafo.nodes_iter(data=True):
        print '%s - %s' % (n, d['label'])

    # Setando a origem e destino como False para o usuario inserir os valores
    origem, destino = False, False

    while not origem:
        origem = raw_input(u'\nInforme o codigo da cidade de origem: ')

    while not destino:
        destino = raw_input(u'Informe o codigo da cidade de destino: ')

    return origem, destino

    print '____________________________________________________________________'

# Perguntar para o usuário se ele deseja continuar utilizando o sistema
def continuar():
    print '                                                                    '
    print '____________________________________________________________________'
    print '                                                                    '
    print 'Calculo de rotas terminado, continuar no sistema?'
    
    opcao = ''
    
    # Opção (S) para sim e opção (N) para não
    while opcao != 'S' and opcao != 'N':
       opcao = raw_input(u'(S) Sim (N) Nao: ').upper()
    if opcao == 'S':
        return True
        limpar_tela()
    return False