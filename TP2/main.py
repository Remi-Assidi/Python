# -*- coding: utf-8 -*-
#!/usr/bin/python3
from utils import *;

def main():
    listeDesProduits = {1:{"Nom":"Banane","Prix":4.0,"Quantite":0}, 2:{"Nom":"Pomme","Prix":2.0,"Quantite":0}, 3:{"Nom":"Orange","Prix":1.5,"Quantite":0}, 4:{"Nom":"Poire","Prix":3.0,"Quantite":0}}

    while True:
        identifiant = int(input("Veuillez saisir l'identifiant de votre produit: "))
        if testerSiIdentifiantExist(identifiant, listeDesProduits):
            listeDesProduits[identifiant]["Quantite"] = demanderQuantite()
        else:
            print("Erreur, l'identifiant n'existe pas, veuillez reessayer.")
        if not testerSiNePLusSaisirDeProduit():
            break

    afficherTableauCommande(listeDesProduits)
    prixTotalHT = calculerTotal(listeDesProduits)
    prixApresRemise = calculerRemise(0.95, 200.0, prixTotalHT)
    remise = prixTotalHT - prixApresRemise
    prixTotalTTC= calculerTotalTTC(prixApresRemise)

    print("Sous total HT: {:.2f}".format(prixTotalHT))
    print("Remise 5%: {:.2f}".format(remise))
    print("Total HT: {:.2f}".format(prixApresRemise))
    print("Le prix total TTC est de {:.2f}".format(prixTotalTTC))

if __name__ == "__main__":
    main()