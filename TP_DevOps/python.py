import argparse
import os
import re
import yaml
import glob
import pandas as pd

def createFolders(path, dataFrame):
    for index, row in dataFrame.iterrows():
        try:
            pathWithDepartment = path + row["nom_region"] + "/" + row["nom_departement"]
            if os.path.exists(pathWithDepartment):
                if len(os.listdir(pathWithDepartment)) > 0:
                    if input("Le dossier " + pathWithDepartment + " contient des fichiers, voulez vous les supprimer ? ") != "yes":
                        continue
                    else:
                        files = glob.glob(pathWithDepartment + "/*")
                        for f in files:
                            os.remove(f)
                        os.rmdir(pathWithDepartment)
                else:
                    continue
            os.makedirs(pathWithDepartment, exist_ok=True)
        except Exception as e:
            print(e)
        else:
            print ("Successfully created the directory %s " % pathWithDepartment)

def createFiles(path, dataFrame, nomRoi):
    for index, row in dataFrame.iterrows():
        try:
            if re.search(nomRoi, str(row["hist"])): 
                pathWithDepartment = path + row["reg"] + "/" + row["dpt_lettre"] + "/" + row["tico"] + ".txt"
                coordinate = str(row["coordonnees_ban"]).split(",")
                dict_file = [{"Nom" : str(row["tico"])}, {"Description" : str(row["hist"])}, {"Commune" : str(row["commune"])}, {"Localisation" : [{"Longitude" : coordinate[0]}, {"Latitude" : coordinate[1]}]}]
                with open(pathWithDepartment,'w') as file:
                    documents = yaml.dump(dict_file, file)
                    file.close()
                    print ("Successfully created the directory %s " % pathWithDepartment)
        except Exception as e:
            print(e)

parser = argparse.ArgumentParser()
parser.add_argument("fileRegions", help="Name of the csv file containing CSV datas")
parser.add_argument("fileMonuments", help="Name of the csv file containing CSV datas")
args = parser.parse_args()
dataFrame = pd.read_csv(args.fileRegions, usecols=['code_departement', 'nom_departement', 'code_region', 'nom_region'])
createFolders("./departements/", dataFrame)
del dataFrame
dataFrame = pd.read_csv(args.fileMonuments, dtype={'tico':str,'ppro':str,'dpro':str,'stat':str,'desc':str,'hist':str,'autr':str,'adrs':str,'reg':str,'dpt_lettre':str,'commune':str,'affe':str,'wadrs':str,'wcom':str,'code_departement':str,'ploc':str,'dmaj':str,'ref':str,'insee':str,'contact':str,'sclx':str,'coordonnees_ban':str}, delimiter=";")
createFiles("./departements/", dataFrame, "Philippe Auguste")
del dataFrame