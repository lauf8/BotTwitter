import datetime
import time
import tweepy

import tweepy

# Insere as chaves para se fazer a autentificação do twitter
auth = tweepy.OAuthHandler("")
auth.set_access_token("")

# Create API object
api = tweepy.API(auth)

# Create a tweet

ano = 2021  # formato AAAA
mes = 8  # usar numeros
dia = 18

datapadrao = datetime.date(ano, mes, dia)
hoje = datetime.date.today()

if datapadrao > hoje:
    delta = datapadrao - hoje

ferias = 'arroz'
if delta.days > 1:
    ferias = 'Faltam {dias} dias para o fim do semestre e início das ferias no IF de Guanambi!'.format(
        dias=delta.days)

if delta.days == 1:
    ferias = 'Falta {dias} dias para o fim do semestre e início das ferias no IF de Guanambi! Tamo quase lá'.format(
        dias=delta.days)

if delta.days == 0:
    ferias = 'Tamo de férias carai, finalmente acabou AEWSKAJKSJLASSKKASAS!'

api.update_status(ferias)
