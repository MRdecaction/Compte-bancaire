import  uuid
from abc import ABC

class Compte(ABC):
    """
        Abstract class Compte
    """

    def init(self, nomProprietaire, kwargs):
        self.nom_proprietaire = nomProprietaire
        self.numero_compte = kwargs.get("numero_compte")
        self.solde = kwargs.get("solde")

    def retrait(self, montant):
        self.solde -= montant

    def versement(self, montant):
        if montant <= 0:
            raise Exception
        self.solde += montant

    def afficherSolde(self):  # pragma: no cover
        pass

    def repr(self):
        return f"CompteCourant - Solde : {self.solde}"

    # Class CompteCourant hérite de Class Compte

    def effectuer_transaction(compte_instance):
        choix = input("Vous souhaitez effectuer un retrait ou un dépôt ? Entrez 'r' pour retrait ou 'd' pour dépôt : ")
        if choix == 'r':
            montant = float(input("Entrez le montant à retirer"))
            compte_instance.retrait(montant)
        elif choix == 'd':
            montant = float(input("Enter the montant a deposer : "))
            compte_instance.versement(montant)
        else:
            print("Choix invalide, veuillez réessayer")


class CompteCourant(Compte):
    def __init__(self, nomProprietaire, **kwargs):
        super().__init__(nomProprietaire, solde=0, numero_compte=kwargs.get("numero_compte"))
        self.autorisation_decouvert = kwargs.get("autorisation_decouvert", True)
        self.pourcentage_agios = kwargs.get("agios")

    # Fonction pour appliquer un agios si le solde est inférieur a 0

    def appliquer_agios(self, montant):
        if self.solde < 0:
            self.solde -= montant * self.pourcentage_agios

    # Si montant du retrait est supérieur au solde par défaut (0) alors applique un agios

    def retrait(self, montant):
        if montant <= 0 or not self.autorisation_decouvert:
            raise Exception
        super().retrait(montant)
        self.appliquer_agios(montant)

    class CompteEpargne(Compte):
        def init(self, nomProprietaire, *kwargs):
            super().init(nomProprietaire, solde=0, numero_compte=kwargs.get("numero_compte"))
            self.pourcentage_interets = kwargs.get("pourcentage_interets")

        def appliquer_interets(self):
            if self.montant > 0:
                self.solde = self.montant(1 + (10 / 100))
            return self.solde