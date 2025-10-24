# WhatsApp Toplu Mesaj Gönderici

Üniversite topluluğu WhatsApp grubu üyelerine otomatik mesaj gönderme aracı. PyWhatKit kullanarak WhatsApp Web üzerinden grup üyelerine toplu mesajlar gönderir.

## 🎯 Özellikler

- WhatsApp Web otomasyonu (pywhatkit)
- Grup üyelerine toplu mesaj gönderme
- Terminal tabanlı basit kullanım
- Mesaj gönderimi sırasında ilerleme takibi
- Her mesaj arası otomatik bekleme
- Normal WhatsApp hesabınızla çalışır (İşletme hesabı gerekmez!)

## 📋 Gereksinimler

- Python 3.7 veya üzeri
- WhatsApp hesabı (normal hesap yeterli)
- WhatsApp Web'de aktif oturum
- macOS/Linux/Windows

## 🚀 Kurulum

### 1. Projeyi açın

```bash
cd "Bumost wp automation"
```

### 2. Gerekli paketleri yükleyin (Zaten kurulu!)

```bash
pip install -r requirements.txt
```

Yüklenen paketler:
- `pywhatkit` - WhatsApp Web otomasyonu
- `pyautogui` - Klavye/mouse kontrolü
- `Pillow` - Görüntü işleme
- `selenium` - Tarayıcı otomasyonu (grup üye çıkarma için)
- `webdriver-manager` - Chrome driver yönetimi

### 3. `group_members.json` dosyası oluşturun

**Seçenek A: Otomatik Çıkar - WhatsApp Web'den (ÖNERİLEN) 🚀**

Selenium ile WhatsApp Web'den otomatik üye çıkarma:

```bash
python3 group_extractor.py
# Seçenek 1'i seçin: "Otomatik çıkar (WhatsApp Web'den)"
```

Script şunları yapacak:
1. Chrome tarayıcısını açar
2. WhatsApp Web'e gider
3. QR kod okutmanızı bekler (ilk seferde)
4. **Siz grubu açarsınız**
5. Grup bilgilerine gidip tüm üyeleri otomatik çıkarır
6. `group_members.json` dosyasını oluşturur

**Avantajları:**
- ✅ Yüzlerce üyeyi otomatik çıkarır
- ✅ İsim bilgilerini otomatik alır
- ✅ Mümkünse telefon numaralarını da alır
- ✅ 5 dakikada 200+ üye

**⚠️ Not:** Bazı üyelerin telefon numaraları gizli olabilir. Bu durumda sadece isimler alınır ve bu üyelere mesaj gönderemezsiniz.

**Seçenek B: Manuel Gir**

```bash
python3 group_extractor.py
# Seçenek 2'yi seçin: "Manuel gir"
```

Her üye için elle isim ve telefon girersiniz (küçük gruplar için).

**Telefon Numarası Formatı:**
- Türkiye için: `90` + telefon numarası (başında + olmadan)
- Örnek: `905551234567` ✅
- Yanlış: `+905551234567` ❌
- Yanlış: `05551234567` ❌

## ⚙️ WhatsApp Web Hazırlığı

### Program çalışmadan önce:

