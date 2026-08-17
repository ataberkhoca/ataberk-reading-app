# Kapsam Raporu — Kalan 17 Dosya (Y2-T2..T6, Y3-T1..T6, Y4-T1..T6)

Y2-Tema1'in kelime kapsamı zaten [03-kapsam-raporu.md](03-kapsam-raporu.md)'de ayrıntılı
yapılmıştı. Bu rapor, her temanın kendi müfredat "a) Target Vocabulary" listesini (yalnızca o
temada **yeni** olan kelimeler — recycled/background olanlar hariç) çıkarıp kalan 17 dosyada
kapsamı kontrol ediyor. Betik: [`coverage_scan.py`](coverage_scan.py), ham çıktı:
`coverage_scan_output.json`.

## Yöntem notu — 3 yanlış pozitif elendi

Otomatik tarama bazı "hiç yok" sonuçlarını üretti, ama üçü gerçek boşluk değil, tarama
yönteminin kendi kusuruydu — elle doğrulanıp elendi:
- **`sitting-room`** (Y2-T5): dosya "sitting room" (tireless, boşluklu) yazıyor; kelime aslında
  var, sadece regex tire arıyordu. **Yanlış pozitif.**
- **`eraser`** (Y2-T2): müfredat "a rubber (an eraser-AmE.)" diyor; dosya tutarlı biçimde
  İngiliz İngilizcesi "rubber" kullanıyor (zaten dolu çıktı) — "eraser" hiç kullanılmaması
  beklenen bir şey, İngiliz/Amerikan varyant tercihi. **Yanlış pozitif.**
- **`cafe`** (Y3-T6, aksansız): dosya tutarlı biçimde "café" (aksanlı) yazıyor, ki o zaten dolu
  çıktı. **Yanlış pozitif — çift kontrol hatası.**

## Gerçek bulgular

### Y2-T2 Classroom Life

```
[CİDDİ] [kapsam-boşluğu] data/grade2/classroom-life.json → hedef kelime "coloured pencil"
Sorun  : "a coloured pencil" (renkli kalem), "a pencil" (adi kalem)'den ayrı bir hedef kelime
         olarak müfredatta listeleniyor, ama dosyada hiç geçmiyor.
```
```
[KÜÇÜK] [kapsam-boşluğu] data/grade2/classroom-life.json → "a blackboard/whiteboard"
Sorun  : Bu çift-isimli hedef kelime toplamda yalnızca 1 kez geçiyor (yalnızca "blackboard"
         olarak; "whiteboard" hiç geçmiyor) — 45 metinlik bir temada çok ince kapsam.
```

### Y3-T1 School Life

```
[CİDDİ] [kapsam-boşluğu] data/grade3/school-life-y3.json → 2 hedef fiil + 1 hedef yer
Sorun  : Doğum günü partisi alt-temasının hedef fiilleri "prepare" ve "decorate"nin ikisi de
         40 metnin hiçbirinde geçmiyor (kök dahi yok — "prepares/preparing" gibi çekimler de
         yok). Hedef yer "a meeting room" da hiç geçmiyor.
Öneri  : Doğum günü/parti metinlerinden birine "They prepare the room. They decorate it with
         balloons." gibi bir cümle eklemek; okul yerleri metinlerinden birine "meeting room"u
         dahil etmek.
```
```
[KÜÇÜK] [kapsam-boşluğu] data/grade3/school-life-y3.json → "play the guitar" / "write a song"
Sorun  : Bu iki hedef DİL KALIBI (chunk) tam olarak geçmiyor — ama ilgili kelimeler ("guitar",
         "song") başka bağlamlarda geçiyor. Yani kelime kaybı yok, ama müfredatın istediği tam
         fiil öbeği (chunk) üretici biçimde kurulmamış.
```

### Y3-T2 Classroom Life

```
[KÜÇÜK] [kapsam-boşluğu] data/grade3/classroom-life-y3.json → "teacher's chair"
Sorun  : Hiç geçmiyor. "Student's desk" ve "locker" de yalnızca 1'er kez — 44 metinlik temada
         ince kapsam.
```

### Y3-T3 Personal Life

```
[STİL] [kapsam-boşluğu] data/grade3/personal-life-y3.json → "fat" / "ugly"
Sorun  : Bu iki hedef sıfat (müfredatın kendi "Physical adjectives" listesinde) hiç
         kullanılmamış. Bu muhtemelen **kasıtlı bir pedagojik tercih** — çocuklara yönelik bir
         uygulamada "şişman/çirkin" gibi olumsuz beden tasviri sıfatlarından kaçınmak makul bir
         karar olabilir. Müfredat ihlali değil, bilinçli bir tercih olarak işaretliyorum;
         dayatma değil.
```

