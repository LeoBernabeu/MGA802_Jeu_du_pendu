# Proposition pour le jeu du pendu (MGA802 ; ETS)
# BERNABEU Léo

from random import choice


def random_word(nom_fichier):
    """Choisi un mot aléatoirement parmi les mots inscrit dans le fichier passé en paramètre.

    ________
    :param nom_fichier: Nom du fichier contenant la liste des mots à utiliser. Donner le nom du fichier avec son
                        extension (ex : mots_pendu.txt)

    ________
    :return: Le mot choisit aléatoirement sous la forme d'une chaîne de caractères.
    """
    fichier = open(nom_fichier, "r")
    dictionnaire = fichier.readlines()
    fichier.close()
    return choice(dictionnaire)[:-1]


def maj_affichage(lettre, mot, affichage):
    """Mets à jour la liste 'affichage' en remplaçant les '_' par la lettre à ses emplacements dans le mot.

    ________
    :param lettre: Lettre entrée par le joueur.
    :param mot: Mot à deviner par le joueur.
    :param affichage: Liste représentant le mot avec les lettres trouvées par le joueur.

    ________
    :return: None
    """
    for i in range(len(mot)):
        if mot[i] == lettre:
            affichage[i] = lettre


def is_win(affichage):
    """Indique si le mot a été trouvé et donc si la partie est gagnée.

    ________
    :param affichage: Liste représentant le mot avec les lettres trouvées par le joueur.

    ________
    :return: booléen True or False
    """

    if '_' in affichage:
        return False
    else:
        return True


def jeu_du_pendu(nom_fichier, nombre_chance=6):
    """Lance une partie du jeu du pendu.

    ________
    :param nom_fichier: Nom du fichier contenant la liste des mots à utiliser. Donner le nom du fichier avec son
                        extension (ex : mots_pendu.txt)

    :param nombre_chance: Nombre d'erreurs autorisées avant de perdre la partie.

    ________
    :return: None
    """

    mot = random_word(nom_fichier)  # Sélection d'un mot aléatoirement
    affichage = ['_' for _ in range(len(mot))]  # Liste représentant le mot avec les lettres trouvées par le joueur.
    liste_essais = []  # Liste pour garder en mémoire les lettres déjà testées.


    # Explication rapide du jeu du pendu
    print(f"Bienvenue dans le jeu du pendu. Vous devez donner des lettres pour réussir à retrouver un mot caché."
          f"Pour cela, vous aurez {nombre_chance} chances.\n")
    input("Appuyer sur une touche quand vous serez prêt à commencer.\n")

    # Boucle d'essais-erreurs jusqu'à trouver le mot où ne plus avoir de chance
    while nombre_chance != 0 and not is_win(affichage):
        lettre = input("Taper une lettre (en minuscule seulement et sans espace) : ")

        # Vérifier que la lettre n'a pas déjà été testé. Si oui, on ne le compte pas comme une erreur.
        if lettre in liste_essais:
            print("Vous avez déjà essayer cette lettre, tester en une autre.\n"
                  f"Rappel : {' ; '.join(liste_essais)}\n")
        else:
            if lettre in mot:
                print("Cette lettre est présente dans le mot\n")
                maj_affichage(lettre, mot, affichage)  # On met à jour la liste représentant le mot à trouver.
            else:
                print("Cette lettre n'est pas présente dans le mot\n")
                nombre_chance -= 1  # On décrémente le nombre de chances restantes.

            liste_essais.append(lettre)
            print(f"Il vous reste {nombre_chance} erreurs autorisées.\n")

        # Affichage de l'état du mot
        print(f"{' '.join(affichage)}\n")

    # Message de fin de partie
    print("Bravo ! Tu as gagné, ", end='') if is_win(affichage) else print("Désolé... Tu as perdu, ", end='')
    print(f"le mot était : {mot}.")