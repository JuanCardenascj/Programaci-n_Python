#Text -- Campo que permite introducir al usuario texto multilinea, se hace del Widget Text
from tkinter import *
root = Tk()

texto_multilineas = Text(root)
texto_multilineas.pack()

root.mainloop()