import csv
import os

arquivo = "eventos.csv"


# cria arquivo se não existir
if not os.path.exists(arquivo):

    with open(arquivo, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "id",
            "jogador",
            "equipe",
            "tipo",
            "subtipo",
            "parte_corpo",
            "zona_propria",
            "zona_adversaria",
            "placar1",
            "placar2"
        ])


def proximo_id():

    with open(arquivo, "r", encoding="utf-8") as f:
        linhas = list(csv.reader(f))

    return len(linhas)


def salvar_evento(
    jogador,
    equipe,
    tipo,
    subtipo,
    parte_corpo,
    zona1,
    zona2,
    placar1,
    placar2
):

    id_evento = proximo_id()

    with open(arquivo, "a", newline="", encoding="utf-8") as f:

        writer = csv.writer(f)

        writer.writerow([
            id_evento,
            jogador,
            equipe,
            tipo,
            subtipo,
            parte_corpo,
            zona1,
            zona2,
            placar1,
            placar2
        ])