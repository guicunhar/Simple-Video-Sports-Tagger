class Partida:

    def __init__(self, equipe1, equipe2, jogadores):
        self.equipe1 = equipe1
        self.equipe2 = equipe2
        self.jogadores = jogadores

        self.placar1 = 0
        self.placar2 = 0

    def ponto(self, equipe):

        if equipe == self.equipe1:
            self.placar1 += 1
        else:
            self.placar2 += 1