# Model/Cellule.py
#

from Model.Constantes import *

#
# Modélisation d'une cellule de la grille d'un démineur
#


def type_cellule(cell: dict) -> bool:
    """
    Détermine si le paramètre est une cellule correcte ou non

    :param cell: objet dont on veut tester le type cellule
    :return: True si c'est une cellule, False sinon
    """
    return type(cell) == dict and const.CONTENU in cell and const.VISIBLE in cell \
        and type(cell[const.VISIBLE] == bool) and type(cell[const.CONTENU]) == int \
        and (0 <= cell[const.CONTENU] <= 8 or cell[const.CONTENU] == const.ID_MINE)


def isContenuCorrect(n: int) -> bool:
    res = False
    if isinstance(n, int):
        if not (n != const.ID_MINE and 0 > n or 8 < n):
            res = True
    return res


def construireCellule(valeur: int = 0, visible: bool = False) -> dict:
    if valeur != const.ID_MINE and 0 > valeur or 8 < valeur:
        raise ValueError(f"construireCellule : le contenu {valeur} n'est pas correct")
    if not isinstance(visible, bool):
        raise TypeError(f"construireCellule : le second paramètre {type(visible)} n'est pas un booléen")
    dico = {}
    dico[const.CONTENU] = valeur
    dico[const.VISIBLE] = visible
    dico[const.ANNOTATION] = None
    return dico


def getContenuCellule(dico: dict) -> int:
    if not type_cellule(dico):
        raise TypeError(f"getContenuCellule : Le paramètre n'est pas une cellule")
    return dico.get(const.CONTENU)


def isVisibleCellule(dico: dict) -> bool:
    if not type_cellule(dico):
        raise TypeError(f"isVisibleCellule : Le paramètre n'est pas une cellule")
    return dico[const.VISIBLE]


def setContenuCellule(dico: dict, contenu: int) -> None:
    if not type_cellule(dico):
        raise TypeError(f"setContenuCellule : Le premier paramètre n'est pas une cellule")
    if not type(contenu) == int:
        raise TypeError(f"setContenuCellule : Le second paramètre n'est pas un entier")
    if not isContenuCorrect(contenu):
        raise ValueError(f"setContenuCellule : La valeur du contenu {contenu} n'est pas correcte")
    dico[const.CONTENU] = contenu
    return None


def setVisibleCellule(dico: dict, visible: bool) -> None:
    if not type_cellule(dico):
        raise TypeError(f"setVisibleCellule : Le premier paramètre n'est pas une cellule")
    if not isinstance(visible,bool):
        raise TypeError(f"setVisibleCellule : Le second paramètre n'est pas un booléen")
    dico[const.VISIBLE] = visible
    return None


def contientMineCellule(dico: dict) -> bool:
    res = False
    if not type_cellule(dico):
        raise TypeError("contientMineCellule : Le paramètre n'est pas une cellule")
    if dico[const.CONTENU] == const.ID_MINE:
        res = True
    return res


def isAnnotationCorrecte(annot: str) -> bool:
    res = False
    if annot == None or annot == const.DOUTE or annot == const.FLAG:
        res = True
    return res


def getAnnotationCellule(cell: dict) -> str:
    if not type_cellule(cell):
        raise TypeError(f"getAnnotationCellule : Le paramètre n'est pas une cellule.")
    return cell.get(const.ANNOTATION)