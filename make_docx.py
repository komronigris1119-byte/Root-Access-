#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PIO va DMA mustaqil ishini .docx (Word) formatiga aylantiruvchi skript.
Faqat standart kutubxonadan foydalanadi (zipfile, xml)."""

import zipfile, datetime

def esc(t):
    return (t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
             .replace('"', "&quot;").replace("'", "&apos;"))

paras = []  # har bir element: (tur, matn/yacheykalar)

def heading(text, level=1):
    paras.append(("h%d" % level, text))

def para(text, bold=False, italic=False, center=False):
    paras.append(("p", (text, bold, italic, center)))

def code(text):
    paras.append(("code", text))

def table(rows):
    paras.append(("table", rows))

def pagebreak():
    paras.append(("pagebreak", None))

# ----------------- KONTENT -----------------
para("PIO VA DMA O'RTASIDAGI FARQNI MODELLASHTIRISH", bold=True, center=True)
para("MUSTAQIL ISH", bold=True, center=True)
para("")
para("Fan: Operatsion tizimlar", bold=True, center=True)
para("Mavzu: PIO (Programmed I/O) va DMA (Direct Memory Access) o'rtasidagi farqni modellashtirish (diagrammalar + tavsif)", center=True)
para("")
para("Talaba: __________________________", center=True)
para("Guruh: __________________________", center=True)
para("O'qituvchi: ______________________", center=True)
para("")
para("Toshkent – 2026", bold=True, center=True)
pagebreak()

heading("MUNDARIJA", 1)
for i, t in enumerate([
    "Kirish", "Ma'lumot kiritish-chiqarish (I/O) tushunchasi",
    "PIO (Programmed I/O) nima?", "DMA (Direct Memory Access) nima?",
    "PIO ish jarayoni diagrammasi", "DMA ish jarayoni diagrammasi",
    "Tizim arxitekturasi (umumiy diagramma)",
    "PIO va DMA o'rtasidagi qiyosiy tahlil (jadval)",
    "Vaqt diagrammasi orqali modellashtirish",
    "20 ta asosiy farq (ro'yxat)", "Amaliy misol (psevdokod)", "Xulosa"], 1):
    para("%d. %s" % (i, t))

heading("1. KIRISH", 1)
para("Operatsion tizimning eng muhim vazifalaridan biri — protsessor (CPU), tezkor xotira (RAM) va tashqi qurilmalar (disk, klaviatura, tarmoq kartasi, printer) o'rtasidagi ma'lumot almashinuvini boshqarishdir. Ma'lumotni qurilmadan xotiraga yoki xotiradan qurilmaga ko'chirishning ikkita asosiy usuli mavjud:")
para("• PIO (Programmed Input/Output) — protsessor har bir baytni shaxsan boshqaradi;")
para("• DMA (Direct Memory Access) — maxsus DMA kontroller ma'lumotni protsessor ishtirokisiz to'g'ridan-to'g'ri xotiraga ko'chiradi.")
para("Ushbu mustaqil ishda ushbu ikki usulning ishlash mexanizmi diagrammalar yordamida modellashtiriladi va ular o'rtasidagi farqlar batafsil tahlil qilinadi.")

heading("2. MA'LUMOT KIRITISH-CHIQARISH (I/O) TUSHUNCHASI", 1)
para("I/O (Input/Output) — bu kompyuterning markaziy qismi (CPU + RAM) bilan tashqi dunyo (qurilmalar) o'rtasidagi ma'lumot oqimi. Har bir tashqi qurilmada qurilma kontrolleri va uning ichida registrlar mavjud:")
para("• Data registri — uzatiladigan ma'lumotni saqlaydi;")
para("• Status registri — qurilma holatini ko'rsatadi (band, tayyor, xato);")
para("• Control registri — qurilmaga buyruq beradi (o'qish, yozish).")
para("Protsessor ushbu registrlar bilan ishlash orqali ma'lumot uzatadi. Aynan shu jarayonni qanday tashkil etish PIO va DMA usullarini farqlaydi.")

heading("3. PIO (PROGRAMMED I/O) NIMA?", 1)
para("PIO (Programmed I/O) — bu ma'lumotni uzatishda protsessorning o'zi har bir bayt yoki so'zni qurilma registri va xotira o'rtasida ko'chirib turadigan usul.")
para("PIO ning asosiy xususiyatlari:", bold=True)
para("• Protsessor butun jarayon davomida band bo'ladi;")
para("• Qurilma tayyorligini tekshirish uchun polling (doimiy so'rov) yoki interrupt (uzilish) ishlatiladi;")
para("• Qo'shimcha apparat (DMA kontroller) talab qilmaydi — soddaroq;")
para("• Kichik hajmdagi ma'lumotlar uchun samarali, katta hajm uchun esa CPU ni isrof qiladi.")
para("PIO ikki turga bo'linadi:", bold=True)
para("1. Polling asosidagi PIO — protsessor status registrni doimiy tekshiradi (busy-waiting).")
para("2. Interrupt asosidagi PIO — qurilma tayyor bo'lganda protsessorga uzilish signali yuboradi.")

heading("4. DMA (DIRECT MEMORY ACCESS) NIMA?", 1)
para("DMA (Direct Memory Access) — bu ma'lumotni tashqi qurilma va tezkor xotira o'rtasida protsessorni jalb qilmasdan, maxsus DMA kontroller yordamida to'g'ridan-to'g'ri ko'chirish usuli.")
para("DMA ning asosiy xususiyatlari:", bold=True)
para("• Protsessor faqat uzatishni boshlaydi (manzil, hajm, yo'nalishni belgilaydi), keyin boshqa ishlar bilan band bo'ladi;")
para("• DMA kontroller butun ma'lumot blokini mustaqil ko'chiradi;")
para("• Ko'chirish tugagach, DMA kontroller protsessorga bitta uzilish (interrupt) yuboradi;")
para("• Katta hajmdagi ma'lumotlar (disk, tarmoq, video) uchun juda samarali;")
para("• Qo'shimcha apparat (DMA kontroller) talab qiladi.")
para("DMA rejimlari:", bold=True)
para("1. Burst mode — butun blok bir martada ko'chiriladi;")
para("2. Cycle stealing mode — bitta so'z ko'chiriladi, keyin CPU ga shina qaytariladi;")
para("3. Transparent mode — faqat CPU shinadan foydalanmagan paytda ko'chiradi.")

heading("5. PIO ISH JARAYONI DIAGRAMMASI", 1)
para("PIO da har bir bayt protsessor orqali o'tadi:")
code(r"""        PIO (Programmed I/O) - Polling rejimi
        =====================================

   +---------+                         +-------------+
   |  CPU    |                         |  Qurilma    |
   |         |   1. Status so'rovi      | Kontrolleri |
   |         |------------------------->|             |
   |         |   2. "Band" javobi       |             |
   |         |<------------------------ |             |
   |         |   (qayta-qayta tekshir)  |             |
   |  BAND   |   3. "Tayyor" javobi     |             |
   |  100%   |<------------------------ |             |
   |         |   4. Ma'lumotni o'qish   |             |
   |         |<------------------------ |             |
   |         |                         +-------------+
   |         |   5. Xotiraga yozish
   |         |-------------------+
   +---------+                   |
                                 v
                          +-------------+
                          |    RAM      |
                          |  (xotira)   |
                          +-------------+

   Har bir bayt uchun 1-5 qadamlar TAKRORLANADI!
   CPU butun vaqt davomida band.""")
para("PIO da protsessor \"vositachi\" bo'lib, har bir baytni qurilmadan o'qib, xotiraga yozadi. Bu CPU ni to'liq band qiladi.")

heading("6. DMA ISH JARAYONI DIAGRAMMASI", 1)
para("DMA da ma'lumot CPU ni chetlab o'tadi:")
code(r"""        DMA (Direct Memory Access) ish jarayoni
        ========================================

   +---------+   1. Buyruq: manzil,    +-------------+
   |  CPU    |      hajm, yo'nalish    |     DMA     |
   |         |------------------------>| Kontrolleri |
   |  BO'SH  |   ... CPU boshqa ishni   |             |
   |  (boshqa|       bajaradi ...       |             |
   |  ishda) |                         |             |
   +---------+                         |             |
        ^                              |             |
        | 4. Tugadi (1 ta uzilish)     |             |
        |<-----------------------------|             |
                          2. To'g'ridan-to'g'ri      |
                             ma'lumot ko'chirish      |
              +-------------+ <---------------> +-----+-------+
              |    RAM      |                   |  Qurilma    |
              |  (xotira)   | <================ | (disk/tarmoq)|
              +-------------+   3. Butun blok    +-------------+
                                ko'chiriladi

   CPU faqat 1-qadamda (boshlash) va 4-qadamda (tugash)
   ishtirok etadi. Qolgan vaqtda BO'SH.""")
