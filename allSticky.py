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
canvas_bg = '#f10000'
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
        self.canvas = Canvas(self.frame_Canvas, bg=canvas_bg, height=250, width=500)
        self.scrollable_frame = Frame(self.canvas)
        self.scroll = Scrollbar(self.frame_Canvas, orient='vertical', command=self.canvas.yview)
        
        # configuração dos widgets do scrollable_frame
        self.canvas_frame = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scroll.set)
        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)

        # apresentação na tela dos elementos da scrollable_frame, o próprio scrollable_frame n recebe um pack
        self.scroll.grid(row=0, column=1, sticky=NS)
        self.canvas.grid(row=0, column=0, sticky=NSEW)

        self.frame_Canvas.grid()

        # self.frame_widgets = Frame(self.janela, relief='groove', borderwidth=2, bg=background_color) 
        self.frame_widgets = Frame(self.scrollable_frame, relief='groove', borderwidth=2, bg=canvas_bg) 

        infPessoa = Label(self.frame_widgets, text="Informações Pessoais", bg=intern_bg, relief='groove')
        infPessoa.grid(columnspan=99, sticky=NSEW, pady=2)

        self.lbl_nome = Label(self.frame_widgets, text="Nome* ", bg=intern_bg)
        self.lbl_nome.grid(row=1, column=0, sticky=NSEW, pady=2)
        self.ent_nome = Entry(self.frame_widgets)
        self.ent_nome.grid(row=2, column=0, columnspan=4, sticky=EW, padx=(1, 2))
        
        self.lbl_cpf = Label(self.frame_widgets, text="CPF* ", bg=intern_bg)
        self.lbl_cpf.grid(row=1, column=4, sticky=NSEW, padx=2, pady=2)
        self.ent_cpf = CpfEntry(self.frame_widgets)
        self.ent_cpf.grid(row=2, column=4, columnspan=2, sticky=EW, padx=2)

        self.lbl_rg = Label(self.frame_widgets, text="RG* ", bg=intern_bg)
        self.lbl_rg.grid(row=5, column=4, sticky=NSEW, padx=2, pady=2)
        self.ent_rg = Entry(self.frame_widgets)
        self.ent_rg.grid(row=6, column=4, padx=2)

        frame_estado_civil = Frame(self.frame_widgets, bg=canvas_bg)
        self.lbl_estado_civil = Label(frame_estado_civil, text="Estado Civil*", bg=intern_bg)
        self.lbl_estado_civil.grid(row=0, column=0, sticky=NSEW, pady=2)
        estados_civis = (
            'Solteiro (a)', 
            'Casado (a)', 
            'Viúvo (a)', 
            'Separado (a)', 
            'Divorciado (a)',
            'Outro'
        )
        # self.estado_civil = ttk.Combobox(frame_estado_civil, values=estados_civis, state='readonly')
        self.estado_civil = ttk.Combobox(frame_estado_civil)
        self.estado_civil['values'] = estados_civis
        self.estado_civil['state'] = 'readonly'
        self.estado_civil.grid(row=1, column=0, columnspan=2)
        frame_estado_civil.grid(row=5, column=0, columnspan=2, rowspan=2)


        frame_sexo = Frame(self.frame_widgets, bg=canvas_bg)
        self.lbl_sexo = Label(frame_sexo, text='Sexo* ', bg=intern_bg)
        self.lbl_sexo.grid(row=0, column=0, sticky=NSEW, pady=2)
        self.sexoVar = IntVar(value=0)
        self.sex_masc = Radiobutton(frame_sexo, text="Masculino", variable=self.sexoVar, value=1, bg=canvas_bg)
        self.sex_masc.grid(row=1, column=0)
        self.sex_fem = Radiobutton(frame_sexo, text="Feminino", variable=self.sexoVar, value=2, bg=canvas_bg)
        self.sex_fem.grid(row=1, column=1)
        frame_sexo.grid(row=5, column=2, columnspan=2, rowspan=2)

        self.lbl_email = Label(self.frame_widgets, text="Email* ", bg=intern_bg)
        self.lbl_email.grid(row=7, column=0, sticky=NSEW, pady=2)
        self.ent_email = Entry(self.frame_widgets)
        self.ent_email.grid(row=8, column=0, columnspan=3, sticky=EW)

        self.lbl_phone = Label(self.frame_widgets, text="Phone* ", bg=intern_bg)
        self.lbl_phone.grid(row=7, column=3, sticky=NSEW, padx=(10, 0), pady=2)
        self.ent_phone = PhoneEntry(self.frame_widgets)
        self.ent_phone.grid(row=8, column=3, columnspan=2, sticky=EW, padx=(10, 40))

        infEnd = Label(self.frame_widgets, text="Informações De Endereço", bg=intern_bg, relief='groove')
        infEnd.grid(columnspan=99, sticky=NSEW, pady=(5, 0))

        self.lbl_cep = Label(self.frame_widgets, text="CEP* ", bg=intern_bg)
        self.lbl_cep.grid(row=10, column=0, sticky=NSEW, pady=2)
        self.ent_cep = CepEntry(self.frame_widgets)
        self.ent_cep.grid(row=11, column=0, columnspan=2, sticky=EW)

        self.lbl_rua = Label(self.frame_widgets, text="Rua* ", bg=intern_bg)
        self.lbl_rua.grid(row=10, column=2, sticky=NSEW, padx=10, pady=2)
        self.ent_rua = Entry(self.frame_widgets)
        self.ent_rua.grid(row=11, column=2, columnspan=3, sticky=EW, padx=(10, 5))        

        self.lbl_bairro = Label(self.frame_widgets, text="Bairro* ", bg=intern_bg)
        self.lbl_bairro.grid(row=12, column=0, sticky=NSEW, pady=2)
        self.ent_bairro = Entry(self.frame_widgets)
        self.ent_bairro.grid(row=13, column=0, columnspan=3, sticky=EW)    

        self.lbl_comp = Label(self.frame_widgets, text="Complemento* ", bg=intern_bg)
        self.lbl_comp.grid(row=12, column=3, sticky=NSEW, padx=5, pady=2)
        self.ent_comp = Entry(self.frame_widgets)
        self.ent_comp.grid(row=13, column=3, columnspan=3, sticky=EW, padx=5)    

        self.lbl_num = Label(self.frame_widgets, text="Número* ", bg=intern_bg)
        self.lbl_num.grid(row=14, column=0, sticky=NSEW, pady=2)
        self.ent_num = Entry(self.frame_widgets)
        self.ent_num.grid(row=15, column=0, columnspan=2, sticky=EW)   
            
        frame_estado = Frame(self.frame_widgets, bg=canvas_bg)
        self.lbl_estado = Label(frame_estado, text="Estado*", bg=intern_bg)
        self.lbl_estado.grid(row=0, column=0, sticky=NSEW, pady=2)
        estados = ('AC', 'AL', 'AP', 'AM', 'BA', 'CE', 
                                     'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 
                                     'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 
                                     'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 
                                     'SP', 'SE', 'TO')
        self.unidade_federal = ttk.Combobox(frame_estado, values=estados, state='readonly')
        self.unidade_federal.grid(row=1, column=0)
        frame_estado.grid(row=14, column=2, rowspan=2, padx=(5, 0))

        self.lbl_cidade = Label(self.frame_widgets, text="Cidade* ", bg=intern_bg)
        self.lbl_cidade.grid(row=14, column=3, sticky=NSEW, padx=5, pady=2)
        self.ent_cidade = Entry(self.frame_widgets)
        self.ent_cidade.grid(row=15, column=3, columnspan=3, sticky=EW, padx=5) 

        infFin = Label(self.frame_widgets, text="Informações De Endereço", bg=intern_bg, relief='groove')
        infFin.grid(row=16, column=0, columnspan=99, sticky=NSEW, pady=(5, 0))

        self.lbl_prof = Label(self.frame_widgets, text="Profissão* ", bg=intern_bg)
        self.lbl_prof.grid(row=17, sticky=NSEW, pady=2)
        self.ent_prof = Entry(self.frame_widgets)
        self.ent_prof.grid(row=18, columnspan=2, sticky=EW) 

        self.lbl_renda = Label(self.frame_widgets, text="Renda Mensal* ", bg=intern_bg)
        self.lbl_renda.grid(row=17, column=2, sticky=NSEW, padx=5, pady=2)
        self.ent_renda = Entry(self.frame_widgets)
        self.ent_renda.grid(row=18, column=2, columnspan=2, sticky=EW, padx=5) 

        # b = Button(self.frame_widgets, text='Imprime Ai', command=self.printAll)
        # b.grid()

        self.frame_widgets.grid()

        self.janela.update_idletasks()
        wid = self.frame_widgets.winfo_width()
        self.canvas.configure(width=wid)

        self.janela.grid_rowconfigure(0, weight=1)
        self.janela.grid_columnconfigure(0, weight=1)
        
    
    def on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def changeCanvasSize(self, event):
        canvas_width = 500
        self.canvas.itemconfig(self.canvas_frame, width=canvas_width)
    
    def getInfos(self):
        self.nome = self.ent_nome.get()
        self.cpf = self.ent_cpf.get()
        self.estadoCivil = self.estado_civil.get()
        self.sexo = self.sexoVar.get()
        self.rg = self.ent_rg.get()
        self.email = self.ent_email.get()
        self.celular = self.ent_phone.get()

        self.cep = self.ent_cep.get()
        self.rua = self.ent_rua.get()
        self.bairro = self.ent_bairro.get()
        self.complemento = self.ent_comp.get()
        self.estado = self.unidade_federal.get()
        self.cidade = self.ent_cidade.get()
    
    def printAll(self):
        self.getInfos()
        if self.nome and self.cpf and self.estadoCivil and self.sexo and self.rg and self.email and self.celular:
            print(self.nome, self.cpf, self.estadoCivil, self.sexo, self.rg, self.email, self.celular)
        else:
            print(bool(self.nome), bool(self.cpf), bool(self.estadoCivil), bool(self.sexo), bool(self.rg), bool(self.email), bool(self.celular))
            print(self.estadoCivil)
        if self.cep and self.rua and self.bairro and self.complemento and self.estado and self.cidade:
            print(self.cep, self.rua, self.bairro, self.complemento, self.estado, self.cidade)
        else:
            print("Segundo nope")


app = Tk()
master = Register(app)
app.mainloop()