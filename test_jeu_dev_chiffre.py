import requests
import os
from random import randint
from dotenv import load_dotenv

load_dotenv()
API_KEY=os.getenv("DEEPSEEK_API_KEY")

def gen_nb(valmax):
    import random
    nb_obj=randint(0,valmax) #randint(valmin,valmax) entier aleatoire
    return nb_obj

def com_ia(question):
    responseia =requests.post(
    "https://api.deepseek.com/v1/chat/completions",
     headers={"Authorization":"Bearer {API_KEY}",
         "Content-Type":"application/json"
         },  
    json={
      "model":"deepseek-chat",
      "messages":[{"role":"user","content":question}]
     }
    )
    print(responseia.json()["choices"][0]["message"]["content"])
    reponse=extractValue(responseia.json()["choices"][0]["message"]["content"])
    return reponse

def extractValue(text):
    sep=" "
    value="erreur"
    decText=text.split(sep)
    for element in decText:
        if element.isnumeric():
            value=element
    return value

def jeu():
    print("bienvenue dans ce jeu de devine le nombre,pour commencer indiquer la valeur maximal que peu prendre le nombre a trouver (nombre entier uniquement) ")
    nb_max=com_ia("bienvenue dans ce jeu de devine le nombre,pour commencer indiquer la valeur maximal que peu prendre le nombre a trouver (nombre entier uniquement) ")
    if nb_max=="erreur":
       while nb_max=="erreur":
           nb_max=com_ia("veuillez entrer une valeur max (entier)")
    nb_cible=gen_nb(nb_max)
    print("maintenant veuillez entrer le nombre de vie(s) que vous voulez (nombre entier uniquement)")
    nb_vie=com_ia("maintenant veuillez entrer le nombre de vie(s) que vous voulez (nombre entier uniquement)")
    if nb_vie=="erreur":
        while nb_vie=="erreur":
            nb_vie=com_ia("veuillez entrer un nombre de vie (entier)")
    vie=nb_vie
    partie_en_cour=True
    print("je pense a un nombre entier entre 0 et "+nb_max+" devine ce nombre") #req
   # nb_prop=int(input("saisiser votre proposition: "))# rep
    nb_prop=com_ia("je pense a un nombre entier entre 0 et "+nb_max+" devine ce nombre")
    while partie_en_cour==True:
        if vie>0:
           if nb_prop=="erreur":
             print("veuillez proposer une valeur")
             nb_prop=com_ia("veuillez proposer un nombre")
           if nb_prop<nb_cible:
            if nb_cible-nb_prop>10:
             vie-=1
             print("c'est beaucoup + , il vous reste "+vie+"vie(s)")#req
             # nb_prop=int(input("saisiser votre proposition: "))#req
             nb_prop=com_ia("c'est beaucoup + , il vous reste "+vie+"vie(s)")
            else:
               vie-=1
               print("c'est un peu + , il vous reste "+vie+"vie(s)")
               nb_prop=com_ia("c'est un peu + , il vous reste "+vie+"vie(s)")
           if nb_prop>nb_cible:
            if nb_prop-nb_cible>10:
             vie-=1
             print("c'est beaucoup - , il vous reste "+vie+"vie(s)")#req
             # nb_prop=int(input("saisiser votre proposition: "))#rep
             nb_prop=com_ia("c'est beaucoup - , il vous reste "+vie+"vie(s)")
            else:
                vie-=1
                print("c'est un peu - , il vous reste "+vie+"vie(s)")
                nb_prop=com_ia("c'est un peu - , il vous reste "+vie+"vie(s)")
           if nb_prop==nb_cible:
             print("bravo vous avez trouvez le nombre auquel je pensait.")#req
             partie_en_cour=False
             # nv_partie=input("souhaitez vous faire une nouvelle partie?")#req/rep
             nv_partie=com_ia("bravo vous avez trouvez le nombre auquel je pensait. souhaitez vous faire une nouvelle partie?")
             sep=" "
             decText=nv_partie.split(sep)
             for element in decText:
              if element=="oui":
               jeu()
             if element=="non":
              partie_en_cour==False
              print("au revoir")
              com_ia("au revoir")
        else:
            partie_en_cour=False
            print("vous n'avez plus de vie, c'est perdu ,souhaitez vous réessayer?")
            nv_partie=com_ia("vous n'avez plus de vie, c'est perdu ,souhaitez vous réessayer?")
            sep=" "
            decText=nv_partie.split(sep)
            for element in decText:
              if element=="oui":
               jeu()
              if element=="non":
               partie_en_cour==False
               print("au revoir")
               com_ia("au revoir")

jeu()




