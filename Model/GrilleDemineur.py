# GrilleDemineur.py

from Model.Cellule import *
from Model.Coordonnee import *
from random import shuffle, randint
from itertools import filterfalse


# Méthode gérant la grille du démineur
# La grille d'un démineur est un tableau 2D régulier (rectangulaire)
#
# Il s'agira d'une liste de liste


def type_grille_demineur(grille: list) -> bool:
    """
    Détermine si le paramètre représente une grille d'un démineur.

    :param grille: objet à tester
    :return: `True` s'il peut s'agit d'une grille de démineur, `False` sinon
    """
    if type(grille) != list:
        return False
    # Récupération du nombre de lignes
    nl = len(grille)
    # Il faut que la grille comporte au moins une ligne
    if nl == 0:
        return False
    nc = len(grille[0])
    if nc == 0:
        return False
    return next(filterfalse(lambda line: type(line) == list and len(line) == nc
                            and next(filterfalse(type_cellule, line), True) is True, grille), True) is True
    # Tableau régulier
    # nc = None
    # for line in grille:
    #     if type(line) != list:
    #         return False
    #     if nc is None:
    #         nc = len(line)
    #         # Il faut que la grille comporte au moins une colonne
    #         if nc == 0:
    #             return False
    #     elif nc != len(line):
    #         return False
    #     # Test des cellules de la ligne
    #     if not next(filterfalse(type_cellule, line), True):
    #         return False
    # for cell in line:
    #     if not type_cellule(cell):
    #         return False
    # return True



def construireGrilleDemineur(nl: int, nc: int) -> list:
    if nl <= 0 or nc <= 0:
        raise ValueError(f"construireGrilleDemineur : Le nombre de lignes {nl} ou de colonnes {nc} est négatif ou nul")
    if not isinstance(nl,int) or not isinstance(nc,int):
        raise TypeError(f"construireGrilleDemineur : Le nombre de lignes {type(nl)} ou de colonnes {type(nc)} n'est pas un entier")
    grille = list()
    for i in range(nl):
        ligne = list()
        for j in range(nc):
            ligne.append(construireCellule())
        grille.append(ligne)
    return grille


def getNbLignesGrilleDemineur(grille: list) -> int:
    if not type_grille_demineur(grille):
        raise TypeError(f"getNbLignesGrilleDemineur : Le paramètre n'est pas une grille")
    nbLignes = 0
    for i in range(len(grille)):
        nbLignes += 1
    return nbLignes


def getNbColonnesGrilleDemineur(grille: list) -> int:
    if not type_grille_demineur(grille):
        raise TypeError(f"getNbColonnesGrilleDemineur : Le paramètre n'est pas une grille")
    nbColonnes = 0
    for i in range(len(grille[0])):
        nbColonnes += 1
    return nbColonnes


def isCoordonneeCorrecte(grille: list, coord: tuple) -> bool:
    if not type_grille_demineur(grille) or not type_coordonnee(coord):
        raise TypeError(f"isCoordonneeCorrecte : un des paramètres n’est pas du bon type.")
    res = False
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            if (i, j) == coord:
                res = True
    return res


def getCelluleGrilleDemineur(grille: list, coord: tuple) -> dict:
    if not type_grille_demineur(grille) or not type_coordonnee(coord):
        raise TypeError(f"getCelluleGrilleDemineur : Un des paramètres n’est pas du bon type.")
    if not isCoordonneeCorrecte(grille, coord):
        raise IndexError(f"getCelluleGrilleDemineur : Coordonnée non contenue dans la grille.")
    return grille[coord[0]][coord[1]]


def getContenuGrilleDemineur(grille: list, coord: tuple) -> int:
    if not type_grille_demineur(grille) or not type_coordonnee(coord):
        raise TypeError(f"getContenuGrilleDemineur : Un des paramètres n'est pas du bon type.")
    if not isCoordonneeCorrecte(grille, coord):
        raise IndexError(f"getContenuGrilleDemineur : Coordonnée non contenue dans la grille.")
    return getContenuCellule(getCelluleGrilleDemineur(grille, coord))


def setContenuGrilleDemineur(grille: list, coord: tuple, contenu: int) -> None:
    if not type_grille_demineur(grille) or not type_coordonnee(coord) or type(contenu) != int:
        raise TypeError(f"setContenuGrilleDemineur : Un des paramètres n'est pas du bon type.")
    if not isContenuCorrect(contenu):
        raise ValueError(f"setContenuGrilleDemineur : La valeur du contenu {contenu} n'est pas correcte.")
    if not isCoordonneeCorrecte(grille, coord):
        raise IndexError(f"setContenuGrilleDemineur : Coordonnée non contenue dans la grille.")
    setContenuCellule(getCelluleGrilleDemineur(grille, coord), contenu)
    return None


def isVisibleGrilleDemineur(grille: list, coord: tuple) -> bool:
    if not type_grille_demineur(grille) or not type_coordonnee(coord):
        raise TypeError(f"isVisibleGrilleDemineur : Un des paramètres n'est pas du bon type.")
    if not isCoordonneeCorrecte(grille, coord):
        raise IndexError(f"isVisibleGrilleDemineur : Coordonnée non contenue dans la grille.")
    return isVisibleCellule(getCelluleGrilleDemineur(grille, coord))


def setVisibleGrilleDemineur(grille: list, coord: tuple, visible: bool) -> None:
    if not type_grille_demineur(grille) or not type_coordonnee(coord):
        raise TypeError(f"setVisibleGrilleDemineur : Un des paramètres n'est pas du bon type.")
    if not isCoordonneeCorrecte(grille, coord):
        raise IndexError(f"setVisibleGrilleDemineur : Coordonnée non contenue dans la grille.")
    setVisibleCellule(getCelluleGrilleDemineur(grille, coord), visible)
    return None


def contientMineGrilleDemineur(grille: list, coord: tuple) -> bool:
    if not type_grille_demineur(grille) or not type_coordonnee(coord):
        raise TypeError(f"contientMineGrilleDemineur : Un des paramètres n'est pas bon.")
    if not isCoordonneeCorrecte(grille, coord):
        raise IndexError(f"contientMineGrilleDemineur : Coordonnée non contenue dans la grille.")
    return contientMineCellule(getCelluleGrilleDemineur(grille, coord))


def getCoordonneeVoisinsGrilleDemineur(grille: list, coord: tuple) -> list:
    voisins = list()
    if not type_grille_demineur(grille) or not type_coordonnee(coord):
        raise TypeError("getCoordonneeVoisinsGrilleDemineur : Un des paramètres n’est pas du bon type.")
    if not isCoordonneeCorrecte(grille, coord):
        raise IndexError("getCoordonneeVoisinsGrilleDemineur :  La coordonnée n’est pas dans la grille.")
    for i in range(coord[0] - 1, coord[0] + 2):
        for j in range(coord[1] - 1, coord[1] + 2):
            if (i, j) != coord and 0 <= i <= getNbLignesGrilleDemineur(grille) - 1 and 0 <= j <= getNbColonnesGrilleDemineur(grille) - 1:
                voisins.append(construireCoordonnee(i, j))
    return voisins
