#importar o tkinter 
import tkinter as tk
login_e=''
senha_e=''

#criar a janela inicial
janela=tk.Tk()
janela.geometry('300x400')


#criar a def home()
def home():
    print("""  
          [1]estoque
          [2]vendas
          [3]configuraçoes
          [4]contatos
         """)
        
    escolha=input('digite a escolha')
    if escolha =='1':
        estoque()
    if escolha =='2':
        vendas()
    if escolha =='3':
        config()
    if escolha =='4':
        contatos()


#criar def main pra colocar todas as def dentro()
def main():
    print('*'* 30)
    print('P.O.G.E.R.S')
    print('*'* 30)
    login()
#criar a def pegar login():
def pegar_login():
    global login_e , senha_e
    login=login_e.get()
    senha=senha_e.get()
    print(login)
    print(senha)
    janela.destroy()

#criar def login()
def login():

    login_l=tk.Label(janela,text='login' )
    login_l.pack()

    login_e=tk.Entry(janela)
    login_e.pack()

    senha_l=tk.Label(janela,text='senha' )
    senha_l.pack()

    senha_e=tk.Entry(janela)
    senha_e.pack()

    botao=tk.Button(janela, text="ENVIAR", command=pegar_login, borderwidth=0)
    botao.pack()

    


#criar def estoque ()
def estoque():
    print('estoque')


#criar def vendas()
def vendas():
    print('vendas')


#criar def configurações ()
def config():
    print('configurações')


#criar a def contatos
def contatos():
    print('contatos')


main()
janela.mainloop()