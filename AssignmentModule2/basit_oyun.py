"""
    **Basit Oyun**: Kullanıcı ile bilgisayarın taş-kağıt-makas oynadığı program
"""

import random
choices = ['taş', 'kağıt', 'makas']
user_choice = input("Taş, Kağıt, Makas seçin: ").lower()
if user_choice not in choices:
    print("Lütfen sadece Taş, Kağıt, Makas seçimi yapınız!")
else:
    computer_choice = random.choice(choices)
    # print(computer_choice)

    if user_choice == computer_choice:
        print("Ben de aynısını seçtim!")
    elif (user_choice == 'taş' and computer_choice == 'makas') or (user_choice == 'kağıt' and computer_choice == 'taş') or (user_choice == 'makas' and computer_choice == 'kağıt'):
        print("Tebrikler! Kazandınız!")
    else:
        print("Kaybettiniz! Tekrar deneyin.")
