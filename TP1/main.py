# -*- coding: utf-8 -*-
#!/usr/bin/python3
prix = 0.0
quantite = 0.0
prixTotal = 0.0

nbrProduits = int(input("Combien de produit voulez vous rentrer: "))
for i in range(nbrProduits):
    while True:
        prix = float(input("Veuillez saisir le prix (HT) de votre produit: "))
        if prix <= 0:
            print("Erreur votre prix doit être supérieur à 0.")
        else:
            break
    while True:
        quantite = float(input("Veuillez saisir la quantité: "))
        if quantite <= 0:
            print("Erreur votre quantite doit être supérieur à 0.")
        else:
            break
    prixTotal = prix*quantite*1.2

if prixTotal > 200:
    prixTotal = prixTotal*0.95
    print("Vous avez eu une remise de 5% car votre commande est supérieur à 200 euros.")
print("Le prix total est de {:.2f}".format(prixTotal))