para("DMA da ma'lumot to'g'ridan-to'g'ri qurilma va xotira o'rtasida harakatlanadi. Protsessor faqat boshida buyruq beradi va oxirida bitta uzilish oladi.")

heading("7. TIZIM ARXITEKTURASI (UMUMIY DIAGRAMMA)", 1)
para("Quyidagi diagramma har ikkala usulning tizimdagi o'rnini ko'rsatadi:")
code(r"""              KOMPYUTER TIZIMI ARXITEKTURASI
              ==============================

   +----------------+        Tizim shinasi (System Bus)
   |      CPU       |=============================================
   +----------------+        ||              ||            ||
                             ||              ||            ||
                       +-----v-----+   +-----v------+  +---v------+
                       |   RAM     |   |    DMA     |  | Qurilma  |
                       | (xotira)  |   | Kontroller |  |Kontroller|
                       +-----------+   +------------+  +----------+
                                              ||             ||
                                              ||  DMA yo'li   ||
                                              ===============
                                          (CPU ni chetlab o'tadi)

   PIO yo'li:  CPU <-> Qurilma <-> CPU <-> RAM   (CPU vositachi)
   DMA yo'li:  Qurilma <-> DMA Kontroller <-> RAM (CPU erkin)""")

heading("8. PIO VA DMA O'RTASIDAGI QIYOSIY TAHLIL (JADVAL)", 1)
table([
    ["#", "Mezon", "PIO (Programmed I/O)", "DMA (Direct Memory Access)"],
    ["1", "Boshqaruvchi", "Protsessor (CPU)", "DMA kontroller"],
    ["2", "CPU bandligi", "To'liq band (100%)", "Deyarli bo'sh (faqat start/stop)"],
    ["3", "Ma'lumot yo'li", "Qurilma → CPU → Xotira", "Qurilma → Xotira (to'g'ridan-to'g'ri)"],
    ["4", "Tezlik", "Sekin", "Tez"],
    ["5", "Uzilishlar soni", "Ko'p (har bayt/blok)", "Kam (bitta, blok tugaganda)"],
    ["6", "Apparat narxi", "Arzon (qo'shimcha apparat yo'q)", "Qimmat (DMA kontroller kerak)"],
    ["7", "Murakkablik", "Sodda", "Murakkabroq"],
    ["8", "Mos hajm", "Kichik ma'lumotlar", "Katta ma'lumot bloklari"],
    ["9", "Samaradorlik", "Past (katta hajmda)", "Yuqori"],
    ["10", "Misol qurilmalar", "Klaviatura, sichqoncha", "Disk, tarmoq, video, audio"],
])

