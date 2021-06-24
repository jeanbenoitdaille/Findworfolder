    import os
    from glob import glob
     
    dossier = "/Users/thibh/Documents"
    mot = "Python"
     
    fichiers = glob(f"{dossier}/**/*.txt", recursive=True)
     
    fichiers_trouves = []
     
    for filename in fichiers:
        with open(filename, "r") as file:
            contenu_fichier = file.read()
            if mot in contenu_fichier:
                fichiers_trouves.append(filename)
     
    print(fichiers_trouves)
