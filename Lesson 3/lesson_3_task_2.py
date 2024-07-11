from smartphone import Smartphone

phone1 = Smartphone("Iphone", "5s", "+79210000000")
phone2 = Smartphone("Iphone", "15","+79115567788" )
phone3 = Smartphone("Sumsung", "Galaxy", "+79140987654" )
phone4 = Smartphone("Xiaomi", "13 lite","+79991234567")
phone5 = Smartphone("OPPO", "Reno 5", "+79960988990")

catalog = [phone1, phone2, phone3, phone4, phone5]
len = len(catalog)

for i in range (0, len):
    print(catalog[i])