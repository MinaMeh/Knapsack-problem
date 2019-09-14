import numpy as np
import time
import random
from getData import getData
#Created by Amine
populationSize=50
C=100
Generation=10
combinationBitOfItem={}
Weight=[]
Profits=[]
Chromosomes=[]
Fitness=[]
bestFitness=[]
mutationPercentage=0.3
bestChromosomes=[]
runSetting=10
N=100
def calculateWeight(chromosome,weights):
    gens=chromosome.split(' ')
    totalWeight=0
    for i in range(len(gens)):
        #print('weight[i] =',Weight[i])
        totalWeight=totalWeight+convertStringToBinary(gens[i]) *Weight[i]

    return totalWeight


def calculateFitness(chromosome,values):
    gens=chromosome.split(' ')
    totalValue=0
    for i in range(len(gens)):
        totalValue=totalValue+convertStringToBinary(gens[i]) *values[i]

    return totalValue

def convertStringToBinary(str):
    result=0
    k=0
    i=0
    i=len(str)-1
    while(i>=0):
        bit=0
        if (str[i]=='1'):
            bit=1
        result=result+(2**k)*bit
        k=k+1
        i=i-1

    return result

def convertBinaryToGen(bit,sizeofGene):
    binary=format(bit,'b')
    result=binary.zfill(sizeofGene)
    return result

def getSizeOfGen(maxBit):
    binary=format(maxBit,'b')
    return len(binary)-1

def cuttingGen(chromosome,end,start=0):
    gens=[]
    gens=chromosome.split(' ')

    result=[]
    for i in range(len(gens)-1):
        if (start==0):
            if (i<= end):
                result.append(gens[i])
        else:
            if(i> start and i<= end):
                result.append(gens[i])


    if(not result):
        return ''


    return " ".join(result)


def initPopulation():
    i=0
    while(i<populationSize):
        #print('init population i = ',i)
        strs=[]
        chromosomesweight=0
        chromosomesfitness=0

        for key,value in combinationBitOfItem.items():
            capacityleft=C-chromosomesweight
            maxQuantity=int(capacityleft/Weight[key]) + 1
            r=random.randint(0,maxQuantity-1)

            #print('la taille du tableau value ',len(value),'et il vaut ',value)
           # print('key vaut',key)

            gen=value[r]


            quantity=convertStringToBinary(gen)
            #print('Quantité aléatoire de l objet',key,' est ',quantity,'son poids est',Weight[key],'la capacité ',C)
            #print('la quantité du gene ',r,'est ',quantity,'mais C/ w[key] vaut',C/Weight[key])
            #print('Weight avant',chromosomesweight)
            chromosomesweight=chromosomesweight+quantity*Weight[key]
            #print('weight apres',chromosomesweight)
            chromosomesfitness=chromosomesfitness+quantity*Profits[key]
            strs.append(value[r])
        if (chromosomesweight > C):
            print('Chromosome dépasse la capacité , Sac a dos ',C,' chromosome',chromosomesweight)

            continue

        string=' '.join(strs)
        Chromosomes.append(string)
        Fitness.append(chromosomesfitness)
        i=i+1
    return Chromosomes

def preProcess():
    i=0
    j=0
    for i in range(N):
        weight=Weight[i]
        profit=Profits[i]
        l= int(C/weight) +1
        #l=int(C/weight)
        binaries=[]
        maxSizeOfGene=getSizeOfGen(l)
        #print('Max Size du gene dont l= ',l,'est ',maxSizeOfGene)
        for j in range(l):
            binary=convertBinaryToGen(j,maxSizeOfGene)
         #   print('binaries[j] = ',binary)
            binaries.append(binary)

        #print('binaries sans toArray',binaries)
        combinationBitOfItem[i]=binaries #Binaries to array ?!
    return combinationBitOfItem

def parentSelection():
    size=len(Chromosomes)
    parentIndex=random.randint(0,size-1)
    bestFitness=Fitness[parentIndex]
    round=random.randint(2,size)
    for i in range(1,round):
        index=random.randint(0,size-1)
        if (index!=parentIndex and bestFitness<Fitness[index]):
            parentIndex=index
            bestFitness=Fitness[index]

    return parentIndex

def sortChromosomesByFitness():
    n=len(Chromosomes)
    for i in range(0,n-1):
        min_idx=i
        for j in range(i+1,n):
            if(Fitness[j] > Fitness[min_idx]):
                min_idx=j
        temp=Chromosomes[min_idx]
        Chromosomes[min_idx]=Chromosomes[i]
        Chromosomes[i]=temp

        indexTemp=Fitness[min_idx]
        Fitness[min_idx]=Fitness[i]
        Fitness[i]=indexTemp
    return Fitness,Chromosomes

