import requests
from random import randint

def gen_nb():
    import random
    nb_obj=randint(0,100) #randint(valmin,valmax) entier aleatoire
    return nb_obj

def com_ia(question):
    responseia =requests.post(
    "https://api.deepseek.com/v1/chat/completions",
     headers={"Authorization":"Bearer TA_CLE",
         "Content-Type":"application/json"
         },  
    json={
      "model":"deepseek-chat",
      "messages":[{"role":"user","content":question}]
     }
    )
    print(responseia.json()["choices"][0]["message"]["content"])
    reponse=extractValue(responseia.json()["content"])
    return reponse

def extractValue(text):
    sep=" "
    decText=text.split(sep)
    for element in decText:
        if element.isnumeric():
            value=element
    return value

def jeu():
    nb_cible=gen_nb()
    partie_en_cour=True
    print("je pense a un nombre entier entre 0 et 100 devine ce nombre") #req
   # nb_prop=int(input("saisiser votre proposition: "))# rep
    nb_prop=com_ia("je pense a un nombre entier entre 0 et 100 devine ce nombre")
    while partie_en_cour==True:
       if nb_prop<nb_cible:
          print("c'est +")#req
         # nb_prop=int(input("saisiser votre proposition: "))#rep
          nb_prop=com_ia("c'est +")
       if nb_prop>nb_cible:
          print("c'est -")#req
         # nb_prop=int(input("saisiser votre proposition: "))#rep
          nb_prop=com_ia("c'est -")
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

jeu()




