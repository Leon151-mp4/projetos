import customtkinter as ctk


class app(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x500")
        self.title("calculadora")

        self.b1 = ctk.CTkButton(self, text="clique aqui")
        self.b1.grid(row=0, column=0, padx=20, pady=10)



    def bt(self):
        print("hellow word")






















app = app()
app.mainloop()        