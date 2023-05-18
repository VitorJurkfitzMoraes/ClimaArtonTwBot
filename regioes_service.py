import pandas as pd
import random
import datetime
from sorteador_service import SorteadorService
from definicoes_service import DefinicoesService

class RegioesService:

    def importarRegioes():
        regioes = pd.read_csv('regioes.txt', sep="/")
        regioes["Regiao"] = regioes["Regiao"].str.replace("=","",regex=True)
        regioes["Pronome"] = regioes["Pronome"].str.replace("=","",regex=True)
        return regioes
    
    def importarTemperaturas():
        temperaturas = pd.read_csv('regioes_ult_temperatura.txt', sep="/")
        return temperaturas
    
    def calcularRandomico():
        rand = (random.random()-0.5)*10
        return rand
    
    def gerarRegioes():
        df = RegioesService.importarRegioes()
        listaRegioes = SorteadorService.sortearValor(df["ID"], df["MP"], 3)

        df_temp = RegioesService.importarTemperaturas()

        #Conecta arquivos
        df = pd.concat([df, df_temp], axis=1, join="inner")
        df = df.query('ID in @listaRegioes')
        
        return df
    
    def variarTempeturaRegioes(df):      
        #Varia Temperaturas
        df["UltTemp"] = round(df["Temp"],0)
        df["Temp"] = round(df["UltTemp"] + (df["TVar"] * RegioesService.calcularRandomico()),0)
        df["MaxTemp"] = round(df["Temp"] + (2.5 * df["TVar"]),0)
        df["MinTemp"] = round(df["Temp"] - (2.5 * df["TVar"]),0)

        df = df[["ID","Regiao","Pronome","Especial","UltTemp","Temp","MaxTemp","MinTemp"]]

        return df

    def gerarEventos(especial : str, min : int, max : int):
            evento = random.choice([1,2,3,4,5,6])
            if evento <= 4 :
                texto = DefinicoesService.definirTempoClima(max)
            elif evento >= 5:
                match especial:
                    case "C":
                        texto = DefinicoesService.definirEventoCaos() + ". Talvez " + DefinicoesService.definirAgenteCaos() + " tenha " + DefinicoesService.definirCausaCaos()
                    case "E":
                        texto = DefinicoesService.definirEventoCaos() + ". Talvez " + DefinicoesService.definirAgenteCaos() + " tenha " + DefinicoesService.definirCausaCaos()                  
                    case "I":
                        texto = DefinicoesService.definirEventoCaos() + ". Talvez " + DefinicoesService.definirAgenteCaos() + " tenha " + DefinicoesService.definirCausaCaos()            
                    case "D":
                        texto = DefinicoesService.definirEventoCaosDeserto() + ". Talvez " + DefinicoesService.definirAgenteCaosDeserto() + " tenha " + DefinicoesService.definirCausaCaos()
                    case "F":
                        texto = DefinicoesService.definirEventoCaosFloresta() + ". Talvez " + DefinicoesService.definirAgenteCaosFloresta() + " tenha " + DefinicoesService.definirCausaCaos()                
            return texto
    
    def montarIntrodução():
        texto : str
        texto = DefinicoesService.definirTurno()
        texto += ", "
        texto += DefinicoesService.definirVocativo()
        texto += "!\n"
        texto += "\no Clima em Arton :\n"

        return texto
    
    def montarTextoRegiao(df):
        evento = RegioesService.gerarEventos(df["Especial"], df["MinTemp"], df["MaxTemp"])
        texto = df["Pronome"] + " " + df["Regiao"] + ", " + evento

        return texto

    def montarTexto():
        df = RegioesService.gerarRegioes()

        df1 = df.iloc[0]
        df1 = RegioesService.variarTempeturaRegioes(df1)
        df2 = df.iloc[1]
        df2 = RegioesService.variarTempeturaRegioes(df2)
        df3 = df.iloc[2]
        df3 = RegioesService.variarTempeturaRegioes(df3)

        texto = RegioesService.montarIntrodução()
        texto += "\n"
        texto += RegioesService.montarTextoRegiao(df1)
        texto += "\n"
        texto += RegioesService.montarTextoRegiao(df2)
        texto += "\n"
        texto += RegioesService.montarTextoRegiao(df3)

        return texto    