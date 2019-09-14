import sys

def getParamsRS(filename):
    file =open(filename,'r+')
    str=""
    end=0
    sampling_size=0
    line= file.readline()
    while line:
        if (line.rfind("sampling size:") > -1):
            ind=line.rfind("sampling size:");
            fin_de_chaine=line[ind:];
            test=fin_de_chaine.split(';')[0] ;
            sampling_size=int(test.split(':')[1],10);
        line=file.readline()
        if (line.rfind("temperature initiale:") > -1):
            ind = line.rfind("temperature initiale:");
            fin_de_chaine = line[ind:];
            test = fin_de_chaine.split(';')[0];
            temp_init = int(test.split(':')[1], 10);
        line = file.readline()
        if (line.rfind("taux de refroidissement:") > -1):
            ind = line.rfind("taux de refroidissement:");
            fin_de_chaine = line[ind:];
            test = fin_de_chaine.split(';')[0];
            cooling_fact = float(test.split(':')[1]);
        line = file.readline()
        if (line.rfind("temperature finale:") > -1):
            ind = line.rfind("temperature finale:");
            fin_de_chaine = line[ind:];
            test = fin_de_chaine.split(';')[0];
            temp_final = int(test.split(':')[1], 10);
        line = file.readline()

    return sampling_size,temp_init,cooling_fact,temp_final

def getParamsAG(filename):
    file =open(filename,'r+')
    str=""
    end=0
    line= file.readline()
    while line:
        if (line.rfind("nombre de tours:") > -1):
            ind=line.rfind("nombre de tours:");
            fin_de_chaine=line[ind:];
            test=fin_de_chaine.split(';')[0] ;
            nbr_tours=int(test.split(':')[1],10);
        line=file.readline()
        if (line.rfind("nombre de solutions:") > -1):
            ind = line.rfind("nombre de solutions:");
            fin_de_chaine = line[ind:];
            test = fin_de_chaine.split(';')[0];
            nbr_sol = int(test.split(':')[1], 10);
        line = file.readline()
        if (line.rfind("taille de tournoi:") > -1):
            ind = line.rfind("taille de tournoi:");
            fin_de_chaine = line[ind:];
            test = fin_de_chaine.split(';')[0];
            taille_tournoi = int(test.split(':')[1]);
        line = file.readline()
        if (line.rfind("probabilite de mutation:") > -1):
            ind = line.rfind("probabilite de mutation:");
            fin_de_chaine = line[ind:];
            test = fin_de_chaine.split(';')[0];
            prob_mutation = float(test.split(':')[1]);
        line = file.readline()

    return nbr_tours,nbr_sol,taille_tournoi,prob_mutation

def getParamsAG_A(filename):
    file =open(filename,'r+')
    str=""
    end=0
    line= file.readline()
    while line:
        if (line.rfind("nombre d'iterations:") > -1):
            ind=line.rfind("nombre d'iterations:");
            fin_de_chaine=line[ind:];
            test=fin_de_chaine.split(';')[0] ;
            nbr_iter=int(test.split(':')[1],10);
        if (line.rfind("taille de la population:") > -1):
            ind = line.rfind("taille de la population:");
            fin_de_chaine = line[ind:];
            test = fin_de_chaine.split(';')[0];
            population_size = int(test.split(':')[1], 10);
        line = file.readline()


    return nbr_iter,population_size
def getBestParamsRS(famille, taille):
    if (famille== "difficile"):
        if (taille=="petite"):
            return getParamsRS("paramètres/RS/DifficilePetite.txt")
        elif (taille=="moyenne"):
            return getParamsRS("paramètres/RS/DifficileMoyenne.txt")
        elif (taille=="grande"):
            return getParamsRS("paramètres/RS/DifficileGrande.txt")
    if (famille == "facile"):
        if (taille == "petite"):
            return getParamsRS("paramètres/RS/FacilePetite.txt")
        elif (taille == "moyenne"):
            return getParamsRS("paramètres/RS/FacileMoyenne.txt")
        elif (taille == "grande"):
            return getParamsRS("paramètres/RS/FacileGrande.txt")
    if (famille == "moyenne"):
        if (taille == "petite"):
            return getParamsRS("paramètres/RS/MoyennePetite.txt")
        elif (taille == "moyenne"):
            return getParamsRS("paramètres/RS/MoyenneMoyenne.txt")
        elif (taille == "grande"):
            return getParamsRS("paramètres/RS/MoyenneGrande.txt")

