import datetime

def  salutation_personnalisee(nom):
    heure = datetime.datetime.now().hour
    if heure < 18:
        return "Bonjour"
    else: 
        return "Bonsoir"
#salutatations des gens
    
def calcul_facture(montants: float ,pourcentage_pourboire=15):
    total_sans_pourboire = sum(montants)
    montant_pourboire = total_sans_pourboire * (pourcentage_pourboire / 100)
    total_avec_pourboire = total_sans_pourboire + montant_pourboire
    return total_sans_pourboire , montant_pourboire ,total_avec_pourboire    
#calcul de la facture

try:
    nombre_personne = int(input("Combien de personnes dans le groupe?"))
except ValueError:
    print("Veuillez entrer un nombre valide.")
    
#lecture de la reponse ,si c'est un chiffre on continue ...

noms_et_montants = {}
for i in range(nombre_personne):
    nom = input(f"Entrez le nom de la personne {i+1}:")
    try:
        montant = float (input (f"Entrez le montant de la facture pour {nom}:"))
 
        if montant < 0:
            print("Le montant de la facture ne peut pas être négatif.")
            montant = 0.0 
        
        noms_et_montants [nom] = montant 
        
    except ValueError:
     print("Montant invalide . Ce participant sera ignoré")

# repetition pour chaque personne

total_facture , pourboire_final , total_final = calcul_facture([montant])
print("\n--- Récapitulatif de la facture ---")
for nom , montant in noms_et_montants.items():
    print(f"{salutation_personnalisee(nom)},votre contribution est de {montant:2f} G ")
    print(f"\nFacture Totale anvant le pourboire : {total_facture : .2f} G ")
    print(f"Pourboire (15%): {pourboire_final : .2f} G ")
    print(f"Facture totale avec pourboire : {total_final : .2f} G ")
    #Utilisation d'un pourboire par défaut de 15% 

