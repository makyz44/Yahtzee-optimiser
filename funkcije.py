import kombinacije
import random
import os

imekombinacija = ["jedinice", "dvojke", "trojke", "cetvorke", "petice", "sestice", "maximum", "minimum", "kenta", "triling", "ful", "kare", "jamb"]

#Generator prvog bacanja(kockice)
def prvobacanje():        
    kockice = []
    for i in range(5):
        kockice.append(random.randint(1, 6))
    kockice.sort()
    return kockice

#Drugo bacanje za random igraca
def randdrugobacanje(n, kockice):      
    kockice2=kockice
    for i in range(n):
        k=random.randint(0, 4)
        kockice2[k]=random.randint(1, 6)
        kockice2.sort()
    return kockice2

#Racuna n[i+1] - n[i]
def izvod(niz):     
    izvodkoc = []
    for i in range(len(niz)-1):
        izvodkoc.append(niz[i+1]-niz[i])
    return izvodkoc

#Broji koliko ima "broja" u "nizu"
def izbroji(broj, niz):
    bb=0
    for i in range(len(niz)):
        if niz[i]==broj:
            bb=bb+1
    return bb

#Transformise niz u histogram oblika [n1 n2 n3 n4 n5 n6] npr. [2 3 3 3 5] -> [0 1 3 0 1 0]
def arrtohis(niz):      
    n1=izbroji(1, niz)
    n2=izbroji(2, niz)
    n3=izbroji(3, niz)
    n4=izbroji(4, niz)
    n5=izbroji(5, niz)
    n6=izbroji(6, niz)
    histogram=[n1, n2, n3, n4, n5, n6]
    return histogram

#Pravi niz od histograma nrp. [0 1 3 0 1 0] -> [2 3 3 3 5]
def histtoarr(histogram):     
    niz=[]
    for i in range(histogram[0]):
        niz.append(1)
    for i in range(histogram[1]):
        niz.append(2)
    for i in range(histogram[2]):
        niz.append(3)
    for i in range(histogram[3]):
        niz.append(4)
    for i in range(histogram[4]):
        niz.append(5)
    for i in range(histogram[5]):
        niz.append(6)
    return niz

#Racuna sumu niza
def suma(niz):      
    s=0
    for i in range(len(niz)):
        s=s+niz[i]
    return s

#Izracunava verovatnocu x od z
def vrv(x, z):    
    if z==[] or z==[0, 0, 0, 0, 0]:
        v=0
    else:
        tx= arrtohis(x)
        r=[]
        vnn=[]
        ns=0
        v=1
        tz=arrtohis(z)
        for i in range(6):
            r.append(tx[i]-tz[i])
        for i in range(6):
            if r[i] > 0:
                vnn.append(r[i])
        ns=suma(vnn)
        v=(1/6)**ns
    return v

#Menja nepotrebne kockice x niza da bi se dobila z kombinacija
def zamena(x, z):       
    inn=[]
    vnn=[]
    r=[]
    n=[]
    tx=arrtohis(x)
    tz=arrtohis(z)
    for i in range(6):
        r.append(tx[i]-tz[i])
    for i in range(6):
        if r[i]>0:
            vnn.append(r[i])
            inn.append(i)
    for i in range(6):
        if r[i]>0:
            tx[i]=tx[i]-r[i]
    for i in range(sum(vnn)):
        k=random.randint(0, 5);
        tx[k]=tx[k]+1
    n=histtoarr(tx)
    return n

#Racunanje bodova kombinacije x u zavisnosti od imena kombinacije
def bodovi(x, string):
    p=izvod(x)
    b=0
    if string=="jedinice":
        b=izbroji(1, x)*1
    elif string=="dvojke":
        b=izbroji(2, x)*2
    elif string=="trojke":
        b=izbroji(3, x)*3
    elif string=="cetvorke":
        b=izbroji(4, x)*4
    elif string=="petice":
        b=izbroji(5, x)*5
    elif string=="sestice":
        b=izbroji(6, x)*6
    elif string=="maximum":
        b=suma(x);
    elif string=="minimum":
        b=suma(x);
    elif string == "triling":
        if izbroji(0, p)>=2:
            b=suma(x)
        else:
            b=0
    elif string == "ful":
        if izbroji(0, p)>=3 and (p[1]>=1 or p[2]>=1):
            b=suma(x)+30
        else:
            b=0      
    elif string == "kare":
        if izbroji(0, p)>=3 and (p[0]>=1 or p[3]>=1):
            broj=[]
            nb=0
            for i in range(6):
                broj.append(izbroji(i+1, x))
            for i in range(6):
                if broj[i]>nb:
                    nb=broj[i]
                    z=i+1
            b=z*4+40   
        else:
            b=0
    elif string == "jamb":
        if izbroji(0, izvod(x))==4:
            broj=[]
            nb=0
            for i in range(6):
              broj.append(izbroji(i+1, x));
            for i in range(6):
               if broj[i]>nb:
                   nb=broj[i]
                   z=i+1
            b=z*5+50
        else:
           b=0
    elif string==None:
        b=0
    return b

