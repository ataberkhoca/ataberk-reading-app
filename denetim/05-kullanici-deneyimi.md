# Kullanıcı Deneyimi Raporu — Y2 Tema 1 (School Life)

## Yöntem

`py -m http.server` ile proje kökünden yerel sunucu açıldı (`data/grade2/school-life.json`'ı
kapsayan tüm dosya ağacı servis edildi), tarayıcı otomasyonuyla gerçek akış oynandı: profil
oluşturma → sınıf/konu seçimi (2. Sınıf → School Life) → beceri seçimi → metin seçimi → hikâyeyi
okuma → soruları cevaplama (doğru + kasıtlı yanlış) → ipucu açma → sonuç ekranı → rozet bildirimleri.
Konsol ve ağ istekleri sürekli izlendi.

## Genel sonuç: teknik olarak sağlam, akış tamamlanabiliyor

- **Konsol hatası: 0.** Oturum boyunca (profil oluşturma, 6 tema arası dolaşma, 4 beceri türü,
  tam bir metin baştan sona tamamlama, rozet bildirimleri) hiçbir JavaScript hatası, uyarı ya da
  network hatası görülmedi.
- **Ağ istekleri: hepsi 200 OK.** `data/grade2/*.json` dosyalarının tamamı (6 tema) başarıyla
  yükleniyor, `reading-skills.html` de sorunsuz sunuluyor. Kırık yol, 404, yüklenemeyen varlık yok.
- **Tam bir "Çıkarım" metnini (inf-1, "Who Is She?") baştan sona oynadım:** hikâyeyi okuma ekranı →
  5 soru → 1 kasıtlı yanlış cevap → sonuç ekranı → 3 ayrı rozet bildirimi (İlk Adım, Çıkarım, Üç
  Yıldız, Tam İsabet, Cesur Okur ilerlemesi) sırayla ve doğru çalıştı. **Bulgu yok — bu akış sağlam.**

## Bulgu 1 — Cast/avatar satırı gerçek konuşan karakterle uyuşmuyor (KRİTİK, görsel olarak doğrulandı)

Pedagojik raporda ([04-pedagojik-rapor.md](04-pedagojik-rapor.md) §2b) JSON üzerinden tespit edilen
`int-9` bulgusu tarayıcıda doğrulandı:

```
[KRİTİK] [UX] data/grade2/school-life.json:int-9 → cast satırı (canlı ekran)
Gözlem : "Dikkatli Okuma · A New Teacher Visits" ekranı açıldığında üstte 3 karakter rozeti
         görünüyor: "👧 Eda", "👦🏻 Tom", "👨‍🏫 Mr. Aras". Ama hikâyenin kendisi şöyle başlıyor:
         "Miss Oli: A new teacher is in school today." ve devamı boyunca konuşan, hikâyenin
         öznesi olan karakter "Miss Pinar" ("Miss Pinar: I am Miss Pinar. I am a teacher." — 4 kez
         konuşuyor). Ekranda ne Miss Oli'nin ne de Miss Pinar'ın bir rozeti/avatarı var. Buna
         karşılık ekrandaki "Mr. Aras" hikâyede hiç konuşmuyor, yalnızca "Nerede?" diye sorulan bir
         isim.
Sorun  : Bir öğretmen/veli gözüyle: çocuk hikâyeyi okurken "Miss Pinar kim, nasıl görünüyor?"
         sorusuna ekranda hiçbir görsel karşılık bulamıyor — hikâyenin öznesi görünmez, alakasız
         bir karakter (Mr. Aras) görünür duruyor.
Öneri  : `cast` alanını ["Miss Oli", "Miss Pinar", "Tom"] ya da ["Miss Oli", "Miss Pinar", "Eda"]
         yap — gerçekten konuşan karakterlerle eşleştir.
Dayanak: Ekran görüntüsüyle doğrulandı (bu oturumda alınan canlı görüntü).
```

`int-11` ("Miss Oli in Classroom") için aynı desen JSON üzerinden doğrulandı (cast'te "Lila" yok,
ama Lila konuşuyor ve bir sorunun doğru cevabı) — zaman kısıtı nedeniyle ayrıca ekran görüntüsü
alınmadı, ama `int-9` ile birebir aynı mekanizma olduğu için aynı güvenilirlikte KRİTİK kabul
edildi.

## Bulgu 2 — İpucu davranışı: buton her zaman tıklanabilir, ama otomatik açılmıyor (düzeltme notu)

`hintMode: "always"` alanı ilk bakışta "ipucu ekranda sürekli açık" izlenimi veriyordu (bkz.
04-pedagojik-raporunun ilk taslağı) — ama canlı testte bu **yanlış** çıktı:

