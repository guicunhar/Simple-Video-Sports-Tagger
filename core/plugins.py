import json
import os


def carregar_esportes():

    esportes = []

    pasta = "plugins"

    for arquivo in os.listdir(pasta):

        if arquivo.endswith(".json"):

            caminho = os.path.join(pasta, arquivo)

            with open(caminho, encoding="utf-8") as f:

                dados = json.load(f)

                esportes.append(dados)

    return esportes