#Nalazi niz "jedinice", "dvojke",...,"sestice" sa najvecom verovatncom da se dobije za kombinaciju x
#npr. za kombinaciju [1 2 3 3 5] za "trojke" je najbolja kombinacija [2 3 3 3 5]
def najvrv123456(x, string):
    uk=[];
    nv=[];
    rvr=0;
    for t in range(6):
        if string==imekombinacija[t]:
            for i in range(6):
                k=[t+1, t+1, t+1, t+1]
                k.extend([i+1])
                k.sort()
                uk.append(k)
            for i in range(len(uk)):
                nv.append(vrv(x, uk[i]))
            for i in range(len(nv)):
                if nv[i]>=rvr:
                    rvr=nv[i]
                    dk=uk[i]
    return dk;

#Radi isto kao i prethodna f-ja, samo sto je ova za max i min
def najvrvmnmx(x, string):
    if string=="maximum":
        return najvrv123456(x, "sestice")
    elif string=="minimum":
        return najvrv123456(x, "jedinice");

def najvrvdkolona(x, string):
    brojcifara=[]
    rvr=0;
    nv=[];
    nbc=0;
    uk=[];
##########################################################################
    if string == "kenta":
        if vrv(x, [1, 2, 3, 4, 5]) > vrv(x, [2, 3, 4, 5, 6]):
            rvr=vrv(x, [1, 2, 3, 4, 5])
            dk=[1, 2, 3, 4, 5]
        else:
            rvr=vrv(x, [2, 3, 4, 5, 6])
            dk=[1, 2, 3, 4, 5]
##########################################################################
    elif string == "triling":
        for i in range(6):
            brojcifara.append(izbroji(i+1, x))
        for i in range(6):
            if brojcifara[i]>=nbc:
                nbc=brojcifara[i]
                z=i+1
        for i in range(6):
            for j in range(6):
                if j>=i:
                    k=[z, z, z]
                    k.extend([i+1, j+1])
                    k.sort()
                    uk.append(k)
        for i in range(len(uk)):
            nv.append(vrv(x, uk[i]))
        for i in range(len(nv)):
            if nv[i]>=rvr:
                rvr=nv[i]
                dk=uk[i]
##########################################################################
    elif string == "ful":
        for i in range(6):
                for j in range(6):
                        k=[i+1, i+1, j+1, j+1, j+1]
                        k.sort()
                        uk.append(k)
        for i in range(len(uk)):
            nv.append(vrv(x, uk[i]))
        for i in range(len(nv)):
            if nv[i]>=rvr:
                rvr=nv[i]
                dk=uk[i]
##########################################################################
    elif string == "kare":
        for i in range(6):
            brojcifara.append(izbroji(i+1, x))
        for i in range(6):
            if brojcifara[i]>=nbc:
                nbc=brojcifara[i]
                z=i+1
        for i in range(6):
                    k=[z, z, z, z]
                    k.extend([i+1])                 
                    k.sort()
                    uk.append(k)
        for i in range(len(uk)):
            nv.append(vrv(x, uk[i]))
        for i in range(len(nv)):
            if nv[i]>=rvr:
                rvr=nv[i]
                dk=uk[i]
##########################################################################
    elif string == "jamb":
        for i in range(6):
            brojcifara.append(izbroji(i+1, x))
        for i in range(6):
            if brojcifara[i]>=nbc:
                nbc=brojcifara[i]
                z=i+1
        dk=[z, z, z, z, z]
    return dk

##Bez obzira na kombinaciju racuna najpogodniji niz
#def najpogodnijiniz(x, string):
#    niz=[];
#    for i in range(6):
#        if string == imekombinacija[i]:
#            niz = najvrv123456(x, string);
#    if string==imekombinacija[6] or string==imekombinacija[7]:
#            niz = najvrvmnmx(x, string)
#    else:
#        for i in range(8, 13):
#            if string==imekombinacija[i]:
#                niz = najvrvdkolona(x, string)
#    return niz

#Bez obzira na kombinaciju racuna najpogodniji niz
def najpogodnijiniz(x, string=None):
    niz=[];
    br=0;
    for i in range(6):
        if string == imekombinacija[i]:
            niz = najvrv123456(x, string);
    if string==imekombinacija[6] or string==imekombinacija[7]:
            niz = najvrvmnmx(x, string)
    for i in range(8, 13):
            if string==imekombinacija[i]:
                niz = najvrvdkolona(x, string)
    for i in range(13):
        if string == imekombinacija[i]:
            br=br+1
    if br==0 or string==None:
        niz=[0, 0, 0, 0, 0]
    return niz

def koef(bodovi, verovatnoca):
    k=bodovi*verovatnoca
    return k

