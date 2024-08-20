from tkinter import *
from tkinter import ttk
import os
import os.path
import re
from tkinter import filedialog
from leitor_txt import *
from aplicacoes import *
import re

lista=Ler_txt()
lista_vazia=[]
def iniciar():
    def atualizar():
        TreeView(frame_1,lista)

    #Tela1
    Tela_1 = Tk()
    Tela_1.title("KIDSTOK")
    Tela_1.configure(background='#1e3743')
    Tela_1.geometry("1280x800")
    Tela_1.resizable(True,True)
    Tela_1.maxsize(width=1280, height=800)
    Tela_1.minsize(width=1000 , height=500)
    #Frame Tela 1
    frame_1 = Frame(Tela_1, bd=4, bg='#dfe3ee', highlightbackground= '#759fe6', highlightthickness=2)
    frame_1.place(relx=0.025, rely=0.225, relwidth=0.7, relheight=0.5)
    #Widgets
    #bt_txt = Button(Tela_1, text='TXT', command=Ler_txt)
    #bt_txt.place(relx=0.025, rely=0.125,relwidth=0.1,relheight=0.05)
    #bt_sql = Button(Tela_1, text='SQL')
    #bt_sql.place(relx=0.125, rely=0.125,relwidth=0.1,relheight=0.05)
    #bt_manual = Button(Tela_1, text='Manual', command='')
    #bt_manual.place(relx=0.225, rely=0.125,relwidth=0.1,relheight=0.05)
    bt_incluir = Button(Tela_1, text='Atualizar', command=atualizar)
    bt_incluir.place(relx=0.025, rely=0.775,relwidth=0.1,relheight=0.05)
    #bt_pareto = Button(Tela_1, text='Vendedor',command='')
    #bt_pareto.place(relx=0.775, rely=0.45,relwidth=0.15,relheight=0.125)
    bt_addboletas = Button(Tela_1, text='Add Boletas',command=Tela_AddBoleta)
    bt_addboletas.place(relx=0.775, rely=0.6,relwidth=0.15,relheight=0.125)

    TreeView(frame_1,lista)

   
   
    

    
    
    Tela_1.mainloop()

def Tela_AddBoleta():
    lista_temp = []

    
    def add_listatemp():
        L1 = []
        L1.append(vendedora_list.get(vendedora_list.curselection()))
        L1.append('R$ '+valor_entry.get())
        L1.append(cod_entry.get())
        L1.append(boleta_entry.get())
        L1.append(pa_entry.get())
        L1.append(data_entry.get())
        L1.append(modpagamento_list.get(modpagamento_list.curselection()))
        if modpagamento_list.get(modpagamento_list.curselection()) == 'Débito à vista':
            L1.append(bandeira_list.get(bandeira_list.curselection()))
            L1.append('')
        elif modpagamento_list.get(modpagamento_list.curselection()) == 'Crédito à vista':
            L1.append(bandeira_list.get(bandeira_list.curselection()))
            L1.append('')
        elif modpagamento_list.get(modpagamento_list.curselection()) == 'Crédito Parcelado':
            L1.append(bandeira_list.get(bandeira_list.curselection()))
            L1.append(parcela_entry.get())
        else:    
            L1.append('')
            L1.append('')
        L1.append(obs_entry.get())

        lista_temp.append(L1)
        print(lista_temp)
        TreeView(frame_1,lista_temp)
        valor_entry.delete(0, END)
        cod_entry.delete(0, END)
        boleta_entry.delete(0, END)
        parcela_entry.delete(0, END)
        obs_entry.delete(0, END)
        pa_entry.delete(0, END)
    def salvar_listatemp():
        for i in lista_temp:
            lista.append(i)









    Tela_AddBoleta = Tk()
    Tela_AddBoleta.title("KIDSTOK")
    Tela_AddBoleta.configure(background='#1e3743')
    Tela_AddBoleta.geometry("800x500")
    Tela_AddBoleta.resizable(True,True)
    Tela_AddBoleta.maxsize(width=800, height=500)
    Tela_AddBoleta.minsize(width=700 , height=500)
    #Frame Tela 1
    frame_1 = Frame(Tela_AddBoleta, bd=4, bg='#dfe3ee', highlightbackground= '#759fe6', highlightthickness=2)
    frame_1.place(relx=0.025, rely=0.225, relwidth=0.5, relheight=0.5)
    #Widgets
    bt_salvar = Button(Tela_AddBoleta, text='Salvar', command=salvar_listatemp)
    bt_salvar.place(relx=0.025, rely=0.125,relwidth=0.1,relheight=0.05)
    bt_addlista = Button(Tela_AddBoleta, text='Add na lista',command=add_listatemp)
    bt_addlista.place(relx=0.8, rely=0.925,relwidth=0.1,relheight=0.05)
