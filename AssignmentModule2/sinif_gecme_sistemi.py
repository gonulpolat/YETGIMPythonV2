"""
    **Sınıf Geçme Sistemi**: Kullanıcıdan notları alıp sınıf geçip geçmediğini, harf notunu gösteren program
"""

midterm1 = int(input("İlk vize notunuzu girin: "))
midterm2 = int(input("İkinci vize notunuzu girin: "))
final = int(input("Final notunuzu girin: "))

avg = (midterm1 + midterm2) * 0.3 + final * 0.4

if avg >= 90:
    grade = 'AA'
elif avg >= 85:
    grade = 'BA'
elif avg >= 80:
    grade = 'BB'
elif avg >= 75:
    grade = 'CB'
elif avg >= 70:
    grade = 'CC'
elif avg >= 60:
    grade = 'DC'
elif avg >= 50:
    grade = 'DD'
else:
    grade = 'FF'

if grade != 'FF':
    print(f"Olaysın! Dersi geçtin. Harf notun: {grade}")
else:
    print(f"Yaz okulundan bekleniyorsunuz 😊")
    