import tkinter as tk
from ui.tela_config import TelaConfig
from core.plugins import carregar_esportes


class TelaInicio:

    def __init__(self, root):

        self.root = root

        self.frame = tk.Frame(root)
        self.frame.pack(expand=True)

        tk.Label(
            self.frame,
            text="Selecionar Esporte",
            font=("Arial", 20)
        ).pack(pady=20)

        esportes = carregar_esportes()

        for esporte in esportes:

            tk.Button(
                self.frame,
                text=esporte["nome"],
                width=20,
                height=2,
                command=lambda e=esporte: self.abrir_config(e)
            ).pack(pady=5)

    def abrir_config(self, esporte):

        self.frame.destroy()

        TelaConfig(self.root, esporte)