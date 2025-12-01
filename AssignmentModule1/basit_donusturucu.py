"""
    **Basit Dönüştürücü**: Metre-Feet, Kilogram-Pound dönüştürücüsü yapın
"""

print("1: Metre to Feet")
print("2: Feet to Metre")
print("3: Kilogram to Pound")
print("4: Pound to Kilogram")

secim = input("Dönüştürme türünü seçin (1-4): ")

if secim == '1':
    metre = float(input("Metre cinsinden değeri girin: "))
    feet = metre * 3.28084
    print(f"{metre} metre = {feet} feet")
elif secim == '2':
    feet = float(input("Feet cinsinden değeri girin: "))
    metre = feet / 3.28084
    print(f"{feet} feet = {metre} metre")
elif secim == '3':
    kilogram = float(input("Kilogram cinsinden değeri girin: "))
    pound = kilogram * 2.20462
    print(f"{kilogram} kilogram = {pound} pound")
elif secim == '4':
    pound = float(input("Pound cinsinden değeri girin: "))
    kilogram = pound / 2.20462
    print(f"{pound} pound = {kilogram} kilogram")
else:
    print("Geçersiz seçim. Lütfen 1-4 arasında bir değer girin.")