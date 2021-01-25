liste = {}

def menu():
    ''' Cette fonction permet d'afficher le menu principal
        result: affiche le menu
        return: ouvre la fonction menu_ associée
    '''
    print("0-quitter")
    print("1-écrire dans le répertoire")
    print("2-rechercher dans le répertoire")
    print()
    choix = int(input("Votre choix ? "))
    
    if choix == 1:
        menu_creer()
    elif choix == 2:
        menu_chercher()

def menu_creer():
    ''' Cette fonction permet d'afficher le menu de création d'une nouvelle entrée
        parameters: etape= nombre entier, facultatif
        result: affiche le menu et ajouter au fichier texte l'entrée
    '''
    nom = input("Nom (0 pour terminer) : ")
    if nom == '0':
        menu()
    tel = input("Téléphone : ")
    liste[nom] = tel
    
    with open('repertoire.txt','a') as f :
        f.write(nom)
        f.write("\n")
        f.write(tel)
        f.write("\n")
    
    menu_creer()

def menu_chercher():
    ''' Cette fonction permet d'afficher le menu de recherche dans le repertoire
        result: affiche le menu et retourne le résultat
        
        On stocke dans un tableau toutes les lignes du fichier repertoire.txt. On parcoure toutes les lignes jusqu'à trouver une concordance avec le 'nom'
    '''
    nom = input("Entrer un nom : ")
    tableau = [] 
    total = 0
    tel = ""
    nom = nom+'\n'
    with open('repertoire.txt','r') as f :
        # création d'un tableau avec chaque ligne du fichier
        # création d'un total de lignes
        for ligne in f:
            tableau.append(ligne)
            total += 1
    for i in range(0,total):
    	if tableau[i] == nom:
    		tel = tableau[i+1]
    if tel != "":
    	print("Le numéro recherché est: ",tel.replace('\n', ''))
    	print()
    else:
    	print("Inconnu")
    	print()
    menu()
                

menu()
