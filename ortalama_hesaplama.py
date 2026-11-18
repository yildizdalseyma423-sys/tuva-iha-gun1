def liste_ortalamasi(sayilar):
  if len(sayilar) == 0:
    return 0
  return sum(sayilar) / len(sayilar)


# Test:
irtifalar = [100, 120, 115, 130, 125]
print("Ortalama İrtifa:", liste_ortalamasi(irtifalar))