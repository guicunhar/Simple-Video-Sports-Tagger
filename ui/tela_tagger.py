import tkinter as tk
from tkinter import ttk
from core.eventos import salvar_evento


class TelaTagger:

    def __init__(self, root, partida, esporte):

        self.root = root
        self.partida = partida
        self.esporte = esporte

        self.eventos = esporte["eventos"]
        self.zonas = esporte["zonas"]
        self.zonas_extras = esporte["zonas_extras"]

        self.zona_propria = None
        self.zona_adv = None

        self.frame = tk.Frame(root)
        self.frame.pack()

        # ENTER registra jogada
        root.bind("<Return>", lambda e: self.registrar())

        # ---------------------
        # PLACAR
        # ---------------------

        self.placar = tk.Label(self.frame, font=("Arial", 20))
        self.placar.pack(pady=10)

        self.atualizar_placar()

        # ---------------------
        # CONTROLES
        # ---------------------

        top = tk.Frame(self.frame)
        top.pack(pady=10)

        # jogador
        tk.Label(top, text="Jogador").grid(row=0, column=0)

        self.jogador = ttk.Combobox(top, state="readonly")
        self.jogador["values"] = partida.jogadores
        self.jogador.grid(row=1, column=0)

        # tipo principal
        tk.Label(top, text="Evento").grid(row=0, column=1)

        self.tipo = ttk.Combobox(top, state="readonly")
        self.tipo["values"] = list(self.eventos.keys())
        self.tipo.grid(row=1, column=1)

        self.tipo.bind("<<ComboboxSelected>>", self.atualizar_subtipos)

        # subtipo
        tk.Label(top, text="Resultado").grid(row=0, column=2)

        self.subtipo = ttk.Combobox(top, state="readonly")
        self.subtipo.grid(row=1, column=2)

        tk.Label(top, text="Parte do Corpo").grid(row=0, column=3)

        self.parte_corpo = ttk.Combobox(top, state="readonly")
        self.parte_corpo.grid(row=1, column=3)

        # ---------------------
        # ZONAS
        # ---------------------

        quadras = tk.Frame(self.frame)
        quadras.pack(pady=10)

        self.frame_propria = tk.LabelFrame(quadras, text="Quadra Própria")
        self.frame_propria.grid(row=0, column=0, padx=20)

        self.frame_adv = tk.LabelFrame(quadras, text="Quadra Adversária")
        self.frame_adv.grid(row=0, column=1, padx=20)

        self.criar_grid(self.frame_propria, self.selecionar_propria)
        self.criar_grid(self.frame_adv, self.selecionar_adv)

        # ---------------------
        # BOTÃO REGISTRAR
        # ---------------------

        self.botao = tk.Button(
            self.frame,
            text="Registrar (ENTER)",
            height=2,
            width=25,
            command=self.registrar
        )

        self.botao.pack(pady=10)

        # status

        self.status = tk.Label(self.frame, text="")
        self.status.pack()

    # ---------------------

    def atualizar_placar(self):

        self.placar["text"] = (
            f"{self.partida.equipe1} {self.partida.placar1} x "
            f"{self.partida.placar2} {self.partida.equipe2}"
        )

    # ---------------------

    def atualizar_subtipos(self, event=None):

        tipo = self.tipo.get()

        evento = self.eventos[tipo]

        subtipos = []

        for k, v in evento.items():
            if k != "campos":
                subtipos.append(k)

        self.subtipo["values"] = subtipos

        if subtipos:
            self.subtipo.current(0)

        # campos extras

        if "campos" in evento and "parte_corpo" in evento["campos"]:

            self.parte_corpo["values"] = evento["campos"]["parte_corpo"]
            self.parte_corpo.current(0)

        else:
            self.parte_corpo.set("")
            self.parte_corpo["values"] = []

    # ---------------------

    def selecionar_propria(self, zona):

        self.zona_propria = zona

        self.status["text"] = f"Quadra própria: {zona}"

    # ---------------------

    def selecionar_adv(self, zona):

        self.zona_adv = zona

        self.status["text"] = f"Quadra adversária: {zona}"

    # ---------------------

    def criar_grid(self, frame, func):

        for i, linha in enumerate(self.zonas):

            for j, zona in enumerate(linha):

                btn = tk.Button(
                    frame,
                    text=zona,
                    width=12,
                    height=3,
                    command=lambda z=zona: func(z)
                )

                btn.grid(row=i, column=j, padx=3, pady=3)

        linha_base = len(self.zonas)

        for i, zona in enumerate(self.zonas_extras):

            btn = tk.Button(
                frame,
                text=zona,
                width=12,
                height=2,
                bg="#dddddd",
                command=lambda z=zona: func(z)
            )

            btn.grid(row=linha_base, column=i, padx=3, pady=3)

    # ---------------------

    def registrar(self):

        if not self.jogador.get():
            self.status["text"] = "Selecione jogador"
            return

        if not self.tipo.get():
            self.status["text"] = "Selecione evento"
            return

        if not self.subtipo.get():
            self.status["text"] = "Selecione resultado"
            return

        if not self.zona_propria or not self.zona_adv:
            self.status["text"] = "Selecione as duas zonas"
            return

        jogador_sel = self.jogador.get()

        jogador, equipe = jogador_sel.split(" - ")

        tipo = self.tipo.get()
        subtipo = self.subtipo.get()
        parte_corpo = self.parte_corpo.get()

        regra = self.eventos[tipo][subtipo]

        # aplicar pontuação

        if regra == "ponto_proprio":

            if equipe == self.partida.equipe1:
                self.partida.placar1 += 1
            else:
                self.partida.placar2 += 1

        elif regra == "ponto_adversario":

            if equipe == self.partida.equipe1:
                self.partida.placar2 += 1
            else:
                self.partida.placar1 += 1

        self.atualizar_placar()

        salvar_evento(
            jogador,
            equipe,
            tipo,
            subtipo,
            parte_corpo,
            self.zona_propria,
            self.zona_adv,
            self.partida.placar1,
            self.partida.placar2
        )

        self.status["text"] = f"{jogador} | {tipo} - {subtipo}"

        # reset zonas

        self.zona_propria = None
        self.zona_adv = None