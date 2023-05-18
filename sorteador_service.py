import pandas as pd
import random

class SorteadorService:
    def sortearValor(sorteaveis : pd.Series, pesos : pd.Series, k : int):
        sorteados : list[any]
        sorteados = random.choices(population = sorteaveis, weights = pesos, k=1)
        while len(sorteados) < k:
            item = random.choices(population = sorteaveis, weights = pesos, k=1)[0]
            if (item not in sorteados):
                sorteados.append(item)
        return sorteados
    
    def importarRegioes():
        regioes = pd.read_csv('regioes.txt', sep="/")
        regioes["Regiao"] = regioes["Regiao"].str.replace("=","",regex=True)
        regioes["Pronome"] = regioes["Pronome"].str.replace("=","",regex=True)
        return regioes

#SorteadorService(SorteadorService.importarRegioes()["Regiao"],SorteadorService.importarRegioes()["MP"],5)