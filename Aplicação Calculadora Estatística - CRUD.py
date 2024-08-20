#import matplotlib.pyplot as plt
from math import log
from tkinter import *
from tkinter import ttk
import os
import os.path
import re
from tkinter import filedialog
# Variáveis Globais
cod_entry = ""
desc_entry = ""
valor_entry = ""
lista=[]
local=""
#Entrada de dados!!
    #Entrada TXT
#Import para teste
# lista = [[1,"mercado",1000],[2,"agua, luz e net",500],[3,"aluguel",1500],[4,"lazer",600],[5,"cartão de crédito",1200]]
#lista = [[1,'',100],[2,'',101],[3,'',100],[4,'',99],[5,'',95],[6,'',90],[7,'',99],[8,'',99],[9,'',96],[10,'',98],[11,'',102],[12,'',124],[13,'',112],[14,'',106],[15,'',108],[16,'',91],[17,'',90],[18,'',90],[19,'',96],[20,'',93],[21,'',102],[22,'',98],[23,'',103],[24,'',103],[25,'',93],[26,'',93],[27,'',92]]
#Processamento Pareto [cod,str,num]
def pareto():
    global lista
    print(lista)
    listord=[]
    L=len(lista)
    v=True
    m=0
    while L!=0:
        y = lista[m]
        for i in lista:
            if y[2]<i[2]: 
                y=i
        for i in lista:
            if y[2]>=i[2]:
                v=True
            else:
                v=False
                m+=1    
        if v == True:        
            lista.remove(y)
            listord.append(y)
            m=0
        L=len(lista)
    print('lista ordenada = ', listord)
    lista = listord
    lr=[]
    lr2=[]
    soma=0
    p=0
    legenda = []
    for i in lista:
        legenda.append(i[1])
    for i in lista:
        soma=soma+i[2]
    for i in lista:
        r=(i[2]/soma)*100
        lr.append(r)
        p+=1
    print(lr)
    r=0
    for i in lr:
       r+=i
       lr2.append(r) 
    print(lr2)
    print (legenda)
    plt.title("Análise de Pareto")
    plt.xlabel("Descrição")
    plt.ylabel("Percentual")
    plt.bar(legenda,lr)
    plt.plot(lr2)
    plt.show()





