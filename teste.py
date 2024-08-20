from aplicacoes import filtrar_vendas_por_data, lista_de_modos_de_pagamento,total_vendas_por_modo,total_de_vendas_da_lista
import leitor_txt
import re


lista = leitor_txt.Ler_txt()
mes = 'jun'



def fluxo_de_caixa(lista,mes):
    lista_filtrada = lista
    lista_bruta = lista_filtrada.copy()
    lista_temp = []
    lista_vazia = []
    lista_entradas = []
    lista_dinheiro = []
    lista_debito = []
    lista_credito_vista = []
    lista_credito_parcelado = []
    lista_pix = []
    lista_link = []
    delta = 0
    for dia in range(1,32):
        if dia<10:
            dia = str(dia)
            dia = '0'+dia
        else:
            dia = str(dia)
        data = dia+'/'+mes
        
        lista_filtrada = filtrar_vendas_por_data(lista_filtrada,data)
        

        lista_entradas.append(total_de_vendas_da_lista(lista_filtrada))
        for modo in lista_de_modos_de_pagamento:
            valor = total_vendas_por_modo(lista_filtrada,modo)


            lista_temp.append(valor)
            
        lista_dinheiro.append(lista_temp[0])
        lista_pix.append(lista_temp[1])
        lista_credito_vista.append(lista_temp[2])
        lista_credito_parcelado.append(lista_temp[3])
        lista_debito.append(lista_temp[4])
        lista_link.append(lista_temp[5])
        lista_temp = lista_vazia.copy()
        lista_filtrada = lista_bruta.copy()
    delta = [a-b-c-d-e-f-g for a,b,c,d,e,f,g in zip(lista_entradas,lista_dinheiro,lista_debito, lista_pix, lista_credito_vista, lista_credito_parcelado, lista_link)]

    
    
    cont = 0
    for i in lista_entradas:
        i="{:.2f}".format(i)
        i=str(i)
        i='R$ '+i
        lista_entradas[cont] = i
        cont+=1
    cont = 0
    for i in lista_dinheiro:
        i="{:.2f}".format(i)
        i=str(i)
        i='R$ '+i
        lista_dinheiro[cont] = i
        cont+=1
    cont = 0

    for i in lista_pix:
        i="{:.2f}".format(i)
        i=str(i)
        i='R$ '+i
        lista_pix[cont] = i
        cont+=1
    cont = 0

    for i in lista_credito_vista:
        i="{:.2f}".format(i)
        i=str(i)
        i='R$ '+i
        lista_credito_vista[cont] = i
        cont+=1
    cont = 0

    for i in lista_credito_parcelado:
        i="{:.2f}".format(i)
        i=str(i)
        i='R$ '+i
        lista_credito_parcelado[cont] = i
        cont+=1
    cont = 0

    for i in lista_debito:
        i="{:.2f}".format(i)
        i=str(i)
        i='R$ '+i
        lista_debito[cont] = i
        cont+=1
    cont = 0

    for i in lista_link:
        i="{:.2f}".format(i)
        i=str(i)
        i='R$ '+i
        lista_link[cont] = i
        cont+=1
    cont = 0

    for i in delta:
        i="{:.2f}".format(i)
        i=str(i)
        i='R$ '+i
        delta[cont] = i
        cont+=1


    print(lista_entradas[10])
    print(f'{lista_dinheiro[10]},{lista_credito_vista[10]},{lista_credito_parcelado[10]},{lista_link[10]},{lista_pix[10]},{lista_debito[10]}')
    print(delta[10])


    relatório = f'''                                        FLUXO DE CAIXA TAUBATÉ
Mês referência: {mes}

{''.ljust(25)} | {'1'.ljust(15)} | {'2'.ljust(15)} | {'3'.ljust(15)} | {'4'.ljust(15)} | {'5'.ljust(15)} | {'6'.ljust(15)} | {'7'.ljust(15)} | {'8'.ljust(15)} | {'9'.ljust(15)} | {'10'.ljust(15)} | {'11'.ljust(15)} | {'12'.ljust(15)} | {'13'.ljust(15)} | {'14'.ljust(15)} | {'15'.ljust(15)} | {'16'.ljust(15)} | {'17'.ljust(15)} | {'18'.ljust(15)} | {'19'.ljust(15)} | {'20'.ljust(15)} | {'21'.ljust(15)} | {'22'.ljust(15)} | {'23'.ljust(15)} | {'24'.ljust(15)} | {'25'.ljust(15)} | {'26'.ljust(15)} | {'27'.ljust(15)} | {'28'.ljust(15)} | {'29'.ljust(15)} | {'30'.ljust(15)} | {'31'.ljust(15)} 
{'Entradas'.ljust(25)} | {lista_entradas[0].ljust(15)} | {lista_entradas[1].ljust(15)} | {lista_entradas[2].ljust(15)} | {lista_entradas[3].ljust(15)} | {lista_entradas[4].ljust(15)} | {lista_entradas[5].ljust(15)} | {lista_entradas[6].ljust(15)} | {lista_entradas[7].ljust(15)} | {lista_entradas[8].ljust(15)} | {lista_entradas[9].ljust(15)} | {lista_entradas[10].ljust(15)} | {lista_entradas[11].ljust(15)} | {lista_entradas[12].ljust(15)} | {lista_entradas[13].ljust(15)} | {lista_entradas[14].ljust(15)} | {lista_entradas[15].ljust(15)} | {lista_entradas[16].ljust(15)} | {lista_entradas[17].ljust(15)} | {lista_entradas[18].ljust(15)} | {lista_entradas[19].ljust(15)} | {lista_entradas[20].ljust(15)} | {lista_entradas[21].ljust(15)} | {lista_entradas[22].ljust(15)} | {lista_entradas[23].ljust(15)} | {lista_entradas[24].ljust(15)} | {lista_entradas[25].ljust(15)} | {lista_entradas[26].ljust(15)} | {lista_entradas[27].ljust(15)} | {lista_entradas[28].ljust(15)} | {lista_entradas[29].ljust(15)} | {lista_entradas[30].ljust(15)} 
{lista_de_modos_de_pagamento[0].ljust(25)} | {lista_dinheiro[0].ljust(15)} | {lista_dinheiro[1].ljust(15)} | {lista_dinheiro[2].ljust(15)} | {lista_dinheiro[3].ljust(15)} | {lista_dinheiro[4].ljust(15)} | {lista_dinheiro[5].ljust(15)} | {lista_dinheiro[6].ljust(15)} | {lista_dinheiro[7].ljust(15)} | {lista_dinheiro[8].ljust(15)} | {lista_dinheiro[9].ljust(15)} | {lista_dinheiro[10].ljust(15)} | {lista_dinheiro[11].ljust(15)} | {lista_dinheiro[12].ljust(15)} | {lista_dinheiro[13].ljust(15)} | {lista_dinheiro[14].ljust(15)} | {lista_dinheiro[15].ljust(15)} | {lista_dinheiro[16].ljust(15)} | {lista_dinheiro[17].ljust(15)} | {lista_dinheiro[18].ljust(15)} | {lista_dinheiro[19].ljust(15)} | {lista_dinheiro[20].ljust(15)} | {lista_dinheiro[21].ljust(15)} | {lista_dinheiro[22].ljust(15)} | {lista_dinheiro[23].ljust(15)} | {lista_dinheiro[24].ljust(15)} | {lista_dinheiro[25].ljust(15)} | {lista_dinheiro[26].ljust(15)} | {lista_dinheiro[27].ljust(15)} | {lista_dinheiro[28].ljust(15)} | {lista_dinheiro[29].ljust(15)} | {lista_dinheiro[30].ljust(15)} 
{lista_de_modos_de_pagamento[1].ljust(25)} | {lista_pix[0].ljust(15)} | {lista_pix[1].ljust(15)} | {lista_pix[2].ljust(15)} | {lista_pix[3].ljust(15)} | {lista_pix[4].ljust(15)} | {lista_pix[5].ljust(15)} | {lista_pix[6].ljust(15)} | {lista_pix[7].ljust(15)} | {lista_pix[8].ljust(15)} | {lista_pix[9].ljust(15)} | {lista_pix[10].ljust(15)} | {lista_pix[11].ljust(15)} | {lista_pix[12].ljust(15)} | {lista_pix[13].ljust(15)} | {lista_pix[14].ljust(15)} | {lista_pix[15].ljust(15)} | {lista_pix[16].ljust(15)} | {lista_pix[17].ljust(15)} | {lista_pix[18].ljust(15)} | {lista_pix[19].ljust(15)} | {lista_pix[20].ljust(15)} | {lista_pix[21].ljust(15)} | {lista_pix[22].ljust(15)} | {lista_pix[23].ljust(15)} | {lista_pix[24].ljust(15)} | {lista_pix[25].ljust(15)} | {lista_pix[26].ljust(15)} | {lista_pix[27].ljust(15)} | {lista_pix[28].ljust(15)} | {lista_pix[29].ljust(15)} | {lista_pix[30].ljust(15)} 
{lista_de_modos_de_pagamento[2].ljust(25)} | {lista_credito_vista[0].ljust(15)} | {lista_credito_vista[1].ljust(15)} | {lista_credito_vista[2].ljust(15)} | {lista_credito_vista[3].ljust(15)} | {lista_credito_vista[4].ljust(15)} | {lista_credito_vista[5].ljust(15)} | {lista_credito_vista[6].ljust(15)} | {lista_credito_vista[7].ljust(15)} | {lista_credito_vista[8].ljust(15)} | {lista_credito_vista[9].ljust(15)} | {lista_credito_vista[10].ljust(15)} | {lista_credito_vista[11].ljust(15)} | {lista_credito_vista[12].ljust(15)} | {lista_credito_vista[13].ljust(15)} | {lista_credito_vista[14].ljust(15)} | {lista_credito_vista[15].ljust(15)} | {lista_credito_vista[16].ljust(15)} | {lista_credito_vista[17].ljust(15)} | {lista_credito_vista[18].ljust(15)} | {lista_credito_vista[19].ljust(15)} | {lista_credito_vista[20].ljust(15)} | {lista_credito_vista[21].ljust(15)} | {lista_credito_vista[22].ljust(15)} | {lista_credito_vista[23].ljust(15)} | {lista_credito_vista[24].ljust(15)} | {lista_credito_vista[25].ljust(15)} | {lista_credito_vista[26].ljust(15)} | {lista_credito_vista[27].ljust(15)} | {lista_credito_vista[28].ljust(15)} | {lista_credito_vista[29].ljust(15)} | {lista_credito_vista[30].ljust(15)} 
{lista_de_modos_de_pagamento[3].ljust(25)} | {lista_credito_parcelado[0].ljust(15)} | {lista_credito_parcelado[1].ljust(15)} | {lista_credito_parcelado[2].ljust(15)} | {lista_credito_parcelado[3].ljust(15)} | {lista_credito_parcelado[4].ljust(15)} | {lista_credito_parcelado[5].ljust(15)} | {lista_credito_parcelado[6].ljust(15)} | {lista_credito_parcelado[7].ljust(15)} | {lista_credito_parcelado[8].ljust(15)} | {lista_credito_parcelado[9].ljust(15)} | {lista_credito_parcelado[10].ljust(15)} | {lista_credito_parcelado[11].ljust(15)} | {lista_credito_parcelado[12].ljust(15)} | {lista_credito_parcelado[13].ljust(15)} | {lista_credito_parcelado[14].ljust(15)} | {lista_credito_parcelado[15].ljust(15)} | {lista_credito_parcelado[16].ljust(15)} | {lista_credito_parcelado[17].ljust(15)} | {lista_credito_parcelado[18].ljust(15)} | {lista_credito_parcelado[19].ljust(15)} | {lista_credito_parcelado[20].ljust(15)} | {lista_credito_parcelado[21].ljust(15)} | {lista_credito_parcelado[22].ljust(15)} | {lista_credito_parcelado[23].ljust(15)} | {lista_credito_parcelado[24].ljust(15)} | {lista_credito_parcelado[25].ljust(15)} | {lista_credito_parcelado[26].ljust(15)} | {lista_credito_parcelado[27].ljust(15)} | {lista_credito_parcelado[28].ljust(15)} | {lista_credito_parcelado[29].ljust(15)} | {lista_credito_parcelado[30].ljust(15)} 
{lista_de_modos_de_pagamento[4].ljust(25)} | {lista_debito[0].ljust(15)} | {lista_debito[1].ljust(15)} | {lista_debito[2].ljust(15)} | {lista_debito[3].ljust(15)} | {lista_debito[4].ljust(15)} | {lista_debito[5].ljust(15)} | {lista_debito[6].ljust(15)} | {lista_debito[7].ljust(15)} | {lista_debito[8].ljust(15)} | {lista_debito[9].ljust(15)} | {lista_debito[10].ljust(15)} | {lista_debito[11].ljust(15)} | {lista_debito[12].ljust(15)} | {lista_debito[13].ljust(15)} | {lista_debito[14].ljust(15)} | {lista_debito[15].ljust(15)} | {lista_debito[16].ljust(15)} | {lista_debito[17].ljust(15)} | {lista_debito[18].ljust(15)} | {lista_debito[19].ljust(15)} | {lista_debito[20].ljust(15)} | {lista_debito[21].ljust(15)} | {lista_debito[22].ljust(15)} | {lista_debito[23].ljust(15)} | {lista_debito[24].ljust(15)} | {lista_debito[25].ljust(15)} | {lista_debito[26].ljust(15)} | {lista_debito[27].ljust(15)} | {lista_debito[28].ljust(15)} | {lista_debito[29].ljust(15)} | {lista_debito[30].ljust(15)} 
{lista_de_modos_de_pagamento[5].ljust(25)} | {lista_link[0].ljust(15)} | {lista_link[1].ljust(15)} | {lista_link[2].ljust(15)} | {lista_link[3].ljust(15)} | {lista_link[4].ljust(15)} | {lista_link[5].ljust(15)} | {lista_link[6].ljust(15)} | {lista_link[7].ljust(15)} | {lista_link[8].ljust(15)} | {lista_link[9].ljust(15)} | {lista_link[10].ljust(15)} | {lista_link[11].ljust(15)} | {lista_link[12].ljust(15)} | {lista_link[13].ljust(15)} | {lista_link[14].ljust(15)} | {lista_link[15].ljust(15)} | {lista_link[16].ljust(15)} | {lista_link[17].ljust(15)} | {lista_link[18].ljust(15)} | {lista_link[19].ljust(15)} | {lista_link[20].ljust(15)} | {lista_link[21].ljust(15)} | {lista_link[22].ljust(15)} | {lista_link[23].ljust(15)} | {lista_link[24].ljust(15)} | {lista_link[25].ljust(15)} | {lista_link[26].ljust(15)} | {lista_link[27].ljust(15)} | {lista_link[28].ljust(15)} | {lista_link[29].ljust(15)} | {lista_link[30].ljust(15)} 
{'Lançamentos incorretos'.ljust(25)} | {delta[0].ljust(15)} | {delta[1].ljust(15)} | {delta[2].ljust(15)} | {delta[3].ljust(15)} | {delta[4].ljust(15)} | {delta[5].ljust(15)} | {delta[6].ljust(15)} | {delta[7].ljust(15)} | {delta[8].ljust(15)} | {delta[9].ljust(15)} | {delta[10].ljust(15)} | {delta[11].ljust(15)} | {delta[12].ljust(15)} | {delta[13].ljust(15)} | {delta[14].ljust(15)} | {delta[15].ljust(15)} | {delta[16].ljust(15)} | {delta[17].ljust(15)} | {delta[18].ljust(15)} | {delta[19].ljust(15)} | {delta[20].ljust(15)} | {delta[21].ljust(15)} | {delta[22].ljust(15)} | {delta[23].ljust(15)} | {delta[24].ljust(15)} | {delta[25].ljust(15)} | {delta[26].ljust(15)} | {delta[27].ljust(15)} | {delta[28].ljust(15)} | {delta[29].ljust(15)} | {delta[30].ljust(15)} 




'''

    leitor_txt.Salvar_relatorio_txt(relatório)
fluxo_de_caixa(lista,mes)