heading("9. VAQT DIAGRAMMASI ORQALI MODELLASHTIRISH", 1)
para("Quyida 4 ta ma'lumot blokini uzatish jarayonida CPU ning bandligi taqqoslanadi:")
code(r"""   PIO (CPU butun vaqt band):
   CPU: [###BLOK1###][###BLOK2###][###BLOK3###][###BLOK4###]
        |<---------- CPU 100% band -------------------->|
        Boshqa vazifalar bajarilmaydi!

   DMA (CPU deyarli erkin):
   CPU: [S]..................................[E]
        | (DMA ishlayotganda CPU boshqa vazifa bajaradi) |
   DMA:    [###BLOK1###][###BLOK2###][###BLOK3###][###BLOK4###]
        S = Start (boshlash buyrug'i)
        E = End (tugash uzilishi)
        . = CPU boshqa foydali ishlarni bajaradi""")
para("Bu diagramma DMA ning asosiy ustunligini ko'rsatadi: protsessor ma'lumot ko'chirilayotgan paytda boshqa hisob-kitoblarni bajarib, tizim umumiy unumdorligini oshiradi.")

heading("10. PIO VA DMA O'RTASIDAGI 20 TA ASOSIY FARQ (RO'YXAT)", 1)
farqlar = [
 "Boshqaruv: PIO da ma'lumot uzatishni protsessor boshqaradi; DMA da maxsus DMA kontroller boshqaradi.",
 "CPU yuki: PIO protsessorni to'liq band qiladi; DMA protsessorni deyarli bo'sh qoldiradi.",
 "Ma'lumot yo'li: PIO da ma'lumot CPU orqali o'tadi; DMA da to'g'ridan-to'g'ri xotiraga boradi.",
 "Tezlik: DMA PIO ga qaraganda ancha tezroq ishlaydi.",
 "Uzilishlar soni: PIO da uzilishlar ko'p; DMA da blok tugaganda faqat bitta uzilish bo'ladi.",
 "Apparat ehtiyoji: PIO qo'shimcha apparat talab qilmaydi; DMA alohida DMA kontrollerni talab qiladi.",
 "Narx: PIO arzon; DMA qimmatroq (qo'shimcha apparat tufayli).",
 "Murakkablik: PIO sodda; DMA dasturiy va apparat jihatdan murakkabroq.",
 "Mos hajm: PIO kichik ma'lumotlar uchun; DMA katta ma'lumot bloklari uchun.",
 "Samaradorlik: Katta hajmda PIO samarasiz; DMA juda samarali.",
 "Shina egaligi: PIO da shinani doimo CPU boshqaradi; DMA da shina vaqtincha DMA kontrollerga o'tadi.",
 "Parallel ishlash: PIO da CPU parallel ish bajara olmaydi; DMA da CPU parallel ishlay oladi.",
 "Energiya sarfi: PIO ko'proq CPU vaqtini va energiyani sarflaydi; DMA tejamkorroq.",
 "Polling/Busy-wait: PIO ko'pincha pollingdan foydalanadi; DMA pollingga muhtoj emas.",
 "Kechikish (latency): PIO da kichik uzatishlar uchun kechikish kam; DMA da boshlang'ich sozlash qo'shimcha vaqt oladi.",
 "Tizim unumdorligi: PIO umumiy unumdorlikni pasaytiradi; DMA umumiy unumdorlikni oshiradi.",
 "Dasturiy yuk (overhead): PIO da har uzatishda dasturiy yuk yuqori; DMA da bir martalik sozlash yuki bor.",
 "Tipik foydalanish: PIO — klaviatura, sichqoncha kabi sekin qurilmalar; DMA — disk, SSD, tarmoq, grafika.",
 "Xotiraga kirish: PIO bilvosita (CPU registrlari orqali); DMA bevosita (RAM ga to'g'ridan-to'g'ri).",
 "Kengayuvchanlik (scalability): PIO ko'p yoki tez qurilmalarda yaxshi kengaymaydi; DMA yuqori tezlikli ko'p qurilmalarni samarali qo'llab-quvvatlaydi.",
]
for i, f in enumerate(farqlar, 1):
    para("%d. %s" % (i, f))

