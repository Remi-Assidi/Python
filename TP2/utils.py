def testerSiIdentifiantExist(identifiant, listeDesProduits):
    if identifiant in listeDesProduits.keys():
        return True
    else: 
        return False

def testerSiNePLusSaisirDeProduit():
    saisirAutreProduit = input("Voulez vous saisir un autre produit ? (y/n) ")
    if saisirAutreProduit != "y":
        return False
    else:
        return True

def demanderQuantite():
    while True:
        quantite = float(input("Veuillez saisir la quantité: "))
        if quantite <= 0:
            print("Erreur votre quantite doit être supérieur à 0.")
        else:
            return quantite

def afficherTableauCommande(listeDesProduits):
    print("+----------------------------------+---------+------------------------+----------------+")
    print("+------------NOM-------------------+--Prix---+--------Quantité--------+-----Total-HT---+")
    for produit in listeDesProduits:
        if listeDesProduits[produit]["Quantite"] != 0:
            totalht = listeDesProduits[produit]["Prix"]*listeDesProduits[produit]["Quantite"]
            print("|           {Nom}                 |   {Prix}   |          {Quantite}          |     {TotalHT}     |".format(Nom=listeDesProduits[produit]["Nom"], Prix=listeDesProduits[produit]["Prix"], Quantite=listeDesProduits[produit]["Quantite"], TotalHT=totalht))
    print("+----------------------------------+---------+------------------------+----------------+")

def calculerTotal(listeDesProduits):
    prixTotal = 0.0
    for produit in listeDesProduits:
        if listeDesProduits[produit]["Quantite"] != 0:
            totalht = listeDesProduits[produit]["Prix"]*listeDesProduits[produit]["Quantite"]
            prixTotal += totalht
    return prixTotal

def calculerTotalTTC(prixTotalHT):
    return prixTotalHT * 1.20

def calculerRemise(pourcentageRemise, limiteDeclanchement, prixTotalHT):
    if prixTotalHT > limiteDeclanchement:
        return prixTotalHT*pourcentageRemise
    else:
        return prixTotalHT