nbCode=0
nbNCode=0
listPNum=[]
listAll=[]
for i in range(0, 100000) :
    langage=genererLangage()
    numProperty=NumProperty(langage)
    if numProperty.isCode==0 and nbNCode!=2500:
        nbNCode+=1 
        listPNum.append(numProperty)
    elif numProperty.isCode==1 and nbCode!=2500 :
        nbCode+=1
        listPNum.append(numProperty)
    listAll.append(numProperty)
        
NumProperty.export_to_csv(listPNum, 'dataLangages.csv')
NumProperty.export_to_csv(listAll, 'all.csv')


df = pd.read_csv('dataLangages.csv')

# Séparer les variables explicatives (X) de la variable cible (y)
X = df.iloc[:, 0:-1].values
y = df.iloc[:, -1].values

# Créer un modèle de forêt aléatoire et l'entraîner sur l'ensemble des données
clf = RandomForestClassifier(random_state=0)
clf.fit(X, y)

# Sauvegarder le modèle dans un fichier joblib
joblib.dump(clf, 'modele_foret_aleatoire.joblib')