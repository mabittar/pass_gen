import os
from password import Password
from tkinter import *
import tkinter.font as tkFont


def window():
    # inicializa o tkinter na instância window
    window = Tk()

    # definindo variáveis iniciais
    global pass_label
    passwordText = ""

    # configuração do frame principal
    window.config(bg="#344955")
    window.resizable(0, 0)
    w = 400  # width for the Tk root
    h = 400  # height for the Tk root
    ws = window.winfo_screenwidth()  # width of the screen
    hs = window.winfo_screenheight()  # height of the screen
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))

    # fonte principal
    font1 = tkFont.Font(family="Roboto", size=12)

    # título da caixa
    title = Label(window, text="Gerador de Password",
                  bg="#232f34", font=font1, fg="white")
    title.pack(ipadx=5, ipady=5, fill="x")

    # rótulo do scaler
    length_label = Label(
        window, text="Número de \nCaracteres", bg="#4a6572", fg="white")
    length_label.place(x=0.05, y=90)

    # obtendo o valor do scaler
    def buttonCallback(val):
        global scale_widget
        global length
        length = int(val)

    # rótulo do tamanho do password (length)
    scale_widget = Scale(window, from_=6, to=40, tickinterval=34,
                         orient=HORIZONTAL, length=(w*.65), command=buttonCallback, bg="#4a6572", fg="white")
    scale_widget.set(8)
    scale_widget.place(x=(w*0.25), y=80)
    scale_widget.get()

    # rótulo da chamada de texto password
    text5 = Text(window, bg="#4a6572", bd=0, width=9,
                 height=1, font=font1, fg="white")
    text5.pack()
    text5.place(x=1, y=235)
    text5.insert('1.0', " Password:")

    # saída password
    pass_label = Label(window, text="PassWord", font=font1,
                       bg="#4a6572", fg="white")
    pass_label.pack()
    pass_label.config(width=32, height=2)
    pass_label.place(x=90, y=225)

    # função para gerar o password
    def password():
        passw = Password()  # chama a classe Password do import
        passw.length = length  # recebe o comprimento do password
        passwordText = passw.password_generator()  # gera o password
        # atribui o valor do password na caixa de texto correspondente
        pass_label["text"] = str(passwordText)

    # botão para gerar o password
    generate = Button(window, text="Gerar Password",
                      command=password, font=font1, bg='#f9aa33')  # chama a função password
    generate.pack()
    generate.place(x=((w/2)-35), y=150)
    window.update_idletasks()  # atualiza a janela para receber o valor de password

    # função para copiar o password
    def copy_button():
        clip = Tk()
        clip.withdraw()
        clip.clipboard_clear()
        clip.clipboard_append(pass_label["text"])
        clip.destroy()

    # botão para copiar password gerado
    copy_button = Button(window, text="Clique para copiar",
                         command=copy_button, bg='#f9aa33')
    copy_button.pack
    copy_button.place(x=((w/2)-25), y=275)

    # botão de saída
    quit_button = Button(window, text="Saída",
                         command=window.destroy, font=font1, bg='#f9aa33')
    quit_button.pack(fill="x")
    quit_button.place(x=((w/2)), y=365)

    # mantém a janela aberta até clicar em "sair"
    window.mainloop()

#chama a função tkinter para gerar a janela
window()
