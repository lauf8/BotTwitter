import time
import tweepy

import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("2H88ZxcEvVnoifMwMVNGc5wQd", "layXv2AhbVH0FFziwUBgxcM7LiAqlCNzatNYalIVodcN55Mzsc")
auth.set_access_token("1394737783722348547-dW6xY5CyMj4x2pCJDfyRFxM50wbBrS", "VxCelurbG9Uivy0MGL1oU5JwuGJXobvSHb2CjKJ6UJy8G")

# Create API object
api = tweepy.API(auth)

# Create a tweet

ano= 2021       #formato AAAA
mes=  8        #usar numeros
dia= 18

import datetime
datapadrao = datetime.date(ano, mes, dia)
hoje = datetime.date.today()

if datapadrao > hoje:
    delta = datapadrao - hoje

ferias = 'arroz'
if delta.days > 1:
    ferias = 'Faltam {dias} dias para o fim do semestre e início das ferias no IF de Guanambi!'.format(dias = delta.days)

if delta.days == 1:
    ferias = 'Falta {dias} dias para o fim do semestre e início das ferias no IF de Guanambi! Tamo quase lá'.format(dias = delta.days)

if delta.days == 0:
    ferias = 'Tamo de férias carai, finalmente acabou AEWSKAJKSJLASSKKASAS!'

api.update_status(ferias)
