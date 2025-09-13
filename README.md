Challenge : Gestion d’un compte bancaire en POO
Objectif : S’initier à la programmation orientée objet avec Python à travers la création d’une classe, la manipulation des attributs et l’appel de méthodes. Ce challenge permet de comprendre l'encapsulation des données et les actions associées à un objet.
Travail a faire: Crée une classe CompteBancaire avec les caractéristiques suivantes :
Attributs :
nom_proprietaire (chaîne)
solde (float, initialisé à 0.0 par défaut)
Méthodes :
__init__() : initialise le compte avec le nom du propriétaire et un solde optionnel.
deposer(montant) : ajoute le montant au solde.
retirer(montant) : retire le montant du solde si suffisant, sinon affiche un message d’erreur.
afficher_solde() : affiche le nom du propriétaire et le solde actuel.

Challenge :  Système de gestion d’école 
Objectif : Mettre en pratique les concepts fondamentaux de la POO à travers la modélisation d’un système scolaire. Ce challenge permet de manipuler les classes, l’héritage, le polymorphisme, l'encapsulation, les propriétés et les méthodes abstraites.
Spécifications :
Classe abstraite Personne (à l'aide du module abc)
Attributs : nom, prenom, age
Méthode abstraite : afficher_infos()
Classe Etudiant héritée de Personne
Attributs supplémentaires : matricule, notes (liste de floats)
Méthodes : ajouter_note(note), moyenne(), afficher_infos() (redéfinition)
Classe Enseignant héritée de Personne
Attributs supplémentaires : specialite, salaire
Méthode afficher_infos() (redéfinition) @property et @setter pour sécuriser l’accès/modification du salaire
Classe Ecole
Attributs : nom
liste_etudiants (liste d’objets Etudiant)
liste_enseignants (liste d’objets Enseignant)
Méthodes :
ajouter_etudiant(etudiant)
ajouter_enseignant(enseignant)
afficher_tous_les_membres() (polymorphisme via afficher_infos())