#Medidas e tabelas de distribuição de frequência [cod,str,num]
def dist_freq():
    global lista
    newlista=[]
    for v in lista:
        newlista.append(v[2])
    newlista.sort()
    tamanho = len(newlista)
    media = sum(newlista)/len(newlista)
    maximo = max(newlista)
    minimo = min(newlista)
    amplitude = maximo-minimo
    if tamanho%2 == 0:
        mediana = (newlista[(tamanho//2)-1]+newlista[(tamanho//2)])/2
        quartis1 = (newlista[((tamanho//2)//2)-1]+newlista[((tamanho//2)//2)])/2
        quartis3 = (newlista[(tamanho*3//4)]+newlista[(tamanho*3//4)+1])/2
    else:
        mediana = newlista[(tamanho//2)-1]
        quartis1 = newlista[((tamanho//2)//2)-1]
        quartis3 = newlista[(tamanho*3//4)+1]
    iqr = quartis3-quartis1
    outup = quartis3 + 1.5*iqr
    outdown = quartis1 - 1.5*iqr
    dados_out = []
    for i in newlista:
        if i > outup or i < outdown:
            dados_out.append(i)
    if tamanho<100:
        quant_linhas = round(tamanho**(1/2))
    else:
        quant_linhas = round(1+3.33*log(tamanho))
    tamanho_classe = round(amplitude/quant_linhas)
#moda autoral
    moda=[]
    x=0
    y=0
    for i in newlista:
        x=newlista.count(i)
        if x > y:
            moda=[]
            y=x
            moda.append(i)
        elif x == y:
            if i not in moda:
                moda.append(i)
    #motando gráfico
    #agrupamentos
    numSemRepticao =[]
    for i in newlista:
        if i not in numSemRepticao:
            numSemRepticao.append(i)
    print ("lista sem repetiçaõ" , numSemRepticao)
    i=[]
    x=[]
    y=[]
    c=1
    cc=0
    m=1
    i.append(minimo)
    i.append("---")
    i.append(minimo+tamanho_classe)
    x.append(i)
    for a in newlista:
        if a >= i[0] and a <= i[2]:
            cc+=1
    y.append(cc)
    while c<quant_linhas:
        i=[]
        cc=0
        i.append(minimo+m*tamanho_classe+1)
        i.append("---")
        i.append(minimo+(m+1)*tamanho_classe)
        x.append(i)
        for a in newlista:
            if a>=i[0] and a<=i[2]:
                cc+=1
        y.append(cc)
        c+=1
        m+=1
    x2=[]
    for i in x:
        a=str(i[0])+str(i[1])+str(i[2])
        x2.append(a)
    y2=[]
    for i in y:
        a=round((i/tamanho)*100,2)
        y2.append(a)    
    plt.bar(x2,y2)
    plt.title("Histograma")
    plt.xlabel("Descrição")
    plt.ylabel("Percentual")
    plt.show()
    print('lista ordenada: ',newlista)
    print("Tamanho da Lista= ",tamanho)
    print("Média= ",media)
    print("Máximo= ",maximo)
    print("Mínimo= ",minimo)
    print("Amplitude= ",amplitude)
    print("1º Quartil= ",quartis1)
    print("Mediana= ",mediana)
    print("3º Quartil= ",quartis3)
    print('dados fora: ',dados_out)
    print("Moda= ",moda)
    print(f"Quantidade de Linhas= {quant_linhas}")
    print(f"Tamanho da classe= {tamanho_classe}")





def iniciar():
    global lista
    global cod_entry 
    global desc_entry 
    global valor_entry
    global local
    def atualizar():
        listaCli.delete(*listaCli.get_children())
        for (i,d,v) in lista:
            listaCli.insert("", "end", values=(i,d,v))
    def txt():
        global lista
        global local
        local = 'txt'
        arquivo = filedialog.askopenfilename(filetypes=[("Arquivo de Texto", "*.txt")])
        with open(arquivo,'r') as txtbd:
            L1 = []
            L2 = []
            L3 = []
            y = '*'
            for i in txtbd:
                L1.append(i.rstrip())
            for i in L1:
                i = i.split(";")
                L2 = i
                L3.append(L2)
                print('tamanho',len(L2))
                print('l3: ',L3)
            if len(L2)==3:
                L2=[]
                for i in L3:
                    L1=[]
                    L1.append(int(i[0]))
                    if y in i[1]:
                        i[1] = ""
                    L1.append(i[1])
                    L1.append(int(i[2]))
                    L2.append(L1)
                lista = L2
                print('lista: ',lista)
            else:
                cont=1
                L2=[]
                for i in L3:
                    for m in i:
                        L2=[]
                        print('xxx: ',m)
                        L2.append(cont) 
                        L2.append('')
                        L2.append(int(m))
                        cont+=1
                        lista.append(L2)
                print('lista: ',lista)
    #Tela1
    Tela_1 = Tk()
    Tela_1.title("Calculadora Estatística")
    Tela_1.configure(background='#1e3743')
    Tela_1.geometry("700x600")
    Tela_1.resizable(True,True)
    Tela_1.maxsize(width=840, height=720)
    Tela_1.minsize(width=583 , height=500)
    #Frame Tela 1
    frame_1 = Frame(Tela_1, bd=4, bg='#dfe3ee', highlightbackground= '#759fe6', highlightthickness=2)
    frame_1.place(relx=0.025, rely=0.225, relwidth=0.7, relheight=0.5)
    #Widgets
    bt_txt = Button(Tela_1, text='TXT', command=txt)
    bt_txt.place(relx=0.025, rely=0.125,relwidth=0.1,relheight=0.05)
    bt_sql = Button(Tela_1, text='SQL')
    bt_sql.place(relx=0.125, rely=0.125,relwidth=0.1,relheight=0.05)
    bt_manual = Button(Tela_1, text='Manual', command=insert_manual)
    bt_manual.place(relx=0.225, rely=0.125,relwidth=0.1,relheight=0.05)
    bt_incluir = Button(Tela_1, text='Atualizar', command=atualizar)
    bt_incluir.place(relx=0.025, rely=0.775,relwidth=0.1,relheight=0.05)
    bt_pareto = Button(Tela_1, text='Pareto',command=pareto)
    bt_pareto.place(relx=0.775, rely=0.45,relwidth=0.15,relheight=0.125)
    bt_medidas = Button(Tela_1, text='Medidas',command=dist_freq)
    bt_medidas.place(relx=0.775, rely=0.6,relwidth=0.15,relheight=0.125)
    #TreeView
    listaCli = ttk.Treeview(frame_1, height=3, columns=("col1","col2","col3"))
    listaCli.heading("#0", text="#")
    listaCli.heading("#1", text="Descrição")
    listaCli.heading("#2", text="Valor")
    listaCli.column("#0", width=10)
    listaCli.column("#1", width=90)
    listaCli.column("#2", width=50)
    listaCli.place(relx=0.01, rely=0.025, relwidth=0.95, relheight=0.95)
    scroolLista = Scrollbar(frame_1, orient='vertical')
    listaCli.configure(yscroll=scroolLista.set)
    scroolLista.place(relx=0.96, rely=0.025, relwidth=0.04, relheight=0.95)
    Tela_1.mainloop()

def tela_pareto():
    telaPareto=Tk()
    telaPareto.title("Calculadora Estatística")
    telaPareto.configure(background='#1e3743')
    telaPareto.geometry("700x600")
    telaPareto.resizable(True,True)
    telaPareto.maxsize(width=840, height=720)
    telaPareto.minsize(width=583 , height=500)
    
def insert_manual():
    #Variáveis
    global lista
    global cod_entry 
    global desc_entry 
    global valor_entry
    def add():
        global lista
        global desc_entry 
        global valor_entry 
        l=[]
        lista_tree=[]
        cod=len(lista)+1
        desc=desc_entry.get()
        valor=int(valor_entry.get())
        l.append(cod)
        l.append(desc)
        l.append(valor)
        lista.append(l)
        lista_tree.append(l)
        print(lista)
        print(l)
        for (i,d,v) in lista_tree:
            listaCli_2.insert("", "end", values=(i,d,v))
        cod_entry.delete(0,"end")
        desc_entry.delete(0,"end")
        valor_entry.delete(0,"end")
    def alterar():
        global lista
        global cod_entry
        global desc_entry 
        global valor_entry
        l=[]
        cod=int(cod_entry.get())
        cod-=1
        desc=desc_entry.get()
        valor=int(valor_entry.get())
        l.append(cod+1)
        l.append(desc)
        l.append(valor)
        lista[cod]=l
        print(lista)
        listaCli_2.delete(*listaCli_2.get_children())
        for (i,d,v) in lista:
            listaCli_2.insert("", "end", values=(i,d,v))
        cod_entry.delete(0,"end")
        desc_entry.delete(0,"end")
        valor_entry.delete(0,"end")
    def apagar():
        global lista
        lista=[]
        listaCli_2.delete(*listaCli_2.get_children())
    #Tela2
    Tela_2 = Tk()
    Tela_2.title("Inserir Dados Manual")
    Tela_2.configure(background='#1e3743')
    Tela_2.geometry("400x400")
    Tela_2.resizable(True,True)
    Tela_2.maxsize(width=480, height=480)
    Tela_2.minsize(width=333 , height=333)
    #Widgets
    bt_salvar = Button(Tela_2, text='Apagar',command=apagar)
    bt_salvar.place(relx=0.025, rely=0.875,relwidth=0.2,relheight=0.1)
    bt_sair = Button(Tela_2, text='Sair', command=Tela_2.destroy)
    bt_sair.place(relx=0.775, rely=0.875,relwidth=0.2,relheight=0.1)
    bt_add = Button(Tela_2, text='Adicionar', command=add)
    bt_add.place(relx=0.75, rely=0.55,relwidth=0.2,relheight=0.1)
    bt_alterar = Button(Tela_2, text='Alterar', command=alterar)
    bt_alterar.place(relx=0.75, rely=0.65,relwidth=0.2,relheight=0.1)
    ##Frame TreeView
    frame_2 = Frame(Tela_2, bd=4, bg='#dfe3ee', highlightbackground= '#759fe6', highlightthickness=2)
    frame_2.place(relx=0.025, rely=0.225, relwidth=0.7, relheight=0.5)
    listaCli_2 = ttk.Treeview(frame_2, height=3, columns=("col1","col2","col3"), show="headings")
    listaCli_2.heading("#0", text="#")
    listaCli_2.heading("#1", text="Descrição")
    listaCli_2.heading("#2", text="Valor")
    listaCli_2.column("#0", width=20)
    listaCli_2.column("#1", width=80)
    listaCli_2.column("#2", width=50)
    listaCli_2.place(relx=0.01, rely=0.025, relwidth=0.95, relheight=0.95)
    scroolLista = Scrollbar(frame_2, orient='vertical')
    listaCli_2.configure(yscroll=scroolLista.set)
    scroolLista.place(relx=0.96, rely=0.025, relwidth=0.04, relheight=0.95)
    ## Criação da label e entrada #
    lb_cod = Label(Tela_2, text = "#",bg='#1e3743',fg='white')
    lb_cod.place(relx= 0.75, rely= 0.2 )
    cod_entry = Entry(Tela_2)
    cod_entry.place(relx= 0.75, rely= 0.25, relwidth= 0.2)
    ## Criação da label e entrada descrição
    lb_desc = Label(Tela_2, text = "Descrição", bg='#1e3743', fg='white')
    lb_desc.place(relx= 0.75, rely= 0.3 )
    desc_entry = Entry(Tela_2)
    desc_entry.place(relx= 0.75, rely= 0.35, relwidth= 0.2)
    ## Criação da label e entrada valor
    lb_valor = Label(Tela_2, text = "Valor", bg='#1e3743', fg='white')
    lb_valor.place(relx= 0.75, rely= 0.4 )
    valor_entry = Entry(Tela_2)
    valor_entry.place(relx= 0.75, rely= 0.45, relwidth= 0.2)
    #Escrever lista 
    for (i,d,v) in lista:
        listaCli_2.insert("", "end", values=(i,d,v))
    Tela_2.mainloop()
iniciar()    

    
        









