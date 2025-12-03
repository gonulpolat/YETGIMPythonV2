"""
    **Multiplication Quiz**: Rastgele çarpma soruları soran quiz programı
"""

import random

def multiplication_quiz():
    ilk_mi = False
    while True:
        if ilk_mi:
            devam_mi = input("Çıkmak için q, devam etmek için herhangi bir tuşa basın: ")
            if devam_mi == 'q' or devam_mi == 'Q':  
                break
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        answer = a * b
        try:
            girdi = int(input(f"{a} x {b} = "))
            if girdi == answer:
                print("✅")
            else:
                print("❌")
        except ValueError:
            print(f"Lütfen bir sayı girin.")
        ilk_mi = True


if __name__ == "__main__":
    multiplication_quiz()
    