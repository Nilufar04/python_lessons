#1-masala!
class Student:
    def __init__(self,ism,familiya,yil,malumot,email,kursi,telefonraqami):
#class xususiyatlari
        self.ism = ism
        self.familiya = familiya
        self.yil = yil
        self.malumot = malumot
        self.email = email
        self.kursi = kursi
        self.telefonraqami = telefonraqami

studentqiz = Student("Nilufar", "Husinova",2006,"oliy","nilufarhusinova2@gmail.com","2-kurs", 91_234_56_78 )
studentqiz1= Student("Lola","Gulmonova",2007,"oliy","lolagulmonova59@gmail.com","2-kurs",99_876_54_32)
studentqiz2 = Student("Shaydo","Pirnazarova",2005,"oliy","shaydopirnazarova15@gmail.com","2-kurs",50_123_45_67)
print(studentqiz.ism)
print(studentqiz.familiya)
print(studentqiz.yil)
print(studentqiz.malumot)
print(studentqiz.email)
print(studentqiz.kursi)
print(studentqiz.telefonraqami)

print(studentqiz1.ism)
print(studentqiz1.familiya)
print(studentqiz1.yil)
print(studentqiz1.malumot)
print(studentqiz1.email)
print(studentqiz1.kursi)
print(studentqiz1.telefonraqami)

print(studentqiz2.ism)
print(studentqiz2.familiya)
print(studentqiz2.yil)
print(studentqiz2.malumot)
print(studentqiz2.email)
print(studentqiz2.kursi)
print(studentqiz2.telefonraqami)



#ikkinchi masala!
class Student:
    def __init__(self,ism,familiya,yil,malumot,email,kursi,telefonraqami):
#class xusuxiyatlari
        self.ism = ism
        self.familiya = familiya
        self.yil = yil
        self.malumot = malumot
        self.email = email
        self.kursi = kursi
        self.telefonraqami = telefonraqami

#talaba haqida ma'lumot qaytaruvchi funksiya
    def get_info(self):
        return f"Ismi:{self.ism}, Familiyasi {self.familiya},Yil{self.yil},Malumot{self.malumot},Email{self.email} kursi {self.kursi} telefonraqami {self.telefonraqami}"

talabaqiz= Student("Nilufar","Husinova",2006,"Oliy" ,"nilufarhusinova11@gmail.com" , "2-kurs" ,91_234_56_78)
talabaqiz1 = Student("Lola","Gulmonova",2007,"Oliy","lolagulmonova07@gmail.com","2-kurs",99-876-54-32)

print(talabaqiz.get_info())
print(talabaqiz1.get_info())

#
3-Masala
class Student:
    def __init__(self,ism,familiya,yil):
        self.ism= ism
        self.familiya= familiya
        self.yil= yil
    def salom_ber(self):
        return f"Salom,{self.ism}!"
    def yilga_qosh (self):
        self.yil += 1
        return f"{self.ism}ning yangi yoshi : {self.yil} "
#obyekt yaratish
stu = Student("NIlufar","Husinova",2006)
stu1= Student("Lola","Gulmonova",2007)

#metodlarni chiqarish
print(stu.salom_ber())
print(stu1.salom_ber())
print(stu.yilga_qosh())
print(stu1.yilga_qosh())

# Qoshimcha masala!

class Avto:
    def __init__(self, model,yil,yurgan_km,narx):
        #Xususiyatlari
        self.model = model
        self.yil = yil
        self.yurgan_km = yurgan_km
        self.narx = narx

    def info(self):
        return (f"Model: {self.model}\n"
                f"Yil: {self.yil}\n"
                f"Yurgan KM: {self.yurgan_km}\n"
                f"Narx: ${self.narx}" )
    def yurish(self,km):
        if km < 0:
            print("km manfiy bo'lishi mumikin emas")
        else:
            self.yurgan_km += km

    def Chegirma(self,foiz):
        self.narx -= self.narx*foiz/100
#obyekti
malibu = Avto("Malibu",2024,150000,7000)
tracker = Avto("Tracker",2023,165000,6000)

#info metodlarni chiqarish
print(malibu.info())
print()
print(tracker.info())
print()

#chegirmalar
malibu.Chegirma(10)
tracker.Chegirma(10)
print(malibu.info())
print()
print(tracker.info())
print()


















