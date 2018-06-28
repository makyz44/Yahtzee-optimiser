import os
import random
import time
import funkcija
import kombinacije

nazkolone=[kombinacije.nazkombd, kombinacije.nazkombg, kombinacije.nazkombsp1, kombinacije.nazkombsp2, kombinacije.nazkombun1, kombinacije.nazkombun2, kombinacije.nazkombs]
reznazkolone=[kombinacije.reznazkombd, kombinacije.reznazkombg, kombinacije.reznazkombsp1, kombinacije.reznazkombsp2, kombinacije.reznazkombun1, kombinacije.reznazkombun2, kombinacije.reznazkombs]
vredkolone=[kombinacije.vredkombd, kombinacije.vredkombg, kombinacije.vredkombsp1, kombinacije.vredkombsp2, kombinacije.vredkombun1, kombinacije.vredkombun2, kombinacije.vredkombs]
rezvredkolone=[kombinacije.rezvredkombd, kombinacije.rezvredkombg, kombinacije.rezvredkombsp1, kombinacije.rezvredkombsp2, kombinacije.rezvredkombun1, kombinacije.rezvredkombun2, kombinacije.rezvredkombs]

brojpoteza=65
brojac=0
while brojac<brojpoteza:
    nizkombinacije = []
    nizkombinacijes=[]
    nizverovatnoce = []
    nizverovatnoces=[]
    refver=0;
    refvers=0;
    z=0;
    z1=0;
    z2=0;
    zs=0;
    x=funkcija.prvobacanje();
    for i in range(6):
        if len(nazkolone[i])>=1:
            niz=funkcija.najpogodnijiniz(x, nazkolone[i][0])
            nizkombinacije.append(niz);
            ver=funkcija.vrv(x, niz);
            nizverovatnoce.append(ver);
        else:
            continue
    for i in range(len(nizverovatnoce)):
        if nizverovatnoce[i]>refver:
            refver=nizverovatnoce[i]
            z=i
    n1=funkcija.zamena(x, nizkombinacije[z])
    if funkcija.vrv(n1, nizkombinacije[z]) == 1:                        #
        if len(nazkolone[z])>=1:
            vredkolone[z][0]=funkcija.bodovi(n1, nazkolone[z][0])
            rezvredkolone[z].append(vredkolone[z].pop(0))
            reznazkolone[z].append(nazkolone[z].pop(0))
        else:
            continue
    else:
        for i in range(6):
            niz=funkcija.najpogodnijiniz(n1, nazkolone[i][0])
            nizkombinacije.append(niz);
            ver=funkcija.vrv(n1, niz);
            nizverovatnoce.append(ver);
        for i in range(len(nizverovatnoce)):
            if nizverovatnoce[i]>refver:
                refver=nizverovatnoce[i]
                z1=i
        n2=funkcija.zamena(n1, nizkombinacije[z1])
        if funkcija.vrv(n2, nizkombinacije[z1]) == 1:
            if len(nazkolone[z1])>=1:                                                   #
                vredkolone[z1][0]=funkcija.bodovi(n2, nazkolone[z1][0])
                rezvredkolone[z1].append(vredkolone[z1].pop(0))
                reznazkolone[z1].append(nazkolone[z1].pop(0))
            else:
                continue
        else:
            for i in range(len(nazkolone[6])):
                nizs=funkcija.najpogodnijiniz(n2, nazkolone[6][i])
                nizkombinacijes.append(nizs)
                vers=funkcija.vrv(n2, nizs)
                nizverovatnoces.append(vers)
            for i in range(len(nizverovatnoces)):
                if nizverovatnoces[i]>refvers:
                    refvers=nizverovatnoces[i];
                    zs=i
            if funkcija.vrv(n2, nizkombinacijes[zs])==1:
                if len(nazkolone[zs])>=1:                                   #
                    vredkolone[6][zs]=funkcija.bodovi(n2, nazkolone[6][zs])
                    rezvredkolone[6].append(vredkolone[6].pop(zs))
                    reznazkolone[6].append(nazkolone[6].pop(zs))
                    kombinacije.vremkombs[zs]=brojac
                else:
                    continue
            else:
                vredkolone[z][0]=0
                rezvredkolone[z].append(vredkolone[z].pop(0))
                reznazkolone[z].append(nazkolone[z].pop(0))
    brojac=brojac+1
    print(rezvredkolone)











    










