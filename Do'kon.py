# #product
# class Product():
#     def __init__(self, id ,nomi, narxi,soni,):
#         self.id = id
#         self.nomi = nomi
#         self.narxi = narxi
#         self.soni = 0
#     def get_info(self):
#         return (f"ID={self.id},Nomi {self.nomi} , 1 kgsi={self.narxi},{ self.soni}-kg bor")
#     def set_soni(self,soni):
#         self.soni = soni
# meva = Product (1,"Olma",10000,0)
# meva1 = Product(2,"Anor",15000,0)
# meva2 = Product(3,"Mandarin",15000,0)
# meva3 = Product(4,"Banan",18000,0)
# sabzavot = Product(5,"Kartoshka",6000,0)
# sabzavot1 = Product(6,"Piyoz",7000,0)
# meva.set_soni(100)
# meva1.set_soni(500)
# meva2.set_soni(200)
# meva3.set_soni(200)
# sabzavot.set_soni(110)
# sabzavot1.set_soni(550)
# print(meva.get_info())
# print(meva1.get_info())
# print(meva2.get_info())
# print(meva3.get_info())
# print(sabzavot.get_info())
# print(sabzavot1.get_info())
#

class Savat():
    def __init__(self):
        self.Mahsulot = []
        self.umumiy_narxi = 0
    def Mahsulot_qoshish(self,nom,narx):
        self.Mahsulot.append({"Nomi":nom,"Narxi":narx})
        self.umumiy_narxi += narx
print(f" {nomi} Savatga qoshildi.")




















