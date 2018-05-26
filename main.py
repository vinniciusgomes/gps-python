# -*- coding: utf-8 -*-
import os
# Chamando o menu
from libs import menu
# Chamando o GPS
from libs.gps import GPS

def limpar_tela():
    # Limpando a tela para iniciar o sistema
    os.system('clear')

def main():
    try:
        gps = GPS()
        # Buscando mapa .GML
        gps.ler_mapa('mapas/mapa.gml')
        origem, destino = menu.mostrar(gps.grafo)
        # Setando local de origem
        gps.setar_origem(origem)
        # Setando local de destino
        gps.setar_destino(destino)
        limpar_tela()
        # Realizando o processo
        gps.processar()
        # Se o usuario quiser continuar limpa a tela e roda o main.py novamente
        if menu.continuar():
            limpar_tela()
            main()
        # Se o usuario quiser sair limpa a tela e fecha o sistema    
        else:
            limpar_tela()
            exit()
    except Exception, e:
        # Se a rota não for possível exibe a mensagem e volta para o main.py
        print 'Rota impossivel de calcular! %s' % e.message
        print '\n'

        main()

main()