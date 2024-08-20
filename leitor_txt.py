from tkinter import filedialog

def Ler_txt():
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
    return L3
def Salvar_txt(lista,arquivo):
    arquivo = filedialog.askopenfilename(filetypes=[("Arquivo de Texto", "*.txt")])
    with open(arquivo,'w') as txtbd:
        for m in lista:
            for i in m:
                txtbd.write(str(i))
                txtbd.write(';')
            txtbd.write('\n')

def Salvar_automatico(lista,arquivo):
    with open(arquivo,'a') as txtbd:
        for m in lista:
            for i in m:
                txtbd.write(str(i))
                txtbd.write(';')
            txtbd.write('\n')

def Salvar_relatorio_txt(relatorio):
    arquivo = filedialog.askopenfilename(filetypes=[("Arquivo de Texto", "*.txt")])
    with open(arquivo,'w') as txtbd:
        txtbd.write(relatorio)
        

