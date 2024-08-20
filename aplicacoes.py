import os
import os.path
import re
from tkinter import filedialog
import leitor_txt




lista_de_vendedoras_taubate = 'Diana','Debora', 'Bruna', 'Free'
lista_de_modos_de_pagamento = 'dinheiro', 'pix', 'credito a vista', 'credito parcelado', 'debito a vista', 'link'
meses_do_ano = 'jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez'
lista_de_saidas = 'Pedidos', 'Aluguel', 'Pro labore', 'Vale Transporte', 'Funcionarios', 'Limpeza da Vitrine', 'Custo lojas (papelaria,agua,cafe)', 'Despesas Comerciais', 'Despesas Administrativas', 'Contabilidade', 'Medicina do Trabalho', 'Gcom', 'Sindicato', 'FGTS', 'Simples Nacional', 'Lanche domingo funcionaria', 'Internet'

def verificar_vendedora(vendedora):
    if vendedora in lista_de_vendedoras_taubate:
        return True
def verificar_data(data):
    dia = str(data[0]+data[1])
    mes = data[3]+data[4]+data[5]
    if data[2] == '/':
        if mes in meses_do_ano:
            if dia.isdigit() == True:
                return True
            else:
                print('Data Incorreta')
def verificar_mes (mes):
    if mes in meses_do_ano:
        return True
def verificar_modo_de_pagamento(modo_de_pagamento):
    if modo_de_pagamento in lista_de_modos_de_pagamento:
        return True
    else:
        print('modo de pagamento inválido')


def valor_apenas_numero(valor):
    if not isinstance(valor,float):
        valor = re.sub('[^0-9]','',valor)
        if valor == '':
            valor = 0
        valor = float(valor)/100
    return valor
def imprimir_lista(lista):
    if lista == []:
        print('Lista Vazia')
    else:
        print('\n')
        print(f"{'Vendedora'.ljust(10)}|{'Valor'.ljust(15)}|{'Cod. Pag.'.ljust(10)}|{'Boleta'.ljust(10)}|{'PA'.ljust(5)}|{'Data'.ljust(10)}|{'Mod. Pag.'.ljust(20)}|{'Bandeira'.ljust(10)}|{'Parcelas'.ljust(10)}|Obs") 
        for i in lista:
            print(f"{i[0].ljust(10)}|{i[1].ljust(15)}|{i[2].ljust(10)}|{i[3].ljust(10)}|{i[4].ljust(5)}|{i[5].ljust(10)}|{i[6].ljust(20)}|{i[7].ljust(10)}|{i[8].ljust(10)}|{i[9]}") 

        

def filtrar_vendas_por_vendedora(lista,vendedora):
    lista_filtrada_vendedora = []
    for venda in lista:
        if venda[0] == vendedora:
            lista_filtrada_vendedora.append(venda)
    return lista_filtrada_vendedora

def filtrar_vendas_por_data(lista,data):
    if verificar_data(data):
        lista_filtrada_data = []
        for venda in lista:
            if venda[5] == data:
                lista_filtrada_data.append(venda)
        return lista_filtrada_data
    else:
        print('Data inválida. Verfique o formato (dd/mmm) ex: 01/jun')
def filtrar_vendas_por_mes(lista,mes):
    if verificar_mes(mes):
        lista_filtrada_mes = []
        for venda in lista:
            if venda[5][3]+venda[5][4]+venda[5][5] == mes:
                lista_filtrada_mes.append(venda)
        return lista_filtrada_mes
    else:
        print('Mês não encontrado. Verifique o formato da abreviação ex: jan, fev')
def filtrar_vendas_por_data_e_vendedora(lista,data,vendedora):
    lista_filtrada_vendedora_e_data = []
    for venda in lista:
        if venda[0] == vendedora and venda[5] == data:
            lista_filtrada_vendedora_e_data.append(venda)
    return lista_filtrada_vendedora_e_data


def total_vendas_pelos_modos(lista):
    dinheiro = 0
    credito_parcelado = 0
    credito_a_vista = 0
    debito = 0
    pix = 0
    link = 0
    total = 0
    for venda in lista:
        if not venda == []:
            venda[1] = valor_apenas_numero(venda[1])
            total += venda[1]
            if venda[6] == lista_de_modos_de_pagamento[0]:
                dinheiro += venda[1]
            elif venda[6] == lista_de_modos_de_pagamento[1]:
                pix += venda[1]
            elif venda[6] == lista_de_modos_de_pagamento[2]:
                credito_a_vista += venda[1]
            elif venda[6] == lista_de_modos_de_pagamento[3]:
                credito_parcelado += venda[1]
            elif venda[6] == lista_de_modos_de_pagamento[4]:
                debito += venda[1]
            elif venda[6] == lista_de_modos_de_pagamento[5]:
                link += venda[1]
    print(f"Dinheiro: R$ {dinheiro:.2f}\nPix: R$ {pix:.2f}\nCrédito à vista: R$ {credito_a_vista:.2f}\nCrédito parcelado: R$ {credito_parcelado:.2f}\nDébito à vista: R$ {debito:.2f}\nLink: R$ {link:.2f}\nTotal: R$ {total:.2f}")

