from tkinter import *
from PIL import Image, ImageTk
from start import StartScreen

import os 

base_dir = os.path.dirname(os.path.abspath(__file__))

background_color = '#1075a9'
foreground_color = '#ddffaa'

janela = Tk()
iconpath = os.path.join(base_dir, 'bobAgiota.ico')
janela.iconbitmap(iconpath)
janela.geometry('500x400')
janela.title('Banquin do Bob')
janela.configure(bg=background_color)

image_path = os.path.join(base_dir, "bobAgiota.png")
caminho_imagem = Image.open(image_path)

imagem = ImageTk.PhotoImage(caminho_imagem.resize((180,180)))

def EntrarFrame(master:Tk):
        janela = master
        background_color = '#1075a9'
        foreground_color = '#ddffaa'
        frameCenter = Frame(janela, bg=background_color, relief='ridge', borderwidth=2)

        frameForm = Frame(frameCenter, bg=background_color)

        userVar = StringVar()
        lbl_user = Label(frameForm, text='Usuário:', bg=background_color, font='Helvetica 14 bold')
        ent_user = Entry(frameForm, textvariable=userVar)

        passVar = StringVar()
        lbl_pass = Label(frameForm, text='Senha:', bg=background_color, font='Helvetica 14 bold')
        ent_pass = Entry(frameForm, textvariable=passVar, show='*')

        btn_entrar  = Button(frameForm, text='Entrar')
        btn_cadastro = Button(frameForm, text='Cadastrar')


        lbl_user.grid(row=0, column=0, columnspan=2)
        ent_user.grid(row=0, column=2, columnspan=3, pady=3, sticky=NSEW)

        lbl_pass.grid(row=1, column=0, columnspan=2)
        ent_pass.grid(row=1, column=2, columnspan=3, pady=3, sticky=NSEW)

        btn_entrar.grid(row=2, column=0, columnspan=2, sticky=NSEW, padx=2, pady=2)
        btn_cadastro.grid(row=2, column=2, columnspan=3, sticky=NSEW, pady=2)

        lbl_imagem = Label(frameCenter, image=imagem, bg=background_color)

        lbl_text = Label(frameCenter, text="Banco do Bob Agiota.", bg=background_color, fg=foreground_color, font='Helvetica 18 bold')
        lbl_imagem.grid()
        lbl_text.grid()
        frameForm.grid()

        return frameCenter


# frame_start = StartScreen(janela)
# frame_start.place(in_=janela, anchor="c", relx=.5, rely=.5)

janela.mainloop()