# İpucu Tam Tarama — 3. ve 4. Sınıf'ın Kalan 12 Teması

**✅ Bu raporda ve 07-tum-uygulama-oynanis-raporu.md'de belgelenen 37 ipucu-sızıntısı bulgusunun
tamamı düzeltildi** (bkz. `12-genel-ozet.md` "Uygulanan Düzeltmeler"). Aşağıdaki metinler artık
tarihsel kayıt niteliğindedir — mevcut ipucu metinleri değişti, ama bulguların hangi soruda,
hangi gerekçeyle bulunduğunu belgelemeye devam ediyor.

[07-tum-uygulama-oynanis-raporu.md](07-tum-uygulama-oynanis-raporu.md)'de örneklem düzeyinde
bırakılan iş burada tamamlandı: 3. ve 4. Sınıf'ın 12 temasındaki **`inf` (Çıkarım) grubunun
tamamı — 570 ipucu — tek tek okundu** (uygulamayı gerçekten oynatarak, her ipucunu tıklayıp
gerçek metnini görerek). 2. Sınıf'ın 6 teması zaten önceki turda tam okunmuştu
([07-tum-uygulama-oynanis-raporu.md](07-tum-uygulama-oynanis-raporu.md) §3). Bu raporla birlikte
**18 temanın 18'inde de `inf` grubu ipuçlarının tamamı okunmuş oldu** — artık örneklem değil.

## Yöntem notu — kriter

Y2-Tema1 denetiminde kurulan kritere sadık kalındı: bir ipucu, sorunun cevabını **doğrudan
söylüyorsa** ya da cevabın içeriğini **neredeyse birebir başka kelimelerle tekrarlıyorsa**
sorun; cevabı **isimlendirmeden** ipucu veren (eleme — "X değil, Y değil" — ya da tanımlayıcı
özellik — "yeşil, uzun, çıtır" gibi) ipuçları sorun değil. Bu ayrımı her ipucu için tek tek
uyguladım.

## Sonuç: 3-4. Sınıf çok daha temiz, ama tamamen temiz değil

| Tema | Bulgu sayısı | Not |
|---|---|---|
| Y3-T1 School Life | 4 | 2 gerçek + 2 orta düzey |
| Y3-T2 Classroom Life | 0 | "X'imizi bul" (bul-yönlendirme) tutarlı house style |
| Y3-T3 Personal Life | 0 | Aynı house style |
| Y3-T4 Family Life | 2 | İkisi de orta düzey (akrabalık tanımı) |
| Y3-T5 Homes & Houses | 0 | Temiz |
| Y3-T6 Life in the City | 2 | İkisi de orta düzey |
| Y4-T1 School Life | 1 | 1 gerçek |
| Y4-T2 Classroom Life | 0 | "değil/değil" eleme house style — çok disiplinli |
| Y4-T3 Personal Life | 0 | Karşılaştırmalı/betimleyici ipuçları iyi tasarlanmış |
| Y4-T4 Family Life | 0 | Dedektif-hikâye tarzı, hiç sızıntı yok — en iyi tasarlanmış tema |
| Y4-T5 Homes & Houses | 0 | "bak/ele/düşün" yönlendirme tarzı, temiz |
| Y4-T6 Life in the City | 5 | 3 gerçek + 2 orta düzey |
| **Toplam (12 tema)** | **14** | |

**2. Sınıf'la karşılaştırma:** 2. Sınıf'ın 6 temasında (önceki turda tam okundu) 23 bulgu vardı,
ağırlıklı olarak Personal Life (~7) ve Family Life (~10) temalarında yoğunlaşmıştı. 3-4. Sınıf'ın
12 temasında toplam yalnızca 14 bulgu var — ve bunların üçte biri (5) tek bir temada (Y4-T6 Life
in the City) toplanıyor. **9 temanın 12'sinde sıfır bulgu** — bu, 3-4. Sınıf içeriğinin ipucu
yazımı açısından genel olarak 2. Sınıf'tan daha disiplinli olduğu sonucunu güçlendiriyor.

## Doğrulanmış bulgular

