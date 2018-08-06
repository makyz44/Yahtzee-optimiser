import os
import random
import time
import funkcije
import kombinacije

def heuristika2():
    nazkolone=[kombinacije.nazkombd[:], kombinacije.nazkombg[:], kombinacije.nazkombsp1[:], kombinacije.nazkombsp2[:], kombinacije.nazkombun1[:], kombinacije.nazkombun2[:], kombinacije.nazkombs[:]]
    reznazkolone=[kombinacije.reznazkombd[:], kombinacije.reznazkombg[:], kombinacije.reznazkombsp1[:], kombinacije.reznazkombsp2[:], kombinacije.reznazkombun1[:], kombinacije.reznazkombun2[:], kombinacije.reznazkombs[:]]
    vredkolone=[kombinacije.vredkombd[:], kombinacije.vredkombg[:], kombinacije.vredkombsp1[:], kombinacije.vredkombsp2[:], kombinacije.vredkombun1[:], kombinacije.vredkombun2[:], kombinacije.vredkombs[:]]
    rezvredkolone=[kombinacije.rezvredkombd[:], kombinacije.rezvredkombg[:], kombinacije.rezvredkombsp1[:], kombinacije.rezvredkombsp2[:], kombinacije.rezvredkombun1[:], kombinacije.rezvredkombun2[:], kombinacije.rezvredkombs[:]]

    dtcpsniz=[]
    jedind=0
    minind=0
    maxind=0
    brojpoteza=65
    brojac=0
    while brojac<brojpoteza:
        nizkombinacije = []
        nizkombinacijes=[]
        nizverovatnoce = []
        nizverovatnoces=[]
        refver=0
        refvers=0
        z=0
        z1=0
        zs=0
        x=funkcije.prvobacanje()
        for i in range(len(nazkolone)-1):
            if len(nazkolone[i])==0:
                l="*"
            else:
                l=nazkolone[i][0]
            nz=funkcije.najpogodnijiniz(x, l)
            nizkombinacije.append(nz)
            ver=funkcije.vrv(x, nz)
            nizverovatnoce.append(ver)
            if ver>refver:
                 refver=ver
                 z=i
        if funkcije.vrv(x, nizkombinacije[z]) == 1:
            vredkolone[z][0]=funkcije.bodovi(x, nazkolone[z][0])
            rezvredkolone[z].append(vredkolone[z].pop(0))
            reznazkolone[z].append(nazkolone[z].pop(0))
        else:
                n1=funkcije.zamena(x, nizkombinacije[z])
                for i in range(len(nazkolone)-1):
                    if len(nazkolone[i])==0:
                        l="*"
                    else:
                        l=nazkolone[i][0]
                    nz=funkcije.najpogodnijiniz(n1, l)
                    nizkombinacije.append(nz)
                    ver=funkcije.vrv(n1, nz)
                    nizverovatnoce.append(ver)
                    if ver>refver:
                        refver=ver
                        z=i
                if funkcije.vrv(n1, nizkombinacije[z]) == 1:
                    vredkolone[z][0]=funkcije.bodovi(n1, nazkolone[z][0])
                    rezvredkolone[z].append(vredkolone[z].pop(0))
                    reznazkolone[z].append(nazkolone[z].pop(0))###############
                else:
                        n2=funkcije.zamena(n1, nizkombinacije[z])
                        for i in range(len(nazkolone)-1):
                            if len(nazkolone[i])==0:
                                l="*"
                            else:
                                l=nazkolone[i][0]
                        nz=funkcije.najpogodnijiniz(n2, l)
                        nizkombinacije.append(nz)
                        ver=funkcije.vrv(n2, nz)
                        nizverovatnoce.append(ver)
                        if ver>refver:
                            refver=ver
                            z=i
                        if funkcije.vrv(n2, nizkombinacije[z]) == 1:
                            vredkolone[z][0]=funkcije.bodovi(n2, nazkolone[z][0])
                            rezvredkolone[z].append(vredkolone[z].pop(0))
                            reznazkolone[z].append(nazkolone[z].pop(0))###############
                        else:
                                for i in range(len(nazkolone[6])):
                                    if len(nazkolone[6])==0:
                                        m="*"
                                    else:
                                        m=nazkolone[6][i]
                                    nzs=funkcije.najpogodnijiniz(n2, m)
                                    nizkombinacijes.append(nzs)
                                    vers=funkcije.vrv(n2, nzs)
                                    nizverovatnoces.append(vers)
                                    if vers>refvers:
                                            refvers=vers
                                            zs=i
                                if funkcije.vrv(n2, nizkombinacijes[zs]) == 1:
                                    if nazkolone[6][zs]=="dvojke" or nazkolone[6][zs]=="trojke" or nazkolone[6][zs]=="cetvorke" or nazkolone[6][zs]=="petice" or nazkolone[6][zs]=="sestice":
                                        dtcpsniz.append(len(reznazkolone[6]))
                                    elif nazkolone[6][zs]=="jedinice":
                                        jedind=len(reznazkolone[6])
                                    elif nazkolone[6][zs]=="minimum":
                                        minind=len(reznazkolone[6])
                                    elif nazkolone[6][zs]=="maximum":
                                        maxind=len(reznazkolone[6])
                                    vredkolone[6][zs]=funkcije.bodovi(n2, nazkolone[6][zs])
                                    rezvredkolone[6].append(vredkolone[6].pop(zs))
                                    reznazkolone[6].append(nazkolone[6].pop(zs))
                                    #print(len(nazkolone[6]))
                                else:
                                    if len(vredkolone[z])!=0 or len(nazkolone[z])!=0:
                                        vredkolone[z][0]=funkcije.bodovi(n2, vredkolone[z][0])
                                        rezvredkolone[z].append(vredkolone[z].pop(0))
                                        reznazkolone[z].append(nazkolone[z].pop(0))
                                    else:
                                        continue
            
        brojac=brojac+1

    brojbodova0=funkcije.suma(rezvredkolone[0])-rezvredkolone[0][6]-rezvredkolone[0][7]+rezvredkolone[0][6]-rezvredkolone[0][7]
    brojbodova1=funkcije.suma(rezvredkolone[1])-(rezvredkolone[1][5]+rezvredkolone[1][6])+(rezvredkolone[1][6]-rezvredkolone[1][5])
    brojbodova34=funkcije.suma(rezvredkolone[2])+funkcije.suma(rezvredkolone[3])-(rezvredkolone[2][0]+rezvredkolone[3][0])+(rezvredkolone[2][0]-rezvredkolone[3][0])
    brojbodova56=funkcije.suma(rezvredkolone[4])+funkcije.suma(rezvredkolone[5])-(rezvredkolone[4][6]+rezvredkolone[5][5])+(rezvredkolone[4][6]-rezvredkolone[5][5])
    brojbodovaslobodne=funkcije.suma(rezvredkolone[6])-(rezvredkolone[6][6]+rezvredkolone[6][7])+(rezvredkolone[6][6]-rezvredkolone[6][7])
    bonus11=0
    bonus22=0
    bonus33=0
    bonus44=0
    bonus1=0
    for i in range(6):
        bonus1=bonus1+rezvredkolone[0][i]
    if bonus1>=60:
        bonus11=30
    bonus2=0
    for i in range(7, 13):
        bonus2=bonus2+rezvredkolone[1][i]
    if bonus2>=60:
        bonus22=30
    bonus3=0
    for i in range(1, 7):
        bonus3=bonus3+rezvredkolone[2][i]
    if bonus3>=60:
        bonus33=30
    bonus4=0
    for i in range(6):
        bonus4=bonus4+rezvredkolone[5][i]
    if bonus4>=60:
        bonus44=30
    ukupnobodova=brojbodova0+brojbodova1+brojbodova34+brojbodova56+brojbodovaslobodne+bonus11+bonus22+bonus33+bonus44
    print(jedind)
    print(dtcpsniz)
    print(minind)
    print(maxind)
    print(rezvredkolone)

heuristika2()

    
