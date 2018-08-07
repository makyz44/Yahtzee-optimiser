import os
import random
import time
import funkcije
import kombinacije

def heuristika1():
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
            if funkcije.vrv(n1, nizkombinacije[z]) == 1:
               vredkolone[z][0]=funkcije.bodovi(n1, nazkolone[z][0])
               rezvredkolone[z].append(vredkolone[z].pop(0))
               reznazkolone[z].append(nazkolone[z].pop(0))
            else:
                n2=funkcije.zamena(n1, nizkombinacije[z])
                if funkcije.vrv(n2, nizkombinacije[z]) == 1:
                    vredkolone[z][0]=funkcije.bodovi(n2, nazkolone[z][0])
                    rezvredkolone[z].append(vredkolone[z].pop(0))
                    reznazkolone[z].append(nazkolone[z].pop(0))     
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
                    else:
                        if len(vredkolone[z])!=0 or len(nazkolone[z])!=0:
                            vredkolone[z][0]=funkcije.bodovi(n2, vredkolone[z][0])
                            rezvredkolone[z].append(vredkolone[z].pop(0))
                            reznazkolone[z].append(nazkolone[z].pop(0))
                        else:
                            continue
        brojac=brojac+1

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

    return ukupno

b=0
for i in range(100):
    l=heuristika1()
    b=b+l
    print("{0}   {1}".format(i+1, l))
print("{0}   {1}".format("ukupno" ,b/100))


    
    
    

            

