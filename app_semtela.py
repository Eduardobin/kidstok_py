import os
import os.path
import leitor_txt
import aplicacoes
import menu_simples
lista_bruta = []
lista_filtrada = []



while True:

    try:
        os.system('cls')
        op = menu_simples.menu_principal()
        if op == 1:
            lista_bruta = leitor_txt.Ler_txt()
            lista_filtrada = lista_bruta.copy()
            input('Lista carregada com sucesso! ')
        elif op == 2:
            vendedora = input('Insira o nome da vendedora: ')
            vendedora = vendedora.capitalize()
            if aplicacoes.verificar_vendedora(vendedora) == True:
                lista_filtrada = aplicacoes.filtrar_vendas_por_vendedora(lista_filtrada,vendedora)
                input('Lista Filtrada com sucesso! ')
            else:
                input('Nome do vendedor não encontrado.')
        elif op == 3:
            data = input('Insira a data: ')
            data = data.lower()
            lista_filtrada = aplicacoes.filtrar_vendas_por_data(lista_filtrada,data)
            input('Lista Filtrada com sucesso! ')

        elif op == 4:
            mes = input('Insira o mês')
            mes = mes.lower()
            lista_filtrada = aplicacoes.filtrar_vendas_por_mes(lista_filtrada,mes)
            input('Lista Filtrada com sucesso! ')
        elif op == 5:
            aplicacoes.imprimir_lista(lista_filtrada)
            input('Precione Enter para continuar')
        elif op == 6:
            aplicacoes.total_vendas_pelos_modos(lista_filtrada)
            input('Precione Enter para continuar')
        elif op == 7:
            lista_filtrada = lista_bruta
        elif op == 8:
            aplicacoes.total_vendas_todos_vendedores(lista_filtrada)
            input('Precione Enter para continuar')
        elif op == 9:
            lista_bruta = menu_simples.menu_boletas()
            lista_filtrada = lista_bruta.copy()
        elif op == 10:
            if lista_bruta == '':
                input('Lista Vazia!')
            else:
                leitor_txt.Salvar_txt(lista_bruta)
                input('Lista salva com sucesso!')
        elif op == 11:
            if lista_filtrada == '':
                input('Lista Vazia! ')
            else:
                leitor_txt.Salvar_txt(lista_filtrada)
                input('Lista salva com sucesso!')
        elif op ==12:
            mes = input('Insira o mês')
            mes = mes.lower()
            if aplicacoes.verificar_mes(mes):
                aplicacoes.fluxo_de_caixa(lista_bruta,mes)
                input('Fluxo de caixa salvo com sucesso!')
            else:
                input('Mês não encontrado')




        

            
    except:
        input('\nTente novamente. Aperte enter para continuar.')