1. **WhatsApp Web'de oturum açın:**
   - [web.whatsapp.com](https://web.whatsapp.com) adresine gidin
   - Telefonunuzla QR kodu okutun
   - "Oturumu açık tut" seçeneğini işaretleyin

2. **Tarayıcı ayarları:**
   - Varsayılan tarayıcınızın Chrome, Firefox veya Safari olduğundan emin olun
   - Program her mesaj için otomatik olarak yeni sekme açacak

## 💡 Kullanım

### Hızlı Başlangıç (3 Adım)

```bash
# 1. Grup üyelerini WhatsApp Web'den otomatik çıkar
python3 group_extractor.py

# 2. WhatsApp Web'de oturum açın (script açacak)
# QR kod okutun, grubu açın, Enter'a basın

# 3. Mesaj gönder
python3 main.py
```

### Detaylı Kullanım

#### Adım 1: Grup Üyelerini Otomatik Çıkar

```bash
python3 group_extractor.py
```

**İnteraksiyon:**

1. **Seçim yapın:** "1" - Otomatik çıkar
2. **Chrome açılacak** - WhatsApp Web'e gidecek
3. **QR kod okutun** (ilk seferde)
4. **Grubu açın** - İstediğiniz WhatsApp grubuna girin
5. **Terminale dönün** - Enter'a basın
6. **Bekleyin** - Script otomatik olarak:
   - Grup başlığına tıklar
   - Tüm üyeleri yüklemek için kaydırma yapar
   - Her üyenin ismini ve telefon numarasını çıkarır
   - `group_members.json` dosyasını oluşturur

**Örnek Çıktı:**
```
============================================================
   WhatsApp Grup Üyeleri Otomatik Çıkarıcı
============================================================

🌐 Tarayıcı başlatılıyor...

────────────────────────────────────────────────────────────
⚠️  ÖNEMLİ:
   1. QR kodu telefonunuzla okutun (ilk seferde)
   2. WhatsApp Web açıldıktan sonra istediğiniz GRUBU açın
   3. Grup sohbetini açtıktan sonra terminale dönün
────────────────────────────────────────────────────────────

Grubu açtıktan sonra Enter'a basın...

🔍 Grup bilgileri alınıyor...
✅ Grup başlığına tıklandı
📊 Grup: BÜMOST Topluluğu

📜 Üyeler yükleniyor (kaydırma yapılıyor)...
   📍 Kaydırma 5/50...
   📍 Kaydırma 10/50...
✅ Tüm üyeler yüklendi (scroll sayısı: 12)

👥 Üye bilgileri çıkarılıyor...
🔍 156 üye elementi bulundu, işleniyor...

1. ✅ Ahmet Yılmaz (905551234567)
2. ✅ Ayşe Demir (telefon numarası gizli)
3. ✅ Mehmet Kaya (905559876543)
...
156. ✅ Zeynep Aksoy (905557778899)

────────────────────────────────────────────────────────────
✅ group_members.json dosyası başarıyla oluşturuldu!
────────────────────────────────────────────────────────────
📊 Grup: BÜMOST Topluluğu
👥 Toplam üye: 156
   📱 Telefon numaralı: 89
   🔒 Telefon numarası gizli: 67

⚠️  NOT: Bazı üyelerin telefon numaraları gizli.
   Bu üyelere mesaj gönderilemeyecek.

🚀 Artık 'python main.py' komutuyla mesaj gönderebilirsiniz!
```

#### Adım 2: Mesaj Gönder

### Program Çalıştırma

```bash
python main.py
```

veya

```bash
python3 main.py
```

### Adım Adım Kullanım

1. **Programı çalıştırın:**
   ```bash
   python main.py
   ```

2. **Uyarıları okuyun:**
   - WhatsApp Web'de oturum açık olmalı
   - Bilgisayarınızın başında olmalısınız
   - Mouse ve klavyeye dokunmayın

3. **Mesajınızı yazın:**
   - Göndermek istediğiniz mesajı terminal'e yazın
   - Çok satırlı mesajlar yazabilirsiniz
   - Mesajı bitirmek için iki kez Enter'a basın

4. **Mesajı onaylayın:**
   - Program mesajı gösterecek
   - `evet` veya `e` yazarak onaylayın

5. **Otomatik gönderimi izleyin:**
   - Program her kişi için otomatik olarak:
     - Tarayıcıda yeni sekme açar
     - WhatsApp Web'e gider
     - Mesajı yazar ve gönderir
     - Sekmeyi kapatır
     - 30 saniye bekler (bir sonraki mesaj için)

### Örnek Kullanım

```
============================================================
   WhatsApp Toplu Mesaj Gönderici (pywhatkit)
============================================================

⚠️  ÖNEMLİ UYARILAR:
   • WhatsApp Web'de oturum açmış olmalısınız
   • İşlem sırasında bilgisayarınızın başında olmalısınız
   • Mouse ve klavyeye dokunmayın (otomatik kontrol edilecek)
   • Her mesaj için tarayıcı yeni sekme açacak
────────────────────────────────────────────────────────────

Hazır olduğunuzda Enter'a basın...

Göndermek istediğiniz mesajı yazın (Enter'a iki kez basarak bitirin):
────────────────────────────────────────────────────────────
Merhaba! 

Bu hafta sonu yapacağımız etkinliğe davetlisiniz.
📅 Tarih: 26 Ekim 2025, Cumartesi
🕐 Saat: 14:00
📍 Yer: Kampüs Konferans Salonu

Katılım için lütfen geri dönüş yapın.


────────────────────────────────────────────────────────────
📝 Gönderilecek mesaj:
────────────────────────────────────────────────────────────
Merhaba! 

Bu hafta sonu yapacağımız etkinliğe davetlisiniz.
📅 Tarih: 26 Ekim 2025, Cumartesi
🕐 Saat: 14:00
📍 Yer: Kampüs Konferans Salonu

Katılım için lütfen geri dönüş yapın.
────────────────────────────────────────────────────────────

📊 Toplam 3 kişiye gönderilecek.

⚠️  Bu mesajı tüm grup üyelerine göndermek istiyor musunuz? (evet/hayır): evet

🚀 Mesaj gönderimi başlıyor...
⚠️  Lütfen bilgisayarınızın başında kalın ve işleme müdahale etmeyin!


📱 3 kişiye mesaj gönderiliyor...

⏰ Mesajlar arası bekleme süresi: 30 saniye
────────────────────────────────────────────────────────────

1/3 📤 Ahmet Yılmaz (+905551234567)...
   ⏳ WhatsApp Web açılıyor, lütfen bekleyin...
   ✅ Mesaj gönderildi!
   ⏰ Sonraki mesaja kadar 30 saniye bekleniyor...

2/3 📤 Ayşe Demir (+905559876543)...
   ⏳ WhatsApp Web açılıyor, lütfen bekleyin...
   ✅ Mesaj gönderildi!
   ⏰ Sonraki mesaja kadar 30 saniye bekleniyor...

3/3 📤 Mehmet Kaya (+905551112233)...
   ⏳ WhatsApp Web açılıyor, lütfen bekleyin...
   ✅ Mesaj gönderildi!

────────────────────────────────────────────────────────────

📊 Özet:
   ✅ Başarılı: 3
   ❌ Başarısız: 0
   📊 Toplam: 3
```

## ⚙️ Yapılandırma

### Mesajlar Arası Bekleme Süresini Değiştirmek

`main.py` dosyasının 16. satırında değiştirebilirsiniz:

```python
self.delay_between_messages = 30  # Saniye cinsinden (varsayılan: 30)
```

**Önerilen:** Minimum 20 saniye (WhatsApp'ın spam algılamasını önlemek için)

## ⚠️ Önemli Notlar

### PyWhatKit Nasıl Çalışır?

PyWhatKit, WhatsApp Web'i otomatik olarak açar ve klavye/mouse hareketlerini simüle eder:

1. Tarayıcıda yeni sekme açar
2. `web.whatsapp.com/send?phone=NUMARA` adresine gider
3. Mesaj kutusunu bulur
4. Mesajı yazar (klavye simülasyonu)
5. Enter'a basar (mesaj gönderir)
6. Sekmeyi kapatır

### Dikkat Edilmesi Gerekenler

- ⚠️ **İşlem sırasında bilgisayarı kullanmayın** - Otomatik klavye/mouse kontrolü yapılıyor
- ⚠️ **WhatsApp Web oturumu açık olmalı** - Her seferinde QR kod okutmayın
- ⚠️ **Spam olarak algılanabilir** - Çok fazla kişiye çok hızlı mesaj atmayın
- ⚠️ **Test edin** - İlk önce birkaç kişiye test mesajı gönderin
- ⚠️ **İnternet bağlantısı** - Stabil internet gerekli

### Avantajlar vs Dezavantajlar

**✅ Avantajlar:**
- İşletme hesabı gerekmez
- Normal WhatsApp hesabınızla çalışır
- API key/token gerekmez
- Ücretsiz
- Kolay kurulum

**❌ Dezavantajlar:**
- Yavaş (her mesaj ~30 saniye)
- Bilgisayar başında olmanız gerekir
- Tarayıcı sekmelerini otomatik açar/kapatır
- İşlem sırasında bilgisayarı kullanamazsınız

## 🆘 Sorun Giderme

### "group_members.json bulunamadı" Hatası
```bash
# Otomatik oluştur (önerilen)
python group_extractor.py

# veya manuel oluştur
cp group_members.example.json group_members.json
```
Sonra dosyayı düzenleyin.

### Mevcut Dosyaya Üye Eklemek
```bash
python group_extractor.py
# Seçenek 2'yi seçin: "Mevcut dosyaya üye ekle"
```

### "pywhatkit modülü bulunamadı" Hatası
```bash
pip install pywhatkit pyautogui Pillow
```

### WhatsApp Web Açılmıyor
- Varsayılan tarayıcınızı kontrol edin
- WhatsApp Web'de manuel olarak oturum açın
- Tarayıcı güncellemelerini kontrol edin

### Mesajlar Gönderilmiyor
- WhatsApp Web'de oturum açık mı kontrol edin
- İnternet bağlantınızı kontrol edin
- Telefon numaralarının doğru formatta olduğundan emin olun
- Bekleme süresini artırın (30+ saniye)

### "Permission Denied" veya Erişim Hataları (macOS)
macOS'ta PyAutoGUI için erişim izinleri gerekebilir:
1. **Sistem Ayarları** → **Güvenlik ve Gizlilik** → **Erişilebilirlik**
2. Terminal veya Python'a erişim izni verin

### Klavye/Mouse Kontrolü Çalışmıyor
- PyAutoGUI'nin doğru yüklendiğinden emin olun
- İşlem sırasında klavye/mouse'a dokunmayın
- Ekran koruyucu veya uyku modunu devre dışı bırakın

## 🔒 Güvenlik ve Gizlilik

- `group_members.json` dosyası `.gitignore`'da - kişisel veriler korunur
- Telefon numaralarını başkalarıyla paylaşmayın
- WhatsApp kullanım koşullarına uyun
- Spam göndermeyin, kullanıcıların iznini alın

## 📚 Kaynaklar

- [PyWhatKit Documentation](https://github.com/Ankit404butfound/PyWhatKit)
- [WhatsApp Web](https://web.whatsapp.com)
- [PyAutoGUI Documentation](https://pyautogui.readthedocs.io/)

## 📄 Lisans

Bu proje eğitim ve topluluk etkinlikleri için geliştirilmiştir.

## 🤝 Katkıda Bulunma

Bu proje Bumost üniversite topluluğu için geliştirilmiştir. İyileştirme önerileri için lütfen iletişime geçin.

---

**Not:** WhatsApp kullanım koşullarına uyun. Spam göndermekten kaçının ve kullanıcıların onayını alın.
