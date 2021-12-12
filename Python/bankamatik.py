# take input from user 

sayi = int(input("Alacağınız Parayı Seçin"))


#250
ikiYuzluk = int(sayi / 200)

sayi = int(sayi % 200)

yuzluk = sayi /100

sayi = sayi % 100

ellilik = sayi / 50

sayi = sayi % 50

yirmilik = sayi / 20

sayi = sayi % 20

onluk = sayi / 10

sayi = sayi % 10

beslik = sayi / 5

sayi = sayi % 5

print(ikiYuzluk,yuzluk,ellilik,yirmilik,onluk,beslik)