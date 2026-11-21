import math


def koordinat_mesafesi(baslangic, bitis):
  # baslangic ve bitis (x, y) şeklinde iki elemanlı demetler (tuple) veya listelerdir.
  mesafesi = math.sqrt((bitis[0] - baslangic[0]) ** 2 + (bitis[1] - baslangic[1]) ** 2)
  return mesafesi


# Test:
nokta_a = (0, 0)
nokta_b = (3, 4)
print("Mesafe:", koordinat_mesafesi(nokta_a, nokta_b))  # Çıktı: 5.0
nokta_c = (1, 2)
nokta_d = (4, 6)

print("İkinci mesafe:", koordinat_mesafesi(nokta_c, nokta_d))
def haversine_mesafesi(baslangic, bitis):
    # Dünya'nın ortalama yarıçapı (km)
    R = 6371.0

    # Enlem ve boylam değerleri
    lat1, lon1 = baslangic
    lat2, lon2 = bitis

    # Dereceleri radyana çevir
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # Koordinat farkları
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Haversine hesabı
    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(lat1) * math.cos(lat2)
        * math.sin(dlon / 2) ** 2
    )

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c


# GPS TESTİ
gps_a = (41.0, 28.0)
gps_b = (41.1, 28.1)

print("GPS Mesafesi:", haversine_mesafesi(gps_a, gps_b), "km")
