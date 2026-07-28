import random
import string

def generer_mot_de_passe(longueur):
    if longueur < 4:
        print("La longueur doit être d'au moins 4.")
        return ""

