import os

os.chdir('D:\ProjetosDev\ClimaArton')

import tweepy 
from regioes_service import RegioesService

#Define keys
api_key = "23dAA3MiVCmq8YY0cUX4uBp16"
api_key_secret = "szCVXREOxmM4Z1aY02ENqYpIksDv8J6fNfMOoOhmcnIfAmasUl"
bearer_token = r"AAAAAAAAAAAAAAAAAAAAAL6enAEAAAAAfM9PjrfZWNQo2HkiQoAIQNHZqPo%3DuYzBnlKR3BND1p4GbSU0iIbjCmY19bAz9bYww3F00BbFXYAdSG"
access_token = "1653076055446413315-DHZKsvrT62tfo68Olui5ur1A0fxvSg"
access_token_secret = "aZTmWxn4ErDBunXKQyupNcwg815kVfLfnqhxMXQK5zPUE"

client = tweepy.Client(bearer_token, api_key, api_key_secret, access_token, access_token_secret)

texto = RegioesService.montarTexto()

while len(texto) > 280:
    texto = RegioesService.montarTexto()
    
client.create_tweet(text=texto)