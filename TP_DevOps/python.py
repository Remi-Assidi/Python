import argparse
import os
import glob
import pandas as pd

def createFolders(path, folder):
    for index, row in df.iterrows():
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

parser = argparse.ArgumentParser()
parser.add_argument("file", help="Name of the csv file containing CSV datas")
args = parser.parse_args()
print(args.file)
df = pd.read_csv(args.file, usecols=['code_departement', 'nom_departement', 'code_region', 'nom_region'])
createFolders("./departements/", df)