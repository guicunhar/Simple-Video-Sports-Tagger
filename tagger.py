import tkinter as tk
from esportes import futvolei


def abrir_esporte(event):
    selecionado = lista.get(lista.curselection())

    if selecionado == "Futvôlei":
        root.destroy()
        futvolei.iniciar()


root = tk.Tk()
root.title("Sports Tagger")

tk.Label(
    root,
    text="Selecione o Esporte",
    font=("Arial", 16)
).pack(pady=20)

lista = tk.Listbox(root, height=5, width=25)
lista.pack(pady=10)

# esportes disponíveis
esportes = [
    "Futvôlei"
]

for e in esportes:
    lista.insert(tk.END, e)

# duplo clique abre
lista.bind("<Double-Button-1>", abrir_esporte)

root.mainloop()