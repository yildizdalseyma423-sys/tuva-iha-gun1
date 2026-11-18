def kelime_sayaci(metin):
  kelimeler = metin.lower().split()
  sayac = {}
  for kelime in kelimeler:
    # Eğer kelime sözlükte varsa 1 artır, yoksa 0'dan başlat
    sayac[kelime] = sayac.get(kelime, 0) + 1
  return sayac


# Test:
log_metni = "iha baglanti koptu baglanti hata"
print("Kelime Frekansi:", kelime_sayaci(log_metni))