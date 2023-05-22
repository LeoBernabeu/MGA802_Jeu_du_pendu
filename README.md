# MGA802 Jeu du pendu
Jeu du pendu réalisé en Python dans le cadre du cours MGA802 à l'ETS.

Ce dépôt contient le fichier *jeu_du_pendu.py* qui contient le code en Python pour jouer au jeu du pendu
et le fichier *mots_pendu.txt* qui contient une liste de mots utiliser pour le jeu.

## Utilisation

Pour lancer le jeu, suivez les étapes suivantes :
* Cloner le dépôt *git* ou télécharger le code puis décompresser l'archive obtenue.
* Ouvrir un terminal et se déplacer dans le dossier contenant le code.

Exemple :
````commandline
cd Downloads/MGA802_Jeu_du_pendu
````

* Lancer Python avec la commande *python* ou *python3*
* Importer le module *jeu_du_pendu*.
* Lancer la fonction jeu_du_pendu avec votre fichier contenant la liste des mots.

Exemple :
````python
import jeu_du_pendu as jp
jp.jeu_du_pendu("mots_pendu.txt")
````
````python
from jeu_du_pendu import *
jeu_du_pendu("mots_pendu.txt")
````

Si votre dictionnaire n'est pas dans le même niveau d'arborescence que le fichier *jeu_du_pendu.py*, par exemple :

`````bash
└───MGA802_Jeu_du_pendu
    ├───jeu_du_pendu.py
    ├───Dico
    │   └───mots_pendu.txt
`````
Alors, indiquer le chemin relatif du fichier en argument, c'est-à-dire :

````python
jeu_du_pendu("Dico/mots_pendu.txt")
````