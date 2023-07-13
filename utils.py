import tkinter as tk
from tkinter import ttk
from re import sub

class ScrollableFrame(tk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.canvas = tk.Canvas(self)
        scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        self.canvas.configure(yscrollcommand=scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

class DateEntry(tk.Entry):
    def __init__(self, master, *args, **kwargs):
        super(DateEntry, self).__init__(master, *args, **kwargs)
        mycmd = (self.register(self.valida), '%d', '%P')
        # inval = self.register(self.invalido)  # -- não necessário criar uma de ivcmd
        self.text = tk.StringVar()
        self.ent = tk.Entry(self)
        self.ent.configure(validate='key', validatecommand=mycmd, textvariable=self.text)
        self.configure(validate='key', validatecommand=mycmd, textvariable=self.text)
        self.pack()
    
    def onlyDigit(self, string):
        subs = sub('[^0-9]', '', string)
        if str.isdigit(subs):
            return True
        return False

    def valida(self, d, String_after):
        size = len(String_after)
        if (self.onlyDigit(String_after) or String_after=="") and size <= 10:
            if (size == 2 or size == 5) and d == '-1':
                    self.insertEnd("/")
            return True
        return False
        
    def insertEnd(self, char):
        self.insert(tk.END, char)
        return True

class CpfEntry(tk.Entry):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        mycmd = (self.register(self.valida), '%d', '%P')
        # inval = self.register(self.invalido)  # -- não necessário criar uma de ivcmd
        self.text = tk.StringVar()
        self.ent = tk.Entry(self)
        self.ent.configure(validate='key', validatecommand=mycmd, textvariable=self.text)
        self.configure(validate='key', validatecommand=mycmd, textvariable=self.text)
        self.pack()
    
    def onlyDigit(self, string):
        subs = sub('[^0-9]', '', string)
        if str.isdigit(subs):
            return True
        return False

    def valida(self, d, String_after):
        size = len(String_after)
        if (self.onlyDigit(String_after) or String_after=="") and size <= 14:
            if (size == 3 or size == 7 or size == 11) and d == '-1':
                self.insertEnd('.' if size < 10 else '-')    
            return True
        else:
            return False
        
    def insertEnd(self, char):
        self.insert(tk.END, char)
        return True

class PhoneEntry(tk.Entry):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        mycmd = (self.register(self.valida), '%d', '%P', '%s')
        # inval = self.register(self.invalido)  # -- não necessário criar uma de ivcmd
        self.text = tk.StringVar()
        self.ent = tk.Entry(self)
        self.ent.configure(validate='key', validatecommand=mycmd, textvariable=self.text)
        self.configure(validate='key', validatecommand=mycmd, textvariable=self.text)
        self.pack()
    
    def onlyDigit(self, string):
        subs = sub('[^0-9]', '', string)
        if str.isdigit(subs):
            return True
        return False

    def valida(self, d, String_after, String_before):
        size_after = len(String_after)
        size_before = len(String_before)
        if (self.onlyDigit(String_after) or String_after=="" or String_after=="(") and size_after <= 15:
            if (size_after == 1 or size_after == 3 or size_after == 10) and d == '-1' and (size_after > size_before or size_after < 2):
                pos = 0 if size_after == 1 else tk.END
                if size_after == 1: char = '(' 
                elif size_after == 3: char = ') ' 
                else: char = '-' 
                self.insertPos(pos, char)    
            return True
        else:
            return False
        
    def insertPos(self, pos, char):
        self.insert(pos, char)
        return True  

class CepEntry(tk.Entry):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        mycmd = (self.register(self.valida), '%d', '%P')
        # inval = self.register(self.invalido)  # -- não necessário criar uma de ivcmd
        self.text = tk.StringVar()
        self.ent = tk.Entry(self)
        self.ent.configure(validate='key', validatecommand=mycmd, textvariable=self.text)
        self.configure(validate='key', validatecommand=mycmd, textvariable=self.text)
        self.pack()
    
    def onlyDigit(self, string):
        subs = sub('[^0-9]', '', string)
        if str.isdigit(subs):
            return True
        return False

    def valida(self, d, String_after):
        size = len(String_after)
        if (self.onlyDigit(String_after) or String_after=="") and size <= 10:
            if (size == 2 or size == 6) and d == '-1':
                pos = tk.END
                char = '.' if size == 2 else '-'
                self.insertPos(pos, char)    
            return True
        else:
            return False
        
    def insertPos(self, pos, char):
        self.insert(pos, char)
        return True  
    
root = tk.Tk()

scrollable = ScrollableFrame(root)

phone = PhoneEntry(scrollable).pack()

scrollable.pack()

root.mainloop()