heading("11. AMALIY MISOL (PSEVDOKOD)", 1)
para("PIO (polling) usulida disk blokini o'qish:", bold=True)
code(r"""// PIO - protsessor har bir baytni o'zi ko'chiradi
funksiya PIO_oqish(disk, xotira_manzil, n_bayt):
    disk.control = O'QISH_BUYRUG'I
    uchun i = 0 dan n_bayt gacha:
        // status registrni doimiy tekshirish (busy-wait)
        while (disk.status != TAYYOR):
            kutish   // CPU band - hech nima qilmaydi!
        // baytni o'qib, xotiraga yozish
        xotira[xotira_manzil + i] = disk.data
    qaytish: BAJARILDI""")
para("DMA usulida disk blokini o'qish:", bold=True)
code(r"""// DMA - kontroller mustaqil ko'chiradi
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
    qaytish: BAJARILDI""")
para("Ushbu ikkala misol o'rtasidagi farq aniq: PIO da while sikli protsessorni band qiladi, DMA da esa CPU boshqa_vazifalarni_bajarish() orqali foydali ish qiladi.")

heading("12. XULOSA", 1)
para("PIO va DMA — operatsion tizimda ma'lumot kiritish-chiqarishni tashkil etishning ikki asosiy usuli bo'lib, ularning har biri o'z o'rniga ega:")
para("• PIO sodda, arzon va kichik hajmdagi, sekin qurilmalar (klaviatura, sichqoncha) uchun mos. Ammo u protsessorni to'liq band qilgani uchun katta hajmdagi ma'lumotlar bilan ishlashda samarasizdir.")
para("• DMA qo'shimcha apparat talab qilsa-da, ma'lumotni protsessor ishtirokisiz to'g'ridan-to'g'ri xotiraga ko'chiradi. Bu protsessorni boshqa vazifalar uchun ozod qiladi va katta hajmdagi ma'lumotlar (disk, tarmoq, video) bilan ishlashda tizim unumdorligini sezilarli oshiradi.")
para("Zamonaviy kompyuterlarda yuqori tezlikdagi qurilmalar (SSD, tarmoq adapterlari, grafik kartalar) deyarli har doim DMA dan foydalanadi, sekin va sodda qurilmalar esa PIO bilan ishlashi mumkin. Demak, ikkala usul ham bir-birini to'ldiradi va tizim loyihalovchisi qurilma turi hamda ma'lumot hajmiga qarab to'g'ri usulni tanlaydi.")
para("")
para("Mustaqil ish · Operatsion tizimlar fani · 2026", italic=True, center=True)

