import csv
import Sardinas

class NumProperty :
    def __init__(self, langage) :
        self.nbMots=len(langage)
        self.sumLongueurMot=0
        tot0=0
        tot1=0
        self.sumB10=0
        for i in range(0, len(langage)) :
            self.sumLongueurMot+=len(langage[i])
            self.sumB10+=int(langage[i], 2)
            for j in range(0, len(langage[i])) :
                if langage[i][j]=="0" :
                    tot0+=1
                else :
                    tot1+=1
        self.frequence0=tot0/(tot0+tot1)
        self.frequence1=tot1/(tot0+tot1)
        self.nbPrefixeSelf=Sardinas.getNbPrefixeSelf(langage)
        self.isCode=0
        if Sardinas.isCode(langage) :
            self.isCode=1


    @staticmethod
    def export_to_csv(data, filename):
        with open(filename, mode='w', newline='') as csv_file:
            fieldnames = ['nbMots', 'sumLongueurMot', 'sumB10', 'frequence0', 'frequence1', 'nbPrefixeSelf', 'isCode']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            for num_property in data:
                writer.writerow(vars(num_property))

    def individuToArray(self) :
        result=[]
        result.append(self.nbMots)
        result.append(self.sumLongueurMot)
        result.append(self.sumB10)
        result.append(self.frequence0)
        result.append(self.frequence1)
        return result

    def classToArray(self) :
        result=[]
        result.append(self.isCode)
        return result