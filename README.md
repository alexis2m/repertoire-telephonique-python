# **Répertoire téléphonique sous Python 3**

Cette application permet de stocker des noms et numéros de téléphone dans un fichier texte externe, et de retrouver le numéro associé au nom donné

## Fichiers associés:

 - app.py —> contient le logiciel
 - repertoire.txt —> contient les données

## Wiki

**Fonction *menu()*:**

 Cette fonction affiche le menu principal:
 

    0- Quitter
    1- Écrire dans le répertoire
    2 - Rechercher dans le répertoire
    
    Votre choix ?

On récupère un entier.

 - Si on entre `0` le programme s’arrête.
 - Si on entre `1` le programme
   charge la fonction *menu_creer()* 
  - Si on entre `2` le programme charge
   la fonction *menu_chercher()*