# ----------------- XML GENERATSIYA -----------------
def run(text, bold=False, italic=False, mono=False):
    rpr = "<w:rPr>"
    if bold: rpr += "<w:b/>"
    if italic: rpr += "<w:i/>"
    if mono: rpr += '<w:rFonts w:ascii="Courier New" w:hAnsi="Courier New"/><w:sz w:val="18"/>'
    rpr += "</w:rPr>"
    return '<w:r>%s<w:t xml:space="preserve">%s</w:t></w:r>' % (rpr, esc(text))

body = []
for kind, data in paras:
    if kind.startswith("h"):
        lvl = int(kind[1])
        sz = {1: "30", 2: "26"}.get(lvl, "24")
        body.append('<w:p><w:pPr><w:keepNext/><w:spacing w:before="240" w:after="120"/><w:jc w:val="left"/></w:pPr>'
                    '<w:r><w:rPr><w:b/><w:sz w:val="%s"/></w:rPr><w:t xml:space="preserve">%s</w:t></w:r></w:p>'
                    % (sz, esc(data)))
    elif kind == "p":
        text, bold, italic, center = data
        jc = '<w:jc w:val="center"/>' if center else ""
        body.append('<w:p><w:pPr>%s</w:pPr>%s</w:p>' % (jc, run(text, bold, italic)))
    elif kind == "code":
        runs = []
        lines = data.split("\n")
        for idx, line in enumerate(lines):
            runs.append(run(line, mono=True))
            if idx != len(lines) - 1:
                runs.append('<w:r><w:rPr><w:rFonts w:ascii="Courier New" w:hAnsi="Courier New"/><w:sz w:val="18"/></w:rPr><w:br/></w:r>')
        shd = '<w:shd w:val="clear" w:fill="F2F2F2"/>'
        pbdr = ('<w:pBdr>'
                '<w:top w:val="single" w:sz="4" w:space="4" w:color="B0B0B0"/>'
                '<w:left w:val="single" w:sz="4" w:space="4" w:color="B0B0B0"/>'
                '<w:bottom w:val="single" w:sz="4" w:space="4" w:color="B0B0B0"/>'
                '<w:right w:val="single" w:sz="4" w:space="4" w:color="B0B0B0"/>'
                '</w:pBdr>')
        body.append('<w:p><w:pPr><w:spacing w:after="160" w:line="240" w:lineRule="auto"/>%s%s<w:jc w:val="left"/></w:pPr>%s</w:p>' % (pbdr, shd, "".join(runs)))
    elif kind == "pagebreak":
        body.append('<w:p><w:r><w:br w:type="page"/></w:r></w:p>')
    elif kind == "table":
        rows = data
        tbl = ['<w:tbl><w:tblPr><w:tblW w:w="0" w:type="auto"/>'
               '<w:tblBorders>'
               '<w:top w:val="single" w:sz="4" w:color="000000"/>'
               '<w:left w:val="single" w:sz="4" w:color="000000"/>'
               '<w:bottom w:val="single" w:sz="4" w:color="000000"/>'
               '<w:right w:val="single" w:sz="4" w:color="000000"/>'
               '<w:insideH w:val="single" w:sz="4" w:color="000000"/>'
               '<w:insideV w:val="single" w:sz="4" w:color="000000"/>'
               '</w:tblBorders></w:tblPr>']
        for ri, r in enumerate(rows):
            tbl.append("<w:tr>")
            for c in r:
                fill = ' w:fill="D9E2F3"' if ri == 0 else ' w:fill="FFFFFF"'
                cell = ('<w:tc><w:tcPr><w:shd w:val="clear"%s/><w:tcMar>'
                        '<w:top w:w="40" w:type="dxa"/><w:bottom w:w="40" w:type="dxa"/>'
                        '<w:left w:w="80" w:type="dxa"/><w:right w:w="80" w:type="dxa"/></w:tcMar></w:tcPr>'
                        '<w:p><w:pPr><w:spacing w:after="0" w:line="240" w:lineRule="auto"/><w:jc w:val="left"/></w:pPr>%s</w:p></w:tc>'
                        % (fill, run(c, bold=(ri == 0))))
                tbl.append(cell)
            tbl.append("</w:tr>")
        tbl.append("</w:tbl>")
        body.append("".join(tbl))
        body.append("<w:p/>")

