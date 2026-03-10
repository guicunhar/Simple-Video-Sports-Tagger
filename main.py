import tkinter as tk
from ui.tela_inicio import TelaInicio

root = tk.Tk()
root.title("Sports Tagger")
root.geometry("900x600")

app = TelaInicio(root)

root.mainloop()