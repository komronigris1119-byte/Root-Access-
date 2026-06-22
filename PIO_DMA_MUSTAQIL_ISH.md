# PIO VA DMA O'RTASIDAGI FARQNI MODELLASHTIRISH

## MUSTAQIL ISH

---

**Fan:** Operatsion tizimlar

**Mavzu:** PIO (Programmed I/O) va DMA (Direct Memory Access) o'rtasidagi farqni modellashtirish (diagrammalar + tavsif)

**Talaba:** [Ism Familiya]

**Guruh:** [Guruh raqami]

**O'qituvchi:** [F.I.O.]

**Toshkent – 2026**

---

## MUNDARIJA

1. Kirish
2. Ma'lumot kiritish-chiqarish (I/O) tushunchasi
3. PIO (Programmed I/O) nima?
4. DMA (Direct Memory Access) nima?
5. PIO ish jarayoni diagrammasi
6. DMA ish jarayoni diagrammasi
7. Tizim arxitekturasi (umumiy diagramma)
8. PIO va DMA o'rtasidagi qiyosiy tahlil (jadval)
9. Vaqt diagrammasi orqali modellashtirish
10. 20 ta asosiy farq (ro'yxat)
11. Amaliy misol (psevdokod)
12. Xulosa

---

## 1. KIRISH

Operatsion tizimning eng muhim vazifalaridan biri — protsessor (CPU), tezkor xotira (RAM) va tashqi qurilmalar (disk, klaviatura, tarmoq kartasi, printer) o'rtasidagi ma'lumot almashinuvini boshqarishdir. Ma'lumotni qurilmadan xotiraga yoki xotiradan qurilmaga ko'chirishning ikkita asosiy usuli mavjud:

- **PIO (Programmed Input/Output)** — protsessor har bir baytni shaxsan boshqaradi;
- **DMA (Direct Memory Access)** — maxsus DMA kontroller ma'lumotni protsessor ishtirokisiz to'g'ridan-to'g'ri xotiraga ko'chiradi.

Ushbu mustaqil ishda ushbu ikki usulning ishlash mexanizmi diagrammalar yordamida modellashtiriladi va ular o'rtasidagi farqlar batafsil tahlil qilinadi.

---

## 2. MA'LUMOT KIRITISH-CHIQARISH (I/O) TUSHUNCHASI

I/O (Input/Output) — bu kompyuterning markaziy qismi (CPU + RAM) bilan tashqi dunyo (qurilmalar) o'rtasidagi ma'lumot oqimi. Har bir tashqi qurilmada qurilma kontrolleri va uning ichida registrlar mavjud:

- **Data registri** — uzatiladigan ma'lumotni saqlaydi;
- **Status registri** — qurilma holatini ko'rsatadi (band, tayyor, xato);
- **Control registri** — qurilmaga buyruq beradi (o'qish, yozish).

Protsessor ushbu registrlar bilan ishlash orqali ma'lumot uzatadi. Aynan shu jarayonni qanday tashkil etish PIO va DMA usullarini farqlaydi.

---

## 3. PIO (PROGRAMMED I/O) NIMA?

**PIO (Programmed I/O)** — bu ma'lumotni uzatishda protsessorning o'zi har bir bayt yoki so'zni qurilma registri va xotira o'rtasida ko'chirib turadigan usul.

PIO ning asosiy xususiyatlari:
- Protsessor butun jarayon davomida band bo'ladi;
- Qurilma tayyorligini tekshirish uchun **polling** (doimiy so'rov) yoki **interrupt** (uzilish) ishlatiladi;
- Qo'shimcha apparat (DMA kontroller) talab qilmaydi — soddaroq;
- Kichik hajmdagi ma'lumotlar uchun samarali, katta hajm uchun esa CPU ni isrof qiladi.

PIO ikki turga bo'linadi:
1. **Polling asosidagi PIO** — protsessor status registrni doimiy tekshiradi (busy-waiting).
2. **Interrupt asosidagi PIO** — qurilma tayyor bo'lganda protsessorga uzilish signali yuboradi.

---

## 4. DMA (DIRECT MEMORY ACCESS) NIMA?

**DMA (Direct Memory Access)** — bu ma'lumotni tashqi qurilma va tezkor xotira o'rtasida **protsessorni jalb qilmasdan**, maxsus **DMA kontroller** yordamida to'g'ridan-to'g'ri ko'chirish usuli.

DMA ning asosiy xususiyatlari:
- Protsessor faqat uzatishni boshlaydi (manzil, hajm, yo'nalishni belgilaydi), keyin boshqa ishlar bilan band bo'ladi;
- DMA kontroller butun ma'lumot blokini mustaqil ko'chiradi;
- Ko'chirish tugagach, DMA kontroller protsessorga bitta uzilish (interrupt) yuboradi;
- Katta hajmdagi ma'lumotlar (disk, tarmoq, video) uchun juda samarali;
- Qo'shimcha apparat (DMA kontroller) talab qiladi.

DMA rejimlari:
1. **Burst mode** — butun blok bir martada ko'chiriladi;
2. **Cycle stealing mode** — bitta so'z ko'chiriladi, keyin CPU ga shina qaytariladi;
3. **Transparent mode** — faqat CPU shinadan foydalanmagan paytda ko'chiradi.

---

## 5. PIO ISH JARAYONI DIAGRAMMASI

PIO da har bir bayt protsessor orqali o'tadi:

```
        PIO (Programmed I/O) - Polling rejimi
        =====================================

   +---------+                         +-------------+
   |  CPU    |                         |  Qurilma    |
   |         |   1. Status so'rovi      | Kontrolleri |
   |         |------------------------->|             |
   |         |                         |             |
   |         |   2. "Band" javobi       |             |
   |         |<------------------------ |             |
   |         |   (qayta-qayta tekshir)  |             |
   |  BAND   |                         |             |
   |  100%   |   3. "Tayyor" javobi     |             |
   |         |<------------------------ |             |
   |         |                         |             |
   |         |   4. Ma'lumotni o'qish   |             |
   |         |<------------------------ |             |
   |         |                         +-------------+
   |         |   5. Xotiraga yozish
   |         |-------------------+
   +---------+                   |
                                 v
                          +-------------+
                          |    RAM      |
                          | (xotira)    |
                          +-------------+

   Har bir bayt uchun 1-5 qadamlar TAKRORLANADI!
   CPU butun vaqt davomida band.
```

PIO da protsessor "vositachi" bo'lib, har bir baytni qurilmadan o'qib, xotiraga yozadi. Bu CPU ni to'liq band qiladi.

---

## 6. DMA ISH JARAYONI DIAGRAMMASI

DMA da ma'lumot CPU ni chetlab o'tadi:

```
        DMA (Direct Memory Access) ish jarayoni
        ========================================

   +---------+   1. Buyruq: manzil,    +-------------+
   |  CPU    |      hajm, yo'nalish    |     DMA     |
   |         |------------------------>| Kontrolleri |
   |         |                         |             |
   |  BO'SH  |   ... CPU boshqa ishni   |             |
   |  (boshqa|       bajaradi ...       |             |
   |  ishda) |                         |             |
   +---------+                         |             |
        ^                              |             |
        |                              |             |
        | 4. Tugadi (1 ta uzilish)     |             |
        |<-----------------------------|             |
                                       |             |
                          2. To'g'ridan-to'g'ri      |
                             ma'lumot ko'chirish      |
              +-------------+ <----------------> +----+--------+
              |    RAM      |                    |  Qurilma    |
              |  (xotira)   | <================= | (disk/tarmoq)|
              +-------------+   3. Butun blok     +-------------+
                                ko'chiriladi

   CPU faqat 1-qadamda (boshlash) va 4-qadamda (tugash)
   ishtirok etadi. Qolgan vaqtda BO'SH.
```

DMA da ma'lumot to'g'ridan-to'g'ri qurilma va xotira o'rtasida harakatlanadi. Protsessor faqat boshida buyruq beradi va oxirida bitta uzilish oladi.

---

## 7. TIZIM ARXITEKTURASI (UMUMIY DIAGRAMMA)

Quyidagi diagramma har ikkala usulning tizimdagi o'rnini ko'rsatadi:

```
              KOMPYUTER TIZIMI ARXITEKTURASI
              ==============================

   +----------------+        Tizim shinasi (System Bus)
   |      CPU       |==============================================
   +----------------+        ||              ||            ||
                             ||              ||            ||
                       +-----v-----+   +-----v------+  +---v-------+
                       |   RAM     |   |    DMA     |  | Qurilma   |
                       | (xotira)  |   | Kontroller |  | Kontroller|
                       +-----------+   +------------+  +-----------+
                                              ||             ||
                                              ||  DMA yo'li   ||
                                              ===============
                                          (CPU ni chetlab o'tadi)

   PIO yo'li:  CPU <--> Qurilma <--> CPU <--> RAM   (CPU vositachi)
   DMA yo'li:  Qurilma <--> DMA Kontroller <--> RAM (CPU erkin)
```

---

## 8. PIO VA DMA O'RTASIDAGI QIYOSIY TAHLIL (JADVAL)

| # | Mezon | PIO (Programmed I/O) | DMA (Direct Memory Access) |
|---|-------|----------------------|----------------------------|
| 1 | Boshqaruvchi | Protsessor (CPU) | DMA kontroller |
| 2 | CPU bandligi | To'liq band (100%) | Deyarli bo'sh (faqat start/stop) |
| 3 | Ma'lumot yo'li | Qurilma → CPU → Xotira | Qurilma → Xotira (to'g'ridan-to'g'ri) |
| 4 | Tezlik | Sekin | Tez |
| 5 | Uzilishlar soni | Ko'p (har bayt/blok) | Kam (bitta, blok tugaganda) |
| 6 | Apparat narxi | Arzon (qo'shimcha apparat yo'q) | Qimmat (DMA kontroller kerak) |
| 7 | Murakkablik | Sodda | Murakkabroq |
| 8 | Mos hajm | Kichik ma'lumotlar | Katta ma'lumot bloklari |
| 9 | Samaradorlik | Past (katta hajmda) | Yuqori |
| 10 | Misol qurilmalar | Klaviatura, sichqoncha | Disk, tarmoq, video, audio |

---

## 9. VAQT DIAGRAMMASI ORQALI MODELLASHTIRISH

Quyida 4 ta ma'lumot blokini uzatish jarayonida CPU ning bandligi taqqoslanadi:

```
   PIO (CPU butun vaqt band):
   CPU: [###BLOK1###][###BLOK2###][###BLOK3###][###BLOK4###]
        |<---------- CPU 100% band -------------------->|
        Boshqa vazifalar bajarilmaydi!

   DMA (CPU deyarli erkin):
   CPU: [S]..................................[E]
        |  (DMA ishlayotganda CPU boshqa vazifa bajaradi)  |
   DMA:    [###BLOK1###][###BLOK2###][###BLOK3###][###BLOK4###]
        S = Start (boshlash buyrug'i)
        E = End (tugash uzilishi)
        . = CPU boshqa foydali ishlarni bajaradi
```

Bu diagramma DMA ning asosiy ustunligini ko'rsatadi: protsessor ma'lumot ko'chirilayotgan paytda boshqa hisob-kitoblarni bajarib, tizim umumiy unumdorligini oshiradi.

---

## 10. PIO VA DMA O'RTASIDAGI 20 TA ASOSIY FARQ (RO'YXAT)

1. **Boshqaruv:** PIO da ma'lumot uzatishni protsessor boshqaradi; DMA da maxsus DMA kontroller boshqaradi.
2. **CPU yuki:** PIO protsessorni to'liq band qiladi; DMA protsessorni deyarli bo'sh qoldiradi.
3. **Ma'lumot yo'li:** PIO da ma'lumot CPU orqali o'tadi; DMA da to'g'ridan-to'g'ri xotiraga boradi.
4. **Tezlik:** DMA PIO ga qaraganda ancha tezroq ishlaydi.
5. **Uzilishlar soni:** PIO da uzilishlar ko'p; DMA da blok tugaganda faqat bitta uzilish bo'ladi.
6. **Apparat ehtiyoji:** PIO qo'shimcha apparat talab qilmaydi; DMA alohida DMA kontrollerni talab qiladi.
7. **Narx:** PIO arzon; DMA qimmatroq (qo'shimcha apparat tufayli).
8. **Murakkablik:** PIO sodda; DMA dasturiy va apparat jihatdan murakkabroq.
9. **Mos hajm:** PIO kichik ma'lumotlar uchun; DMA katta ma'lumot bloklari uchun.
10. **Samaradorlik:** Katta hajmda PIO samarasiz; DMA juda samarali.
11. **Shina egaligi:** PIO da shinani doimo CPU boshqaradi; DMA da shina vaqtincha DMA kontrollerga o'tadi.
12. **Parallel ishlash:** PIO da CPU parallel ish bajara olmaydi; DMA da CPU parallel ishlay oladi.
13. **Energiya sarfi:** PIO ko'proq CPU vaqtini va energiyani sarflaydi; DMA tejamkorroq.
14. **Polling/Busy-wait:** PIO ko'pincha pollingdan foydalanadi; DMA pollingga muhtoj emas.
15. **Kechikish (latency):** PIO da kichik uzatishlar uchun kechikish kam; DMA da boshlang'ich sozlash qo'shimcha vaqt oladi.
16. **Tizim unumdorligi:** PIO umumiy unumdorlikni pasaytiradi; DMA umumiy unumdorlikni oshiradi.
17. **Dasturiy yuk (overhead):** PIO da har uzatishda dasturiy yuk yuqori; DMA da bir martalik sozlash yuki bor.
18. **Tipik foydalanish:** PIO — klaviatura, sichqoncha kabi sekin qurilmalar; DMA — disk, SSD, tarmoq, grafika.
19. **Xotiraga kirish:** PIO bilvosita (CPU registrlari orqali); DMA bevosita (RAM ga to'g'ridan-to'g'ri).
20. **Kengayuvchanlik (scalability):** PIO ko'p yoki tez qurilmalarda yaxshi kengaymaydi; DMA yuqori tezlikli ko'p qurilmalarni samarali qo'llab-quvvatlaydi.

---

## 11. AMALIY MISOL (PSEVDOKOD)

**PIO (polling) usulida disk blokini o'qish:**

```
// PIO - protsessor har bir baytni o'zi ko'chiradi
funksiya PIO_oqish(disk, xotira_manzil, n_bayt):
    disk.control = O'QISH_BUYRUG'I
    uchun i = 0 dan n_bayt gacha:
        // status registrni doimiy tekshirish (busy-wait)
        while (disk.status != TAYYOR):
            kutish   // CPU band - hech nima qilmaydi!
        // baytni o'qib, xotiraga yozish
        xotira[xotira_manzil + i] = disk.data
    qaytish: BAJARILDI
```

**DMA usulida disk blokini o'qish:**

```
// DMA - kontroller mustaqil ko'chiradi
funksiya DMA_oqish(disk, xotira_manzil, n_bayt):
    // 1. DMA kontrollerni sozlash
    dma.manzil = xotira_manzil
    dma.hajm   = n_bayt
    dma.yonalish = QURILMADAN_XOTIRAGA
    dma.start = TRUE          // uzatishni boshlash

    // 2. CPU endi boshqa ishlarni bajaradi
    boshqa_vazifalarni_bajarish()

    // 3. Tugaganda DMA uzilish yuboradi
    uzilish_kutish(DMA_TUGADI)
    qaytish: BAJARILDI
```

Ushbu ikkala misol o'rtasidagi farq aniq: PIO da `while` sikli protsessorni band qiladi, DMA da esa CPU `boshqa_vazifalarni_bajarish()` orqali foydali ish qiladi.

---

## 12. XULOSA

PIO va DMA — operatsion tizimda ma'lumot kiritish-chiqarishni tashkil etishning ikki asosiy usuli bo'lib, ularning har biri o'z o'rniga ega:

- **PIO** sodda, arzon va kichik hajmdagi, sekin qurilmalar (klaviatura, sichqoncha) uchun mos. Ammo u protsessorni to'liq band qilgani uchun katta hajmdagi ma'lumotlar bilan ishlashda samarasizdir.

- **DMA** qo'shimcha apparat talab qilsa-da, ma'lumotni protsessor ishtirokisiz to'g'ridan-to'g'ri xotiraga ko'chiradi. Bu protsessorni boshqa vazifalar uchun ozod qiladi va katta hajmdagi ma'lumotlar (disk, tarmoq, video) bilan ishlashda tizim unumdorligini sezilarli oshiradi.

Zamonaviy kompyuterlarda yuqori tezlikdagi qurilmalar (SSD, tarmoq adapterlari, grafik kartalar) deyarli har doim DMA dan foydalanadi, sekin va sodda qurilmalar esa PIO bilan ishlashi mumkin. Demak, ikkala usul ham bir-birini to'ldiradi va tizim loyihalovchisi qurilma turi hamda ma'lumot hajmiga qarab to'g'ri usulni tanlaydi.

---

*Mustaqil ish · Operatsion tizimlar fani · 2026*
