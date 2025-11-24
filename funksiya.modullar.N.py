#""" funksiyalar!, *Args Usuliga misol"""
# def summa(*sonlar):
#     """Siz kiritgan sonlarning yig'indisini hisoblovchi funksiya"""
#     yigindi = 0
#     for sonlar in sonlar:
#         yigindi += sonlar
#     return yigindi
# print(summa(2,3,4,5))
#
# """Siz kiritgan sonlarning ko'paytmasini hisoblovchi funksiya"""
# def summa(*son):
#     kopaytma = 1
#     for son in son:
#         kopaytma *= son
#     return kopaytma
# print(summa(21,11,6))

# def summa(a, b,*sonlar):
#     """Siz kiritgan sonlarning yig'indisini hisoblovchi funksiya"""
#     return a+b+sum(sonlar)
# print(summa(1,2,3,4,5,6,7,8,9))

# """**Kwargs usuliga misol"""
# def gullar_dokoni(nomi, ranggi ,**malumotlar):
#     """Gullar haqida ma'lumotlarni lug'at ko'rinishida qay.fun"""
#     malumotlar['nomi']=nomi
#     malumotlar['ranggi']=ranggi
#     return malumotlar
#
# gullar = gullar_dokoni("Pion", "pushti", turi="ko'p yillik",sezoni="Baxor,yoz",narxi="35.000")
# gullar1 = gullar_dokoni("Atirgul","oq", turi="ko'p yillik",sezoni="Baxor,yoz,kuz",narxi="15.000")
# print(gullar,gullar1)

# """Modullarga misollar"""
# def nilesh_chechaklari(nomi, ranggi, hajmi ,narxi=None):
#     gul = {'nomi':nomi,
#            'ranggi':ranggi,
#            'hajmi':hajmi,
#            'narxi':narxi}
#     return gul
# def gul_tanla():
#     gullar=[] #Do'kondagi gullar uchun bo'sh ro'yxat!
#     while True:
#         print("\nQuyidagi ma;lumotlarni kiriting",end='')
#         nomi = input("Gul nomi: ")
#         ranggi = input("Gul ranggi: ")
#         hajmi = input("Gul hajmi: ")
#         narxi = input("Gul narxi: ")
#         gullar.append(nilesh_chechaklari(nomi, ranggi, hajmi, narxi))
#         javob = input(" Yana gullar qo'shamizmi (ha/yo'q): ")
#         if javob == 'yoq':
#             break
#     return gullar
#
# def gullar_print(nilesh_chechaklari):
#     print(f"{nilesh_chechaklari['nomi'].title() }"
#           f"{nilesh_chechaklari['rangi'].upper()}"
#           f"{nilesh_chechaklari['hajmi'].upper()}"
#           f"{nilesh_chechaklari['narxi']} $")
# """Pythondagi modullar!"""
# import math
# import random

# import  math
# """math moduli"""
# x=25
# print(math.sqrt(x))
# """Pow moduli"""
# print(pow(2,8))
# """PI moduli"""
# from math import pi
# print(pi)
# """.log moduli"""
# print(math.log2(8))
# print(math.log10(100))
# print(math.floor(math.log10(100)))
# print(math.ceil(math.log2(8)))
# """Random Moduli"""
import random as N #random modulini N deb chaqiramiz
# son = N.randint(11,21)
# print(son)
# import random as N #random modulini N deb chaqiramiz
# gullar =['Pion','Lola','atirgul','boychechak']
# gul=N.choice(gullar) #Gullardan tasodifiy gul tanlaydi
# print(gul)
# print(N.choice(gul))#guldan tasodifiy harfni tanlaydi

# x =list(range(11,21,6))
# print(x)
# print(N.choices(x))
#
# x = list(range(21))
# print(x)
# N.shuffle(x)
# print(x)