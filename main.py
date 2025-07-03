#challenge1
class CompteBancaire:
    def __init__(self, nom, solde=0.0 ):
        self.nom=nom
        self.solde=solde

    def deposer(self, montant):
        self.montant=montant
        if self.montant>0:
            self.solde+=montant
            print(f'votre solde est devenu: {self.solde}')
        else:
            print("le montant que vous avez entrer est invalide")

    def retirer(self, montant):
        self.montant = montant
        if self.solde<=self.montant:
            print("rentrer un montant inferieur ou egale votre solde")
        else:
            self.solde-=self.montant
            print(f'votre solde est devenu: {self.solde}')

    def afficher_solde(self):
        print(f'Bienvenue {self.nom}, votre solde est {self.solde}')


Compte = CompteBancaire("hasnae", 10000)

Compte.afficher_solde()
Compte.retirer(100)
Compte.deposer(500)

#challenge2
from abc import ABC, abstractmethod

class Personne(ABC):
    def _init_(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age

    @abstractmethod
    def afficher_infos(self):
        pass


class Etudiant(Personne):
    def _init_(self, nom, prenom, age, matricule):
        super()._init_(nom, prenom, age)
        self.matricule = matricule
        self.notes = []

    def ajouter_note(self, note):
        self.notes.append(note)

    def moyenne(self):
        return sum(self.notes) / len(self.notes) if self.notes else 0

    def afficher_infos(self):
        print(f"[Etudiant] {self.prenom} {self.nom}, {self.age} ans, Matricule: {self.matricule}, Moyenne: {self.moyenne():.2f}")


class Enseignant(Personne):
    def _init_(self, nom, prenom, age, specialite, salaire):
        super()._init_(nom, prenom, age)
        self.specialite = specialite
        self._salaire = salaire

    @property
    def salaire(self):
        return self._salaire

    @salaire.setter
    def salaire(self, nouveau_salaire):
        if nouveau_salaire > 0:
            self._salaire = nouveau_salaire
        else:
            print("Salaire invalide.")

    def afficher_infos(self):
        print(f"[Enseignant] {self.prenom} {self.nom}, {self.age} ans, Specialite: {self.specialite}, Salaire: {self._salaire} MAD")


class Ecole:
    def _init_(self, nom):
        self.nom = nom
        self.liste_etudiants = []
        self.liste_enseignants = []

    def ajouter_etudiant(self, etudiant):
        self.liste_etudiants.append(etudiant)

    def ajouter_enseignant(self, enseignant):
        self.liste_enseignants.append(enseignant)

    def afficher_tous_les_membres(self):
        print(f"Membres de l'école : {self.nom}")
        for e in self.liste_etudiants + self.liste_enseignants:
            e.afficher_infos()
