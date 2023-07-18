from tkinter import *
from tkinter import ttk
from utils import (
    ScrollableFrame, 
    GridScrollableFrame, 
    CepEntry, 
    CpfEntry, 
    DateEntry, 
    PhoneEntry, 
    MaskedEntry,
)
import os

base_dir = os.path.dirname(os.path.abspath(__file__))

background_color = '#1075a9'
foreground_color = '#ddffaa'
canvas_bg = '#f00000'
intern_bg = '#0000ff'

class Register:
    def __init__(self, master: Tk):
        self.janela = master

        iconpath = os.path.join(base_dir, 'bobAgiota.ico')
        self.janela.iconbitmap(iconpath)
        self.janela.geometry('700x600')
        self.janela.title('Banquin do Bob')
        self.janela.configure(bg=background_color)

        # criação dos elementos de um scrollable_frame
        self.frame_Canvas = Frame(self.janela, relief='groove', borderwidth=2, bg=background_color)
        self.canvas = Canvas(self.frame_Canvas, bg=canvas_bg, height=250)
        self.scrollable_frame = Frame(self.canvas)
        self.scroll = Scrollbar(self.frame_Canvas, orient='vertical', command=self.canvas.yview)
        
        # configuração dos widgets do scrollable_frame
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scroll.set)
        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)

        # apresentação na tela dos elementos da scrollable_frame, o próprio scrollable_frame n recebe um pack
        self.scroll.grid(row=0, column=1, sticky=NS)
        self.canvas.grid(row=0, column=0, sticky=NSEW)

        self.frame_Canvas.grid()

        self.frame_widgets = Frame(self.janela, relief='groove', borderwidth=2, bg=background_color) 
        # self.frame_widgets = Frame(self.scrollable_frame, relief='groove', borderwidth=2, bg=canvas_bg) 

        infPessoa = Label(self.frame_widgets, text="Informações Pessoais", bg=intern_bg, relief='groove')
        infPessoa.grid(row=0, column=0, columnspan=99, sticky=NSEW)

        lbl_nome = Label(self.frame_widgets, text="Nome: ", bg=intern_bg)
        lbl_nome.grid(row=1, column=0, sticky=W)
        ent_nome = Entry(self.frame_widgets)
        ent_nome.grid(row=2, column=0, columnspan=4, sticky=EW, padx=(1, 2))
        
        lbl_cpf = Label(self.frame_widgets, text="CPF: ", bg=intern_bg)
        lbl_cpf.grid(row=1, column=4, sticky=W, padx=2)
        ent_cpf = CpfEntry(self.frame_widgets)
        ent_cpf.grid(row=2, column=4, columnspan=2, sticky=EW, padx=2)

        lbl_rg = Label(self.frame_widgets, text="RG: ", bg=intern_bg)
        lbl_rg.grid(row=5, column=4, sticky=W)
        ent_rg = Entry(self.frame_widgets)
        ent_rg.grid(row=6, column=4, padx=(0, 2))

        # frame_estado_civil = Frame(self.frame_widgets, bg=background_color)
        frame_estado_civil = Frame(self.frame_widgets, bg=canvas_bg)
        lbl_estado_civil = Label(frame_estado_civil, text="Estado Civil", bg=intern_bg)
        lbl_estado_civil.grid(row=0, column=0, sticky=W)
        estado_civil = ttk.Combobox(frame_estado_civil,)
        estado_civil.grid(row=1, column=0, columnspan=2)
        frame_estado_civil.grid(row=5, column=0, columnspan=2, rowspan=2)


        # frame_sexo = Frame(self.frame_widgets, bg=background_color)
        frame_sexo = Frame(self.frame_widgets, bg=canvas_bg)
        lbl_sexo = Label(frame_sexo, text='Sexo: ', bg=intern_bg)
        lbl_sexo.grid(row=0, column=0, sticky=W)
        self.sexo = StringVar(frame_sexo, 'NONE')
        # sex_masc = Radiobutton(frame_sexo, text="Masculino", variable=self.sexo, value='masc', bg=background_color)
        sex_masc = Radiobutton(frame_sexo, text="Masculino", variable=self.sexo, value='masc', bg=canvas_bg)
        sex_masc.grid(row=1, column=0)
        # sex_fem = Radiobutton(frame_sexo, text="Feminino", variable=self.sexo, value='fem', bg=background_color)
        sex_fem = Radiobutton(frame_sexo, text="Feminino", variable=self.sexo, value='fem', bg=canvas_bg)
        sex_fem.grid(row=1, column=1)
        frame_sexo.grid(row=5, column=2, columnspan=2, rowspan=2)

        lbl_email = Label(self.frame_widgets, text="Email: ", bg=intern_bg)
        lbl_email.grid(row=7, column=0, sticky=W)
        ent_email = Entry(self.frame_widgets)
        ent_email.grid(row=8, column=0, columnspan=3, sticky=EW)

        lbl_phone = Label(self.frame_widgets, text="Phone: ", bg=intern_bg)
        lbl_phone.grid(row=7, column=3, sticky=W, padx=(10, 0))
        ent_phone = PhoneEntry(self.frame_widgets)
        ent_phone.grid(row=8, column=3, columnspan=2, sticky=EW, padx=(10, 40))

        infEnd = Label(self.frame_widgets, text="Informações De Endereço", bg=intern_bg, relief='groove')
        infEnd.grid(row=9, column=0, columnspan=99, sticky=NSEW, pady=(5, 0))

        lbl_cep = Label(self.frame_widgets, text="CEP: ", bg=intern_bg)
        lbl_cep.grid(row=10, column=0, sticky=W)
        ent_cep = CepEntry(self.frame_widgets)
        ent_cep.grid(row=11, column=0, columnspan=2, sticky=EW)

        lbl_rua = Label(self.frame_widgets, text="Rua: ", bg=intern_bg)
        lbl_rua.grid(row=10, column=2, sticky=W, padx=10)
        ent_rua = Entry(self.frame_widgets)
        ent_rua.grid(row=11, column=2, columnspan=3, sticky=EW, padx=10)        

        lbl_bairro = Label(self.frame_widgets, text="Bairro: ", bg=intern_bg)
        lbl_bairro.grid(row=12, column=0, sticky=W)
        ent_bairro = Entry(self.frame_widgets)
        ent_bairro.grid(row=13, column=0, columnspan=3, sticky=EW)    

        lbl_comp = Label(self.frame_widgets, text="Complemento: ", bg=intern_bg)
        lbl_comp.grid(row=12, column=3, sticky=W, padx=5)
        ent_comp = Entry(self.frame_widgets)
        ent_comp.grid(row=13, column=3, columnspan=3, sticky=EW, padx=5)    

        lbl_num = Label(self.frame_widgets, text="Número: ", bg=intern_bg)
        lbl_num.grid(row=14, column=0, sticky=W)
        ent_num = Entry(self.frame_widgets)
        ent_num.grid(row=15, column=0, columnspan=2, sticky=EW)   
            
        # frame_estado = Frame(self.frame_widgets, bg=background_color)
        frame_estado = Frame(self.frame_widgets, bg=canvas_bg)
        lbl_estado = Label(frame_estado, text="Estado: ", bg=intern_bg)
        lbl_estado.grid(row=0, column=0, sticky=W)
        estado = ttk.Combobox(frame_estado,)
        estado.grid(row=1, column=0, columnspan=2)
        frame_estado.grid(row=14, column=2, columnspan=2, rowspan=2)

        lbl_cidade = Label(self.frame_widgets, text="Cidade: ", bg=intern_bg)
        lbl_cidade.grid(row=14, column=4, sticky=W)
        ent_cidade = Entry(self.frame_widgets)
        ent_cidade.grid(row=15, column=4, columnspan=2, sticky=EW) 

        lbl_cep2 = Label(self.frame_widgets, text="CEP2: ", bg=intern_bg)
        lbl_cep2.grid(row=15, column=0, sticky=W)
        ent_cep2 = MaskedEntry(self.frame_widgets, "99.999-999")
        ent_cep2.grid(row=16, column=0, columnspan=2, sticky=EW)


        self.frame_widgets.grid()
        self.janela.grid_rowconfigure(0, weight=1)
        self.janela.grid_columnconfigure(0, weight=1)
        
    
    def on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")


app = Tk()
master = Register(app)
app.mainloop()