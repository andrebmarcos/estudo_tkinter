from tkinter import *
from tkinter import ttk
import sqlite3 

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.platypus import SimpleDocTemplate, Image
import webbrowser

root = Tk()

class Relatorios():
    def printCliente(self):
        webbrowser.open("Cliente.pdf")
    def geraRelatCliente(self):
        self.c = canvas.Canvas("Cliente.pdf")
        self.codigoRel = self.codigo_entry.get()
        self.nomeRel = self.nome_entry.get()
        self.telefoneRel = self.telefone_entry.get()
        self.cidadeoRel = self.cidade_entry.get()

        self.c.setFont("Helvetica-Bold", 24)
        self.c.drawString(200, 790, 'Ficha do Cliente')

        self.c.setFont("Helvetica-Bold", 18)
        self.c.drawString(50,700, 'Codigo: ' + self.codigoRel)
        self.c.drawString(50,670, 'Nome: ' + self.nomeRel)
        self.c.drawString(50,640, 'Telefone: ' + self.telefoneRel)
        self.c.drawString(50,610, 'Cidade: ' + self.cidadeoRel)

        self.c.rect(40,780,500,40,fill=False, stroke=True)


        self.c.showPage()
        self.c.save()
        self.printCliente()

class Funcs():
    def limpa_tela(self):
        self.codigo_entry.delete(0,END)
        self.nome_entry.delete(0,END)
        self.telefone_entry.delete(0,END)
        self.cidade_entry.delete(0,END)
    def conecta_db(self):
        self.conn = sqlite3.connect("clientes_teste.db")
        self.cursor = self.conn.cursor()
    def desconectar_db(self):
        self.conn.close()
    def montaTabelas(self):
        self.conecta_db(); print("Conectando ao banco de dados")
        ###Criar Tabela
        self.cursor.execute("""
                            CREATE TABLE IF NOT EXISTS clientes (
                            cod INTEGER PRIMARY KEY,
                            nome_cliente CHAR(40) NOT NULL,
                            telefone INTEGER(20),
                            cidade CHAR(40)
                            );
                            """)
        self.conn.commit(); print("Banco de dados criado")
        self.desconectar_db()
    def variaveis(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.telefone = self.telefone_entry.get()
        self.cidade = self.cidade_entry.get()
    def add_cliente(self):
        self.variaveis()
        self.conecta_db()

        self.cursor.execute("""INSERT INTO clientes (nome_cliente,telefone,cidade) VALUES (?,?,?)""",(self.nome,self.telefone, self.cidade))
        
        self.conn.commit()
        self.desconectar_db()
        self.select_lista()
        self.limpa_tela()
    def select_lista(self):
        self.listaCli.delete(*self.listaCli.get_children())
        self.conecta_db()
        lista = self.cursor.execute("""SELECT cod, nome_cliente, telefone, cidade FROM clientes 
                                        ORDER BY nome_cliente ASC;""")
        for i in lista:
            self.listaCli.insert("", END, values=i)
        self.desconectar_db()
    def OnDoubleClick(self, event):
        self.limpa_tela()
        self.listaCli.selection()

        for n in self.listaCli.selection():
            col1,col2,col3,col4 = self.listaCli.item(n, 'values')
            self.codigo_entry.insert(END, col1)
            self.nome_entry.insert(END, col2)
            self.telefone_entry.insert(END, col3)
            self.cidade_entry.insert(END, col4)
    def deleta_cliente(self):
        self.variaveis()
        self.conecta_db()

        self.cursor.execute("""DELETE FROM clientes WHERE cod = ?""", (self.codigo,))
        self.conn.commit()
        
        self.desconectar_db()
        self.limpa_tela()
        self.select_lista()
    def alterar_cliente(self):
        self.variaveis()
        self.conecta_db()
        self.cursor.execute("""UPDATE clientes SET nome_cliente = ?, telefone = ?, cidade = ?
                            WHERE cod = ? """, (self.nome, self.telefone, self.cidade, self.codigo))
        self.conn.commit()
        self.desconectar_db()
        self.select_lista()
        self.limpa_tela()
    def buscar_cliente(self):
        
        self.conecta_db()
        self.listaCli.delete(*self.listaCli.get_children())
        self.nome_entry.insert(END, '%')
        nome = self.nome_entry.get()
        self.cursor.execute("""SELECT cod, nome_cliente, telefone, cidade FROM clientes
                            WHERE nome_cliente LIKE '%s' ORDER BY nome_cliente ASC""" % nome)
        buscanomeCli = self.cursor.fetchall()
        for i in buscanomeCli:
            self.listaCli.insert("", END, values=i)
        self.limpa_tela()
        self.desconectar_db()


class Application(Funcs, Relatorios):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_frame2()
        self.montaTabelas()
        self.select_lista()
        self.menus()
        root.mainloop()
    def tela(self):
        self.root.title("Cadastro de Clientes")
        self.root.configure(background='#1e3743')
        self.root.geometry("700x500")
        self.root.resizable(True, True)
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=480, height=300)
    def frames_da_tela(self):
        self.frame1 = Frame(self.root, bd=4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=3)
        self.frame1.place(relx= 0.02, rely= 0.02, relwidth= 0.96, relheight= 0.46)

        self.frame2 = Frame(self.root, bd=4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=3)
        self.frame2.place(relx= 0.02, rely= 0.5, relwidth= 0.96, relheight= 0.46)
    def widgets_frame1(self):
        ##criando o botao limpar
        self.bt_limpar = Button(self.frame1, text='Limpar', bd = 4, bg= '#a3b1d6', fg = 'white', font = ('veridiana', 8, 'bold'), command= self.limpa_tela)
        self.bt_limpar.place(relx= 0.2 , rely=0.1,relwidth= 0.1 ,relheight= 0.15)
        ##criando o botao buscar
        self.bt_buscar = Button(self.frame1, text='Buscar', bd = 4, bg= '#a3b1d6', fg = 'white', font = ('veridiana', 8, 'bold'), command= self.buscar_cliente)
        self.bt_buscar.place(relx= 0.31 , rely=0.1,relwidth= 0.1 ,relheight= 0.15)
        ##criando o botao novo
        self.bt_novo = Button(self.frame1, text='Novo', bd = 4, bg= '#7ec4a5', fg = 'white', font = ('veridiana', 8, 'bold'), command= self.add_cliente)
        self.bt_novo.place(relx= 0.6 , rely=0.1,relwidth= 0.1 ,relheight= 0.15)
        ##criando o botao alterar
        self.bt_alterar = Button(self.frame1, text='Alterar', bd = 4, bg= '#c4a77e', fg = 'white', font = ('veridiana', 8, 'bold'), command=self.alterar_cliente)
        self.bt_alterar.place(relx= 0.71 , rely=0.1,relwidth= 0.1 ,relheight= 0.15)
        ##criando o botao apagar
        self.bt_apagar = Button(self.frame1, text='Apagar', bd = 4, bg= '#c47e7e', fg = 'white', font = ('veridiana', 8, 'bold'), command=self.deleta_cliente)
        self.bt_apagar.place(relx= 0.82 , rely=0.1,relwidth= 0.1 ,relheight= 0.15)

        #Criação da label de entrada codigo

        self.lb_codigo = Label(self.frame1, text = 'Codigo', bg='#dfe3ee',  font = ('veridiana', 8, 'bold'))
        self.lb_codigo.place(relx= 0.05, rely= 0.05 )

        self.codigo_entry = Entry(self.frame1)
        self.codigo_entry.place(relx= 0.05, rely= 0.15, relwidth= 0.08 )

        #Criação da label de entrada nome

        self.nome = Label(self.frame1, text = 'Nome', bg='#dfe3ee',  font = ('veridiana', 8, 'bold'))
        self.nome.place(relx= 0.05, rely= 0.35 )

        self.nome_entry = Entry(self.frame1)
        self.nome_entry.place(relx= 0.05, rely= 0.45, relwidth= 0.8 )

        #Criação da label de entrada Telefone

        self.telefone = Label(self.frame1, text = 'Telefone', bg='#dfe3ee',  font = ('veridiana', 8, 'bold'))
        self.telefone.place(relx= 0.05, rely= 0.65 )

        self.telefone_entry = Entry(self.frame1)
        self.telefone_entry.place(relx= 0.05, rely= 0.75, relwidth= 0.3 )

        #Criação da label de entrada Cidade

        self.cidade = Label(self.frame1, text = 'Cidade', bg='#dfe3ee',  font = ('veridiana', 8, 'bold'))
        self.cidade.place(relx= 0.50, rely= 0.65 )

        self.cidade_entry = Entry(self.frame1)
        self.cidade_entry.place(relx= 0.50, rely= 0.75, relwidth= 0.4 )
    def lista_frame2(self):
        self.listaCli = ttk.Treeview(self.frame2, height=3, column=("col1","col2","col3","col4"))
        self.listaCli.heading ("#0", text="") 
        self.listaCli.heading ("#1", text="Codigo")
        self.listaCli.heading ("#2", text="Nome") 
        self.listaCli.heading ("#3", text="Telefone") 
        self.listaCli.heading ("#4", text="Cidade") 

        self.listaCli.column("#0", width=1)
        self.listaCli.column("#1", width=50)
        self.listaCli.column("#2", width=200)
        self.listaCli.column("#3", width=125)
        self.listaCli.column("#4", width=125)

        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)
        
        self.scroolLista =Scrollbar(self.frame2, orient='vertical')
        self.listaCli.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96,rely=0.1,relwidth=0.03, relheight=0.85)
        self.listaCli.bind("<Double-1>", self.OnDoubleClick)
    def menus(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)

        def Quit(): self.root.destroy()

        menubar.add_cascade(label = "Opções", menu= filemenu)
        menubar.add_cascade(label = "Relatorios", menu= filemenu2)

        filemenu.add_command(label="Sair", command= Quit)
        filemenu.add_command(label="Limpa Cliente", command= self.limpa_tela)

        filemenu2.add_command(label="Ficha do Cliente", command= self.geraRelatCliente)

Application()