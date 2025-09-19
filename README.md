# Calculateur-de-Pourboire-Personnalis-

Ce code Python gère le calcul et le récapitulatif de factures pour un groupe de personnes, en incluant un pourboire. Voici un aperçu de ses fonctionnalités :
1. Salutation personnalisée
La fonction salutation_personnalisee(nom) détermine si c'est le matin ou le soir et renvoie "Bonjour" ou "Bonsoir" en conséquence.
Elle utilise le module datetime pour obtenir l'heure actuelle.

2. Calcul de la facture
La fonction calcul_facture(montants, pourcentage_pourboire=15) calcule le total d'une facture.
Elle prend une liste de montants et un pourcentage de pourboire (par défaut 15 %).
Elle renvoie le total sans pourboire, le montant du pourboire et le total avec pourboire.

3. Saisie des informations
Le programme demande à l'utilisateur le nombre de personnes dans le groupe. Il gère les erreurs si l'entrée n'est pas un nombre.
Ensuite, pour chaque personne, il demande son nom et le montant de sa facture individuelle.
Il valide que le montant n'est pas négatif et gère les erreurs de saisie (si le montant n'est pas un nombre, le participant est ignoré).

4. Récapitulatif
Une fois toutes les informations collectées, le programme affiche un récapitulatif détaillé.
Pour chaque personne, il affiche une salutation personnalisée et sa contribution.
Enfin, il présente la facture totale avant pourboire, le montant du pourboire (calculé avec 15 % par défaut) et la facture totale finale avec pourboire.