def total_vendas_por_modo(lista,modo):
    soma = 0
    venda = []
    for venda in lista:
        venda[1] = valor_apenas_numero(venda[1])
        if venda[6] == modo:
            soma += venda[1]
    return soma

def total_de_vendas_da_lista(lista):
    total = 0
    for venda in lista:
        if not venda == []:
            venda[1] = valor_apenas_numero(venda[1])
            total += venda[1]
    return total


def total_vendas_todos_vendedores(lista):
    total_geral = 0
    total = 0
    for vendedor in lista_de_vendedoras_taubate:
        total_geral += total
        total=0
        for venda in lista:
            if venda[0] == vendedor:
                venda[1] = valor_apenas_numero(venda[1])
                total+=venda[1]
        print(f"{vendedor}: R$ {total:.2f}")
    print(f"Total: R$ {total_geral:.2f}")        

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




#########################BOLETAS##########################
def digitar_boletas(data,vendedora):
    lista=[]
    continuar = True
    while continuar:
        os.system('cls')
        print('Data: ',data)
        print('Vendedora: ',vendedora)
        valor = input('Valor :R$ ')
        if valor == '':
            valor = '0'
        valor = 'R$ '+valor
        if ',' not in valor:
            valor = valor+','
        padrao = r",\d{2}$"
        while True: 
            verificacao_valor = re.search(padrao,valor)
            if verificacao_valor:
                break
            else:
                valor = valor+'0'
        cod_pag = input('Cod de Pagamento: ')
        boleta = input('Boleta: ')
        pa = input('PA: ')
        try:
            mod_pag = input(''' 
1 - dinheiro
2 - pix
3 - crédito à vista
4 - crédito parcelado
5 - débito à vista
6 - link
Mod de Pagamento: ''')
            mod_pag = int(mod_pag)-1
            mod_pag = lista_de_modos_de_pagamento[mod_pag]
        except:
            print('Valor incorreto')    
        if mod_pag == lista_de_modos_de_pagamento [2] or mod_pag == lista_de_modos_de_pagamento [4]:
            bandeira = input('Bandeira: ')
            parcelas = ''
        elif mod_pag == lista_de_modos_de_pagamento [3] or mod_pag == lista_de_modos_de_pagamento [5]:
            bandeira = input('Bandeira: ')
            parcelas = input('Parcelas: ')
        else:
            bandeira = ''
            parcelas = ''
        bandeira = bandeira.lower()
        obs = input('Obs: ')
        lista_temp = []
        lista_temp.append(vendedora)
        lista_temp.append(valor)
        lista_temp.append(cod_pag)
        lista_temp.append(boleta)
        lista_temp.append(pa)
        lista_temp.append(data)
        lista_temp.append(mod_pag)
        lista_temp.append(bandeira)
        lista_temp.append(parcelas)
        lista_temp.append(obs)
        lista_temp2 = lista_temp.copy()
        print(lista_temp2)
        confirmar = input('Os dados estão corretos s/n? ')
        if confirmar == 's':
            lista.append(lista_temp2)
        else: 
            input('Dados descartados')
        
        if input('Para encerrar insira 0: ') == '0':
            continuar = False
            return lista
        imprimir_lista(lista)
        input()



def TreeView(frame,lista):
    listaCli = ttk.Treeview(frame, height=6, columns=("col1","col2","col3","col4","col5","col6","col7"))
    listaCli.heading("#0", text="")
    listaCli.heading("#1", text="Vendedora")
    listaCli.heading("#2", text="Valor")
    listaCli.heading("#3", text="Cod Pag")
    listaCli.heading("#4", text="Boleta")
    listaCli.heading("#5", text="PA")
    listaCli.heading("#6", text="Data")
    listaCli.column("#0", width=10)
    listaCli.column("#1", width=90)
    listaCli.column("#2", width=90)
    listaCli.column("#3", width=90)
    listaCli.column("#4", width=90)
    listaCli.column("#5", width=50)
    listaCli.place(relx=0.01, rely=0.025, relwidth=0.95, relheight=0.95)
    scroolListay = Scrollbar(frame, orient='vertical')
    listaCli.configure(yscroll=scroolListay.set)
    scroolListay.place(relx=0.96, rely=0.025, relwidth=0.04, relheight=0.95)
    scroolListax = Scrollbar(frame, orient='horizontal')
   
    listaCli.configure(xscroll=scroolListax.set)
    scroolListax.place(relx=0.025, rely=0.96, relwidth=0.95, relheight=0.04)

        
    listaCli.delete(*listaCli.get_children())
    for (valor) in lista:
        listaCli.insert("", "end", values=(valor[0],valor[1],valor[2],valor[3],valor[4],valor[5]))
        print('valor ', valor )


