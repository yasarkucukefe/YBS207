def fiyat_hash_uret(urun:str)->int:
    sum = 0
    for harf in urun:
        sum += ord(harf)
    return sum

print(fiyat_hash_uret('americano'))