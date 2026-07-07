import tkinter as tk
from tkinter import ttk

#janela primaria
win = tk.Tk()
win.title("CALCULADORA DE PESSO")
win.geometry("400x500")


#Configurações da janela primaria
style = ttk.Style()
style.theme_use('clam')

#elementos
#ALTURA
label_altura = ttk.Label(win, text="Altura (m):")
label_altura.pack(pady=5)
cam_altura = ttk.Entry(win)
cam_altura.pack(pady=5)

#LARGURA
label_largura = ttk.Label(win, text="Largura (m):")
label_largura.pack(pady=5)
cam_largura = ttk.Entry(win)
cam_largura.pack(pady=5)

#PROFUNDIDADE
label_profundidade = ttk.Label(win, text="Profundidade (m):")
label_profundidade.pack(pady=5)
cam_profundidade = ttk.Entry(win)
cam_profundidade.pack(pady=5)

#resultado
text_resulte = ttk.Label(win, text="Aguardando....")
text_resulte.pack(pady = 10)

def calcular():
    try:
     valor1 = float(cam_altura.get())
     valor2 = float(cam_largura.get())
     valor3 = float(cam_profundidade.get())
     
     peso = float( valor1 * valor2 * valor3 * 400)
     text_resulte.config(text=f"RESULTADO: {peso}")
    except ValueError:
       text_resulte.config(text ="ERROR")

#botão
button = ttk.Button(win, text="Calcular", command= calcular)
button.pack(pady=10)








win.mainloop()







#Anotações:

#Use label para criar inputs