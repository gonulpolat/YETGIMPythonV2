"""
    **İndirim Hesaplayıcı**: Ürün fiyatı ve indirim oranını alıp yeni fiyatı hesaplayan program
"""

product_price = float(input("Ürün fiyatını girin: "))
discount_percentage = float(input("İndirim oranını girin (%): "))
discount_amount = product_price * (discount_percentage / 100)
price = product_price - discount_amount

print(f"İndirimli fiyat: {price} TL")
