import tkinter as tk
from core.eventos import salvar_evento


class TelaTagger:

    def __init__(self, root, partida, esporte):

        self.root = root
        self.partida = partida
        self.esporte = esporte

        self.eventos = esporte["eventos"]
        self.zonas = esporte["zonas"]
        self.zonas_extras = esporte["zonas_extras"]

        self.jogador = None
        self.equipe = None
        self.tipo = None
        self.subtipo = None
        self.parte_corpo = None

        self.zona_propria = None
        self.zona_adv = None

        self.frame = tk.Frame(root)
        self.frame.pack()

        root.bind("<Return>", lambda e: self.registrar())

        # -----------------
        # PLACAR
        # -----------------

        self.placar = tk.Label(self.frame, font=("Arial", 20))
        self.placar.pack(pady=10)

        self.atualizar_placar()

        # -----------------
        # JOGADORES
        # -----------------

        frame_jog = tk.LabelFrame(self.frame, text="Jogador")
        frame_jog.pack(pady=5)

        for j in partida.jogadores:

            btn = tk.Button(
                frame_jog,
                text=j,
                width=20,
                command=lambda x=j: self.selecionar_jogador(x)
            )

            btn.pack(side="left", padx=5)

        # -----------------
        # EVENTOS
        # -----------------

        self.frame_eventos = tk.LabelFrame(self.frame, text="Evento")
        self.frame_eventos.pack(pady=5)

        for ev in self.eventos.keys():

            btn = tk.Button(
                self.frame_eventos,
                text=ev,
                width=15,
                command=lambda x=ev: self.selecionar_evento(x)
            )

            btn.pack(side="left", padx=5)

        # -----------------
        # RESULTADO
        # -----------------

        self.frame_resultado = tk.LabelFrame(self.frame, text="Resultado")
        self.frame_resultado.pack(pady=5)

        # -----------------
        # PARTE DO CORPO
        # -----------------

        self.frame_corpo = tk.LabelFrame(self.frame, text="Parte do Corpo")
        self.frame_corpo.pack(pady=5)

        # -----------------
        # ZONAS
        # -----------------

        quadras = tk.Frame(self.frame)
        quadras.pack(pady=10)

        self.frame_propria = tk.LabelFrame(quadras, text="Quadra Própria")
        self.frame_propria.grid(row=0, column=0, padx=20)

        self.frame_adv = tk.LabelFrame(quadras, text="Quadra Adversária")
        self.frame_adv.grid(row=0, column=1, padx=20)

        self.criar_grid(self.frame_propria, self.selecionar_propria)
        self.criar_grid(self.frame_adv, self.selecionar_adv)

        # -----------------
        # BOTÃO REGISTRAR
        # -----------------

        self.botao = tk.Button(
            self.frame,
            text="Registrar (ENTER)",
            height=2,
            width=25,
            command=self.registrar
        )

        self.botao.pack(pady=10)

        self.status = tk.Label(self.frame, text="")
        self.status.pack()

    # -----------------

    def atualizar_placar(self):

        self.placar["text"] = (
            f"{self.partida.equipe1} {self.partida.placar1} x "
            f"{self.partida.placar2} {self.partida.equipe2}"
        )

    # -----------------

    def selecionar_jogador(self, jogador_sel):

        jogador, equipe = jogador_sel.split(" - ")

        self.jogador = jogador
        self.equipe = equipe

        self.status["text"] = f"Jogador: {jogador}"

    # -----------------

    def selecionar_evento(self, evento):

        self.tipo = evento
        self.subtipo = None

        for w in self.frame_resultado.winfo_children():
            w.destroy()

        evento_dict = self.eventos[evento]

        for k in evento_dict:

            if k == "campos":
                continue

            btn = tk.Button(
                self.frame_resultado,
                text=k,
                width=12,
                command=lambda x=k: self.selecionar_subtipo(x)
            )

            btn.pack(side="left", padx=4)

        # campos extras

        for w in self.frame_corpo.winfo_children():
            w.destroy()

        if "campos" in evento_dict:

            if "parte_corpo" in evento_dict["campos"]:

                for p in evento_dict["campos"]["parte_corpo"]:

                    btn = tk.Button(
                        self.frame_corpo,
                        text=p,
                        width=12,
                        command=lambda x=p: self.selecionar_corpo(x)
                    )

                    btn.pack(side="left", padx=4)

    # -----------------

    def selecionar_subtipo(self, subtipo):

        self.subtipo = subtipo
        self.status["text"] = f"{self.tipo} - {subtipo}"

    # -----------------

    def selecionar_corpo(self, corpo):

        self.parte_corpo = corpo
        self.status["text"] = f"{self.tipo} {self.subtipo} ({corpo})"

    # -----------------

    def selecionar_propria(self, zona):

        self.zona_propria = zona
        self.status["text"] = f"Quadra própria: {zona}"

    # -----------------

    def selecionar_adv(self, zona):

        self.zona_adv = zona
        self.status["text"] = f"Quadra adversária: {zona}"

    # -----------------

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

    # -----------------

    def registrar(self):

        if not self.jogador:
            self.status["text"] = "Selecione jogador"
            return

        if not self.tipo:
            self.status["text"] = "Selecione evento"
            return

        if not self.subtipo:
            self.status["text"] = "Selecione resultado"
            return

        if not self.zona_propria or not self.zona_adv:
            self.status["text"] = "Selecione zonas"
            return

        regra = self.eventos[self.tipo][self.subtipo]

        # pontuação

        if regra == "ponto_proprio":

            if self.equipe == self.partida.equipe1:
                self.partida.placar1 += 1
            else:
                self.partida.placar2 += 1

        elif regra == "ponto_adversario":

            if self.equipe == self.partida.equipe1:
                self.partida.placar2 += 1
            else:
                self.partida.placar1 += 1

        self.atualizar_placar()

        salvar_evento(
            self.jogador,
            self.equipe,
            self.tipo,
            self.subtipo,
            self.parte_corpo,
            self.zona_propria,
            self.zona_adv,
            self.partida.placar1,
            self.partida.placar2
        )

        self.status["text"] = f"{self.jogador} | {self.tipo} {self.subtipo}"

        self.zona_propria = None
        self.zona_adv = None