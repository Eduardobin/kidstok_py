from tkinter import filedialog
import aplicacoes
import leitor_txt
import os
def menu_principal():
    print(10*'x'+' Sistema Kidstok '+10*'x')
    print('\nMenu de opções: \n')
    print('1 - Carregar Banco de dados txt')
    print('2 - Filtrar vendas por vendedor')
    print('3 - Filtrar vendas por data')
    print('4 - Filtrar vendas por mes')
    print('5 - Visualizar vendas filtrado')
    print('6 - Resumo de vendas')
    print('7 - Desfazer filtros')
    print('8 - Resumo de vendas por vendedor')
    print('9 - Registrar Boletas')
    print('10 - Salvar lista bruta txt')
    print('11 - Salvar lista filtrada txt')
    print('12 - Fluxo de Caixa txt')
    op = input('\nInsira o número da opção desejada: ')
    try:
        op = int(op)
    except:
        input('\nInsira o númeor correspondente')
    if op >=1 and op <=12:
        return op
    else: 
        input('\nOpção não encontrada')

def menu_boletas():
    vendedora_temp = ''
    data_temp = ''
    arquivo = filedialog.askopenfilename(filetypes=[("Arquivo de Texto", "*.txt")])

    while True:
        os.system('cls')
        print(10*'x'+' Sistema Kidstok '+10*'x')
        print('\nMenu de opções: \n')
        print(f'''Data: {data_temp}     Vendedora: {vendedora_temp}
1 - Alterar data
2 - Alterar vendedor
3 - Digitar Boletas
4 - Alterar local de salvamento
5 - Juntar arquivos
6 - Voltar''')
        o = int(input('\nInsira o número da opção desejada: '))
        if o == 1:
            while True:
                data_temp = input('Insira a data das boletas: ')
                data_temp = data_temp.lower()
                if aplicacoes.verificar_data(data_temp):
                    input('Data alterada com sucesso! ')
                    break
                else:
                    input('Data incorreta, tente novamente.')
        elif o == 2:
            while True:
                for i in aplicacoes.lista_de_vendedoras_taubate:
                    print(i)
                vendedora_temp = input('Insira o nome da vendedora: ')
                vendedora_temp = vendedora_temp.capitalize()
                if aplicacoes.verificar_vendedora(vendedora_temp):
                    input('Vendedora alterada com sucesso! ')
                    break
                else:
                    input('Vendedora não cadastrada, tente novamente.')
        elif o == 3:
            
            lista = aplicacoes.digitar_boletas(data_temp,vendedora_temp)
            leitor_txt.Salvar_automatico(lista,arquivo)
            input('Lista salva com sucesso!')


            
        elif o == 4:
            arquivo = filedialog.askopenfilename(filetypes=[("Arquivo de Texto", "*.txt")])
        elif o == 5:
            lista_temp = leitor_txt.Ler_txt()
            lista = lista_temp.copy()
            while True:
                input('Lista Carregada com sucesso.')
                decisao = input('Deseja carregar outra lista? s/n')
                if decisao == 's':
                    lista_temp = leitor_txt.Ler_txt()
                    for i in lista_temp:
                        m=i.copy()
                        lista.append(m)
                else:
                    arquivo2 = filedialog.askopenfilename(filetypes=[("Arquivo de Texto", "*.txt")])
                    leitor_txt.Salvar_txt(lista,arquivo2)
                    break
        elif o == 6:
            return lista

