#Importar pacotes
import sqlite3
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

#Criar conexÃ£o e cursor
con = sqlite3.connect('banco.db')
cur = con.cursor()

#Criar tabela clientes
cur.execute("""CREATE TABLE IF NOT EXISTS clientes (
            nome VARCHAR,
            sobrenome VARCHAR,
            email VARCHAR
            senha VARCHAR PRIMARY KEY)""")



class main:
    def __init__(self,master):
        
#--------------------------------------TKINTER INTERFACE------------------------------------------------#
        self.frame1 = Frame(master,bg='sky blue')
        self.frame1.configure(relief=GROOVE)
        self.frame1.configure(borderwidth="2")
        self.frame1.place(relx=0.0,rely=0.0,relheight=1.0,relwidth=0.51)
        Label(self.frame1,text='CADASTRO',font=('Ariel','30'),bg='sky blue').place(relx=0.30,rely=0.01)

        Label(self.frame1,text='Nome',font=('Ariel','15'),bg='sky blue').place(relx=0.02,rely=0.12)
        self.nome=Entry(self.frame1,font=('Ariel','20'))
        self.nome.place(relx=0.02,rely=0.16, relwidth=0.94)

        Label(self.frame1,text='Sobrenome',font=('Ariel','15'),bg='sky blue').place(relx=0.02,rely=0.21)
        self.sobrenome = Entry(self.frame1,font=('Ariel','20'))
        self.sobrenome.place(relx=0.02,rely=0.25,relwidth=0.94)

        Label(self.frame1,text='E-mail',font=('Ariel','15'),bg='sky blue').place(relx=0.02,rely=0.31)
        self.email = Entry(self.frame1,font=('Ariel','20'))
        self.email.place(relx=0.02,rely=0.36,width=400)
        

        Label(self.frame1,text='Senha',font=('Ariel','15'),bg='sky blue').place(relx=0.02,rely=0.50)
        self.senha = Entry(self.frame1,font=('Ariel','20'), show='*')
        self.senha.place(relx=0.02,rely=0.55,relwidth=0.94)


        self.botaocadastra = Button(self.frame1,text='Cadastrar',font=('Ariel','20'),
                                    fg='green',command=self.cadastraclientes)
        self.botaocadastra.place(relx=0.62,rely=0.33,relwidth=0.31)
        
        

        self.botaocancela = Button(self.frame1,text='Atualizar dados',font=('Ariel','20'),
                                   fg='red',command=self.atualizar)
        self.botaocancela.place(relx=0.62,rely=0.44,relwidth=0.31)
        
        
        self.frame2 = Frame(master,bg='sky blue')
        self.frame2.configure(relief=GROOVE)
        self.frame2.configure(borderwidth="2")
        self.frame2.place(relx=0.51,rely=0.0,relheight=0.31,relwidth=0.49)

        Label(self.frame2,text='BUSCAR USUÁRIO',font=('Ariel','30'),bg='sky blue').place(relx=0.20,rely=0.05)
        
        
        self.nome2=Entry(self.frame2,font=('Ariel','20'))
        self.nome2.bind("<Return>",self.mostraclientes_a)
        self.nome2.place(relx=0.03,rely=0.42, width=620)
        

        self.botaook = Button(self.frame2, text='Buscar',font=('Ariel','25'),
                              fg='green',command=self.mostraclientes2)
        self.botaook.place(relx=0.38,rely=0.65)

        self.frame3 = Frame(master)
        self.frame3.configure(relief=GROOVE)
        self.frame3.configure(borderwidth="2")
        self.frame3.place(relx=0.51,rely=0.31,relheight=0.69,relwidth=0.49)


        self.mostra1 = Text(self.frame3,bg='azure',font=('Courier','20','bold'),fg='blue')
        self.mostra1.place(relx=0.00,rely=0.0,relheight=1.0,relwidth=1.0)
        

#-----------------------------------------FUNÇÕES-----------------------------------------------------------#
    def cadastraclientes(self):
        nome=self.nome.get()
        senha=self.senha.get()
        email=self.email.get()
        sobrenome=self.sobrenome.get()
        try:
            cur.execute("INSERT INTO clientes VALUES(?,?,?,?)",
                    (nome,senha,email,sobrenome))
        except:
            messagebox.showinfo('Aviso!','Usuario ja cadastrado')  
        con.commit()
        self.nome.delete(0,END)
        self.senha.delete(0,END)
        self.email.delete(0,END)
        self.sobrenome.delete(0,END)
        

    def atualizar (self):
        nome = self.nome.get()
        cur.execute("DELETE FROM clientes WHERE nome = '%s'" %nome)
        self.nome.delete(0,END)
        self.senha.delete(0,END)
        self.email.delete(0,END)
        self.sobrenome.delete(0,END)
        messagebox.showinfo('Usuario deletado', 'Insira os novos dados')
        
                       

    def mostraclientes2(self):
        self.mostra1.delete(0.0,END)
        nome2 = self.nome2.get()
        cur.execute("SELECT * FROM clientes WHERE nome = '%s'" %nome2)
        consulta = cur.fetchall()
        for i in consulta:
            self.mostra1.insert(END,'''Nome do usuario:{}
Sobrenome:{}
E-mail:{}
Senha:{}'''.format(i[0], i[1],i[2],i[3]))

    
# Funcao q aceita eventos do teclado,chama a func mostraclientes quando a tecla Enter for pressionada
    def mostraclientes_a(self,event):
        self.mostraclientes2()
        
                                           
        
root = Tk()
root.title("Dory")
root.geometry("1366x768")
main(root)
root.mainloop()



