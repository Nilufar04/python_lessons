"""*Args Usuliga misol"""
def summa(*sonlar):
    """Siz kiritgan sonlarning yig'indisini hisoblovchi funksiya"""
    yigindi = 0
    for sonlar in sonlar:
        yigindi += sonlar
    return yigindi
print(summa(2,3,4,5))

"""Siz kiritgan sonlarning ko'paytmasini hisoblovchi funksiya"""
def summa(*son):
    kopaytma = 1
    for son in son:
        kopaytma *= son
    return kopaytma
print(summa(21,11,6))

def summa(a, b,*sonlar):
    """Siz kiritgan sonlarning yig'indisini hisoblovchi funksiya"""
    return a+b+sum(sonlar)
print(summa(1,2,3,4,5,6,7,8,9))

"""**Kwargs usuliga misol"""
def gullar_dokoni(nomi, ranggi ,**malumotlar):
    """Gullar haqida ma'lumotlarni lug'at ko'rinishida qay.fun"""
    malumotlar['nomi']=nomi
    malumotlar['ranggi']=ranggi
    return malumotlar

gullar = gullar_dokoni("Pion", "pushti", turi="ko'p yillik",sezoni="Baxor,yoz",narxi="35.000")
gullar1 = gullar_dokoni("Atirgul","oq", turi="ko'p yillik",sezoni="Baxor,yoz,kuz",narxi="15.000")
print(gullar,gullar1)
