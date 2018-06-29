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
    print(z);
    brojac=brojac+1;