def Parent():
    parentA=parentSelection()
    parentB=parentSelection()
    if (parentA==parentB): return Parent()
    parents=[]
    parents.append(parentA)
    parents.append(parentB)
    return parents
def geneticAlgorithm():
    preProcess()
    kTimes=5
    runs=5
    t=1
    T=6
    global populationSize
   # print('taille de la population',populationSize)

    for r in range(1,runs):
       # print('avant init population')
        initPopulation()
        #print('apres init population')
        global Chromosomes
        global Fitness

        for i in range(0,Generation):
            sortChromosomesByFitness()
            ps=populationSize
            take70percent =ps * (70 / 100)
            Chromosomes=Chromosomes[:int(take70percent)]
            Fitness=Fitness[:int(take70percent)]
            while( len(Chromosomes) < populationSize):
               # print('le nombre de solutions est ',len(Chromosomes))
                parent=Parent()
               # print('Parent vaut ',parent)
                parentAindex=parent[0]
                parentBindex=parent[1]
                division=random.randint(2,N-1)

                childA=cuttingGen(Chromosomes[parentAindex],division)+ ' ' + cuttingGen(Chromosomes[parentBindex],N,division)
               # print('fils A ',childA)
                childB=cuttingGen(Chromosomes[parentBindex],division)+ ' ' + cuttingGen(Chromosomes[parentAindex],N,division)
                #print('fils B ',childB)
                totalWeightA=calculateWeight(childA,Weight)
               # print(' le poids du fils A est ',totalWeightA,' C= ',C)
                if (totalWeightA >0 and totalWeightA<=C):
                    Chromosomes.append(childA)
                    Fitness.append(calculateFitness(childA,Profits))
                if (len(Chromosomes)==populationSize): break
                totalWeightB=calculateWeight(childB,Weight)

                if (totalWeightB > 0 and totalWeightB <= C):
                    Chromosomes.append(childB)
                    Fitness.append(calculateFitness(childB,Profits))
            if (random.random() <= mutationPercentage):
                indexMutation=random.randint(0,populationSize-1)
                genMutation=random.randint(0,N)
                chromosome=Chromosomes[indexMutation]
                gens=chromosome.split(' ')
                newChromosome=[]
                for j in range(0,len(gens)):
                    gen=gens[j]
                    if(j==genMutation):
                        increasingGen=convertStringToBinary(gen)
                        strGen=format(increasingGen,'b')
                        if (len(gen) >= len(strGen)):
                            newGen=convertBinaryToGen(increasingGen,len(gen))
                            if '0' not in newGen : break
                            newChromosome.append(newGen)
                        break
                    else :
                        newChromosome.append(gen)

                if (len(newChromosome)==N and calculateWeight(' '.join(newChromosome) ,Weight) <=C ):
                    Chromosomes[indexMutation]=' '.join(newChromosome)
        maxValue=max(Fitness)
        indexBestValue=np.argmax(Fitness)
        bestChromosomes.append(Chromosomes[indexBestValue])
        bestFitness.append(maxValue)
        maxs=bestChromosomes.count(Chromosomes[indexBestValue])
        if maxs==kTimes: break
        runs=runs+1
        
        if (runs==runSetting):
            #print('dans le if ')
            populationSize=populationSize+ populationSize*2
            runs=0 ##Ajouter

    indexResult=np.argmax(bestFitness)
    Gain=max(bestFitness)
    #print(' best fitness',Gain)
    #print('chromosomes ',Chromosomes[indexResult])
    #print('weight ',calculateWeight(Chromosomes[indexResult],Weight))
    return Gain



def input(runSettingIn,populationSizeIn,filename):
    global runSetting
    global populationSize
    global C
    global N
    runSetting = runSettingIn
    populationSize = populationSizeIn

    tab,N,C=getData(filename)

    for i in range(0,N):
        Weight.append(tab[i][0])
        Profits.append(tab[i][1])
    populationSize=populationSizeIn
    runSetting=runSettingIn
'''
test=getData("test.txt")
items= test[0]
C=test[2]
N=test[1]

input(10,50)
start = time.time()
gain=geneticAlgorithm()
end = time.time()
print("gain : ",gain,"\t temps :",end-start)

'''
'''
Les paramètres:
AG chinois:
nbr de tours
nbr de solutions
taille de tournoi de selection
proba de mutation


AG adaptative:
nbr d'itérations
taille de la population

recuit simulé random:
simpling size
temperature initiale
facteur de refoidissement
température finale

revuit simulé greedy:
simpling size
temperature initiale
facteur de refoidissement
température finale

'''