- İpucu her zaman bir **"💡 İpucu" butonuna tıklanarak** açılıyor, otomatik görünmüyor.
- `inf-1` sorularında bunu doğrudan test ettim: S4'te ipucuya bastığımda ekranda birebir şu metin
  çıktı: **"O öğrenci değil, müdür değil. O bir öğretmen."** — bu, pedagojik raporda JSON'dan
  öngörülen cevap-sızıntısını canlı ortamda **birebir doğruluyor**.
- Yanlış cevap verildiğinde ayrıca otomatik bir yönlendirme çıkıyor: **"👆 Cevap işaretli cümlede —
  bir daha oku."** — bu iyi tasarlanmış, cevabı vermeden öğrenciyi metne geri yönlendiren bir
  mekanizma. **Bulgu yok, bu kısım iyi.**

Sonuç: KRİTİK ipucu-sızıntısı bulgusu (04-pedagojik-rapor.md §2a) geçerliliğini koruyor — sadece
"ekranda sürekli açık" iddiası düzeltildi, "buton her tıklandığında cevabı doğrudan söylüyor" olarak
netleştirildi.

## Bulgu 3 — Doğru/yanlış geri bildirimi: iyi tasarlanmış (bulgu yok)

- Doğru cevap: seçilen şık **yeşile** dönüyor, bir sonraki soruya geçme butonu beliriyor.
- Yanlış cevap: seçilen şık **kırmızı/pembeye** dönüyor, hikâyedeki ilgili cümle (`hl` alanına göre)
  **sarıyla vurgulanıyor**, ve "Cevap işaretli cümlede — bir daha oku." mesajı çıkıyor. Öğrenci
  tekrar deneyebiliyor.
- Şıkların sırası her soru gösteriminde **karıştırılıyor** (randomize) — pozisyona göre ezber/tahmin
  riskini azaltıyor. İyi tasarım kararı.

## Bulgu 4 — Tamamlama ve rozet akışı: iyi tasarlanmış (bulgu yok)

Bir metni bitirince: "Harika Okudun!" başlıklı, doğru/yanlış sayısı ve yıldızları gösteren bir sonuç
ekranı açılıyor; beceriye özel teşvik mesajı geliyor ("Çıkarım becerin çok güçlü! 💪" — Inference
skoru yüksekse). Ardından kazanılan rozetler sırayla (İlk Adım → Çıkarım → Üç Yıldız → Tam İsabet)
tek tek gösteriliyor, her biri "Harika! 🏅" ile kapatılabiliyor. Ekran görüntüsü alma önerisi bile var
("Ekran görüntüsü alıp öğretmenine ya da ailene gösterebilirsin 📸"). **Bulgu yok — bu akış, bir
öğretmenin sınıfta kullanmasını kolaylaştıracak şekilde iyi düşünülmüş.**

## Bulgu 5 — Test sırasında düzeltilen bir yanlış varsayım (metodoloji notu, bulgu DEĞİL)

İlk denemelerimde her hikâye kartına tıkladığımda "Kim oynuyor?" ekranına düşüp profil seçtikten
sonra Konu Seçimi'ne geri atıldığımı gördüm ve bunu olası bir navigasyon hatası sandım. Kaynak kodu
incelediğimde (`reading-skills.html:4505`, `selectProfile()`) bunun gerçek nedeninin kendi
otomasyon hatam olduğunu tespit ettim: tıkladığım eleman aslında her ekranda sabit duran küçük
profil rozeti (sağ üstteki 🐱 ikonu) idi, gerçek hikâye kartı değildi. Doğru hikâye kartına
tıklandığında (bkz. yukarıdaki başarılı `inf-1` ve `int-9` oturumları) akış sorunsuz çalışıyor. Bunu
şeffaflık için not düşüyorum — **rapora bulgu olarak eklemedim, çünkü uygulamada gerçek bir hata
değil.**

## Genel değerlendirme

| Kontrol | Sonuç |
|---|---|
| Sunucu/varlık yükleme | ✅ Sorunsuz, 0 hata |
| Konsol hataları | ✅ 0 |
| Temel akış (profil→konu→beceri→metin→soru→sonuç) | ✅ Çalışıyor |
| Doğru/yanlış geri bildirimi | ✅ İyi tasarlanmış |
| İpucu mekanizması (buton) | ⚠️ Çalışıyor ama 5 metinde içerik hatalı (bkz. 04-pedagojik-rapor.md) |
| Cast/avatar-karakter eşleşmesi | ❌ En az 2 metinde (int-9, int-11) kırık — KRİTİK |
| Rozet/tamamlama akışı | ✅ İyi tasarlanmış |
