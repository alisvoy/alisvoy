# qurulmalar = ["telfon", 'TV', 'wifi', 'sichqoncha', 'headphones']
# print(qurulmalar[1].lower())

# .upper()
# .lower()

# # ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting
# ismlar = ["Ali", "Vali", "Hasan", "Husan", "G'ani"] 

# # Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring:
# print("Salom " + ismlar[0] + ismlar[1] + ismlar[-1] + " ishlaring yaxshimi?")
# print(f"Salom {ismlar[0].upper()}, {ismlar[1].lower()}, {ismlar[-1]} ishlaring yaxshimi?")

# yil = input("Tugùlgan yilizni kiriting:  ")
# print(f'Siz {yil}-yilda tug`ulgansiz.')

# f_name = input("ism familya:  ")
# year = int(input("tug yil kiriting:  "))
# address = input("manzil:  ")
# phone = int(input("tel;  "))
# print(f"""Salom {f_name.title()}, sizning yoshingiz 
# {2022-year}da siz, manzil: {address.capitalize()}, 
# tel: {phone}""")


# print(f"  ")   # f - string
# sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik).

# sonlar = [22, -58.2, 34.0, 67, 1983, 123_456_000_0, 112.4]
# # print(sonlar)
# # print(sonlar[-1])

# # Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring.
# sonlar[0] = sonlar[0] + sonlar[-1]
# sonlar[1] = -67.8
# sonlar[4] = sonlar[4] + 40
# del sonlar[5]
# del sonlar[0]
# print(sonlar)

# t_shaxslar = ["amir temur", "Imom Buxoriy", "Napoleon"]

# z_shaxslar = ["Bill Gates", "Elon Musk", "Doasnald Trump"]

# # # # Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (.pop()), quyidagi ko'rinishda chiqaring:
# print(f"\nMen tarixiy shaxslardan {t_shaxslar.pop(0).title()} \n\
# bilan, zamonaviy shaxslardan esa {z_shaxslar.pop(0)} bilan\n\
# suhbat qilishni istar edim\n")

# print(f"""Men tarixiy shaxslardan {t_shaxslar.pop(1)} bilan,
# zamonaviy shaxslardan esa {z_shaxslar.pop(0)} bilan
# suhbat qilishni istar edim""")

# print(z_shaxslar)
# print(t_shaxslar)

# friends nomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga 
# chaqirmoqchi bo'lgan do'stlaringizni kiriting.
# friends = []
# friends.append("John")
# friends.append("Alex")
# friends.append("Danny")
# friends.append("Sobirjon")
# friends.append("Vanya")
# print(f"To`liq list-{friends}")

# # # # Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang.
# friends.remove("John")
# friends.remove("Alex")
# friends.remove("Vanya")
# print(f"Kelganlar-{friends}")


# friends = []
# # Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.
# friends.append("Hasan")
# friends.insert(0, "Husan")
# friends.insert(2, "Ivan")
# friends.insert(3, "ali")
# print(friends)

# Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating. 
# .pop() va .append() metodlari yordamida mehmonga kelgan 
# do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.
# mehmonlar = []
# mehmonlar.append(friends.pop(1))
# mehmonlar.append(friends.pop(-1))
# mehmonlar.append(friends.pop(0))
# mehmonlar.insert(2, friends.pop(0))
# print("\nKelgan mehmonlar: ", mehmonlar)
