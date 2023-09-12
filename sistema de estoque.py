#____________________________________________________IMPORTANDO BIBLIOTECAS_______________________________________________
import tkinter as tk
from PIL import Image ,ImageTk
import mysql.connector
from tkinter import messagebox
#_____________________________________________________CENTRAL DEF'S_______________________________________________________
def globo():
    global conexao,cursor,janela,janela2,janela3,janela4,janela5,jnaela6,janela7,janela8,imagem1,imagem2,imagem3,imagem4,imagem5,imagem6,imagem7,imagem8
def conect():
    global conexao, cursor
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='macaco123@3',
        database='dados_usuario',
    )
    cursor = conexao.cursor()
def titulo():
    print('*'*30)
    print('P.O.G.E.R.S')
    print('*'*30)
def pular():
    print(' ')
    print('*'*30)
def imagem():
    
    global imagem1,imagem2,imagem3,imagem4,imagem5,imagem6,imagem7,imagem8
    imagem1=r'C:walpaper\tela_login.png'
    imagem2=r'C:walpaper\tela_home.png'
    imagem3=r'C:walpaper\tela_cadastro.png'
    imagem4=r'C:walpaper\tela1_estoque.png'
    imagem5=r'C:walpaper\tela_contatos.png'
    imagem6=r'C:walpaper\tela_caixa.png'
    imagem7=r'C:walpaper\tela_config.png'
    imagem8=r'C:walpaper\tela_botao.png'
def main():
#______________________________________________________MONTAGEM DA JANELA LOGIN_____________________________________________
    #criar a janela login
    janela=tk.Tk()
    janela.title('LOGIN')
    max_width=960
    max_height=540
