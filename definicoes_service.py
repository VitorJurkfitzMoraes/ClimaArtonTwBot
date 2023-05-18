import pandas as pd
import random
import datetime

class DefinicoesService:

    def definirTurno():
        hora_atual = datetime.datetime.now().hour*1
        if hora_atual < 6:
            return "Boa madrugada"
        elif hora_atual < 12:
            return "Bom dia" 
        elif hora_atual < 19:        
            return "Boa tarde"           
        elif hora_atual >= 19:      
            return "Boa noite"     
              
    def definirAdjetivo():
        adjetivo = random.choice([1,2,3,4,5])
        if adjetivo == 1:
            return "nobres"
        elif adjetivo == 2:
            return "plebeus"
        elif adjetivo == 3:
            return "povo"        
        elif adjetivo == 4:
            return "proletários"
        elif adjetivo == 5:
            return "cidadãos"         
        
    def definirVocativo():
        vocativo = random.choice([1,2,3,4,5,6])
        if vocativo == 1:
            return "Artonianos"
        elif vocativo > 1 & vocativo <= 3 :
            texto = DefinicoesService.definirAdjetivo()
            texto += " de Arton"
            return texto 
        elif vocativo >= 4 & vocativo < 6 :
            texto = DefinicoesService.definirAdjetivo()
            texto += " leitores" 
            return texto                              
        elif vocativo == 6:
            return "filhas e filhos de Lena"   

    def definirTipoIntensidade():
        tipoIntensidade = random.choice([1,2,3])
        if tipoIntensidade == 1:
            return "imensa"
        elif tipoIntensidade == 2:
            return "enorme"
        elif tipoIntensidade == 3:
            return "grande"
        
    def definirIntensidade():
        intensidade = random.choice([1,2,3])
        if intensidade == 1:
            return "imensa"
        elif intensidade == 2:
            return "enorme"
        elif intensidade == 3:
            return "grande"    
        
    def definirJornalistas():
        jornalista = random.choice([1,2,3])
        if jornalista == 1:
            return "Nossos jornalistas"
        elif jornalista == 2:
            return "Nossos goblins"
        elif jornalista == 3:
            return "Nossos repórteres"
        
    def definirTempoClima(max : int):
        tempo = random.choice([1,2,3,4,5,6,7,8,9,10,11,12,13])
        if tempo == 1:
            return "um eclipse encobre o sol e a temperatura cai por " + DefinicoesService.definirTempoEventoCaos() + "!"
        elif tempo == 2:
            return "chuva leve com máxima de %d graus." % max 
        elif tempo == 3:
            return "chuva moderada com máxima de %d graus." % max 
        elif tempo == 4:
            return "chuva forte com máxima de %d graus." % max 
        elif tempo == 5:
            return "chove uma tempestade torrencial!"        
        elif tempo == 6:
            return "um tornado vare prédios e plantações. Não saiam à rua!"  
        elif tempo == 7:
            return "uma chuva de sangue rega o solo por " + DefinicoesService.definirTempoEventoCaos() + "!. Seria uma nova área de #Tormenta20 ?!" 
        elif tempo == 8:
            return "faz sol entre nuvens com máxima de %d graus." % max 
        elif tempo == 9:
            max = ((max*0.8)-5)
            return "há uma fortíssima geada e neblina com máxima de %d graus." % max 
        elif tempo == 10:
            max = max*1.1 
            return "há dois sóis com máxima de %d graus." % max
        elif tempo == 11:
            max = max*1.3
            return "há TRÊS sóis com máxima de %d graus." % max
        elif tempo >= 12:
            return "faz sol com máxima de %d graus." % max     
    def definirAgenteCaos():
        agente = random.choice([1,2,3,4,5,6,7,8,9,10,11])
        if agente == 1:
            return "um mago"
        elif agente == 2:
            return "um feiticeiro"
        elif agente == 3:
            return "um bruxo"        
        elif agente == 4:
            return "um dragão"         
        elif agente == 5:
            return "o Gandalf"  
        elif agente == 6:
            return "uma maga"
        elif agente == 7:
            return "uma feiticeira"
        elif agente == 8:
            return "uma bruxa"        
        elif agente == 9:
            return "uma dragoa"         
        elif agente >= 10:
            return "uma deusa, uma louca e uma feiticeira"

    def definirAgenteCaosDeserto():
        agente = random.choice([1,2,3,4])
        if agente == 1:
            return "um mago"
        elif agente == 2:
            return "algum Sar-Allan"    
        elif agente == 3:
            return "um mago"     
        elif agente == 4:
            return "O Khal Drogo"  
        elif agente == 5:
            return "uma deusa, uma louca e uma feiticeira"
        
    def definirAgenteCaosFloresta():
        agente = random.choice([1,2,3,4])
        if agente == 1:
            return "uma dríade"
        elif agente == 2:
            return "um druida"       
        elif agente == 3:
            return "uma druida"  
        elif agente == 4:
            return "o Gandalf"  
        
    def definirEventoCaos():
        evento = random.choice([1,2,3,4,5])
        if evento == 1:
            return "o céu foi coberto por uma nuvem de insetos vermelhos"
        elif evento == 2:
            return "choveu uma tempestade de " + DefinicoesService.definirBebidas()
        elif evento == 3:
            return "a gravidade se inverteu por " + DefinicoesService.definirTempoEventoCaos()        
        elif evento >= 4:
            return DefinicoesService.definirObjeto() + " choveram"            

    def definirEventoCaosDeserto():
        evento = random.choice([1,2,3,4,5])
        if evento == 1:
            return "o céu foi coberto por uma nuvem de insetos vermelhos"
        elif evento == 2:
            return "choveu uma tempestade de insetos vermelhos"
        elif evento == 3:
            return "a gravidade se inverteu por " + DefinicoesService.definirTempoEventoCaos()        
        elif evento >= 4:
            return DefinicoesService.definirObjeto() + " choveram"  

    def definirEventoCaosFloresta():
        evento = random.choice([1,2,3,4,5])
        if evento == 1:
            return "o céu foi coberto por uma nuvem de vagalumes"
        elif evento == 2:
            return "choveu uma tempestade de pólen suficiente para cobrir um Hynne!"
        elif evento == 3:
            return "um fortíssimo vendaval derrubou diversas árvores"        
        elif evento >= 4:
            return DefinicoesService.definirObjeto() + " choveram"  

    def definirCausaCaos():
        evento = random.choice([1,2,3,4,5])
        if evento == 1:
            return "bebido a poção errada."
        elif evento == 2:
            return "acordado com o pé esquerdo."
        elif evento == 3:
            return "errado alguma magia."        
        elif evento >= 4:
            return "feito besteira."  


    def definirBebidas():
        objeto = random.choice([1,2,3])
        if objeto == 1:
            return "vinho"
        elif objeto == 2:
            return "Gorad"
        elif objeto == 3:
            return "cerveja anã"

    def definirObjeto():
        objeto = random.choice([1,2,3,4])
        if objeto == 1:
            return "Tibares"
        elif objeto == 2:
            return "moedas de ouro"
        elif objeto == 3:
            return "adagas"        
        elif objeto == 4:
            return "vacas"   
                
    def definirTempoEventoCaos():
        tempo = random.choice([1,2,3,4,5,6,7,8,9,10])
        if tempo == 1:
            return "alguns minutos"
        elif tempo == 10:
            return "algumas dezenas de minutos"
        elif tempo > 1 & tempo < 10:
            return "breves segundos"
