import os
import random
import time
import funkcije
import kombinacije
def randheuristika():
    nazkolone=[kombinacije.nazkombd, kombinacije.nazkombg, kombinacije.nazkombsp1, kombinacije.nazkombsp2, kombinacije.nazkombun1, kombinacije.nazkombun2, kombinacije.nazkombs]
    reznazkolone=[kombinacije.reznazkombd, kombinacije.reznazkombg, kombinacije.reznazkombsp1, kombinacije.reznazkombsp2, kombinacije.reznazkombun1, kombinacije.reznazkombun2, kombinacije.reznazkombs]
    vredkolone=[kombinacije.vredkombd, kombinacije.vredkombg, kombinacije.vredkombsp1, kombinacije.vredkombsp2, kombinacije.vredkombun1, kombinacije.vredkombun2, kombinacije.vredkombs]
    rezvredkolone=[kombinacije.rezvredkombd, kombinacije.rezvredkombg, kombinacije.rezvredkombsp1, kombinacije.rezvredkombsp2, kombinacije.rezvredkombun1, kombinacije.rezvredkombun2, kombinacije.rezvredkombs]

    brojpoteza=65
    brojac=0
    brojac2=0
    k=12
    while brojac<brojpoteza:
        x=funkcije.prvobacanje()
        ind=random.randint(1, 2)
        index=[]
        if ind==1 and brojac2<52:
            z=random.randint(0, 5)
            while len(nazkolone[z])==0:
                z=random.randint(0, 5)
            vredkolone[z][0]=funkcije.bodovi(x, nazkolone[z][0])
            rezvredkolone[z].append(vredkolone[z].pop(0))
            reznazkolone[z].append(nazkolone[z].pop(0))
            brojac2=brojac2+1 ######################################
        elif ind==2 and len(nazkolone[6])!=0:
                m=random.randint(0, k)
                vredkolone[6][m]=funkcije.bodovi(x, nazkolone[6][m])
                rezvredkolone[6].append(vredkolone[6].pop(m))
                reznazkolone[6].append(nazkolone[6].pop(m))
                k=k-1
        else:
            continue
        brojac=brojac+1

    brojbodova0=funkcije.suma(rezvredkolone[0])-rezvredkolone[0][6]-rezvredkolone[0][7]+rezvredkolone[0][6]-rezvredkolone[0][7]
    brojbodova1=funkcije.suma(rezvredkolone[1])-(rezvredkolone[1][5]+rezvredkolone[1][6])+(rezvredkolone[1][6]-rezvredkolone[1][5])
    brojbodova34=funkcije.suma(rezvredkolone[2])+funkcije.suma(rezvredkolone[3])-(rezvredkolone[2][0]+rezvredkolone[3][0])+(rezvredkolone[2][0]-rezvredkolone[3][0])
    brojbodova56=funkcije.suma(rezvredkolone[4])+funkcije.suma(rezvredkolone[5])-(rezvredkolone[4][6]+rezvredkolone[5][5])+(rezvredkolone[4][6]-rezvredkolone[5][5])
    brojbodovaslobodne=funkcije.suma(rezvredkolone[6])-(rezvredkolone[6][6]+rezvredkolone[6][7])+(rezvredkolone[6][6]-rezvredkolone[6][7])
    ukupnobodova=brojbodova0+brojbodova1+brojbodova34+brojbodova56+brojbodovaslobodne
    return ukupnobodova


        