def getBestParamsAG(famille, taille):
    if (famille== "difficile"):
        if (taille=="petite"):
            return getParamsAG("paramètres/AG/DifficilePetite.txt")
        elif (taille=="moyenne"):
            return getParamsAG("paramètres/AG/DifficileMoyenne.txt")
        elif (taille=="grande"):
            return getParamsAG("paramètres/AG/DifficileGrande.txt")
    if (famille == "facile"):
        if (taille == "petite"):
            return getParamsAG("paramètres/AG/FacilePetite.txt")
        elif (taille == "moyenne"):
            return getParamsAG("paramètres/AG/FacileMoyenne.txt")
        elif (taille == "grande"):
            return getParamsAG("paramètres/AG/FacileGrande.txt")
    if (famille == "moyenne"):
        if (taille == "petite"):
            return getParamsAG("paramètres/AG/MoyennePetite.txt")
        elif (taille == "moyenne"):
            return getParamsAG("paramètres/AG/MoyenneMoyenne.txt")
        elif (taille == "grande"):
            return getParamsAG("paramètres/AG/MoyenneGrande.txt")

def getBestParamsRG(famille, taille):
    if (famille== "difficile"):
        if (taille=="petite"):
            return getParamsRS("paramètres/RG/DifficilePetite.txt")
        elif (taille=="moyenne"):
            return getParamsRS("paramètres/RG/DifficileMoyenne.txt")
        elif (taille=="grande"):
            return getParamsRS("paramètres/RG/DifficileGrande.txt")
    if (famille == "facile"):
        if (taille == "petite"):
            return getParamsRS("paramètres/RG/FacilePetite.txt")
        elif (taille == "moyenne"):
            return getParamsRS("paramètres/RG/FacileMoyenne.txt")
        elif (taille == "grande"):
            return getParamsRS("paramètres/RG/FacileGrande.txt")
    if (famille == "moyenne"):
        if (taille == "petite"):
            return getParamsRS("paramètres/RG/MoyennePetite.txt")
        elif (taille == "moyenne"):
            return getParamsRS("paramètres/RG/MoyenneMoyenne.txt")
        elif (taille == "grande"):
            return getParamsRS("paramètres/RG/MoyenneGrande.txt")
def getBestParamsAGA(famille, taille):
    if (famille== "difficile"):
        if (taille=="petite"):
            return getParamsAG_A("paramètres/AGA/DifficilePetite.txt")
        elif (taille=="moyenne"):
            return getParamsAG_A("paramètres/AGA/DifficileMoyenne.txt")
        elif (taille=="grande"):
            return getParamsAG_A("paramètres/AGA/DifficileGrande.txt")
    if (famille == "facile"):
        if (taille == "petite"):
            return getParamsAG_A("paramètres/AGA/FacilePetite.txt")
        elif (taille == "moyenne"):
            return getParamsRS("paramètres/AGA/FacileMoyenne.txt")
        elif (taille == "grande"):
            return getParamsAG_A("paramètres/AGA/FacileGrande.txt")
    if (famille == "moyenne"):
        if (taille == "petite"):
            return getParamsAG_A("paramètres/AGA/MoyennePetite.txt")
        elif (taille == "moyenne"):
            return getParamsAG_A("paramètres/AGA/MoyenneMoyenne.txt")
        elif (taille == "grande"):
            return getParamsAG_A("paramètres/AGA/MoyenneGrande.txt")


