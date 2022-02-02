import requests                                    #Fournit le protocole http
import time                                        #Fournit un tas de fonction liés au temps
from lxml import etree                             #Fournit la librairie html
from time import sleep                             #On import la fonction "sleep" depuis "temps" 

                                 
response=requests.get("https://data.montpellier3m.fr/sites/default/files/ressources/TAM_MMM_VELOMAG.xml")     #Sert à demander une ressource au serveur.
f1=open("vélo.txt","w", encoding='utf8')       #Ouvre le fichier velo.txt en écriture en utf8
f1.write(response.text)                        #On écrit dans le fichier en text
f1.close()                                     #On ferme le fichier
	
f1=open("vélo_résultat.txt","a", encoding='utf8')                 
tree = etree.parse("vélo.txt")
for user in tree.xpath("/vcs/sl/si"):         #Boucle qui va récupérer les données dans le fichier de données des vélos dans les balises html vcs/sl/si .  
	f1.write(f"Nom de la station : ")       #Nom de la station a afficher dans le vélo_résultat.txt a la suite de la donnée récupéré            
	f1.write(user.get("na"))                   #Récupère les données du serveur sur le nom de la station    
	f1.write("\n")								#Saut de ligne pour mieux organiser le fichier du résultat : vélo_résultat.txt
	f1.write(f"Places libres : ")               #Places libres a afficher dans le vélo_résultat.txt a la suite de la donnée récupéré       
	f1.write(user.get("fr"))                   #Récupère les données du serveur sur le nombre de places libres
	f1.write("\n")
	f1.write(f"Places occupées : ")            #Places occupées a afficher dans le vélo_résultat.txt a la suite de la donnée récupéré          
	f1.write(user.get("av"))                  #Récupère les données du serveur sur le nombre de places occuppées 
	f1.write("\n")
	f1.write(f"Nombre de places totales : ")     #Nombre de places totales a afficher dans le vélo_résultat.txt a la suite de la donnée récupéré                  
	f1.write(user.get("fr"))                   #Récupère les données du serveur sur le nombre de place totales
	f1.write("\n") 
	f1.write("\n")                           #Saut de ligne pour mieux organiser le fichier du résultat : vélo_résultat.txt
	f1.write(f"------- Actualisation de la station dans 30 minutes -------")
	f1.write("\n")
	f1.write("\n")
time.sleep(1800)            #Pour arreter et redémarrer le programmme dans 30min

		                       
	