#######################################################################################################################################
  
    #Criação da Label e Lista de Vendedora
    lb_vendedora = Label(Tela_AddBoleta, text = "Vendedora", bg='#1e3743', fg='white')
    lb_vendedora.place(relx= 0.6, rely= 0.2 )
    vendedora_list = Listbox(Tela_AddBoleta, height=6,exportselection=False)
    vendedora_list.place(relx= 0.6, rely=0.25)
    vendedora_list.insert(1,'Diane')
    vendedora_list.insert(2,'Duda')
    vendedora_list.insert(3,'Fernanda')
    vendedora_list.insert(4,'Letícia')
    vendedora_list.insert(5,'Luara')
    vendedora_list.insert(6,'Victória')
  
    ## Criação da label e entrada DATA
    lb_data = Label(Tela_AddBoleta, text = "Data(dd/mmm)",bg='#1e3743',fg='white')
    lb_data.place(relx= 0.85, rely= 0.1)
    data_entry = Entry(Tela_AddBoleta)
    data_entry.place(relx= 0.9, rely= 0.15, relwidth= 0.05)
    
    
    ## Criação da label e entrada CÓDIGO DE PAGAMENTO
    lb_cod = Label(Tela_AddBoleta, text = "Código de Pagamento",bg='#1e3743',fg='white')
    lb_cod.place(relx= 0.8, rely= 0.2)
    cod_entry = Entry(Tela_AddBoleta)
    cod_entry.place(relx= 0.8, rely= 0.25, relwidth= 0.15)
    
    ## Criação da label e entrada BOLETA
    lb_boleta = Label(Tela_AddBoleta, text = "Boleta", bg='#1e3743', fg='white')
    lb_boleta.place(relx= 0.8, rely= 0.3 )
    boleta_entry = Entry(Tela_AddBoleta)
    boleta_entry.place(relx= 0.8, rely= 0.35, relwidth= 0.15)
    
    
    
    #Criação da label e entrada VALOR R$
    lb_valor = Label(Tela_AddBoleta, text = "Valor", bg='#1e3743', fg='white')
    lb_valor.place(relx= 0.8, rely= 0.4 )
    valor_entry = Entry(Tela_AddBoleta)
    valor_entry.place(relx= 0.8, rely= 0.45, relwidth= 0.07)


    #Criação da label e entrada PA
    lb_pa = Label(Tela_AddBoleta, text = "PA", bg='#1e3743', fg='white')
    lb_pa.place(relx= 0.9, rely= 0.4 )
    pa_entry = Entry(Tela_AddBoleta)
    pa_entry.place(relx= 0.9, rely= 0.45, relwidth= 0.05)




    #Criação da Label e Lista de MODO DE PAGAMENTO
    lb_modpagamento = Label(Tela_AddBoleta, text = "Modo de Pagamento", bg='#1e3743', fg='white')
    lb_modpagamento.place(relx= 0.6, rely= 0.5 )
    modpagamento_list = Listbox(Tela_AddBoleta, height=7,exportselection=False)
    modpagamento_list.place(relx= 0.6, rely=0.55)
    modpagamento_list.insert(1,'Dinheiro')
    modpagamento_list.insert(3,'Débito à vista')
    modpagamento_list.insert(4,'Crédito à vista')
    modpagamento_list.insert(5,'Crédito Parcelado')
    modpagamento_list.insert(6,'Link de pagamento')
    modpagamento_list.insert(7,'')

    #Criação da Label e Lista de BANDEIRA
    lb_bandeira = Label(Tela_AddBoleta, text = "Bandeira", bg='#1e3743', fg='white')
    lb_bandeira.place(relx= 0.8, rely= 0.5 )
    bandeira_list = Listbox(Tela_AddBoleta, height=6,exportselection=False)
    bandeira_list.place(relx= 0.8, rely=0.55)
    bandeira_list.insert(1,'Mastercard')
    bandeira_list.insert(2,'Visa')
    bandeira_list.insert(3,'Elo')
    bandeira_list.insert(4,'American express')
    bandeira_list.insert(5,'Alelo')
    bandeira_list.insert(6,'Outros')
    

    #Criação da label e entrada PARCELA
    lb_parcela = Label(Tela_AddBoleta, text = "Parcelas", bg='#1e3743', fg='white')
    lb_parcela.place(relx= 0.6, rely= 0.8 )
    parcela_entry = Entry(Tela_AddBoleta)
    parcela_entry.place(relx= 0.6, rely= 0.85, relwidth= 0.02)

    #Criação da label e entrada OBSERVAÇÃO
    lb_obs = Label(Tela_AddBoleta,text = "Observação", bg='#1e3743', fg='white')
    lb_obs.place(relx=.8, rely=.8)
    obs_entry = Entry(Tela_AddBoleta)
    obs_entry.place(relx= 0.8, rely= 0.85, relwidth= 0.15)


    TreeView(frame_1,lista_temp)

    

    
    
    Tela_AddBoleta.mainloop()


iniciar()
