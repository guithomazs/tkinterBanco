from tkinter import *
from PIL import Image, ImageTk
import os 

base_dir = os.path.dirname(os.path.abspath(__file__))

background_color = '#1075a9'
foreground_color = '#ddffaa'

root = Tk()
iconpath = os.path.join(base_dir, 'bobAgiota.ico')
root.iconbitmap(iconpath)
root.geometry('500x400')
root.title('Banquin do Bob')
root.configure(bg=background_color)

class StartScreen(Frame):
    def __init__(self, master:Tk) -> None:    
        Frame.__init__(self, master)      
        import os 
        base_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(base_dir, "bobAgiota.png")
        self.caminho_imagem = Image.open(image_path)

        self.configure(bg=background_color)

        self.imagem = ImageTk.PhotoImage(self.caminho_imagem.resize((180,180)))

        frameForm = Frame(self, bg=background_color)

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

        lbl_imagem = Label(self, image=self.imagem, bg=background_color)

        lbl_text = Label(self, text="Banco do Bob Agiota", bg=background_color, fg=foreground_color, font='Helvetica 18 bold')
        lbl_imagem.grid()
        lbl_text.grid()
        frameForm.grid()

app = StartScreen(root)
app.grid()

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
root.mainloop()