import os
import random
import time
import funkcije
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
        if funkcije.vrv(n1, nizkombinacije[z]) == 1:
            vredkolone[z][0]=funkcije.bodovi(n1, nazkolone[z][0])
            rezvredkolone[z].append(vredkolone[z].pop(0))
            reznazkolone[z].append(nazkolone[z].pop(0))
        else:
            n2=funkcije.zamena(n1, nizkombinacije[z])
            if funkcije.vrv(n2, nizkombinacije[z]) == 1:
                vredkolone[z][0]=funkcije.bodovi(n2, nazkolone[z][0])
                rezvredkolone[z].append(vredkolone[z].pop(0))
                reznazkolone[z].append(nazkolone[z].pop(0))     ########
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
                print(zs)
                if funkcije.vrv(n2, nizkombinacijes[zs]) == 1:
                    vredkolone[6][zs]=funkcije.bodovi(n2, nazkolone[6][zs])
                    rezvredkolone[6].append(vredkolone[6].pop(zs))
                    reznazkolone[6].append(nazkolone[6].pop(zs))
                else:
                    if len(vredkolone[z])!=0 or len(nazkolone[z])!=0:
                        rezvredkolone[z].append(vredkolone[z].pop(0))
                        reznazkolone[z].append(nazkolone[z].pop(0))
                    else:
                        continue
    brojac=brojac+1
    print(rezvredkolone)
            

