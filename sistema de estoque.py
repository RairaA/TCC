#importar o tkinter 
import tkinter as tk
from PIL import Image ,ImageTk


def linha():
    print('*'*30)
def pular():
    print(' ')
def voltar_home():
    linha()
def voltar_estoque():
    linha()
#carregar caminho de todas as imagens
imagem1=r'C:\Users\Dell\Downloads\walpaper\tela_login.png'
imagem2=r'C:\Users\Dell\Downloads\walpaper\tela_home.png'
imagem3=r'C:\Users\Dell\Downloads\walpaper\tela_cadlogin.png'
imagem4=r'C:\Users\Dell\Downloads\walpaper\tela1_estoque.png'
imagem5=r'C:\Users\Dell\Downloads\walpaper\tela_contatos.png'
imagem6=r'C:\Users\Dell\Downloads\walpaper\tela_caixa.png'
imagem7=r'C:\Users\Dell\Downloads\walpaper\tela_config.png'
imagem8=r'C:\Users\Dell\Downloads\walpaper\tela_botao.png'

#criar def main pra colocar todas as def dentro()
def main():

    linha()
    print('P.O.G.E.R.S')
    linha()
    #criar a janela login
    janela=tk.Tk()
    #redimensionar altura e largura da janela login
    max_width=960
    max_height=540

    #criar a def home() com as funcionalidades dentro
    def home():
        janela.destroy()

        linha()
        print('HOME')
        pular()

        janela2=tk.Tk()
        janela2.title('HOME')

        #carregando image 2
        carregar_imagem2=Image.open(imagem2)
        carregar_imagem2.thumbnail((max_width, max_height))

        #lendo imagem 2
        lendo_imagem2=ImageTk.PhotoImage(carregar_imagem2)

        #colocar caminho no photo
        lab2=tk.Label(janela2, image=lendo_imagem2)
        lab2.image=lendo_imagem2
        lab2.pack()

        #criar a def estoque (imagem4)
        def voltar_loginh():
            janela2.destroy()
            main()
        
        bot_voltar=tk.Button(janela2, command=voltar_loginh,text=' < Voltar', borderwidth=0, bg='white')
        bot_voltar.place( x=907, y=10,width= 50, height=60 )

        def estoque():
            janela2.destroy()

            linha()
            print( 'ESTOQUE')
            pular()
        
            #criar a janela de estoque 
            janela_e=tk.Tk()
            janela_e.title('Estoque')
        

            #carregando image 4
            carregar_imagem4=Image.open(imagem4)
            carregar_imagem4.thumbnail((max_width, max_height))

            #lendo imagem 4
            lendo_imagem4=ImageTk.PhotoImage(carregar_imagem4)

            #colocar caminho no photo
            lab4=tk.Label(janela_e, image=lendo_imagem4)
            lab4.image=lendo_imagem4
            lab4.pack()
        #criar def vendas (imagem6)
        def vendas():
            janela2.destroy()

            linha()
            print( 'VENDAS')
            pular()
        
            #criar a janela de vendas 
            janela_v=tk.Tk()
            janela_v.title('CAIXA ABERTO')
        

            #carregando image 6
            carregar_imagem6=Image.open(imagem6)
            carregar_imagem6.thumbnail((max_width, max_height))

            #lendo imagem 6
            lendo_imagem6=ImageTk.PhotoImage(carregar_imagem6)

            #colocar caminho no photo
            lab6=tk.Label(janela_v, image=lendo_imagem6)
            lab6.image=lendo_imagem6
            lab6.pack()

            def voltar_loginv():
                janela_v.destroy()
                home()#erro no voltar 

            bot_voltarv=tk.Button(janela_v, command=voltar_loginv,text='< Voltar', borderwidth=0, bg='#8526b9')
            bot_voltarv.place( x=907, y=13,width= 50, height=50 )
        #criar def contatos (imagem5)
        def contatos():
            janela2.destroy()

            linha()
            print( 'CONTATOS')
            pular()
            

            #criar a janela de contatos 
            janela_c=tk.Tk()
            janela_c.title('Contatos')
        

            #carregando image 5
            carregar_imagem5=Image.open(imagem5)
            carregar_imagem5.thumbnail((max_width, max_height))

            #lendo imagem 5
            lendo_imagem5=ImageTk.PhotoImage(carregar_imagem5)

            #colocar caminho no photo
            lab5=tk.Label(janela_c, image=lendo_imagem5)
            lab5.image=lendo_imagem5
            lab5.pack()

            def voltar_loginc():
                janela_c.destroy()
                main()

            bot_voltarv=tk.Button(janela_c, command=voltar_loginc,text='< Voltar', borderwidth=0, bg='#8526b9')
            bot_voltarv.place( x=907, y=13,width= 50, height=50 )
        #criar def configurações (imagem7)
        def config():
            janela2.destroy()

            linha()
            print( 'CONFIGURAÇÕES')
            pular()
            

            #criar a janela de configurações  
            janela_g=tk.Tk()
            janela_g.title('CONFIGURAÇÕES')
        

            #carregando image 7
            carregar_imagem7=Image.open(imagem7)
            carregar_imagem7.thumbnail((max_width, max_height))

            #lendo imagem 7
            lendo_imagem7=ImageTk.PhotoImage(carregar_imagem7)

            #colocar caminho no photo
            lab7=tk.Label(janela_g, image=lendo_imagem7)
            lab7.image=lendo_imagem7
            lab7.pack()

            def voltar_loging():
                janela_g.destroy()
                main()

            bot_voltarv=tk.Button(janela_g, command=voltar_loging,text='< Voltar', borderwidth=0, bg='#8526b9')
            bot_voltarv.place( x=907, y=13,width= 50, height=50 )

        #criar os buttons para destruir a tela home e ir para cada def
        botao_estoque=tk.Button(janela2, text='ESTOQUE', command=estoque,bg='#4d0c85' , borderwidth=0)
        botao_estoque.place(x=260,y=125, width=150 , height=70)

        botao_vendas=tk.Button(janela2, text='VENDAS', command=vendas, bg='#4d0c85' , borderwidth=0)
        botao_vendas.place(x=252, y=270, width=150, height=70)

        botao_config=tk.Button(janela2, text='CONFIGURAÇÕES',command=config, bg='#4d0c85' , borderwidth=0)
        botao_config.place(x=590, y=125, width=150, height=70)

        botao_cont=tk.Button(janela2, text='CONTATOS',command=contatos,bg='#4d0c85' , borderwidth=0)
        botao_cont.place(x=590, y=252, width=120, height=70)
    #criar a def pegar para autentificar a senha e login
    def pegar_login():
        # name e senha autentificar com o mysql
        usuario=entry_name.get().lower()
        print(usuario)
        senha=entry_senha.get()
        print(senha)

        if usuario !='admin' and  senha!='123':
            pular()
            print(f'LOGIN={usuario} ou SENHA= {senha} INCORRETO')
        else:
            
            print('LOGIN CORRETO!')
            home()
    #criar def login()
    def login():
        janela.destroy()
        print('Cadastro de login')
    
        #criar janela
        janela3=tk.Tk()
        janela3.title('cadastro de login')
    
        #carregando image 3
        carregar_imagem3=Image.open(imagem3)
        carregar_imagem3.thumbnail((max_width, max_height))

        #lendo imagem 3
        lendo_imagem3=ImageTk.PhotoImage(carregar_imagem3)

        #colocar caminho no photo
        lab3=tk.Label(janela3, image=lendo_imagem3)
        lab3.image=lendo_imagem3
        lab3.pack()

        def voltar_login():
            janela3.destroy()
            main()
        
        bot_voltar=tk.Button(janela3, command=voltar_login,text=' < Voltar', borderwidth=0, bg='white')
        bot_voltar.place( x=790, y=120,width= 50, height=50 )


    #carregar a imagem 1
    carregar_login=Image.open(imagem1)
    carregar_login.thumbnail((max_width, max_height))

    #lendo imagem
    lendo_imagem1=ImageTk.PhotoImage(carregar_login)

    #colocar caminho no photo
    lab=tk.Label(janela, image=lendo_imagem1)
    lab.pack()

    #entry login
    entry_name=tk.Entry(janela, bg='#be78d1',highlightthickness=0)
    entry_name.place(x=377 , y=260 )

    entry_senha=tk.Entry(janela,bg='#be78d1',highlightthickness=0)
    entry_senha.place(x=377 , y= 365)

    #button LOGIN
    bot_login=tk.Button(janela, text='login',command=pegar_login, borderwidth=0, bg="white" )
    bot_login.place(x=409, y=412, width=150, height=37)
    #button de def login
    bot_cad=tk.Button(janela, command=login, text='novo', borderwidth=0,bg='#781cae',fg="white")
    bot_cad.place(x=380, y=460,width= 100, height=10 )

    janela.mainloop()

main()