document_xml = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
    '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
    '<w:body>' + "".join(body) +
    '<w:sectPr><w:pgSz w:w="11906" w:h="16838"/>'
    '<w:pgMar w:top="1134" w:right="850" w:bottom="1134" w:left="1701" w:header="708" w:footer="708" w:gutter="0"/>'
    '</w:sectPr></w:body></w:document>'
)

# styles.xml — barcha matn uchun standart Times New Roman 14pt (28 half-points), 1.5 interval
styles_xml = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
    '<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
    '<w:docDefaults><w:rPrDefault><w:rPr>'
    '<w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/>'
    '<w:sz w:val="28"/><w:szCs w:val="28"/><w:lang w:val="en-US"/>'
    '</w:rPr></w:rPrDefault>'
    '<w:pPrDefault><w:pPr>'
    '<w:spacing w:after="120" w:line="360" w:lineRule="auto"/>'
    '<w:jc w:val="both"/>'
    '</w:pPr></w:pPrDefault></w:docDefaults>'
    '<w:style w:type="paragraph" w:default="1" w:styleId="Normal">'
    '<w:name w:val="Normal"/><w:qFormat/></w:style>'
    '</w:styles>')

content_types = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
    '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
    '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
    '<Default Extension="xml" ContentType="application/xml"/>'
    '<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
    '<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>'
    '<Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>'
    '</Types>')

rels = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
    '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
    '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>'
    '<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>'
    '</Relationships>')

doc_rels = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
    '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
    '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>'
    '</Relationships>')

now = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
core = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
    '<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" '
    'xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" '
    'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
    '<dc:title>PIO va DMA o\'rtasidagi farq - Mustaqil ish</dc:title>'
    '<dc:creator>Talaba</dc:creator>'
    '<dcterms:created xsi:type="dcterms:W3CDTF">%s</dcterms:created>'
    '<dcterms:modified xsi:type="dcterms:W3CDTF">%s</dcterms:modified>'
    '</cp:coreProperties>' % (now, now))

out = "PIO_DMA_Mustaqil_ish.docx"
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    z.writestr("[Content_Types].xml", content_types)
    z.writestr("_rels/.rels", rels)
    z.writestr("word/document.xml", document_xml)
    z.writestr("word/_rels/document.xml.rels", doc_rels)
    z.writestr("word/styles.xml", styles_xml)
    z.writestr("docProps/core.xml", core)

print("Yaratildi:", out)
