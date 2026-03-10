class Partida:

    def __init__(self, equipe1, equipe2, jogadores_time1, jogadores_time2):

        self.equipe1 = equipe1
        self.equipe2 = equipe2

        self.jogadores_time1 = jogadores_time1
        self.jogadores_time2 = jogadores_time2

        self.placar1 = 0
        self.placar2 = 0

    def ponto(self, equipe):

        if equipe == self.equipe1:
            self.placar1 += 1
        else:
            self.placar2 += 1