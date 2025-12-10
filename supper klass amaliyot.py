# FAN klassi
class Fan:
    def __init__(self, nomi):
        self.nomi = nomi


# TALABA klassi
class Talaba:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh
        self.fanlar = []


    def fanga_yozil(self, fan_obj):
        if isinstance(fan_obj, Fan):
            self.fanlar.append(fan_obj)
            return f"{fan_obj.nomi} faniga yozildingiz."
        return "Xato: Fan obyektini yuboring!"

    def remove_fan(self, fan_nomi):
        for fan in self.fanlar:
            if fan.nomi == fan_nomi:
                self.fanlar.remove(fan)
                return f"{fan_nomi} fani o'chirildi."
        return "Siz bu fanga yozilmagansiz."

    def get_info(self):
        if self.fanlar:
            fanlar_str = ", ".join(f.nomi for f in self.fanlar)
        else:
            fanlar_str = "Fan yo‘q"

        return f"Talaba: {self.ism}, Yosh: {self.yosh}, Fanlar: {fanlar_str}"


# Shaxs klassi
class Professor:
    def __init__(self, ism, yosh, kafedra):
        self.ism = ism
        self.yosh = yosh
        self.kafedra = kafedra

    def get_info(self):
        return f"Professor: {self.ism}, Yosh: {self.yosh}, Kafedra: {self.kafedra}"


# foydalanuvchi klassi
class Foydalanuvchi:
    def __init__(self, ism, yosh, username):
        self.ism = ism
        self.yosh = yosh
        self.username = username

    def get_info(self):
        return f"Foydalanuvchi: {self.username}, Ism: {self.ism}, Yosh: {self.yosh}"


# mijoz klassi
class Mijoz:
    def __init__(self, ism, yosh, balans):
        self.ism = ism
        self.yosh = yosh
        self.balans = balans

    def get_info(self):
        return f"Mijoz: {self.ism}, Yosh: {self.yosh}, Balans: {self.balans} so'm"


# ADMIN
class Admin(Foydalanuvchi):
    def __init__(self, ism, yosh, username):
        super().__init__(ism, yosh, username)

    def ban_user(self, user):
        print(f"Foydalanuvchi bloklandi : {user.username}")
        """"Battar bo'lsin"""


# TEST
fan1 = Fan("Matematika")
fan2 = Fan("Fizika")

talaba = Talaba("Nilufar", 19)
print(talaba.fanga_yozil(fan1))
print(talaba.fanga_yozil(fan2))
print(talaba.get_info())

print(talaba.remove_fan("Fizika"))
print(talaba.remove_fan("Matem"))
print(talaba.get_info())

foyd = Foydalanuvchi("Nilufar", 19, "pynoova_n")
admin = Admin("Nilufar", 19, "pynoova_n")
admin.ban_user(foyd)
