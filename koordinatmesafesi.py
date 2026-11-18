import math


def koordinat_mesafesi(baslangic, bitis):
  # baslangic ve bitis (x, y) şeklinde iki elemanlı demetler (tuple) veya listelerdir.
  mesafesi = math.sqrt((bitis[0] - baslangic[0]) ** 2 + (bitis[1] - baslangic[1]) ** 2)
  return mesafesi


# Test:
nokta_a = (0, 0)
nokta_b = (3, 4)
print("Mesafe:", koordinat_mesafesi(nokta_a, nokta_b))  # Çıktı: 5.0