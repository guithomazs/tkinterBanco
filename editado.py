import tkinter as tk
# from tkinter import ttk
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

        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

class DateEntry(tk.Entry):
    def __init__(self, master, *args, **kwargs):
        super(DateEntry, self).__init__(master, *args, **kwargs)
        mycmd = (self.register(self.valida), '%d', '%P')
        inval = self.register(self.invalido)
        self.text = tk.StringVar()
        self.ent = tk.Entry(self)
        # self.ent.configure(validate='key', validatecommand=mycmd, textvariable=self.text, invalidcommand=self.invalido)
        # self.get_et.configure(validate='key', validatecommand=mycmd, textvariable=self.text, invalidcommand=self.invalido)
        self.configure(validate='key', validatecommand=mycmd, textvariable=self.text, invalidcommand=self.invalido)
        self.pack()
    
    def onlyDigit(self, string):
        subs = sub('[^0-9]', '', string)
        if str.isdigit(subs):
            return True
        return False

    def valida(self, d, String_after):
        if (self.onlyDigit(String_after) or String_after=="") and len(String_after) <= 10:
            if (len(String_after) == 2 or len(String_after) == 5) and d == '-1':
                    self.insertEnd()
            return True
        return False

        
    def insertEnd(self):
        self.insert(tk.END, "/")
        return True
    
    def invalido(self):
        return True
    
    @property
    def get_et(self):
        return self.ent
    
root = tk.Tk()

a = ScrollableFrame(root, bg='blue')
b = DateEntry(a, bg='cyan')

b.pack( padx=5)
a.pack()

root.mainloop()
