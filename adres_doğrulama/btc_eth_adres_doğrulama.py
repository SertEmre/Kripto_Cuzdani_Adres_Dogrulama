def btc_kontrol(adres):
    if len(adres)<26 or len(adres)>35:
        return False
    
    if adres[0]=="1" or adres[0]=="3":
        return True
    elif adres[:3]=="bc1" and len(adres)>42:
        return True
    
    return False

def eth_kontrol(adres):
    if len(adres) == 42 and adres[:2]=="0x":
        hex_karakterler = set("0123456789abcdefABCDEF")
        return all(karakter in hex_karakterler for karakter in adres[2:])
    return False
while True:
    kripto = input("Hangi kripto paranın kontrolünü yapmak istersiniz?(BTC veya ETH): ").strip().upper()
    if kripto== "BTC" or kripto=="ETH":
        break
    else:
        print("Sadece BTC veya ETH kontrolü yapılabilir")   
adres = input("Cüzdan adresini giriniz: ").strip()

if kripto == "BTC":
    if btc_kontrol(adres):
        print("Geçerli bir Bitcoin adresi ✅")
    else:
        print("Geçersiz bir Bitcoin adresi ❌")
elif kripto == "ETH":
    if eth_kontrol(adres):
        print("Geçerli bir ETH adresi ✅")
    else:
        print("Geçersiz bir ETH adresi ❌")

