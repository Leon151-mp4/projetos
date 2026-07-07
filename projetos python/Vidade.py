import customtkinter as ctk

app = ctk.CTk()
app.title("verificar idade")
app.geometry("400x500")
#Seu Madruga Batendo em Dona Florinda por Vingança Aleia kkkkkk.....
def SMBDFVA():

    return voando == "" or voando.isdigite()



Chegou_o_disco_voador = app.register(SMBDFVA)


def LOTERIAAAAHHH():

    idade = voando.get()
    if idade > "":
        kiko.configure(text="sua idade é kiko")
        voando.delete(0,"end")
        voando.focus()


    else:
        voando.delete(0, "end")
        voando.focus()
        kiko.configure(text=f'sua idade é {idade}')



#20kg de cimento CHIQUINHA...............................................
texto = ctk.CTkLabel(app, text="Verifique sua idade.", font=("Arial", 29))
texto.pack(pady=50, padx=50)

#VOANDO................................................CHEGAMOS AO PLANETA KIKO ONDE HÁ SERES SEM CEREBRO................................................#meme
voando = ctk.CTkEntry(app, placeholder_text="Insira sua idade.",
                       height=75, width=290, corner_radius=25,
                       fg_color="blue", font=("Arial",24), text_color="black", validatecommand=(Chegou_o_disco_voador, "%P"))
voando.pack()

#kiko kikando.....................................................
kiko = ctk.CTkLabel (app, text="Aguardando...", font=("Arial", 24))
kiko.pack(pady=10)
#chaves.....................O REI DO CORTIÇO....................................
chaves = ctk.CTkButton(app,text="Concluir", width=200, height=100, font=("Arial", 24), command=LOTERIAAAAHHH)
chaves.pack(pady=50)






app.mainloop()