### Y3-T4 Family Life — en fazla boşluk olan dosya

```
[CİDDİ] [kapsam-boşluğu] data/grade3/family-life-y3.json → 8 hedef kelime/kalıp hiç geçmiyor
Bulgu  : "grandson" (torun-erkek), "granddaughter" (torun-kız), "men" (erkekler-çoğul), "woman"
         (kadın-tekil), "women" (kadınlar-çoğul), "put on" (giyinmek), "study" (ders çalışmak),
         "do homework" (ödev yapmak) — bu 8 hedef öğenin hiçbiri 43 metnin hiçbirinde geçmiyor.
Not    : "man" (tekil) ve "boy/girl/child" gibi yakın kelimeler dosyada var — ama müfredatın
         açıkça istediği "men/woman/women" çoğul/tekil cinsiyet kelimeleri ve "grandson/
         granddaughter" akrabalık kelimeleri boş. Günlük rutin fiilleri "put on/study/do
         homework" da hiç yok — "wake up, wash face, brush teeth, have breakfast, go to
         school..." gibi diğer rutin fiiller var (bkz. aşağıdaki 1-kez'ler) ama bu üçü eksik.
Öneri  : Aile ağacı temalı bir metne "This is my grandson/granddaughter" cümlesi; günlük rutin
         metinlerinden birine "She studies. She does her homework. She puts on her coat."
         cümleleri eklemek.
```
```
[KÜÇÜK] [kapsam-boşluğu] data/grade3/family-life-y3.json → "brush teeth" / "have lunch" /
        "have dinner"
Sorun  : Bu 3 rutin kalıbı yalnızca 1'er kez geçiyor — ince kapsam.
```

### Y2-T6 Life in the City

```
[KÜÇÜK] [kapsam-boşluğu] data/grade2/life-in-city.json → "spinach"
Sorun  : Hedef sebze kelimesi yalnızca 1 kez geçiyor.
```

### Diğer 10 dosya — temiz

Y2-T3, Y2-T4, Y3-T5, Y4-T1, Y4-T2, Y4-T3, Y4-T4, Y4-T5, Y4-T6'da taranan hedef kelimelerin
**hiçbiri sıfır ya da tek-kez** çıkmadı — kapsam sağlam. Özellikle **Y4'ün 6 temasının 6'sı da
kusursuz** — bu, Y4 içeriğinin kelime kapsamı disiplini açısından da (ipucu kalitesinde olduğu
gibi, bkz. 10-ipucu-tam-tarama.md) diğer sınıflardan daha güçlü olduğunu gösteriyor.

## Genel özet

| Dosya | Taranan kelime | Hiç yok (gerçek) | Yalnızca 1 kez |
|---|---|---|---|
| Y2-T2 Classroom Life | 35 | 1 (coloured pencil) | 1 (blackboard, whiteboard'la birlikte) |
| Y2-T3 Personal Life | 41 | 0 | 0 |
| Y2-T4 Family Life | 14 | 0 | 0 |
| Y2-T5 Homes & Houses | 26 | 0 (yanlış pozitif elendi) | 0 |
| Y2-T6 Life in the City | 29 | 0 | 1 (spinach) |
| Y3-T1 School Life | 33 | 3 (meeting room, prepare, decorate) | 0 |
| Y3-T2 Classroom Life | 34 | 1 (teacher's chair) | 2 |
| Y3-T3 Personal Life | 34 | 2 (fat, ugly — kasıtlı olabilir) | 1 |
| Y3-T4 Family Life | 39 | **8** | 3 |
| Y3-T5 Homes & Houses | 23 | 0 | 0 |
| Y3-T6 Life in the City | 23 | 0 (yanlış pozitif elendi) | 0 |
| Y4-T1..T6 (6 dosya) | 178 (toplam) | 0 | 0 |

**En dikkat çekici sonuç:** Y3-Tema4 (Family Life), 8 hedef kelime/kalıbın tamamen eksik olduğu
tek dosya — diğer 16 dosyanın toplamından daha fazla. Bu, [08-mufredat-sizinti-tum-
uygulama.md](08-mufredat-sizinti-tum-uygulama.md)'deki bulgularla birleşince (o raporda Y3-T4'te
yalnızca 4 ham eşleşme vardı, en az sızıntılı dosyalardan biriydi) ilginç bir tablo çiziyor: bu
tema ileri sızıntı yapmıyor ama kendi hedeflerinin bir kısmını da karşılamıyor — iki farklı
sorun (fazla ileri gitmek vs. yeterince ileri gitmemek) birbirinden bağımsız.