```
[CİDDİ] [ipucu-kalitesi] data/grade3/school-life-y3.json:inf-2 → "What is in the room?"
Mevcut : correct="A piano and a drum" | hint="Bir piyano var. Bir davul var."
Sorun  : İpucu, cevabı birebir tekrarlıyor.
```
```
[CİDDİ] [ipucu-kalitesi] data/grade3/school-life-y3.json:inf-4 → "Summer is not far. What is
        the clue?"
Mevcut : correct="It is warm and there are flowers" | hint="Hava ılık. Bahçe çiçek dolu."
Sorun  : İpucu, cevabı neredeyse birebir tekrarlıyor.
```
```
[KÜÇÜK] [ipucu-kalitesi] data/grade3/school-life-y3.json:inf-7 → "It is night. What is the
        clue?"
Mevcut : correct="The sun is down" | hint="Evde güneş doğmuş değil."
Sorun  : "Güneş doğmamış" ("sun hasn't risen"), "güneş battı"nın ("sun is down") olumsuzlanmış
         eşdeğeri — dolaylı ama fiilen aynı bilgiyi veriyor.
```
```
[KÜÇÜK] [ipucu-kalitesi] data/grade3/school-life-y3.json:inf-9 → "It is a summer month. What is
        the clue?"
Mevcut : correct="The weather is warm" | hint="Soğuk bir ay değil."
Sorun  : Aynı desen — "soğuk değil" fiilen "sıcak/ılık"ı doğruluyor.
```
```
[KÜÇÜK] [ipucu-kalitesi] data/grade3/family-life-y3.json:inf-5 → "Who is she?"
Mevcut : correct="My aunt" | hint="Annemin kız kardeşi. Annem değil."
Sorun  : "Annemin kız kardeşi" ("my mother's sister") "teyze/hala"nın sözlük tanımının ta
         kendisi — isim söylenmiyor ama tanım tek bir cevaba çıkıyor.
```
```
[KÜÇÜK] [ipucu-kalitesi] data/grade3/family-life-y3.json:inf-7 → "Who is she?"
Mevcut : correct="My cousin" | hint="Amcamın kızı. Kız kardeşim değil."
Sorun  : Aynı desen — "amcamın kızı" tam olarak "kuzen"in tanımı.
```
```
[KÜÇÜK] [ipucu-kalitesi] data/grade3/life-in-the-city-y3.json:inf-9 → "What does Maya say?"
Mevcut : correct="Pass me the salt, please!" | hint="Maya tuz istiyor."
Sorun  : "Maya tuz istiyor" ("Maya wants salt") cevabın özünü veriyor.
```
```
[KÜÇÜK] [ipucu-kalitesi] data/grade3/life-in-the-city-y3.json:inf-10 → "What special day is
        it?"
Mevcut : correct="Children's Day" | hint="Çocuklar için 23 Nisan."
Sorun  : Tarih + "çocuklar için" ifadesi, Çocuk Bayramı'nın tanımlayıcı unsurlarının ikisini
         birden veriyor.
```
```
[CİDDİ] [ipucu-kalitesi] data/grade4/school-life-y4.json:inf-6 → "What is Sam doing now?"
Mevcut : correct="He is dancing" | hint="Müzikle hareket ediyor."
Sorun  : "Müzikle hareket etmek" ("moving with music") "dans etmek"in yakın eşanlamlısı.
```
```
[CİDDİ] [ipucu-kalitesi] data/grade4/life-in-the-city-y4.json:inf-1 → "What clue does Sam say is
        the biggest?"
Mevcut : correct="The sea is the most beautiful blue" | hint="Deniz en güzel mavi renkte."
Sorun  : İpucu, cevabı neredeyse birebir tekrarlıyor.
```
```
[CİDDİ] [ipucu-kalitesi] data/grade4/life-in-the-city-y4.json:inf-2 → "What does Nora say about
        Sam's gift?"
Mevcut : correct="It is the most thoughtful gift and sounds delicious" | hint="Nora bu
         hediyenin en düşünceli hediye olduğunu söylüyor."
Sorun  : İpucu, cevabın ana tümcesini birebir tekrarlıyor.
```
```
[CİDDİ] [ipucu-kalitesi] data/grade4/life-in-the-city-y4.json:inf-2 → "What is Sam going to
        make?"
Mevcut : correct="A surprise salad for Grandma's birthday" | hint="Bu, Sam'in büyükannesi için
         hazırladığı bir doğum günü sürprizi."
Sorun  : Aynı metinde ikinci bir neredeyse-birebir tekrar.
```
```
[KÜÇÜK] [ipucu-kalitesi] data/grade4/life-in-the-city-y4.json:inf-7 → "Which word is right?"
Mevcut : correct="A little" | hint="Süt sayılamaz ve azdır."
Sorun  : "Az" ("little amount") doğrudan "a little"nin anlamına karşılık geliyor.
```
```
[KÜÇÜK] [ipucu-kalitesi] data/grade4/life-in-the-city-y4.json:inf-8 → "What does Sam say?"
Mevcut : correct="I'm starving" | hint="Sam çok aç."
Sorun  : "Çok aç" ("very hungry") "starving"in yakın eşanlamlısı — tam ifade değil ama anlamı
         veriyor.
```

## Genel değerlendirme

18 temanın `inf` grubu ipuçlarının **tamamı** (761 metnin ~355'i, ~1580 soru) artık tek tek
okunmuş durumda. Toplam doğrulanmış ipucu-sızıntısı: **2. Sınıf'ta 23 + 3-4. Sınıf'ta 14 = 37**.
Bunların çoğu (23/37) 2. Sınıf'ın 2 temasında (Personal Life, Family Life) yoğunlaşıyor; kalan
14'ü 3-4. Sınıf'a dağınık ve daha hafif (çoğu KÜÇÜK, birkaçı CİDDİ). Bu artık örneklem değil,
tam tarama sonucudur.