#______________________________________________________CRIANDO PRIMEIRAS DEF'S_______________________________________________

    # DEF HOME
    def home():
        global imagem2
    #______________________________________________________MONTAGEM DA JANELA HOME____________________________________________
        try:
            janela.destroy()
        except:
            print('janela já destruida')
        print('HOME')
        pular()

        janela2=tk.Tk()
        janela2.title('HOME')

        #______________________________________________________CRIANDO SEGUNDAS DEF'S____________________________________________
        
        #DEF VOLTAR LOGIN
        def voltar_loginh():
            janela2.destroy()
            main()
        # DEF VER ESTOQUE 
        def estoque():
            global imagem4
            janela2.destroy()
            print( 'ESTOQUE')
            pular()
        #________________________________________________MONTAGEM DA JANELA ESTOQUE__________________________________________________
            #criar a janela de estoque 
            janela_e=tk.Tk()
            janela_e.title('Estoque')
         #___________________________________________________CRIANDO TERCEIRA DEF'S____________________________________________________
            def voltar_estoque():
                janela_e.destroy()
                home()
            def adicionar_e():
                titulo()
         #_____________________________________________________ADICIONANDO WIDGETS NA TELA ESTOQUE___________________________________________
            #carregando image 4
            carregar_imagem4=Image.open(imagem4)
            carregar_imagem4.thumbnail((max_width, max_height))
            lendo_imagem4=ImageTk.PhotoImage(carregar_imagem4)

            #CRIAR LABEL PRINCIPAL
            lab4=tk.Label(janela_e, image=lendo_imagem4)
            lab4.image=lendo_imagem4
            lab4.pack()

            #CRIANDO BUTTON'S
            bot_voltare=tk.Button(janela_e, command=voltar_estoque,text='< Voltar', borderwidth=0, bg='#7c14c4')
            bot_voltare.place( x=890, y=20,width= 90, height=50 )
        #DEF PDV
        def vendas():
            global imagem6
            janela2.destroy()

            print( 'VENDAS')
            pular()
        #______________________________________________________MONTAGEM DA JANELA VENDAS________________________________________________________
    
            #criar a janela de vendas 
            janela_v=tk.Tk()
            janela_v.title('CAIXA ABERTO')
        #______________________________________________________CRIANDO TERCEIRA DEF'S_____________________________________________________________
            def voltar_loginv():
                janela_v.destroy()
                home()
        #_____________________________________________________ADICIONANDO WIDGETS NA TELA VENDAS___________________________________________________
            #carregando image 6
            carregar_imagem6=Image.open(imagem6)
            carregar_imagem6.thumbnail((max_width, max_height))
            lendo_imagem6=ImageTk.PhotoImage(carregar_imagem6)

            #CRIAR LABEL PRINCIPAL
            lab6=tk.Label(janela_v, image=lendo_imagem6)
            lab6.image=lendo_imagem6
            lab6.pack()

             #CRIANDO BUTTON'S
            bot_voltarv=tk.Button(janela_v, command=voltar_loginv,text='< Voltar', borderwidth=0, bg='#7c14c4')
            bot_voltarv.place( x=907, y=13,width= 50, height=50 )
        #DEF CONTATOS
        def contatos():
            global imagem5
            janela2.destroy()
            print( 'CONTATOS')
            pular()
        #______________________________________________________MONTAGEM DA JANELA CONTATOS________________________________________________________
            janela_c=tk.Tk()
            janela_c.title('Contatos')
        #______________________________________________________CRIANDO TERCEIRA DEF'S______________________________________________________________
            def voltar_loginc():
                janela_c.destroy()
                home()
        #_____________________________________________________ADICIONANDO WIDGETS NA TELA CONTATOS___________________________________________________
            #carregando image 5
            carregar_imagem5=Image.open(imagem5)
            carregar_imagem5.thumbnail((max_width, max_height))
            lendo_imagem5=ImageTk.PhotoImage(carregar_imagem5)

            #CRIAR LABEL PRINCIPAL
            lab5=tk.Label(janela_c, image=lendo_imagem5)
            lab5.image=lendo_imagem5
            lab5.pack()

            #CRIAR BUTTON'S
            bot_voltarv=tk.Button(janela_c, command=voltar_loginc,text='< Voltar', borderwidth=0, bg='#7c14c4')
            bot_voltarv.place( x=900, y=20,width=70, height=50 )
        #DEF CONFIGURAÇÕES 
        def config():
            global imagem7
            janela2.destroy()
            print( 'CONFIGURAÇÕES')
            pular()
        #______________________________________________________MONTAGEM DA JANELA CONTATOS________________________________________________________
    
            #criar a janela de configurações  
            janela_g=tk.Tk()
            janela_g.title('CONFIGURAÇÕES')
        #______________________________________________________CRIANDO TERCEIRA DEF'S______________________________________________________________
            def voltar_loging():
                janela_g.destroy()
                home()
        #_____________________________________________________ADICIONANDO WIDGETS NA TELA CONFIGURAÇÃO _____________________________________________
            #carregando image 7
            carregar_imagem7=Image.open(imagem7)
            carregar_imagem7.thumbnail((max_width, max_height))
            lendo_imagem7=ImageTk.PhotoImage(carregar_imagem7)

            #CRIANDO LABEL PRINCIPAL
            lab7=tk.Label(janela_g, image=lendo_imagem7)
            lab7.image=lendo_imagem7
            lab7.pack()

             #CRIAR BUTTON'S
            bot_voltarv=tk.Button(janela_g, command=voltar_loging,text='< Voltar', borderwidth=0, bg='#7c14c4')
            bot_voltarv.place( x=907, y=13,width= 50, height=50 )
    #______________________________________________________ADICIONANDO WIDGETS NA TELA HOME_________________________________________
        #carregando image 2
        carregar_imagem2=Image.open(imagem2)
        carregar_imagem2.thumbnail((max_width, max_height))
        lendo_imagem2=ImageTk.PhotoImage(carregar_imagem2)

        #CRIAR LABEL PRINCIPAL
        lab2=tk.Label(janela2, image=lendo_imagem2)
        lab2.image=lendo_imagem2
        lab2.pack()

        #CRIAR BUTTON'S
        bot_voltar=tk.Button(janela2, command=voltar_loginh,text=' < Voltar', borderwidth=0, bg='white')
        bot_voltar.place( x=907, y=10,width= 50, height=60 )

        botao_estoque=tk.Button(janela2, text='ESTOQUE', command=estoque,bg='#4d0c85' , borderwidth=0)
        botao_estoque.place(x=260,y=125, width=150 , height=70)

        botao_vendas=tk.Button(janela2, text='VENDAS', command=vendas, bg='#4d0c85' , borderwidth=0)
        botao_vendas.place(x=252, y=270, width=150, height=70)

        botao_config=tk.Button(janela2, text='CONFIGURAÇÕES',command=config, bg='#4d0c85' , borderwidth=0)
        botao_config.place(x=590, y=125, width=150, height=70)

        botao_cont=tk.Button(janela2, text='CONTATOS',command=contatos,bg='#4d0c85' , borderwidth=0)
        botao_cont.place(x=590, y=252, width=120, height=70)
    #DEF LOGIN 1
    def usu_senh():
        global usuario,senha
         # Obter usuário e senha das entradas
        usuario = entry_name.get()
        senha = entry_senha.get()

        pegar_login()
    #DEF LOGIN 2
    def pegar_login():
        usu=usuario
        sen=senha
        # Autenticar com o banco de dados MySQL
        try:
            cursor = conexao.cursor()
            comando= f"SELECT usuario, senha FROM cadastro WHERE usuario ='{usu}' AND senha = '{sen}'"
            print(comando)
            cursor.execute(comando) #executando o comando
            resultado=cursor.fetchall()#ler o banco de dados 
            print(resultado)

            if resultado:
                home()
            else:
                messagebox.showerror("Erro", "Login incorreto.")
            
            conexao.close()
        except mysql.connector.Error as err:
            messagebox.showerror("Erro de Banco de Dados", f"Erro: {err}")
    #DEF CADASTRAR LOGIN
    def login():
        janela.destroy()
        print('CADASTRAR LOGIN')
        pular()
