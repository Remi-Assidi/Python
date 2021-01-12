import argparse
import os
import re
import yaml
import glob
import pandas as pd

def printNumberOfResults(dataFrame, recherche):
    numberOfResults = 0
    for index, row in dataFrame.iterrows():
        try:
            if re.search(recherche, str(row["hist"])): 
                numberOfResults += 1
        except Exception as e:
            print(e)
    print("Nombre de monument qui match votre recherche: {} ".format(numberOfResults))

def createFile(nomFichier, dataFrame, recherche):
    dict_file = []
    for index, row in dataFrame.iterrows():
        try:
            if re.search(recherche, str(row["hist"])): 
                coordinate = str(row["coordonnees_ban"]).split(",")
                dict_file += [{"Nom" : str(row["tico"])}, {"Description" : str(row["hist"])}, {"Commune" : str(row["commune"])}, {"Localisation" : [{"Longitude" : coordinate[0]}, {"Latitude" : coordinate[1]}]}]
        except Exception:
            pass
    with open(nomFichier,'w') as file:
        documents = yaml.dump(dict_file, file)
        file.close()
        print("Successfully created file %s " % nomFichier)

parser = argparse.ArgumentParser()
parser.add_argument("fileMonuments", help="Name of the csv file containing CSV datas")
parser.add_argument("recherche", help="Word to execute the research")
parser.add_argument("--region", help="Region filter")
parser.add_argument("--export", help="Export the file", type=bool)
args = parser.parse_args()
dataFrame = pd.read_csv(args.fileMonuments, dtype={'tico':str,'ppro':str,'dpro':str,'stat':str,'desc':str,'hist':str,'autr':str,'adrs':str,'reg':str,'dpt_lettre':str,'commune':str,'affe':str,'wadrs':str,'wcom':str,'code_departement':str,'ploc':str,'dmaj':str,'ref':str,'insee':str,'contact':str,'sclx':str,'coordonnees_ban':str}, delimiter=";")
if args.region:
    dataFrame = dataFrame.loc[dataFrame['reg'].str.contains(args.region)]
if args.export:
    createFile("results.txt", dataFrame, args.recherche)
else:
    printNumberOfResults(dataFrame, args.recherche)
del dataFrame