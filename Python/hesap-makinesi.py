# @author  : Esra İclal Boğar (esraiclalbogar@gmail.com)
# @title   : Simple calculator in python 
# @date    : 12.12.2021 
# @version : 1.0

print("toplama için 1")
print("çıkartma için 2")
print("çarpma için 3")
print("bölme için 4")

islem = int(input("işlemi seçiniz :"))

sayi1 = int(input("birinci sayıyı giriniz"))

sayi2 = int(input("ikinci sayıyı giriniz"))

if islem == 1:
    print("sayıların toplamı :",sayi1 + sayi2)

elif islem == 2:
    print("sayıların farkı :", sayi1-sayi2)

elif islem == 3:
    print("sayıların çarpımı :",sayi1*sayi2)

elif islem == 4:
    if sayi2 == 0:
        print("işlem geçersiz")
    else : 
        print("sayıların bölümü :",sayi1/sayi2)

else:
    print("işlem geçersiz")
