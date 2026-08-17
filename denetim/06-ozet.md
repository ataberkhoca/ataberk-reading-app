# Kurul Özeti — Y2 Tema 1: School Life

Kapsam: `data/grade2/school-life.json`, 51 metin (scan 13 · skim 13 · int 13 · inf 12), 255 soru.
Denetim süreci: müfredat haritası (onaylı) → teknik/şema kontrolü → 51 metnin tam okunması → ileri
sızıntı taraması → kapsam analizi → pedagojik puanlama → canlı uygulama testi.

## Ciddiyet dağılımı

| Ciddiyet | Sayı | Kategoriler |
|---|---|---|
| **KRİTİK** | 8 | ipucu-kalitesi (6) · tutarlılık/UX (2) |
| **CİDDİ** | 9 | ileri-sızıntı (6) · kapsam-boşluğu (2) · pedagojik (1) |
| **KÜÇÜK** | 1 | dil-doğallığı (1) |
| **STİL** | 4 | ileri-sızıntı-belirsiz (1) · kapsam-dengesi (3) |
| **Toplam bulgu** | **22** | |

Teknik/şema katmanı (JSON geçerliliği, id, hl indeksleri, choices/soru uyumu, şık uzunluk dengesi):
**0 bulgu** — bu tema o eksende kusursuz. Sorunların tamamı içerik ve uygulama katmanında.

## En kritik 10 bulgu

