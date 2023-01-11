# Coordonnee.py

import const


# Définition des coordonnées (ligne, colonne)


def type_coordonnee(coord: tuple) -> bool:
    """
    Détermine si le paramètre correspond ou non à une coordonnée.

    Cette fonction teste notamment si les lignes et colonnes sont bien positives. Dans le cas contraire, la fonction
    retourne `False`.

    :param coord: couple représentant le numéro de ligne et celui de la colonne (commençant les deux à 0)
    :return: `True` si le paramètre correspond à une coordonnée, `False` sinon.
    """
    return type(coord) == tuple and len(coord) == 2 and type(coord[0]) == int and type(coord[1]) == int \
        and coord[0] >= 0 and coord[1] >= 0


def construireCoordonnee(num_li: int, num_co: int) -> tuple:
    """

    :param num_li: int
    :param num_co: int
    :return: Forme un tuple à partir de deux entiers positifs, si négatif ou pas entier: renvoie une erreur
    """
    if (type(num_li) or type(num_co)) != int:
        raise TypeError(
            f"construireCoordonnee : Le numéro de ligne {type(num_li)} ou le numéro de colonne {type(num_co)} ne sont pas des entiers.")
    elif num_li < 0 or num_co < 0:
        raise ValueError(
            f"construireCoordonnee : Le numéro de ligne ({num_li}) ou le numéro de colonne ({num_co}) ne sont pas positifs.")
    else:
        return num_li, num_co

def estCoordonnee(coord) -> bool:
    """

    :param coord: tuple
    :return: Renvoie True si le paramètre est une coordonnée valide, sinon False
    """
    res = False
    if type(coord) == tuple:
        if (type(coord[0]) and type(coord[1])) == int and (coord[0] and coord[1]) >= 0:
            res = True
    return res

def getLigneCoordonnee(coord: tuple) -> int:
    """

    :param coord: tuple
    :return: Renvoie le numéro de colonne si coord est une coordonnée, sinon renvoie une erreur
    """
    if not estCoordonnee(coord):
        raise TypeError("getLigneCoordonnee : Le paramètre n'est pas une coordonnée")
    else:
        return coord[0]


def getColonneCoordonnee(coord: tuple) -> int:
    """


    :param coord: tuple
    :return: Renvoie le numéro de colonne si coord est une coordonnée, sinon renvoie une erreur
    """
    if not estCoordonnee(coord):
        raise TypeError("getCoordCoordonnee : Le paramètre n'est pas une coordonnée")
    else:
        return coord[1]