#______________________________________________________MONTAGEM DA JANELA CADASTRAR_LOGIN______________________________________________
        janela3=tk.Tk()
        janela3.title('CADASTRAR LOGIN')
#______________________________________________________CRIANDO TERCEIRAS DEF'S_________________________________________________________
        def set_cadastro():
            usuario=entry_nome.get()
            senha=entry_senha1.get()
            num=entry_num.get()
            email=entry_email.get()
            func=entry_func.get()
            
            #ADICIONAR BANCO DE DADOS
            comando= f'INSERT INTO cadastro(usuario,email,funcao,numero,senha) VALUES("{usuario}","{email}","{func}","{num}","{senha}")'
            cursor.execute(comando) 
            conexao.commit()

            conexao.close()
        def voltar_login():
            janela3.destroy()
            main()
#______________________________________________________ADICIONANDO WIDGETS NA TELA LOGIN_______________________________________________
        #carregando image 3
        carregar_imagem3=Image.open(imagem3)
        carregar_imagem3.thumbnail((max_width, max_height))

        #lendo imagem 3
        lendo_imagem3=ImageTk.PhotoImage(carregar_imagem3)

        #colocar caminho no photo
        lab3=tk.Label(janela3, image=lendo_imagem3)
        lab3.image=lendo_imagem3
        lab3.pack()

        #CRIANDO ENTRY'S
        entry_nome=tk.Entry(janela3, bg='white',highlightthickness=0)
        entry_nome.place(x=120,y=205)
        print(f'O nome cadastrado foi={entry_nome}')

        entry_senha1=tk.Entry(janela3, bg='white',highlightthickness=0)
        entry_senha1.place(x=120,y=255)
        print(f'A senha cadastrada foi={entry_senha1}')

        entry_email=tk.Entry(janela3, bg='white',highlightthickness=0)
        entry_email.place(x=120,y=310)
        print(f'O email cadastrado foi={entry_email}')

        entry_num=tk.Entry(janela3, bg='white',highlightthickness=0)
        entry_num.place(x=132,y=370)
        print(f'O numero cadastrado foi={entry_num}')

        entry_func=tk.Entry(janela3, bg='white',highlightthickness=0)
        entry_func.place(x=130,y=430)
        print(f'A função cadastrada foi={entry_func}')

       #CRIANDO BUTTON'S
        bot_voltar=tk.Button(janela3, command=voltar_login,text=' < Voltar', borderwidth=0, bg='white')
        bot_voltar.place( x=790, y=120,width= 50, height=50 )

        bot_salvar=tk.Button(janela3, command=set_cadastro,text=' < Salvar', borderwidth=0, bg='#244c04',fg="white")
        bot_salvar.place( x=77, y=490,width= 57, height=35 )
#______________________________________________________ADICIONANDO WIDGETS NA TELA LOGIN________________________________________
    global imagem1
    #carregar a imagem 1
    carregar_login=Image.open(imagem1)
    carregar_login.thumbnail((max_width, max_height))
    lendo_imagem1=ImageTk.PhotoImage(carregar_login)

    #CRIANDO LABEL PRINCIPAL
    lab=tk.Label(janela, image=lendo_imagem1)
    lab.pack()

    #ENTRY'S
    entry_name=tk.Entry(janela, bg='#be78d1',highlightthickness=0)
    entry_name.place(x=377 , y=260 )

    entry_senha=tk.Entry(janela,bg='#be78d1',highlightthickness=0)
    entry_senha.place(x=377 , y= 365)

    #button LOGIN
    bot_login=tk.Button(janela, text='login',command=usu_senh, borderwidth=0, bg="white" )
    bot_login.place(x=409, y=412, width=150, height=37)

    #button de def login
    bot_cad=tk.Button(janela, command=login, text='novo', borderwidth=0,bg='#781cae',fg="white")
    bot_cad.place(x=380, y=460,width= 100, height=10 )

    janela.mainloop()
#_____________________________________________________EXECUTANDO___________________________________________________________
globo()
imagem()
conect()
titulo()
main()

