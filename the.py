import os
import random
import time
import funkcije
import kombinacije

nazkolone=[kombinacije.nazkombd[:], kombinacije.nazkombg[:], kombinacije.nazkombsp1[:], kombinacije.nazkombsp2[:], kombinacije.nazkombun1[:], kombinacije.nazkombun2[:], kombinacije.nazkombs[:]]
reznazkolone=[kombinacije.reznazkombd[:], kombinacije.reznazkombg[:], kombinacije.reznazkombsp1[:], kombinacije.reznazkombsp2[:], kombinacije.reznazkombun1[:], kombinacije.reznazkombun2[:], kombinacije.reznazkombs[:]]
vredkolone=[kombinacije.vredkombd[:], kombinacije.vredkombg[:], kombinacije.vredkombsp1[:], kombinacije.vredkombsp2[:], kombinacije.vredkombun1[:], kombinacije.vredkombun2[:], kombinacije.vredkombs[:]]
rezvredkolone=[kombinacije.rezvredkombd[:], kombinacije.rezvredkombg[:], kombinacije.rezvredkombsp1[:], kombinacije.rezvredkombsp2[:], kombinacije.rezvredkombun1[:], kombinacije.rezvredkombun2[:], kombinacije.rezvredkombs[:]]
def the():
    dtcpsniz=[]
    jedind=0
    minind=0
    maxind=0
    brojpoteza=65
    brojac=0
    while brojac<brojpoteza:
        brojac=brojac+1
        nizkombinacije=[]
        nizverovarnoce=[]
        nizkoeficijenata=[]
        nizkombinacijes=[]
        nizverovatnoces=[]
        nizkoeficijenatas=[]
        nizbodova=[]
        nizbodovas=[]
        refkoef=0;
        refkoefs=0
        z=0
        zs=0
        x=funkcije.prvobacanje()
        if funkcije.izbroji(1, x)>=3:
            n1=funkcije.zamena(x, funkcije.najpogodnijiniz(x, "jedinice"))
        else:
            for i in range(len(nazkolone)-1):
                if len(nazkolone[i])==0:
                    l="*"
                else:
                    l=nazkolone[i][0]
                niz=funkcije.najpogodnijiniz(x, l)
                nizkombinacije.append(niz)
                ver=funkcije.vrv(x, niz)
                nizverovarnoce.append(ver)
                bod=funkcije.bodovi(niz, l)
                nizbodova.append(bod)
                koef=funkcije.koef(bod, ver)
                nizkoeficijenata.append(koef)
                if koef>refkoef:
                    refkoef=koef
                    z=i
            n1=funkcije.zamena(x, nizkombinacije[z])
        nizkombinacije=[]
        nizverovarnoce=[]
        nizkoeficijenata=[]
        nizbodova=[]
        refkoef=0;
        if funkcije.izbroji(1, n1)>=3:
            n2=funkcije.zamena(n1, funkcije.najpogodnijiniz(n1, "jedinice"))
        else: 
            for i in range(len(nazkolone)-1):
                if len(nazkolone[i])==0:
                    l="*"
                else:
                    l=nazkolone[i][0]
                niz=funkcije.najpogodnijiniz(n1, l)
                nizkombinacije.append(niz)
                ver=funkcije.vrv(n1, niz)
                nizverovarnoce.append(ver)
                bod=funkcije.bodovi(niz, l)
                nizbodova.append(bod)
                koef=funkcije.koef(bod, ver)
                nizkoeficijenata.append(koef)
                if koef>refkoef:
                    refkoef=koef
                    z=i
            n2=funkcije.zamena(n1, nizkombinacije[z])
        nizkombinacije=[]
        nizverovarnoce=[]
        nizkoeficijenata=[]
        nizbodova=[]
        refkoef=0
        if funkcije.izbroji(1, n2)>=4:
            if len(nazkolone[0])!=0 and nazkolone[0][0]=="jedinice":
                vredkolone[0][0]=funkcije.bodovi(n2, nazkolone[0][0])
                rezvredkolone[0].append(vredkolone[0].pop(0))
                reznazkolone[0].append(nazkolone[0].pop(0))
                continue
            elif len(nazkolone[1])!=0 and nazkolone[1][0]=="jedinice":
                vredkolone[1][0]=funkcije.bodovi(n2, nazkolone[1][0])
                rezvredkolone[1].append(vredkolone[1].pop(0))
                reznazkolone[1].append(nazkolone[1].pop(0))
                continue
            elif len(nazkolone[2])!=0 and nazkolone[2][0]=="jedinice":
                vredkolone[2][0]=funkcije.bodovi(n2, nazkolone[2][0])
                rezvredkolone[2].append(vredkolone[2].pop(0))
                reznazkolone[2].append(nazkolone[2].pop(0))
                continue
            elif len(nazkolone[4])!=0 and nazkolone[4][0]=="jedinice":
                vredkolone[4][0]=funkcije.bodovi(n2, nazkolone[4][0])
                rezvredkolone[4].append(vredkolone[4].pop(0))
                reznazkolone[4].append(nazkolone[4].pop(0))
                continue
        else:
            for i in range(len(nazkolone)-1):
                if len(nazkolone[i])==0:
                    l="*"
                else:
                    l=nazkolone[i][0]
                niz=funkcije.najpogodnijiniz(n2, l)
                nizkombinacije.append(niz)
                ver=funkcije.vrv(n2, niz)
                nizverovarnoce.append(ver)
                bod=funkcije.bodovi(niz, l)
                nizbodova.append(bod)
                koef=funkcije.koef(bod, ver)
                nizkoeficijenata.append(koef)
                if koef>refkoef:
                    refkoef=koef
                    z=i
        for i in range(len(nazkolone[6])):
            if len(nazkolone[6])==0:
                m="*"
            else:
                m=nazkolone[6][i]
            nizs=funkcije.najpogodnijiniz(n2, m)
            nizkombinacijes.append(nizs)
            vers=funkcije.vrv(n2, nizs)
            nizverovatnoces.append(vers)
            bods=funkcije.bodovi(nizs, m)
            nizbodovas.append(bods)
            koefs=bods*vers*0.5
            nizkoeficijenatas.append(koefs)
            if koefs>refkoefs:
                refkoefs=koefs
                zs=i
        if len(nazkolone[6])!=0 and nizkoeficijenatas[zs]<=nizkoeficijenata[z]:
            vredkolone[z][0]=funkcije.bodovi(n2, nazkolone[z][0])
            rezvredkolone[z].append(vredkolone[z].pop(0))
            reznazkolone[z].append(nazkolone[z].pop(0))
        elif len(nazkolone[6])!=0:
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
        #brojac=brojac+1

    brojbodova01=0
    for i in range(0, 6):
        brojbodova01=brojbodova01+rezvredkolone[0][i]
    if brojbodova01>=60:
        brojbodova01=brojbodova01+30
    brojbodova02=rezvredkolone[0][0]*(rezvredkolone[0][6]-rezvredkolone[0][7])
    if brojbodova02>=60:
        brojbodova02=brojbodova02+30
    brojbodova03=0
    for i in range(8, 13):
        brojbodova03=brojbodova03+rezvredkolone[0][i]
    ukupno0=brojbodova01+brojbodova02+brojbodova03
    ########################################################################################################
    brojbodova11=0
    for i in range(7, 13):
        brojbodova11=brojbodova11+rezvredkolone[1][i]
    if brojbodova11>=60:
        brojbodova11=brojbodova11+30
    brojbodova12=rezvredkolone[1][12]*(rezvredkolone[1][6]-rezvredkolone[1][5])
    if brojbodova12>=60:
        brojbodova12=brojbodova12+30
    brojbodova13=0
    for i in range(0, 5):
        brojbodova13=brojbodova13+rezvredkolone[1][i]
    ukupno1=brojbodova11+brojbodova12+brojbodova13
    ########################################################################################################
    brojbodova21=0
    for i in range(1, 7):
        brojbodova21=brojbodova21+rezvredkolone[2][i]
    if brojbodova21>=60:
        brojbodova21=brojbodova21+30
    brojbodova22=rezvredkolone[2][6]*(rezvredkolone[2][0]-rezvredkolone[3][0])
    if brojbodova22>=60:
        brojbodova22=brojbodova22+30
    brojbodova23=0
    for i in range(1, 6):
        brojbodova23=brojbodova23+rezvredkolone[3][i]
    ukupno2=brojbodova21+brojbodova22+brojbodova23
    ########################################################################################################
    brojbodova31=0
    for i in range(0, 6):
        brojbodova31=brojbodova31+rezvredkolone[4][i]
    if brojbodova31>=60:
        brojbodova31=brojbodova31+30
    brojbodova32=rezvredkolone[4][0]*(rezvredkolone[4][6]-rezvredkolone[5][5])
    if brojbodova32>=60:
        brojbodova32=brojbodova32+30
    brojbodova33=0
    for i in range(0, 5):
        brojbodova33=brojbodova33+rezvredkolone[5][i]
    ukupno3=brojbodova31+brojbodova32+brojbodova33
    #######################################################################################################
    brojbodovas1=0
    for i in range(len(dtcpsniz)):
        brojbodovas1=brojbodovas1+rezvredkolone[6][dtcpsniz[i]]
    if brojbodovas1>=60:
        brojbodovas1=brojbodovas1+30
    brojbodovas2=rezvredkolone[6][jedind]*(rezvredkolone[6][maxind]-rezvredkolone[6][minind])
    donja=dtcpsniz
    donja.append(minind)
    donja.append(maxind)
    donja.append(jedind)
    vrednostis=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    otpad=[]
    brojbodovas3=0
    for i in range(len(vrednostis)):
        for j in range(len(donja)):
            if i==j:
                otpad.append(vrednostis.pop(0))
    for i in range(len(vrednostis)):
        brojbodovas3=brojbodovas3+rezvredkolone[6][vrednostis[i]]
    ukupnos=brojbodovas1+brojbodovas2+brojbodovas3
    ukupno=ukupno0+ukupno1+ukupno2+ukupno3+ukupnos

    #return ukupno

    prva=[]
    for i in range(len(rezvredkolone[1])):
        prva.append(rezvredkolone[1][len(rezvredkolone[1])-i-1])

    druga=[]
    for i in range(len(rezvredkolone[2])):
        druga.append(rezvredkolone[2][len(reznazkolone[2])-i-1])
    druga.extend(rezvredkolone[3])

    treca=[]
    for i in range(len(rezvredkolone[5])):
        treca.append(rezvredkolone[5][len(reznazkolone[5])-i-1])
    trecca=[]
    trecca.extend(rezvredkolone[4])
    trecca.extend(treca) 

    #print(rezvredkolone[0])
    #print("\n")
    #print(prva)
    #print("\n")
    #print(druga)
    #print("\n")
    #print(trecca)
    #print(ukupno)
    return ukupno


