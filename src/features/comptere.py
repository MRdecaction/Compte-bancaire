import uuid
from abc import ABC


class Compte(ABC):
    """
        Abstract class Compte
    """

    def __init__(self, nomProprietaire, **kwargs):
        pass

    def retrait(self, montant=0):
        pass

    def versement(self, montant=0):
        pass

    def afficherSolde(self):  # pragma: no cover
        pass

    def __repr__(self):
        return ""


class CompteCourant(Compte):
    def __init__(self, nomProprietaire, **kwargs):
        pass


class CompteEpargne(Compte):
    def __init__(self, nomProprietaire, **kwargs):
        pass
