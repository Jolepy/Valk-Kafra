from tkinter import *
import sqlite3

# banco de dados SQLite diretamente
conexao = sqlite3.connect('Estoque.db')
cursor = conexao.cursor()

# Criando a tabela 
cursor.execute('''
CREATE TABLE IF NOT EXISTS Estoque (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Produto TEXT NOT NULL,
    Quantidade INTEGER NOT NULL,
    Conta TEXT NOT NULL
)
''')

conexao.commit()

###Função para configurar o GIF 

def configurar_background(janela, largura, altura, gif_path, total_frames):
    canvas = Canvas(janela, bg="#ffffff", height=altura, width=largura, bd=0, highlightthickness=0, relief="ridge")
    canvas.place(x=0, y=0)
    background_img = PhotoImage(file=gif_path)
    background = canvas.create_image(largura // 2, altura // 2, image=background_img)
    janela.background_img = background_img  
    return canvas, background, background_img, total_frames

### Função para loop do GIF 

def update_gif(janela, canvas, background, background_img, total_frames, frame_count=0):
    try:
        background_img.configure(format=f"gif -index {frame_count}")
        canvas.itemconfig(background, image=background_img)
        frame_count = (frame_count + 1) % total_frames
    except Exception:
        frame_count = 0
    janela.after(100, update_gif, janela, canvas, background, background_img, total_frames, frame_count)

### Funções para criar janelas
def adicionar_na_segunda_janela():
    def confirmar_adicao():
        nome = nome_insumo_sec.get()
        qtde = qtde_insumo_sec.get()
        conta = conta_insumo_sec.get()

        cursor.execute('''
        INSERT INTO Estoque (Produto, Quantidade, Conta)
        VALUES (?, ?, ?)
        ''', (nome, qtde, conta))
        conexao.commit()

        caixa_texto.delete("1.0", END)
        caixa_texto.insert("1.0", f"Item {nome} adicionado ao estoque!")
        segunda_janela.destroy()

    segunda_janela = Toplevel(window)
    segunda_janela.geometry("400x300")
    segunda_janela.title("Adicionar Produto")
    
    ### Desisti de consertar esse GIF Então zerei os frames para não bugar a animação ###
    canvas, background, background_img, total_frames = configurar_background(segunda_janela, 400, 300, "background_topdown.gif", 0)
    segunda_janela.after(0, update_gif, segunda_janela, canvas, background, background_img, total_frames)

    Label(segunda_janela, text="Nome do Produto:").pack()
    nome_insumo_sec = Entry(segunda_janela)
    nome_insumo_sec.pack()

    Label(segunda_janela, text="Quantidade:").pack()
    qtde_insumo_sec = Entry(segunda_janela)
    qtde_insumo_sec.pack()

    Label(segunda_janela, text="Conta:").pack()
    conta_insumo_sec = Entry(segunda_janela)
    conta_insumo_sec.pack()

    Button(segunda_janela, text="Confirmar", command=confirmar_adicao).pack()

def deletar_na_segunda_janela():
    def abrir_terceira_janela(nome):
        def confirmar_terceira():
            cursor.execute('DELETE FROM Estoque WHERE Produto = ?', (nome,))
            conexao.commit()
            caixa_texto.delete("1.0", END)
            caixa_texto.insert("1.0", f"Item {nome} deletado!")
            terceira_janela.destroy()
            segunda_janela.destroy()

        def cancelar_terceira():
            terceira_janela.destroy()

        terceira_janela = Toplevel(segunda_janela)
        terceira_janela.geometry("400x200")
        terceira_janela.title("Confirmar Exclusão")
        
        Label(terceira_janela, text=f"Você tem certeza que deseja deletar '{nome}' permanentemente?").pack()
        Button(terceira_janela, text="Sim", command=confirmar_terceira).pack(side=LEFT, padx=100)
        Button(terceira_janela, text="Não", command=cancelar_terceira).pack(side=LEFT, padx=0)

    def confirmar_delecao():
        nome = nome_insumo_sec.get()
        abrir_terceira_janela(nome)

    segunda_janela = Toplevel(window)
    segunda_janela.geometry("400x200")
    segunda_janela.title("Deletar Produto")

    ### Desisti de consertar esse GIF Então zerei os frames para não bugar a animação ###
    canvas, background, background_img, total_frames = configurar_background(segunda_janela, 400, 200, "background_topdown.gif", 0)
    segunda_janela.after(0, update_gif, segunda_janela, canvas, background, background_img, total_frames)

    Label(segunda_janela, text="Nome do Produto:").pack()
    nome_insumo_sec = Entry(segunda_janela)
    nome_insumo_sec.pack()

    Button(segunda_janela, text="Confirmar", command=confirmar_delecao).pack()

def consumir_na_segunda_janela():
    def confirmar_consumo():
        nome = nome_insumo_sec.get()
        conta = conta_insumo_sec.get()
        qtde = qtde_insumo_sec.get()

        cursor.execute('''
        UPDATE Estoque SET Quantidade = Quantidade - ?
        WHERE Produto = ? AND Conta = ?
        ''', (qtde, nome, conta))
        conexao.commit()

        caixa_texto.delete("1.0", END)
        caixa_texto.insert("1.0", f"Item {nome} consumido em {qtde} unidades!")
        segunda_janela.destroy()

    segunda_janela = Toplevel(window)
    segunda_janela.geometry("400x300")
    segunda_janela.title("Atualizar Registro")
    ### Desisti de consertar esse GIF Então zerei os frames para não bugar a animação ###
    canvas, background, background_img, total_frames = configurar_background(segunda_janela, 400, 300, "background_topdown.gif", 0) 
    segunda_janela.after(0, update_gif, segunda_janela, canvas, background, background_img, total_frames)

    Label(segunda_janela, text="Nome do Produto:").pack()
    nome_insumo_sec = Entry(segunda_janela)
    nome_insumo_sec.pack()

    Label(segunda_janela, text="Quantidade:").pack()
    qtde_insumo_sec = Entry(segunda_janela)
    qtde_insumo_sec.pack()

    Label(segunda_janela, text="Conta:").pack()
    conta_insumo_sec = Entry(segunda_janela)
    conta_insumo_sec.pack()

    Button(segunda_janela, text="Confirmar", command=confirmar_consumo).pack()

def procurar_na_segunda_janela():
    def confirmar_procurar():
        nome = nome_insumo_sec.get()
        conta = conta_insumo_sec.get()

        if nome and conta:
            cursor.execute('SELECT * FROM Estoque WHERE Produto LIKE ? AND Conta = ?', (f'%{nome}%', conta))
        elif nome:
            cursor.execute('SELECT * FROM Estoque WHERE Produto LIKE ?', (f'%{nome}%',))
        elif conta:
            cursor.execute('SELECT * FROM Estoque WHERE Conta = ?', (conta,))

        valores = cursor.fetchall()

        if valores:
            texto = ''
            for tupla in valores:
                id_produto, produto, quantidade, conta = tupla
                texto += f'''
Produto: {produto}
Quantidade: {int(quantidade)}
Conta: {conta}
'''
        else:
            texto = "Nenhum item encontrado."

        caixa_texto.delete("1.0", END)
        caixa_texto.insert("1.0", texto)
        segunda_janela.destroy()

    segunda_janela = Toplevel(window)
    segunda_janela.geometry("400x200")
    segunda_janela.title("Procurar Produto")
    
    ### Desisti de consertar esse GIF Então zerei os frames para não bugar a animação ###
    canvas, background, background_img, total_frames = configurar_background(segunda_janela, 400, 200, "background_topdown.gif", 0) 
    segunda_janela.after(0, update_gif, segunda_janela, canvas, background, background_img, total_frames)

    Label(segunda_janela, text="Nome do Produto:").pack()
    nome_insumo_sec = Entry(segunda_janela)
    nome_insumo_sec.pack()

    Label(segunda_janela, text="Conta:").pack()
    conta_insumo_sec = Entry(segunda_janela)
    conta_insumo_sec.pack()

    Button(segunda_janela, text="Confirmar", command=confirmar_procurar).pack()

### Janela principal

window = Tk()

window.geometry("769x690")
window.configure(bg="#ffffff")
canvas, background, background_img, total_frames = configurar_background(window, 769, 690, "background.gif", 9)
window.after(0, update_gif, window, canvas, background, background_img, total_frames)

######## Botões

img0 = PhotoImage(file=f"img0.png")
b0 = Button(
    image=img0,
    borderwidth=0,
    highlightthickness=0,
    command=procurar_na_segunda_janela,
    relief="flat")

b0.place(
    x=544, y=196,
    width=178,
    height=54)

img1 = PhotoImage(file=f"img1.png")
b1 = Button(
    image=img1,
    borderwidth=0,
    highlightthickness=0,
    command=deletar_na_segunda_janela,
    relief="flat")

b1.place(
    x=544, y=107,
    width=178,
    height=54)

img2 = PhotoImage(file=f"img2.png")
b2 = Button(
    image=img2,
    borderwidth=0,
    highlightthickness=0,
    command=adicionar_na_segunda_janela,
    relief="flat")

b2.place(
    x=337, y=107,
    width=178,
    height=54)

img3 = PhotoImage(file=f"img3.png")
b3 = Button(
    image=img3,
    borderwidth=0,
    highlightthickness=0,
    command=consumir_na_segunda_janela,
    relief="flat")

b3.place(
    x=337, y=196,
    width=178,
    height=54)

### Caixa de Texto para Retorno
caixa_texto = Text(window, bd=0, bg="white", highlightthickness=0)
caixa_texto.place(x=29, y=330, width=711, height=310)

window.resizable(False, False)
window.mainloop()
