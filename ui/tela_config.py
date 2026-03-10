import tkinter as tk
from ui.tela_tagger import TelaTagger
from core.partida import Partida

class TelaConfig:

    def __init__(self, root, esporte):

        self.root = root
        self.esporte = esporte

        self.frame = tk.Frame(root)
        self.frame.pack(pady=20)

        tk.Label(self.frame, text="Equipe 1").grid(row=0, column=0)

        self.equipe1 = tk.Entry(self.frame)
        self.equipe1.grid(row=1, column=0)

        tk.Label(self.frame, text="Jogador 1").grid(row=2, column=0)
        self.j1 = tk.Entry(self.frame)
        self.j1.grid(row=3, column=0)

        tk.Label(self.frame, text="Jogador 2").grid(row=4, column=0)
        self.j2 = tk.Entry(self.frame)
        self.j2.grid(row=5, column=0)

        tk.Label(self.frame, text="Equipe 2").grid(row=0, column=1)

        self.equipe2 = tk.Entry(self.frame)
        self.equipe2.grid(row=1, column=1)

        tk.Label(self.frame, text="Jogador 1").grid(row=2, column=1)
        self.j3 = tk.Entry(self.frame)
        self.j3.grid(row=3, column=1)

        tk.Label(self.frame, text="Jogador 2").grid(row=4, column=1)
        self.j4 = tk.Entry(self.frame)
        self.j4.grid(row=5, column=1)

        tk.Button(
            self.frame,
            text="Iniciar Partida",
            command=self.iniciar
        ).grid(row=6, column=0, columnspan=2, pady=20)

    def iniciar(self):

        equipe1 = self.equipe1.get()
        equipe2 = self.equipe2.get()

        jogadores = [
            f"{self.j1.get()} - {equipe1}",
            f"{self.j2.get()} - {equipe1}",
            f"{self.j3.get()} - {equipe2}",
            f"{self.j4.get()} - {equipe2}",
        ]

        partida = Partida(equipe1, equipe2, jogadores)

        self.frame.destroy()

        TelaTagger(self.root, partida,self.esporte)