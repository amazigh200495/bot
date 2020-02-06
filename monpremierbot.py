#!/usr/bin/python3
import random
import re
import datetime

category = [ "pc","ordinateur" , "telephone" , "voiture" ] 
exclure = ["je","vous","la","le","les","une","un","des"]
requete =input ("Bonjour, je suis votre assisstant MyBot, Que desirez-vous acheter ?\n")
decoupe=(re.findall(r"[a-zA-Z]+", requete))
#print(decoupe)
final = list(set(decoupe) - set(exclure))
finale = [mot.lower() for mot in final if len(mot) > 2 ]
#print (finale)
if ("voiture" in finale):
   print ("voici le catalogue des voitures")
elif ("telephone" in finale):
   print ("voici le catelogue des telephones")
elif ("ordinateur" or "pc" in finale):
   print ("voici le catalogue des ordinateurs")
else:
   print("Vu le {0}".format(datetime.datetime.now()))

