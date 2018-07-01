import os 
import random
import funkcije
import math
import kombinacije

nazkolone=[kombinacije.nazkombd[:], kombinacije.nazkombg[:], kombinacije.nazkombsp1[:], kombinacije.nazkombsp2[:], kombinacije.nazkombun1[:], kombinacije.nazkombun2[:], kombinacije.nazkombs[:]]
reznazkolone=[kombinacije.reznazkombd[:], kombinacije.reznazkombg[:], kombinacije.reznazkombsp1[:], kombinacije.reznazkombsp2[:], kombinacije.reznazkombun1[:], kombinacije.reznazkombun2[:], kombinacije.reznazkombs[:]]
vredkolone=[kombinacije.vredkombd[:], kombinacije.vredkombg[:], kombinacije.vredkombsp1[:], kombinacije.vredkombsp2[:], kombinacije.vredkombun1[:], kombinacije.vredkombun2[:], kombinacije.vredkombs[:]]
rezvredkolone=[kombinacije.rezvredkombd[:], kombinacije.rezvredkombg[:], kombinacije.rezvredkombsp1[:], kombinacije.rezvredkombsp2[:], kombinacije.rezvredkombun1[:], kombinacije.rezvredkombun2[:], kombinacije.rezvredkombs[:]]

brojpoteza=65
brojac=0
while brojac<brojpoteza:
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
        koef=bod*ver
        nizkoeficijenata.append(koef)
        if koef>refkoef:
            refkoef=koef
            z=i
    n1=funkcije.zamena(x, nizkombinacije[z])
    nizkombinacije=[]
    nizverovarnoce=[]
    nizkoeficijenata=[]
    nizkombinacijes=[]
    nizverovatnoces=[]
    nizkoeficijenatas=[]
    nizbodova=[]
    nizbodovas=[]
    refkoef=0;
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
        koef=bod*ver
        nizkoeficijenata.append(koef)
        if koef>refkoef:
            refkoef=koef
            z=i
    n2=funkcije.zamena(n1, nizkombinacije[z])
    nizkombinacije=[]
    nizverovarnoce=[]
    nizkoeficijenata=[]
    nizkombinacijes=[]
    nizverovatnoces=[]
    nizkoeficijenatas=[]
    nizbodova=[]
    nizbodovas=[]
    refkoef=0;
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
        koef=bod*ver
        nizkoeficijenata.append(koef)
        if koef>refkoef:
            refkoef=koef
            z=i
    for i in range(len(nazkolone[6])):
        if len(nazkolone[6])==0:
            l="*"
        else:
            l=nazkolone[6][i]
        nizs=funkcije.najpogodnijiniz(n2, l)
        nizkombinacijes.append(nizs)
        vers=funkcije.vrv(n2, nizs)
        nizverovatnoces.append(vers)
        bods=funkcije.bodovi(nizs, l)
        nizbodovas.append(bods)
        koefs=bods*vers*0.5
        nizkoeficijenatas.append(koefs)
        if koefs>refkoefs:
            refkoefs=koefs
            zs=i
    if nizkoeficijenata[z]>=nizkoeficijenatas[zs] and len(nazkolone[z])!=0:
        vredkolone[z][0]=funkcije.bodovi(n2, nazkolone[z][0])
        rezvredkolone[z].append(vredkolone[z].pop(0))
        reznazkolone[z].append(nazkolone[z].pop(0))
        continue
    elif nizkoeficijenata[z]<nizkoeficijenatas[zs]:
        vredkolone[6][zs]=funkcije.bodovi(n2, nazkolone[6][zs])
        rezvredkolone[6].append(vredkolone[6].pop(zs))
        reznazkolone[6].append(nazkolone[6].pop(zs))
        continue
    print(brojac)
    brojac=brojac+1

print(rezvredkolone)




    
