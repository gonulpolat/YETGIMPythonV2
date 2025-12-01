"""
    **Restoran Hesabı**: Yemek fiyatı, bahşiş oranı ve kişi sayısını alıp kişi başı tutarı hesaplayan program
"""

while True:
    try:
        food_price = float(input("Yemek fiyatını girin: "))
        if food_price <= 0:
            print("Yemek fiyatı negatif veya beleş olamaz. Tekrar deneyin.")
            continue
        tip_percentage = float(input("Bahşiş oranını girin (%): "))
        if tip_percentage < 0:
            print("Bahşiş oranı negatif olamaz. Tekrar deneyin.")
            continue
        number_of_people = int(input("Kişi sayısını girin: "))
        if number_of_people <= 0:
            print("Kişi sayısı sıfır veya negatif olamaz. Tekrar deneyin.")
            continue
        break
    except ValueError:
        print("Lütfen tekrar deneyiniz.")

tip_amount = food_price * (tip_percentage / 100)
total_amount = food_price + tip_amount
amount_per_person = total_amount / number_of_people
print(f"Kişi başı ödenecek tutar: {amount_per_person} TL")