1. **[KRİTİK]** `inf-1` S4 ipucu → "O öğrenci değil, müdür değil. O bir öğretmen." — cevabı ("a
   teacher") doğrudan söylüyor. Canlı uygulamada birebir doğrulandı.
2. **[KRİTİK]** `inf-1` S5 ipucu → "O Miss Oli, İngilizce öğretmeni." — Yes/No sorusunun cevabını
   doğrudan veriyor.
3. **[KRİTİK]** `inf-4` S3 ipucu → "Adı Tom." — cevabı birebir veriyor.
4. **[KRİTİK]** `inf-6` S4 ipucu → "Eda öğrenci, Miss Oli öğretmen. Mr. Aras müdür." — son adımı
   (cevabı) veriyor.
5. **[KRİTİK]** `inf-8` S4 ipucu → "Okul günü değil. Bugün Cumartesi." — cevabı ("Saturday") veriyor.
6. **[KRİTİK]** `inf-9` S3 ipucu → "Adı Tom." — cevabı birebir veriyor.
7. **[KRİTİK]** `int-9` "A New Teacher Visits" — hikâyenin öznesi ve tek konuşan öğretmen karakteri
   olan Miss Pinar (+ sahneyi açan Miss Oli) `cast` listesinde yok; ekranda avatarları görünmüyor
   (canlı ekran görüntüsüyle doğrulandı). Buna karşılık hiç konuşmayan Mr. Aras cast'te.
8. **[KRİTİK]** `int-11` "Miss Oli in Classroom" — konuşan ve bir sorunun doğru cevabı olan "Lila"
   `cast` listesinde yok.
9. **[CİDDİ]** Sıra sayı + tarih kalıbı ("the 23rd of April" vb.) — Y4-Tema2/3 yapısı, Y2-Tema1'de
   yasak — 5 ayrı metinde tekrarlanan sistematik şablon hatası (`scan-10, scan-13, skim-10, int-10,
   inf-10`).
10. **[CİDDİ]** Hedef kelime "headmistress" 51 metnin **hiçbirinde** geçmiyor; "kid" yalnızca **1**
    kez geçiyor (müfredatta ikisi de açık hedef kelime).

## Diğer bulgular (özet)

- **[CİDDİ]** `int-8` sentences[8]: "See you **on** Monday!" — edat "on" Tema 3 yapısı, Tema 1'de
  yasak.
- **[CİDDİ]** 7 milli/dini gün metni (scan-10/13, skim-10/13, int-10/13, inf-10) neredeyse birebir
  aynı 8 cümlelik şablonu tekrarlıyor — gerçek olay/merak/etkileşim yok, "fotoğraf" statüsünde.
- **[KÜÇÜK]** `skim-11` sentences[4]: "Where is **a** library?" — doğal İngilizce değil ("the"
  beklenir).
- **[STİL]** `int-4`: "What day is **after** Tuesday?" — müfredatta doğrulanamayan bir edat/zarf
  kullanımı; kasıtlı mı belirsiz, kullanıcı onayı gerekiyor.
- **[STİL]** "What's your name?" kalıbı yalnızca 5/51, emir kipi yalnızca 9/51 metinde — diğer
  yıldızlara göre ince kapsam.
- **[STİL]** Wednesday/Thursday diğer günlere göre yarı yarıya daha az tekrarlanıyor (10-11 vs
  15-31) — küçük, muhtemelen önemsiz bir dengesizlik.
- **[STİL]** 7 milli/dini günün her biri yalnızca tek bir beceri grubuna atanmış (derinlik değil
  genişlik stratejisi) — kasıtlı olabilir, müfredat bunu ne zorunlu ne yasak kılıyor.

## Neyin sorun OLMADIĞI (önemli, çünkü şişirilmiş bir rapor değil bu)

- JSON şeması, id bütünlüğü, hl indeksleri, choices/soru uyumu: **kusursuz** (checker.py, 0 bulgu).
- Şık uzunluk dengesi: **istatistiksel olarak sıfır önyargı** (255 soru tarandı).
- Yanlış şık makuliyeti: **hiçbir soruda** gülünç derecede elenebilir şık yok.
- Modal "can" (izin), "how many", "have got", "some/any", "there is/are", "will/be going to",
  karşılaştırma dereceleri, "was/were", şimdiki zaman: **tema genelinde sıfır örnek** — bu
  yapıların hiçbiri sızmamış.
- Haftanın 7 günü ve okul yerleri kelime seti: **kusursuz kapsanmış.**
- Uygulamanın temel akışı (profil → konu → beceri → metin → soru → sonuç → rozet): **konsol
  hatasız, ağ hatasız, sorunsuz çalışıyor.** Doğru/yanlış geri bildirimi ve rozet sistemi iyi
  tasarlanmış.

## Kurul kararı

**Bu tema bugün jüri önüne çıksa hangi bulgu yüzünden eleme yer?**

**İpucu sisteminin cevap sızdırması** (bulgu #1-6). Gerekçe: Bu, "MEB Maarif yaklaşımı: dilbilgisi
kural olarak verilmez, bağlamdan sezilir" ilkesinin doğrudan tersine düşüyor — çıkarım yapması
istenen bir öğrenciye, tam çıkarım yapması gereken anda cevabı kelimesi kelimesine veren bir ipucu
sunuluyor. Bu tek bir yazım hatası değil: **12 Çıkarım metninin 5'inde (yaklaşık %42'sinde)**
tekrarlanan, aynı yazarın diğer 7 metinde doğru yaptığı bir disiplini kaybettiği sistematik bir
kalite kontrolü boşluğu. Bir jüri üyesi rastgele 2-3 Çıkarım metni denese, bu sorunla yarı yarıya
ihtimalle karşılaşır — ve "ipucunun işi yönlendirmek, söylemek değil" ilkesinin ihlali, teknik bir
detay değil, temanın iddia ettiği pedagojik yaklaşımın (bağlamdan sezme) özüyle çelişiyor.

İkinci sırada **cast/avatar tutarsızlığı** (bulgu #7-8) gelir — bu daha çok bir yazılım-içerik
entegrasyon kusuru, ama bir sınıf içi kullanımda "bu kim, neden görünmüyor?" sorusuna yol açar ve
düzeltmesi kolay olduğu için gözden kaçmış olması dikkat çekici.

Sıra sayı/tarih sızıntısı (bulgu #9) ve "headmistress" boşluğu (bulgu #10) tek başına eleme sebebi
olacak kadar ağır değil, ama düzeltilmeden bırakılırsa müfredat uyumu iddiasını zayıflatır —
özellikle her ikisi de tek bir yerden (şablon / kelime çifti) düzeltilebilecek, ucuz maliyetli
sorunlar.

**Genel değerlendirme:** İçeriğin dil/gramer/müfredat iskeleti (yıldız kapsamı, kelime kapsamı, alt
tema dengesi, JSON bütünlüğü) sağlam ve büyük ölçüde temiz. Temanın zayıf noktası içerik üretimi
değil, **son kalite kontrolü** — özellikle Çıkarım grubundaki ipucu metinlerinin gözden geçirilmeden
yayınlanmış olması. Bu, kapsamlı bir yeniden yazım değil, **hedefli bir düzeltme turu** (5 ipucu
cümlesi + 2 cast dizisi + 5 tarih cümlesi + 1 edat + 2 kelime kullanımı ≈ 15 satırlık değişiklik)
gerektiriyor.
