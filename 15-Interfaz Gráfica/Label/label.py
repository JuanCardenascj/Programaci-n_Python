#Label-- Es la etiqueta estática que permiter mostrar texto o imagen
from tkinter import *
root = Tk()
root.title("Saludo")
lbl = Label(root, text="Hola gente")
lbl.pack()
root.mainloop()