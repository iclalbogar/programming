# isim = input("İsminizi girin : ")

# soyad = input("Soyadınızı girin : ")

# birlesitirilmis = isim + " " + soyad
# print(birlesitirilmis)

# assume isim = Esra Iclal Boğar
isim = input("İsminizi girin : ")

harfSayisi = 0

for index in isim:
    if index != ' ':
        harfSayisi = harfSayisi + 1

print("İsminizde :",harfSayisi)
        
    