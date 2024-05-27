def getLMoins1L(mots1, mots2) :
    resultat=[]
    for i in range(0, len(mots1)) :
        for j in range(0, len(mots2)) :
            if mots2[j]!=mots1[i] : 
                if mots2[j].startswith(mots1[i]) :
                    resultat.append(mots2[j][len(mots1[i]):len(mots2[j])])
            else :
                resultat.append("")
    return resultat

def hasMotVide(stringList) :
    for i in range(0, len(stringList)) :
        if len(stringList[i])==0 :
            return True
    return False

def isCode(mots):
    lTmp = getLMoins1L(mots, mots)
    l1 = [elem for elem in lTmp if len(elem) != 0]
    nextL = l1.copy()
    listeLn = [mots, l1]
    i = 0
    while True:
        oldNextList = nextL.copy()
        nextL = getLMoins1L(nextL, mots)
        uLMoinsUn = getLMoins1L(mots, oldNextList)
        nextL += uLMoinsUn
        if hasMotVide(nextL):
            return False
        if set(nextL) in [set(item) for item in listeLn] and i != 0:
            return True
        listeLn.append(nextL.copy())
        i += 1

def getNbPrefixeSelf(mot) :
    result=0
    for i in range(0, len(mot)) :
        for j in range(0, len(mot)) :
            if i!=j :
                if mot[j].startswith(mot[i]) :
                    result+=1
    return result

print(getNbPrefixeSelf(['00','010','10','110','111']))