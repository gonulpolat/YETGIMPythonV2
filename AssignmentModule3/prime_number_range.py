"""
    **Prime Number Range**: İki sayı arasındaki tüm asal sayıları bulan program
"""

def is_prime(num):
    """
    Aslında döngüyü sayıya kadar kontrol etmeye gerek yok.
    Sayının karaköküne kadar kontrol etmek yeterli.
    Ben yarın öbür gün bunu kesin unuturum.
    """
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def prime_numbers_between_two_numbers(start_num, end_num):
    prime_numbers = ()
    for num in range(start_num, end_num + 1):
        if is_prime(num):
            prime_numbers += (num,)
    return prime_numbers

if __name__ == "__main__":
    print("İki sayı arasındaki asal sayıları bulalım.")
    try:
        start = int(input("İlk sayı: "))
        end = int(input("İkinci sayı: "))
        if start > end:
            prime_numbers = prime_numbers_between_two_numbers(end, start)
            print(f"{end} ile {start} arasındaki asal sayılar: {prime_numbers}")
        else:
            prime_numbers = prime_numbers_between_two_numbers(start, end)
            print(f"{start} ile {end} arasındaki asal sayılar: {prime_numbers}")
    except ValueError:
        print("Lütfen tam sayı girin.")
