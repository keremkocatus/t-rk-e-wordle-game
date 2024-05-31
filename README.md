# Türkçe Wordle Oyunu

Bu proje, Türkçe dilinde Wordle benzeri bir kelime tahmin oyunudur. Oyuncu, belirli bir kelime uzunluğundaki gizli kelimeyi tahmin etmeye çalışır. 
Doğru harf ve doğru pozisyon yeşil, doğru harf ama yanlış pozisyon sarı, yanlış harf ise gri renkte gösterilir.

## Özellikler

- 5 harfli, 6 harfli ve 7 harfli kelimelerle oynama seçeneği
- Türkçe karakterleri doğru işleme
- Terminal üzerinden oyun oynama

## Gereksinimler

Bu projeyi çalıştırmak için Python 3 yüklü olmalıdır.

## Kurulum

1. Bu projeyi klonlayın veya indirin.
    ```bash
    git clone https://github.com/kullanici-adi/turkce-wordle.git
    cd turkce-wordle
    ```

2. Gerekli kelime dosyalarını oluşturun ve aynı dizine yerleştirin:
    - `kelimeler_5.txt`
    - `kelimeler_6.txt`
    - `kelimeler_7.txt`

   Bu dosyaların her birinde ilgili kelimeler satır satır bulunmalıdır.

## Kullanım

Terminal veya komut istemcisinde aşağıdaki komutu çalıştırarak oyunu başlatın:
```bash
python oyun.py
