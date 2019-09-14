
def getData(filename) :

    file1 =open(filename,'r+')
    str=""
    end=0


    ##Boucle pour atteindre le début du fichier
    while(end==0 ):
        str=""
        str = file1.readline()
        if (str.rfind("c: ") > -1):
            ind=str.rfind("c: ");
            fin_de_chaine=str[ind:];
            test=fin_de_chaine.split(';')[0] ;
            cap=int(test.split(': ')[1],10);


        if (str.rfind("n: ") > -1):
            ind=str.rfind("n: ");
            fin_de_chaine=str[ind:];
            test=fin_de_chaine.split(';')[0] ;
            nb=int(test.split(': ')[1],10);

        if (str.rfind("famille: ") > -1):
            ind=str.rfind("famille: ");
            fin_de_chaine=str[ind:];
            test=fin_de_chaine.split(';')[0] ;
            famille=(test.split(': ')[1]);

        if (str.rfind("taille: ") > -1):
            ind=str.rfind("taille: ");
            fin_de_chaine=str[ind:];
            test=fin_de_chaine.split(';')[0] ;
            taille=(test.split(': ')[1]);


        if (str.split(' ')[0].rfind("begin")> -1):
            end=1


    tab = [[0 for x in range(2)] for y in range(nb)]
    for i in range(nb):
        str = file1.readline()
        tab[i][0]=(int(str.split('\t')[0]))
        tab[i][1]=(int(str.split('\t')[1]))

    return tab,nb,cap,famille,taille
#print(getData("test.txt"))