"""
    **Kişisel Bütçe**: Gelir ve giderleri alıp kalan parayı hesaplayan program
"""

while True:
    try:
        gelir = float(input("Aylık gelirinizi girin: "))
        gider = float(input("Aylık giderlerinizi girin: "))
        if gider < 0:
            print("Aylık gideriniz negatif olamaz. Lütfen tekrar deneyin.")
            continue
        break
    except ValueError:
        print("Lütfen aylık gelir ve gider değerlerinizi sayısal giriniz. Eğer yoksa 0 giriniz.")

para = gelir - gider

if para > 0:
    print(f"Enteresan! Bu ay {para} TL tasarruf ediyorsunuz.")
elif para < 0:
    print(f"Üzülmeyin, kimin borcu yok ki? Bu ay sadece {abs(para)} TL borcunuz bulunmakta")
else:
    print("Tebrikler! Ayağınızı yorganınıza göre uzatıyorsunuz.")