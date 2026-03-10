import tkinter as tk
from tkinter import ttk
import csv
import time

arquivo = "eventos_volei.csv"

# cria arquivo
try:
    open(arquivo, "x").write("tempo,jogador,tipo,zona_propria,zona_adversaria\n")
except:
    pass


zona_propria = None
zona_adv = None


def selecionar_propria(zona):
    global zona_propria
    zona_propria = zona
    status["text"] = f"Quadra própria: {zona}"


def selecionar_adv(zona):
    global zona_adv
    zona_adv = zona
    status["text"] = f"Quadra adversária: {zona}"


def registrar():
    if not zona_propria or not zona_adv:
        status["text"] = "Selecione as duas zonas"
        return

    jogador = jogador_var.get()
    tipo = tipo_var.get()
    tempo = time.strftime("%H:%M:%S")

    with open(arquivo, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([tempo, jogador, tipo, zona_propria, zona_adv])

    status["text"] = f"Registrado: {jogador} | {tipo}"



root = tk.Tk()
root.title("Tagger Vôlei")

# topo
top = tk.Frame(root)
top.pack(pady=10)

tk.Label(top, text="Jogador").grid(row=0, column=0)

jogador_var = tk.StringVar()
jogador = ttk.Combobox(top, textvariable=jogador_var)
jogador["values"] = ["Chau", "Alberto", "J3", "J4", "J5", "J6"]
jogador.grid(row=1, column=0)


tk.Label(top, text="Tipo").grid(row=0, column=1)

tipo_var = tk.StringVar()
tipo = ttk.Combobox(top, textvariable=tipo_var)
tipo["values"] = ["Ponto", "Defesa", "Erro"]
tipo.grid(row=1, column=1)


zonas = [
    ["Frente Esq", "Frente Meio", "Frente Dir"],
    ["Meio Esq", "Meio Meio", "Meio Dir"],
    ["Fundo Esq", "Fundo Meio", "Fundo Dir"]
]


def criar_grid(frame, func):
    for i, linha in enumerate(zonas):
        for j, zona in enumerate(linha):
            btn = tk.Button(
                frame,
                text=zona,
                width=12,
                height=3,
                command=lambda z=zona: func(z)
            )
            btn.grid(row=i, column=j, padx=3, pady=3)


quadras = tk.Frame(root)
quadras.pack()

frame_propria = tk.LabelFrame(quadras, text="Quadra Própria")
frame_propria.grid(row=0, column=0, padx=10)

frame_adv = tk.LabelFrame(quadras, text="Quadra Adversária")
frame_adv.grid(row=0, column=1, padx=10)

criar_grid(frame_propria, selecionar_propria)
criar_grid(frame_adv, selecionar_adv)


botao = tk.Button(root, text="Registrar Jogada", height=2, command=registrar)
botao.pack(pady=10)

status = tk.Label(root, text="")
status.pack()

root.mainloop()