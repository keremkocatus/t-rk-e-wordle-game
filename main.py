import random
import os

turkce_kucuk_harfler = str.maketrans("IİĞÜŞÇÖ", "ıiğüşçö")

def kelime_listesini_yukle(dosya_adi):
    with open(dosya_adi, 'r', encoding='utf-8') as dosya:
        kelimeler = [kelime.strip().translate(turkce_kucuk_harfler).casefold() for kelime in dosya.readlines()]
    return kelimeler

kelime_listesi_5 = kelime_listesini_yukle('kelimeler_5.txt')
#kelime_listesi_6 = kelime_listesini_yukle('kelimeler_6.txt')
#kelime_listesi_7 = kelime_listesini_yukle('kelimeler_7.txt')

kelime_uzunlugu = 5
kelime_listesi = kelime_listesi_5

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def ayarlar():
    global kelime_uzunlugu, kelime_listesi
    while True:
        clear_terminal()
        print("Ayarlar:")
        print("1. 5 harfli kelimeler")
        print("2. 6 harfli kelimeler")
        print("3. 7 harfli kelimeler")
        print("4. Ana menüye dön")
        secim = input("Bir seçenek seçin: ")

        if secim == "1":
            kelime_uzunlugu = 5
            kelime_listesi = kelime_listesi_5
            break
        elif secim == "2":
            kelime_uzunlugu = 6
            #kelime_listesi = kelime_listesi_6
            break
        elif secim == "3":
            kelime_uzunlugu = 7
            #kelime_listesi = kelime_listesi_7
            break
        elif secim == "4":
            break

def oyun():
    global kelime_uzunlugu, kelime_listesi
    gizli_kelime = random.choice(kelime_listesi)
    tahmin_hakki = 6
    tahminler = []

    clear_terminal()
    print("Wordle oyununa hoş geldiniz!")
    print(f"{kelime_uzunlugu} harfli bir kelimeyi tahmin etmeye çalışın.")
    print("Doğru harf ve doğru pozisyon => Yeşil")
    print("Doğru harf ama yanlış pozisyon => Sarı")
    print("Yanlış harf => Gri")
    print("\n\n")

    while tahmin_hakki > 0:
        tahmin = input("Tahmininiz: ").translate(turkce_kucuk_harfler).casefold()

        if len(tahmin) != kelime_uzunlugu:
            print(f"Lütfen {kelime_uzunlugu} harfli bir kelime girin.")
            continue

        if tahmin not in kelime_listesi:
            print("Bu kelime geçerli değil. Lütfen geçerli bir kelime girin.")
            continue

        if tahmin == gizli_kelime:
            gizli_kelime_renkli = " ".join(["\033[1;32m" + harf + "\033[0m" for harf in gizli_kelime])
            tahminler.append(gizli_kelime_renkli)
            clear_terminal()
            print(f"Kalan tahmin hakkınız: {tahmin_hakki}")
            for t in tahminler:
                print(t)
            print("Tebrikler! Doğru tahmin ettiniz:", gizli_kelime)
            break

        sonuc = [""] * kelime_uzunlugu
        gizli_kelime_kopya = list(gizli_kelime)

        for i in range(kelime_uzunlugu):
            if tahmin[i] == gizli_kelime[i]:
                sonuc[i] = "\033[1;32m" + tahmin[i] + "\033[0m"  # Yeşil
                gizli_kelime_kopya[i] = None

        for i in range(kelime_uzunlugu):
            if sonuc[i] == "":
                if tahmin[i] in gizli_kelime_kopya:
                    sonuc[i] = "\033[1;33m" + tahmin[i] + "\033[0m"  # Sarı
                    gizli_kelime_kopya[gizli_kelime_kopya.index(tahmin[i])] = None
                else:
                    sonuc[i] = "\033[1;37m" + tahmin[i] + "\033[0m"  # Gri

        tahminler.append(" ".join(sonuc))
        tahmin_hakki -= 1

        clear_terminal()
        print(f"Kalan tahmin hakkınız: {tahmin_hakki}")
        for t in tahminler:
            print(t)

    if tahmin_hakki == 0:
        gizli_kelime_renkli = " ".join(["\033[1;32m" + harf + "\033[0m" for harf in gizli_kelime])
        print(gizli_kelime_renkli)
        print("Maalesef, tahmin hakkınız bitti. Gizli kelime:", gizli_kelime)

def ana_menu():
    while True:
        clear_terminal()
        print("Ana Menü:")
        print("1. Oyna")
        print("2. Ayarlar")
        print("3. Çıkış")
        secim = input("Bir seçenek seçin: ")

        if secim == "1":
            oyun()
            input("Oyun bitti. Ana menüye dönmek için ENTER tuşuna basın...")
        elif secim == "2":
            ayarlar()
        elif secim == "3":
            break
        else:
            print("Geçersiz seçenek, lütfen tekrar deneyin.")

ana_menu()
