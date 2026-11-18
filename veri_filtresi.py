def veri_filtresi(veri_listesi, esik_deger):
  # Liste üreteci (List Comprehension) kullanarak eşikten büyükleri seçiyoruz
  filtrelenmis = [veri for veri in veri_listesi if veri > esik_deger]
  return filtrelenmis


# Test (Örn: 50 birimden yüksek sıcaklık uyarıları):
sicakliklar = [35, 42, 55, 48, 62, 30]
print("Kritik Sıcaklıklar:", veri_filtresi(sicakliklar, 50))