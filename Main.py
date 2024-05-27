import random

from NumProperty import NumProperty
import pandas as pd
from sklearn.ensemble import *
import joblib
from sklearn.metrics import *

possibilite=["0", "1"]
# 1) Generer un mot binaire 7 caracteres
def genererMotBinaire() :
    longueur=random.randint(1, 7)
    resultat=""
    for i in range(0, longueur) :
        resultat+=possibilite[random.randint(0, 1)]
    return resultat

# 2) Generer un langage de 10 mots(7 caracteres) maximum 
def genererLangage() :
    resultat=[]
    longueurLangage=random.randint(1, 10)
    for i in range(0, longueurLangage) :
        resultat.append(genererMotBinaire())
    return resultat

clf = joblib.load('modele_foret_aleatoire.joblib')
test_data = pd.read_csv('all.csv')
X_test = test_data.iloc[:, 0:-1].values  # Sélectionner toutes les colonnes sauf la dernière
y_test = test_data.iloc[:, -1].values  
y_pred = clf.predict(X_test)

# Calculer l'exactitude (pourcentage de prédictions correctes)
accuracy = accuracy_score(y_test, y_pred)

# Afficher le pourcentage de prédictions correctes
print("Pourcentage de prédictions correctes :", accuracy * 100, "%")