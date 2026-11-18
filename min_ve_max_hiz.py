def min_max_bul(sayilar):
  if not sayilar:
    return None
  sonuc = {"en_buyuk": max(sayilar), "en_kucuk": min(sayilar)}
  return sonuc


# Test:
hizlar = [15.5, 22.1, 8.4, 45.2, 12.0]
print("Hız Analizi:", min_max_bul(hizlar))