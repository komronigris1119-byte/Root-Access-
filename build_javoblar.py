# -*- coding: utf-8 -*-
"""Operatsion tizimlar fanidan savollarga javoblar - Word (.docx) generator."""
import zipfile, html

# Har bir element: (raqam, savol, javob)
QA = []

def add(n, q, a):
    QA.append((n, q, a))


add(1, "Operatsion tizim faniga kirish, uning maqsadi va vazifalari.",
"Operatsion tizim (OT) - kompyuter apparat resurslarini boshqaradigan hamda foydalanuvchi va dasturlar uchun ishchi muhitni ta'minlaydigan asosiy tizim dasturidir. Fanning maqsadi - OT ishlash prinsiplari, tuzilishi va boshqaruv mexanizmlarini o'rgatishdir. Asosiy vazifalari: protsessor, xotira, qurilmalar va fayllarni boshqarish, jarayonlarni rejalashtirish, foydalanuvchi interfeysini ta'minlash, resurslarni taqsimlash, xavfsizlik va himoyani ta'minlash hamda apparat bilan dasturlar o'rtasida vositachilik qilishdir.")

add(2, "Operatsion tizim klassifikatsiyasi.",
"Operatsion tizimlar bir necha mezon bo'yicha turlarga ajratiladi. Vazifalar soni bo'yicha: bir vazifali (single-tasking) va ko'p vazifali (multitasking). Foydalanuvchilar soni bo'yicha: bir foydalanuvchili va ko'p foydalanuvchili. Ish rejimi bo'yicha: paketli (batch), vaqtni bo'lish (time-sharing), real vaqt va taqsimlangan tizimlar. Apparat platformasi bo'yicha: server, ish stoli (desktop), mobil va o'rnatilgan (embedded) OT. Masalan, Windows, Linux, macOS, Android, iOS shular jumlasidandir.")

add(3, "BIOS tizimi.",
"BIOS (Basic Input/Output System) - kompyuter ona platasidagi maxsus mikrosxemada saqlanadigan quyi darajadagi dasturiy ta'minot. U kompyuter yoqilganda birinchi bo'lib ishga tushadi va apparat qurilmalarini boshlang'ich sozlash hamda tekshirishni amalga oshiradi. POST (Power-On Self-Test) dasturi qurilmalar (xotira, klaviatura, disklar) soz holatini tekshiradi, so'ngra boshqaruvni operatsion tizim yuklovchisiga uzatadi. Zamonaviy kompyuterlarda BIOS o'rnini ko'proq imkoniyatga ega UEFI egallamoqda.")

add(4, "Operatsion tizim tarkibiy qismlari.",
"OT asosiy tarkibiy qismlari quyidagilar: yadro (kernel) - apparat va resurslarni boshqaruvchi markaziy qism; jarayonlarni boshqarish moduli; xotirani boshqarish moduli; fayl tizimi; qurilmalar drayverlari; kiritish-chiqarish (I/O) tizimi; foydalanuvchi interfeysi (CLI yoki GUI) hamda tizim xizmatlari va utilitalar. Bu qismlar birgalikda apparat resurslarini samarali taqsimlaydi va dasturlarning bajarilishini ta'minlaydi.")

add(5, "Interfeys va uning turlari.",
"Interfeys - foydalanuvchi yoki dastur bilan operatsion tizim o'rtasidagi o'zaro aloqa vositasi. Asosiy turlari: buyruqli interfeys (CLI) - matnli buyruqlar orqali boshqarish (masalan, Linux terminali, cmd); grafik interfeys (GUI) - oyna, tugma, belgi va sichqoncha orqali boshqarish (Windows, macOS); dasturlash interfeysi (API) - dasturlar OT funksiyalaridan foydalanish uchun. CLI tezkor va resurs tejamkor, GUI esa qulay va tushunarli hisoblanadi.")

add(6, "Operatsion tizimlarni qurish asoslari.",
"OT loyihalashda asosiy yondashuvlar: monolit yadro (barcha xizmatlar bitta katta yadroda - Linux), mikroyadro (faqat eng zarur funksiyalar yadroda, qolganlari foydalanuvchi rejimida), qatlamli (layered) tuzilma va gibrid arxitektura (Windows NT, macOS). Loyihalashda modullilik, kengaytiriluvchanlik, xavfsizlik, samaradorlik va portativlik tamoyillariga rioya qilinadi. Windows gibrid yadroga, Linux esa modulli monolit yadroga asoslangan.")

add(7, "EHM arxitekturasi.",
"EHM (Elektron Hisoblash Mashinasi) arxitekturasi - kompyuterning tarkibiy qismlari va ular o'rtasidagi bog'lanishlar tuzilishi. Klassik fon Neyman arxitekturasi protsessor (ALU va boshqaruv qurilmasi), xotira, kiritish-chiqarish qurilmalari va umumiy shinadan iborat bo'lib, dastur va ma'lumotlar bir xotirada saqlanadi. Garvard arxitekturasida esa buyruq va ma'lumotlar xotiralari ajratilgan. Arxitektura kompyuterning tezligi va imkoniyatlarini belgilaydi.")

add(8, "MS Windows arxitekturasi.",
"Windows NT oilasi gibrid yadroli arxitekturaga ega. U ikki rejimga bo'linadi: foydalanuvchi rejimi (user mode) - ilovalar va tizim xizmatlari ishlaydi, va yadro rejimi (kernel mode) - apparatga to'liq kirish bo'ladi. Asosiy komponentlar: HAL (apparat abstraksiya qatlami), yadro, Executive xizmatlari (jarayon, xotira, I/O menejerlari) va kichik tizimlar. Bu tuzilma barqarorlik va xavfsizlikni ta'minlaydi.")

add(9, "MS DOS operatsion tizimi strukturasi.",
"MS DOS - bir vazifali, bir foydalanuvchili matnli operatsion tizim. Tuzilishi quyidagi qatlamlardan iborat: BIOS bilan ishlovchi quyi qatlam (IO.SYS), yadro (MSDOS.SYS) - fayllar va jarayonlarni boshqaradi, hamda buyruq protsessori (COMMAND.COM) - foydalanuvchi buyruqlarini qabul qilib bajaradi. MS DOS FAT fayl tizimidan foydalangan va grafik interfeysga ega bo'lmagan.")

add(10, "Real vaqt rejimidagi operatsion tizimlar.",
"Real vaqt operatsion tizimlari (RTOS) - vazifalarni qat'iy belgilangan vaqt chegarasida bajarishni kafolatlaydigan tizimlar. Ular ikki turga bo'linadi: qattiq real vaqt (hard real-time) - vaqt chegarasini buzish halokatga olib keladi (masalan, samolyot boshqaruvi), va yumshoq real vaqt (soft real-time) - kechikish yo'l qo'yiladi, lekin sifatni pasaytiradi (masalan, video oqim). RTOS sanoat avtomatikasi, tibbiy va harbiy tizimlarda qo'llaniladi.")

add(11, "Operatsion tizimlarda resurs va jarayon tushunchasi.",
"Resurs - jarayonlar foydalanadigan har qanday apparat yoki dasturiy komponent: protsessor vaqti, operativ xotira, disk, qurilmalar, fayllar. Jarayon (process) - bajarilayotgan dastur, ya'ni kodi, ma'lumotlari, xotira sohasi va holatiga ega bo'lgan faol obyekt. OT resurslarni jarayonlar o'rtasida taqsimlaydi va ularning samarali, ziddiyatsiz foydalanishini ta'minlaydi.")

add(12, "Jarayonlar.",
"Jarayon - xotiraga yuklangan va bajarilayotgan dastur nusxasi. Windows operatsion tizimida jarayonlar uch turga bo'linadi: avtomatik ishga tushuvchi (tizim yuklanganda boshlanadigan) jarayonlar, ilova jarayonlari (foydalanuvchi ishga tushiradigan dasturlar) va tizimli jarayonlar (OT xizmatlari). Har bir jarayon o'z xotira sohasi, identifikatori (PID) va resurslariga ega bo'ladi.")

add(13, "Uzilishlarni qayta ishlovchi dasturlar.",
"Uzilish (interrupt) - protsessorga biror hodisaga (qurilma signali, xato, tizim chaqiruvi) e'tibor berishni bildiruvchi signal. Uzilishlarni qayta ishlovchi dasturlar (interrupt handlers) - shu signal kelganda joriy vazifani vaqtincha to'xtatib, kerakli amalni bajaruvchi maxsus dasturlardir. Ular uzilishlar jadvali (vektor) orqali chaqiriladi va bajarilgach, jarayon kaldirilgan joyidan davom etadi.")

add(14, "Semaforalar.",
"Semafora - jarayonlar va oqimlar o'rtasida umumiy resurslardan foydalanishni boshqaruvchi sinxronizatsiya vositasi. U butun son qiymatga ega bo'lib, ikki amal orqali boshqariladi: wait (P) - qiymatni kamaytiradi, signal (V) - oshiradi. Ikkilik (binary) semafora faqat 0 va 1 qiymat oladi (qulf vazifasini bajaradi), sanovchi (counting) semafora esa bir nechta resursni boshqaradi. Semaforalar deadlock va poyga holatining (race condition) oldini olishga yordam beradi.")

add(15, "Operatsion tizimlarda jarayonlarni boshqarish.",
"Jarayonlarni boshqarish - OT ning jarayonlarni yaratish, bajarish, to'xtatish va tugatish funksiyalari majmuasi. OT har bir jarayon uchun jarayon boshqaruv bloki (PCB) yuritadi, unda holat, PID, registr qiymatlari va resurslar saqlanadi. Boshqaruvga jarayonlarni rejalashtirish, holatdan holatga o'tkazish (tayyor, bajarilayotgan, kutayotgan), sinxronlash va o'zaro aloqani tashkil etish kiradi.")

add(16, "Vazifalarni rejalashtirish algoritmi.",
"Rejalashtirish algoritmi - protsessorni qaysi jarayonga, qancha vaqtga berishni belgilaydi. Asosiy algoritmlar: FCFS (kelish tartibida), SJF (eng qisqa vazifa birinchi), Round Robin (vaqt kvantlari bilan navbatma-navbat), ustuvorlik bo'yicha (priority) va ko'p darajali navbat. Algoritm tanlashda protsessordan foydalanish, o'tkazuvchanlik, kutish va javob vaqti ko'rsatkichlari hisobga olinadi.")

add(17, "Operatsion tizimlarda oqim (threads) tushunchasi.",
"Oqim (thread) - jarayon ichidagi eng kichik bajariluvchi birlik. Bir jarayon bir yoki bir necha oqimga ega bo'lishi mumkin; bir jarayon ichidagi oqimlar umumiy xotira va resurslardan foydalanadi. Bir oqimli tizimlarda vazifalar ketma-ket, ko'p oqimli (multithreading) tizimlarda esa parallel bajariladi. Ko'p oqimlilik tizim samaradorligini, ayniqsa ko'p yadroli protsessorlarda oshiradi.")

add(18, "Operatsion tizimlarda deadlock tushunchasi.",
"Deadlock (o'zaro tiqilish) - bir nechta jarayon bir-biri egallagan resurslarni cheksiz kutib qolib, hech biri davom eta olmaydigan holat. U to'rt shart bir vaqtda bajarilganda yuzaga keladi: o'zaro istisno, ushlab turib kutish, oldindan tortib olmaslik va aylanma kutish. Oldini olish uchun resurslarni tartib bilan taqsimlash, bu shartlardan birini buzish yoki deadlockni aniqlab tugatish usullari qo'llaniladi.")

add(19, "Operatsion tizimlarda xotirani boshqarish.",
"Xotirani boshqarish - operativ xotirani jarayonlar o'rtasida taqsimlash, kuzatish va bo'shatish jarayoni. OT har bir jarayonga zarur xotirani ajratadi, ularni bir-biridan himoya qiladi va xotira to'lganda virtual xotira mexanizmidan foydalanadi. Asosiy usullar: bo'limli (partition), sahifali (paging) va segmentli taqsimlash. Maqsad - xotiradan samarali foydalanish va fragmentatsiyani kamaytirishdir.")

add(20, "Xotirani segmentli tashkillash.",
"Segmentatsiya - xotirani mantiqiy bo'laklarga (segmentlarga) - kod, ma'lumotlar, stek kabi - ajratish usuli. Har bir segment o'z nomi va uzunligiga ega bo'lib, manzil segment raqami va segment ichidagi siljish (offset) orqali aniqlanadi. Bu usul dasturning mantiqiy tuzilishiga mos keladi, himoyani va resurslar taqsimlanishini osonlashtiradi, lekin tashqi fragmentatsiyaga olib kelishi mumkin.")


add(21, "Virtual xotira.",
"Virtual xotira - operativ xotira hajmidan ortiq dasturlarni ishga tushirish imkonini beruvchi mexanizm. Bunda diskning bir qismi (svop fayli yoki sahifa fayli) operativ xotira sifatida ishlatiladi. Hozir zarur bo'lmagan ma'lumotlar diskga ko'chiriladi, kerak bo'lganda qaytariladi. Bu mexanizm sahifali tashkil etishga asoslanadi va har bir jarayonga uzluksiz mantiqiy manzil sohasini taqdim etadi, biroq haddan ortiq ishlatilsa, sekinlashish (thrashing) yuz beradi.")

add(22, "Operatsion tizimlarda fayl tizimlari.",
"Fayl tizimi - ma'lumotlarni diskda saqlash, nomlash, tashkil etish va boshqarish usuli. U fayllarni kataloglar (papkalar) bo'yicha tartiblaydi, ularning joylashuvi, hajmi, kirish huquqlari va atributlarini boshqaradi. Fayl tizimi fayllarni yaratish, o'qish, yozish, o'chirish amallarini ta'minlaydi. Misollar: FAT32, NTFS (Windows), ext4 (Linux), APFS (macOS).")

add(23, "FAT, VFAT, FAT32 va NTFS.",
"FAT (File Allocation Table) - oddiy, eski fayl tizimi bo'lib, fayllar joylashuvini jadval orqali boshqaradi; fayl nomlari qisqa (8.3) bo'lgan. VFAT - FATning uzun fayl nomlarini qo'llab-quvvatlovchi kengaytmasi. FAT32 - katta disklar va fayllarni qo'llab-quvvatlaydi, lekin fayl hajmi 4 GB bilan cheklangan. NTFS (Windows) - jurnal yurituvchi, xavfsizlik (kirish huquqlari), shifrlash, siqish va katta hajmlarni qo'llab-quvvatlovchi zamonaviy va ishonchli fayl tizimi.")

add(24, "Virtual (VFS) va tarmoq (NFS) fayl tizimlari.",
"VFS (Virtual File System) - turli fayl tizimlari ustida ishlaydigan abstrakt qatlam bo'lib, dasturlarga fayl tizimi turidan qat'i nazar yagona interfeys orqali ishlash imkonini beradi. NFS (Network File System) - tarmoq orqali masofadagi serverdagi fayllarga xuddi mahalliy fayllardek kirish imkonini beruvchi taqsimlangan fayl tizimi. NFS Unix/Linux tizimlarida fayllarni tarmoq bo'ylab ulashish uchun keng qo'llaniladi.")

add(25, "Kirish/chiqish tizimlarini tashkillashtirish.",
"Kiritish-chiqarish (I/O) tizimi - protsessor bilan tashqi qurilmalar o'rtasida ma'lumot almashinuvini boshqaradi. U qurilma drayverlari, I/O kontrollerlari va buferlar yordamida ishlaydi. Asosiy usullar: dasturiy boshqaruvli I/O (polling), uzilishlar orqali I/O va to'g'ridan-to'g'ri xotiraga kirish (DMA). Buferlash, keshlash va spooling kabi texnikalar I/O samaradorligini oshiradi.")

add(26, "Operatsion tizimlarda tarmoq xavfsizligi.",
"Tarmoq xavfsizligi - tizimni tarmoq orqali keladigan tahdidlardan himoya qilish chora-tadbirlari majmuasi. Bunga tarmoqaro ekran (firewall), shifrlash, autentifikatsiya, kirishni nazorat qilish, VPN, antivirus va hujumlarni aniqlash tizimlari (IDS/IPS) kiradi. OT ushbu mexanizmlar orqali ma'lumotlarning maxfiyligi, yaxlitligi va foydalanuvchanligini ta'minlaydi.")

add(27, "Bulutli hisoblash tushunchasi.",
"Bulutli hisoblash (cloud computing) - hisoblash resurslarini (serverlar, xotira, ma'lumotlar bazasi, dasturlar) internet orqali, talab asosida taqdim etish modeli. Foydalanuvchi resurslarni o'zi sotib olmasdan, ijaraga olib, ishlatganiga qarab to'laydi. Asosiy xizmat modellari: IaaS, PaaS va SaaS. Afzalliklari - moslashuvchanlik, masshtablanish, tejamkorlik va istalgan joydan kirish imkoniyati.")

add(28, "Bulutli hisoblashda xizmatlar, ma'lumotlarni qayta ishlash markazlari.",
"Bulutli hisoblashning uchta asosiy xizmat modeli mavjud: IaaS (infratuzilma xizmat sifatida - virtual serverlar, xotira), PaaS (platforma - dastur ishlab chiqish muhiti) va SaaS (dastur - tayyor ilovalar). Bu xizmatlar ma'lumotlarni qayta ishlash markazlarida (data center) joylashgan bo'lib, ular minglab serverlar, sovutish, elektr ta'minoti va tarmoq tizimlaridan iborat ulkan inshootlardir. Misollar: AWS, Microsoft Azure, Google Cloud.")

add(29, "Bulutli hisoblash uchun operatsion tizimlar va dasturiy vositalar.",
"Bulutli muhitda asosan Linux asosidagi OT (Ubuntu Server, CentOS, Red Hat) keng qo'llaniladi, chunki ular barqaror, xavfsiz va bepul. Virtuallashtirish uchun VMware, Hyper-V, KVM, konteynerlash uchun Docker va boshqarish uchun Kubernetes ishlatiladi. Bundan tashqari OpenStack kabi bulut platformalari va turli orkestratsiya, monitoring vositalari bulutli infratuzilmani boshqarishda muhim o'rin tutadi.")

add(30, "Mobil operatsion tizimlar.",
"Mobil OT - smartfon va planshetlar uchun mo'ljallangan operatsion tizimlar. Eng keng tarqalganlari: Android (Google, Linux yadrosiga asoslangan, ochiq kodli) va iOS (Apple, faqat o'z qurilmalarida). Ular sensorli ekran, energiya tejamkorlik, ilovalar do'koni, simsiz aloqa va sensorlar bilan ishlashga moslashtirilgan. Mobil OT cheklangan resurslarni samarali boshqarishga e'tibor qaratadi.")

add(31, "IBM, HP, Oracle/Sun va boshqa firmalarning operatsion tizimlari.",
"Yirik kompaniyalar o'z server va ish stantsiyalari uchun maxsus OT ishlab chiqqan: IBM - AIX (Unix asosida) va z/OS (mainframe uchun); HP - HP-UX; Oracle/Sun - Solaris (yuqori ishonchli server OT, ZFS fayl tizimi bilan). Bu tizimlar yuqori barqarorlik, masshtablanish va xavfsizlikni talab qiluvchi yirik korporativ va sanoat muhitlarida ishlatiladi.")

add(32, "Operatsion tizimlarda taqsimlangan tizimlar.",
"Taqsimlangan tizim - tarmoq orqali bog'langan bir nechta mustaqil kompyuterlar to'plami bo'lib, foydalanuvchiga yagona yaxlit tizim sifatida ko'rinadi. Ular umumiy vazifani bajarish uchun resurslarni va hisoblashni o'zaro taqsimlaydi. Afzalliklari: resurslarni ulashish, ishonchlilik, masshtablanish va yuqori unumdorlik. Misol: server klasterlari, bulutli tizimlar. Asosiy muammolar - sinxronlash, aloqa va xatolarga chidamlilik.")

add(33, "Operatsion tizimlarda parallel hisoblash tizimlari.",
"Parallel hisoblash - bir masalani bir nechta protsessor yoki yadroda bir vaqtning o'zida qismlarga bo'lib hal qilish. OT bunda vazifalarni yadrolar o'rtasida taqsimlaydi, sinxronlashtiradi va natijalarni birlashtiradi. Bu hisoblash tezligini sezilarli oshiradi. Parallel tizimlar ko'p protsessorli (SMP), klaster va superkompyuterlarda qo'llaniladi va katta hajmdagi ilmiy, muhandislik masalalarini yechishda muhim.")

add(34, "Operatsion tizimlarda masofadan resurslarni boshqarish.",
"Masofadan boshqarish - tarmoq orqali boshqa kompyuter resurslari va xizmatlarini boshqarish imkoniyati. Buning uchun SSH (xavfsiz terminal), RDP (Windows masofaviy ish stoli), Telnet, VNC kabi protokol va vositalar ishlatiladi. Ular administratorlarga serverlarni masofadan sozlash, kuzatish va xizmat ko'rsatish imkonini beradi. Xavfsizlik uchun shifrlash va autentifikatsiya majburiy hisoblanadi.")

add(35, "Operatsion tizimlarda xavfsizlik.",
"OT xavfsizligi - tizim resurslari va ma'lumotlarini ruxsatsiz kirish, o'zgartirish va yo'qotishdan himoya qilish. Asosiy mexanizmlar: autentifikatsiya (parol, biometriya), avtorizatsiya (kirish huquqlari), shifrlash, audit va loglarni yuritish, antivirus va yangilanishlar. Xavfsizlik maxfiylik, yaxlitlik va foydalanuvchanlik (CIA) tamoyillariga asoslanadi.")

add(36, "Operatsion tizimlarda umumiy ruxsat va foydalanuvchi huquqlarini sozlash.",
"OT da har bir fayl va resursga kirish huquqlari belgilanadi. Linuxda fayllarga uch toifa (egasi, guruh, boshqalar) uchun o'qish (r), yozish (w) va bajarish (x) huquqlari beriladi (chmod, chown). Windowsda esa ACL (kirish nazorati ro'yxatlari) orqali har bir foydalanuvchi yoki guruhga aniq ruxsatlar tayinlanadi. Bu mexanizm ma'lumotlarni himoya qiladi va resurslardan birgalikda xavfsiz foydalanishni ta'minlaydi.")

add(37, "Operatsion tizimlarda samaradorlik monitoringi.",
"Samaradorlik monitoringi - tizim resurslaridan (protsessor, xotira, disk, tarmoq) foydalanishni kuzatish va tahlil qilish. Bu orqali tizimning ishlashidagi muammolar, ortiqcha yuklanish va to'siqlar (bottleneck) aniqlanadi. Windowsda Task Manager va Performance Monitor, Linuxda top, htop, vmstat, iostat kabi vositalar ishlatiladi. Monitoring tizim optimallashtirish va nosozliklarni bartaraf etishga yordam beradi.")

add(38, "Operatsion tizimlarda xizmatchi ilova dasturlari.",
"Xizmatchi (utilita) dasturlar - tizimni sozlash, xizmat ko'rsatish va boshqarishga yordam beruvchi maxsus dasturlardir. Misollar: disk tozalash va defragmentatsiya, arxivatorlar, antivirus, zaxira nusxa olish, fayl menejerlari, tizim diagnostikasi va drayver yangilash vositalari. Ular OT funksiyalarini to'ldiradi va tizim barqarorligi hamda samaradorligini saqlashga xizmat qiladi.")

add(39, "Linux operatsion tizimi terminali.",
"Terminal - Linuxda matnli buyruqlar orqali tizimni boshqarish vositasi (buyruq qatori interfeysi). U bash kabi qobiq (shell) orqali ishlaydi. Asosiy buyruqlar: ls (fayllar ro'yxati), cd (katalog o'zgartirish), mkdir, rm, cp, mv, cat, grep, chmod, sudo va boshqalar. Terminal grafik interfeysga nisbatan tezkor, resurs tejamkor va avtomatlashtirish (skriptlar) uchun juda qulay.")

add(40, "MS Windows operatsion tizimida ota-ona nazorati xizmati.",
"Ota-ona nazorati (Parental Control) - bolalarning kompyuterdan foydalanishini nazorat qilish va cheklash imkonini beruvchi xizmat. U orqali ekran vaqtini chegaralash, ma'lum ilovalar va o'yinlarni cheklash, nomaqbul veb-saytlarni bloklash va faoliyat hisobotlarini olish mumkin. Windowsda bu Microsoft Family Safety hisob yozuvi orqali boshqariladi va bolalar xavfsizligini ta'minlaydi.")


add(41, "O'rnatilgan operatsion tizimlar.",
"O'rnatilgan (embedded) OT - muayyan apparat ichiga joylashtirilgan, aniq vazifani bajarishga moslashtirilgan ixcham operatsion tizimlar. Ular maishiy texnika, avtomobil, sanoat boshqaruvi, marshrutizator va IoT qurilmalarida ishlatiladi. Kam resurs talab qiladi, ko'pincha real vaqt rejimida ishlaydi va yuqori ishonchlilikka ega. Misollar: Embedded Linux, FreeRTOS, VxWorks.")

add(42, "Operatsion tizimlarda ma'lumotlarni kiritish-chiqarishni boshqarish.",
"Kiritish-chiqarishni boshqarish - foydalanuvchi va qurilmalar bilan ma'lumot almashinuvini tashkil etish. OT bunda qurilma drayverlari orqali apparatni boshqaradi, buferlash va keshlashdan foydalanadi hamda I/O so'rovlarini navbatga qo'yib rejalashtiradi. DMA mexanizmi protsessorni yuklamasdan ma'lumotni to'g'ridan-to'g'ri xotiraga uzatadi. Bu samaradorlikni oshiradi va qurilmalarning bir tekis ishlashini ta'minlaydi.")

add(43, "Multidasturlash va multiprotsessorlash.",
"Multidasturlash (multiprogramming) - bir protsessorda bir nechta dasturni xotirada saqlab, biri kutganda boshqasini bajarish orqali protsessordan to'liq foydalanish. Multiprotsessorlash (multiprocessing) esa bir nechta fizik protsessor yoki yadrodan foydalanib, vazifalarni haqiqatda parallel bajarishdir. Birinchisi resurslardan samarali foydalanishni, ikkinchisi esa unumdorlik va tezlikni oshiradi.")

add(44, "Operatsion tizimlarning jarayonlari boshqaruvi.",
"Jarayon boshqaruvi - jarayonlarni yaratish, rejalashtirish, holatini o'zgartirish, sinxronlash va tugatishni o'z ichiga oladi. OT har bir jarayon uchun PCB (jarayon boshqaruv bloki) yuritadi va ularni navbatlar orqali boshqaradi. Jarayonlar holatlari: yangi, tayyor, bajarilayotgan, kutayotgan va tugagan. Boshqaruv protsessordan adolatli va samarali foydalanishni ta'minlaydi.")

add(45, "Jarayonlar boshqaruvini rejalashtirish parametrlari va rivojlantirish ko'rsatkichlari.",
"Rejalashtirish samaradorligi quyidagi ko'rsatkichlar bilan baholanadi: protsessordan foydalanish darajasi (CPU utilization), o'tkazuvchanlik (throughput - vaqt birligida tugatilgan jarayonlar soni), aylanma vaqt (turnaround time), kutish vaqti (waiting time) va javob vaqti (response time). Yaxshi algoritm protsessordan foydalanishni va o'tkazuvchanlikni oshirib, kutish hamda javob vaqtini kamaytirishga intiladi.")

add(46, "Zamonaviy operatsion tizimlar ilovalari.",
"Zamonaviy OT keng ko'lamli ilovalarni qo'llab-quvvatlaydi: ofis dasturlari, brauzerlar, multimedia, o'yinlar, ishlab chiqish muhitlari, ma'lumotlar bazalari va bulutli xizmatlar. Ular ko'p oqimlilik, grafik tezlatish, tarmoq va xavfsizlikni ta'minlaydi. Ilovalar API va kutubxonalar orqali OT xizmatlaridan foydalanadi, bu esa dasturlarning portativligi va imkoniyatlarini kengaytiradi.")

add(47, "Operatsion tizimlarda hisoblash jarayoni.",
"Hisoblash jarayoni - dasturning bajarilishi davomida protsessor, xotira va resurslardan foydalangan holda amallar ketma-ketligini bajarish. OT bu jarayonni boshqaradi: kodni xotiraga yuklaydi, protsessor vaqtini ajratadi, kerakli ma'lumotlarni ta'minlaydi va natijani chiqaradi. Hisoblash jarayoni protsessorga yo'naltirilgan (CPU-bound) yoki kiritish-chiqarishga yo'naltirilgan (I/O-bound) bo'lishi mumkin.")

add(48, "Multidasturlash. Ajratilgan vaqt tizimlarida ko'p foydalanuvchi rejimi.",
"Vaqtni bo'lish (time-sharing) tizimlarida protsessor vaqti kichik bo'laklarga (kvant) bo'linadi va navbatma-navbat har bir foydalanuvchi jarayoniga beriladi. Tez almashish tufayli har bir foydalanuvchiga tizim faqat unga xizmat qilayotgandek tuyuladi. Bu multidasturlashga asoslanib, ko'p foydalanuvchining bir vaqtda interaktiv ishlashini ta'minlaydi va resurslardan samarali foydalanadi.")

add(49, "Jarayon holati diagrammasi va jarayon deskriptori.",
"Jarayon holati diagrammasi jarayonning hayot davridagi holatlarini va ular orasidagi o'tishlarni ko'rsatadi: yangi -> tayyor -> bajarilayotgan -> kutayotgan -> tugagan. Jarayon deskriptori (PCB) esa jarayon haqidagi barcha ma'lumotlarni saqlovchi tuzilma: PID, holat, protsessor registrlari, ustuvorlik, xotira chegaralari, ochilgan fayllar va resurslar ro'yxati. OT bu ma'lumotlar yordamida jarayonni boshqaradi.")

add(50, "Jarayon va topshiriqlarni rejalashtirish va dispetcherlash.",
"Rejalashtiruvchi (scheduler) qaysi jarayonni keyingi navbatda bajarishni tanlaydi, dispetcher (dispatcher) esa shu tanlangan jarayonga protsessorni haqiqatda topshiradi - kontekst almashtirishni amalga oshiradi. Rejalashtirish uzoq, o'rta va qisqa muddatli bo'ladi. Dispetcher tezligi (dispatch latency) tizim samaradorligiga ta'sir qiladi. Birgalikda ular protsessordan adolatli va unumli foydalanishni ta'minlaydi.")

add(51, "Operatsion tizimlar qanday ishlaydi va asosiy vazifalari.",
"OT kompyuter yoqilganda yuklanadi va apparat bilan dasturlar o'rtasida vositachilik qiladi. U tizim chaqiruvlari (system calls) orqali dasturlarga xizmat ko'rsatadi. Asosiy vazifalari: protsessor va jarayonlarni boshqarish, xotirani taqsimlash, fayl tizimini yuritish, qurilmalarni boshqarish, kiritish-chiqarishni tashkil etish, xavfsizlik va foydalanuvchi interfeysini ta'minlash. OT bu vazifalarni yadro orqali muvofiqlashtiradi.")

add(52, "Operatsion tizimlarda fayl tizimi.",
"Fayl tizimi - ma'lumotlarni saqlash qurilmalarida tartibli joylashtirish, nomlash va boshqarish usuli. U fayllar va kataloglar ierarxiyasini, metama'lumotlarni (hajm, sana, huquqlar) va bo'sh joyni boshqaradi. Fayl tizimi fayllarni yaratish, o'qish, yozish, o'chirish hamda himoya qilish imkonini beradi. Jurnal yurituvchi fayl tizimlari (NTFS, ext4) nosozlikdan keyin ma'lumotlarni tiklashga yordam beradi.")

add(53, "Real vaqt operatsion tizimlari va ularning afzalliklari.",
"Real vaqt OT (RTOS) vazifalarni qat'iy belgilangan vaqt chegarasida bajaradi. Afzalliklari: kafolatlangan va oldindan bashorat qilinadigan javob vaqti, yuqori ishonchlilik, ustuvorlikka asoslangan rejalashtirish va resurslardan samarali foydalanish. Shu sababli ular tibbiyot uskunalari, avtomobil, aviatsiya, sanoat avtomatikasi va robototexnikada qo'llaniladi, bu yerda har bir millisekund muhim ahamiyatga ega.")

add(54, "Operatsion tizimlarda tizim resurslarini boshqarish.",
"Tizim resurslarini boshqarish - protsessor, xotira, disk, qurilmalar va tarmoqdan jarayonlar o'rtasida adolatli va samarali foydalanishni tashkil etish. OT resurslarni ajratadi, kuzatadi, ziddiyatlarning oldini oladi va resurs bo'shaganda qaytadan taqsimlaydi. Maqsad - resurslardan maksimal foydalanish, kutishni kamaytirish va tizim barqarorligini ta'minlashdir.")

add(55, "Jarayonlarni boshqarishda operatsion tizim tomonidan qo'llaniladigan asosiy algoritmlar.",
"Jarayonlarni boshqarishda OT turli rejalashtirish algoritmlaridan foydalanadi: FCFS (kelish tartibida), SJF (eng qisqa vazifa birinchi), Round Robin (vaqt kvantli navbat), ustuvorlik bo'yicha (priority scheduling) va ko'p darajali navbat (multilevel queue). Har bir algoritm protsessor vaqtini taqsimlash, kutishni kamaytirish va adolatlilikni ta'minlash maqsadida muayyan vaziyatlarda qo'llaniladi.")

add(56, "Operatsion tizimlarda xotira boshqarish tizimlari qanday ishlaydi?",
"Xotira boshqaruvi jarayonlarga xotira ajratish, ularni himoya qilish va bo'shatishni amalga oshiradi. OT sahifalash (paging) orqali xotirani teng bo'laklarga bo'ladi va virtual manzillarni fizik manzillarga aylantiradi (MMU yordamida). Xotira to'lganda kam ishlatilgan sahifalar diskka ko'chiriladi. Keshlash va virtual xotira tizim samaradorligini oshiradi va resurslardan oqilona foydalanishni ta'minlaydi.")

add(57, "Fayl tizimini optimallashtirish choralari.",
"Fayl tizimi samaradorligini oshirish uchun: defragmentatsiya (fayl bo'laklarini birlashtirish), keshlash va buferlash, indekslash, ma'lumotlarni siqish, ortiqcha fayllarni tozalash va SSD uchun TRIM qo'llash kabi choralar ko'riladi. Bundan tashqari to'g'ri klaster o'lchamini tanlash va jurnal yuritish ham ishlashni yaxshilaydi. Bu choralar fayllarga kirish tezligini oshirib, disk bandligini kamaytiradi.")

add(58, "Tarmoq xavfsizligi va uning operatsion tizimlarda qo'llanilishi.",
"OT tarmoq xavfsizligini ta'minlash uchun tarmoqaro ekran (firewall), shifrlash protokollari (SSL/TLS), autentifikatsiya, kirish nazorati va antivirus vositalaridan foydalanadi. Tarmoq portlari nazorat qilinadi, ruxsatsiz ulanishlar bloklanadi va ma'lumotlar shifrlanib uzatiladi. Bu mexanizmlar ma'lumotlarni o'g'irlash, hujum va viruslardan himoya qilib, tizim yaxlitligini saqlaydi.")

add(59, "Operatsion tizimlarda ko'p foydalanuvchi rejimi qanday ishlaydi?",
"Ko'p foydalanuvchi rejimida OT bir vaqtning o'zida bir nechta foydalanuvchiga xizmat ko'rsatadi. Har bir foydalanuvchining alohida hisob yozuvi, fayllari va huquqlari bo'ladi. Tizim resurslarni (protsessor vaqti, xotira) ular o'rtasida vaqtni bo'lish orqali taqsimlaydi va foydalanuvchilarni bir-biridan himoya qiladi. Linux va serverlar OT bu rejimga to'liq moslashgan.")

add(60, "Linux operatsion tizimining asosiy xususiyatlari.",
"Linux - ochiq kodli, bepul va Unixga o'xshash operatsion tizim. Asosiy xususiyatlari: barqarorlik va ishonchlilik, ko'p foydalanuvchili va ko'p vazifali ishlash, yuqori xavfsizlik, kuchli terminal va skriptlash imkoniyatlari, turli apparatlarga moslashuvchanlik hamda katta hamjamiyat tomonidan qo'llab-quvvatlanishi. U serverlar, superkompyuterlar, mobil qurilmalar (Android) va o'rnatilgan tizimlarda keng qo'llaniladi.")


add(61, "MS Windows operatsion tizimi va uning tarkibiy qismlari.",
"Windows - Microsoft tomonidan ishlab chiqilgan, grafik interfeysli keng tarqalgan OT. Tarkibiy qismlari: yadro (kernel) va HAL, Executive xizmatlari (jarayon, xotira, I/O menejerlari), fayl tizimi (NTFS), registr (sozlamalar bazasi), grafik kichik tizim (GDI), foydalanuvchi interfeysi (Explorer), drayverlar va tizim xizmatlari. Bu qismlar birgalikda apparat va dasturlarni boshqaradi.")

add(62, "Operatsion tizimlarda jarayonlar va vazifalarni boshqarish.",
"OT jarayonlar va vazifalarni yaratish, rejalashtirish, ustuvorlik berish, sinxronlash va tugatish orqali boshqaradi. Vazifalar navbatlarga joylashtiriladi va rejalashtirish algoritmlari yordamida protsessorga taqsimlanadi. Ko'p vazifali muhitda OT vazifalar o'rtasida tez almashadi (kontekst almashtirish). Bu protsessordan samarali foydalanish va tizim javobgarligini oshirishni ta'minlaydi.")

add(63, "Operatsion tizimda virtual xotira va uning ishlashi.",
"Virtual xotira fizik xotiradan kattaroq mantiqiy manzil sohasini yaratadi. Har bir jarayon o'zining uzluksiz virtual manziliga ega bo'ladi, MMU esa virtual manzillarni fizik manzillarga aylantiradi. Hozir kerak bo'lmagan sahifalar diskdagi sahifa fayliga ko'chiriladi (swapping), kerak bo'lganda qaytariladi (page fault orqali). Bu mexanizm kichik fizik xotirada ko'proq dasturlarni ishlatish imkonini beradi.")

add(64, "Operatsion tizimda jarayonlarning sinxronizatsiyasi.",
"Jarayonlar sinxronizatsiyasi - bir nechta jarayon umumiy resursdan foydalanganda ularning tartibli va ziddiyatsiz ishlashini ta'minlash. Buning uchun semaforalar, mutekslar, monitorlar va kritik bo'lim (critical section) mexanizmlari ishlatiladi. Sinxronizatsiya poyga holati (race condition) va ma'lumotlar buzilishining oldini oladi, jarayonlar o'rtasida to'g'ri muvofiqlashtirishni kafolatlaydi.")

add(65, "Tarmoqdagi resurslarni boshqarishning samarali usullari.",
"Tarmoq resurslarini samarali boshqarish uchun: yuk muvozanatlash (load balancing), o'tkazuvchanlikni boshqarish (QoS), keshlash, resurslarni navbatga qo'yish, monitoring va virtuallashtirish usullari qo'llaniladi. Bu resurslardan adolatli foydalanishni, kechikishlarni kamaytirishni va tarmoq barqarorligini ta'minlaydi. Markazlashtirilgan boshqaruv va avtomatlashtirish katta tarmoqlarda samaradorlikni oshiradi.")

add(66, "Operatsion tizimda ko'p oqim (multithreading) ishlashi va afzalliklari.",
"Ko'p oqimlilik bir jarayon ichida bir nechta oqimni parallel bajarish imkonini beradi. Oqimlar umumiy xotira va resurslardan foydalangani uchun ular o'rtasida almashish jarayonlarga nisbatan tez va arzon. Afzalliklari: ko'p yadroli protsessorlardan to'liq foydalanish, dastur javobgarligini oshirish, resurslarni tejash va vazifalarni parallel bajarib tezlikni oshirish. Masalan, brauzerda bir oqim sahifani yuklaydi, boshqasi foydalanuvchi bilan ishlaydi.")

add(67, "O'rnatilgan tizimlar va ularning operatsion tizimlar bilan aloqasi.",
"O'rnatilgan tizimlar - muayyan vazifaga ixtisoslashgan kompyuter tizimlari (mikrokontrollerlar, IoT qurilmalari). Ularda ixcham, kam resurs talab qiluvchi va ko'pincha real vaqt OT (RTOS, embedded Linux) ishlaydi. OT bu tizimlarda apparatni boshqaradi, vazifalarni rejalashtiradi va ishonchli ishlashni ta'minlaydi. Maishiy texnika, avtomobil va sanoat qurilmalari shularga misol.")

add(68, "Operatsion tizimlarda xatoliklarni aniqlash va tuzatish usullari.",
"OT xatoliklarni aniqlash uchun loglar yuritadi, holatni kuzatadi va tekshiruvlar o'tkazadi. Usullar: istisnolarni qayta ishlash (exception handling), nazorat summalari (checksum) va xatolarni tuzatuvchi kodlar (ECC), zaxira nusxa va tiklash, jurnal yuritish (journaling), shuningdek dampe tahlili. Bu mexanizmlar nosozliklarni o'z vaqtida aniqlab, tizim barqarorligi va ma'lumotlar yaxlitligini saqlaydi.")

add(69, "Operatsion tizimlarda resurslarni samarali taqsimlash xususiyatlari.",
"Resurslarni samarali taqsimlash - resurslarni jarayonlar ehtiyojiga qarab adolatli va unumli ulashish. Bunda ustuvorlik, navbatlar, kvotalar va rejalashtirish algoritmlari ishlatiladi. Muhim xususiyatlar: adolatlilik, yuqori foydalanish darajasi, deadlockning oldini olish, javob vaqtini kamaytirish va ochlik (starvation) holatiga yo'l qo'ymaslik. Bu tizim umumiy samaradorligini oshiradi.")

add(70, "Operatsion tizimlarda tarmoqni tashkil etish va boshqarish.",
"OT tarmoqni tashkil etish uchun tarmoq protokollari (TCP/IP) stekini, drayverlar va xizmatlarni qo'llab-quvvatlaydi. U IP-manzil, marshrutlash, portlar va ulanishlarni boshqaradi, ma'lumot paketlarini yuborish va qabul qilishni ta'minlaydi. Tarmoq sozlamalari, xavfsizlik (firewall) va monitoring orqali tarmoqdan barqaror va xavfsiz foydalanish tashkil etiladi.")

add(71, "Operatsion tizimlarda fayl tizimi turlari va afzalliklari.",
"Asosiy fayl tizimlari: FAT32 - oddiy, mos keluvchanligi yuqori, lekin 4 GB cheklov; NTFS - xavfsizlik, jurnal yuritish, katta hajm (Windows); ext4 - barqaror, tez, jurnalli (Linux); APFS - Apple zamonaviy tizimi (SSD uchun optimal); exFAT - katta fayllar uchun flesh xotiralarga mos. Har birining afzalligi maqsadga bog'liq: xavfsizlik, tezlik, mos keluvchanlik yoki katta hajmni qo'llab-quvvatlash.")

add(72, "Operatsion tizimda tizimli jarayonlarni boshqarish.",
"Tizimli jarayonlar - OT xizmatlarini bajaruvchi orqa fon (background) jarayonlari (Windowsda services, Linuxda demonlar). Ular tizim yuklanganda avtomatik ishga tushadi va tarmoq, chop etish, xavfsizlik kabi xizmatlarni ta'minlaydi. OT bu jarayonlarni yuqori ustuvorlik bilan boshqaradi, kuzatadi va kerak bo'lganda qayta ishga tushiradi, bu esa tizim barqarorligini ta'minlaydi.")

add(73, "Operatsion tizimda xotirani segmentlash va afzalliklari.",
"Segmentlash xotirani dasturning mantiqiy qismlariga (kod, ma'lumotlar, stek) mos segmentlarga ajratadi. Har bir segment alohida boshqariladi va himoyalanadi. Afzalliklari: dasturning mantiqiy tuzilishiga moslik, himoyaning osonligi, kod va ma'lumotlarni birgalikda ulashish imkoniyati, modullashtirish. Sahifalash bilan birgalikda (segmentli-sahifali) qo'llanilsa, fragmentatsiya muammosi kamayadi.")

add(74, "Operatsion tizimlarda fayllarni himoya qilish usullari.",
"Fayllarni himoya qilish usullari: kirish huquqlari (o'qish, yozish, bajarish), ACL (kirish nazorati ro'yxatlari), shifrlash (EFS, BitLocker), parol qo'yish, zaxira nusxa olish va audit yuritish. OT foydalanuvchi va guruhlarga aniq ruxsatlar belgilab, ma'lumotlarni ruxsatsiz kirish, o'zgartirish yoki yo'qotishdan himoya qiladi va maxfiylikni ta'minlaydi.")

add(75, "Foydalanuvchi huquqlarini boshqarish va sozlash.",
"Foydalanuvchi huquqlarini boshqarish - har bir foydalanuvchi yoki guruhga tizim resurslariga kirish darajasini belgilash. OT da administrator va oddiy foydalanuvchi hisoblar ajratiladi. Linuxda chmod, chown, sudo, Windowsda esa guruh siyosatlari va ACL ishlatiladi. Eng kam imtiyoz tamoyili (least privilege) bo'yicha foydalanuvchiga faqat zarur huquqlar beriladi, bu xavfsizlikni oshiradi.")

add(76, "Operatsion tizimlarda jarayonlar orasida aloqalarni tashkil etilishi.",
"Jarayonlararo aloqa (IPC - Inter-Process Communication) jarayonlarga ma'lumot almashish va muvofiqlashish imkonini beradi. Asosiy usullar: umumiy xotira (shared memory), xabarlar uzatish (message passing), quvurlar (pipes), navbatlar (message queues), soketlar va signallar. IPC taqsimlangan va parallel ishlovchi jarayonlarning hamkorligini ta'minlaydi va sinxronizatsiya bilan birga ishlatiladi.")

add(77, "Optimal rejalashtirish algoritmlarini ishlab chiqish usullari.",
"Optimal rejalashtirish algoritmini ishlab chiqishda tizim maqsadlari (o'tkazuvchanlik, javob vaqti, adolatlilik) hisobga olinadi. Usullar: vazifa turini tahlil qilish (CPU yoki I/O bound), ustuvorlik va vaqt kvantlarini sozlash, gibrid (ko'p darajali fikrli) navbatlardan foydalanish hamda simulyatsiya va statistik tahlil orqali algoritmni baholash. Maqsad - resurslardan maksimal foydalanib, kutishni minimallashtirish.")

add(78, "Virtual mashinalarda operatsion tizimlar va ularning ahamiyati.",
"Virtual mashina (VM) - bitta fizik kompyuterda bir nechta mustaqil OT ishlatish imkonini beruvchi dasturiy emulyatsiya. Gipervizor (VMware, VirtualBox, Hyper-V, KVM) resurslarni virtual mashinalar o'rtasida taqsimlaydi. Ahamiyati: resurslardan samarali foydalanish, izolyatsiya va xavfsizlik, test va ishlab chiqish qulayligi, bulutli xizmatlar uchun asos hamda turli OT ni bitta apparatda ishlatish.")

add(79, "Operatsion tizimda xatoliklarni boshqarishning asosiy yondashuvlari.",
"Xatoliklarni boshqarish yondashuvlari: oldini olish (yaxshi loyihalash, tekshirish), aniqlash (monitoring, loglar, istisnolar), tiklash (zaxira, qayta ishga tushirish, tranzaksiyalarni bekor qilish) va izolyatsiya (xatoli komponentni ajratish). OT istisnolarni qayta ishlash mexanizmi orqali xatolarni ushlab, tizim ishini to'xtatmasdan davom ettiradi va barqarorlikni saqlaydi.")

add(80, "Operatsion tizimlarda faylni o'zgartirish va arxivlash imkoniyatlari.",
"OT fayllarni yaratish, tahrirlash, nusxalash, ko'chirish va o'chirish imkonini beradi. Arxivlash - fayllarni siqib, bitta arxiv faylga jamlash (ZIP, RAR, tar.gz). Bu disk joyini tejaydi, fayllarni uzatish va saqlashni osonlashtiradi. Zaxira nusxa olish (backup) esa muhim ma'lumotlarni yo'qotishdan himoya qiladi. OT bu funksiyalarni o'rnatilgan vositalar va utilitalar orqali taqdim etadi.")


add(81, "Operatsion tizimlarda samarali ko'p jarayonli boshqaruv.",
"Ko'p jarayonli boshqaruv bir vaqtning o'zida ko'plab jarayonlarni samarali bajarishni tashkil etadi. Buning uchun OT yuk muvozanatlash, ustuvorlikka asoslangan rejalashtirish, resurslarni adolatli taqsimlash va kontekst almashtirishni optimallashtiradi. Ko'p yadroli protsessorlarda jarayonlar yadrolar bo'ylab taqsimlanadi. Bu unumdorlikni oshiradi, kutishni kamaytiradi va tizimning bir tekis ishlashini ta'minlaydi.")

add(82, "Operatsion tizimlarda uzilishlarni qayta ishlash.",
"Uzilishlarni qayta ishlash - apparat yoki dasturdan kelgan signalga javoban joriy ishni to'xtatib, maxsus dasturni (handler) bajarish. Uzilish kelganda protsessor joriy holatni saqlaydi, uzilish vektori orqali tegishli ishlovchini chaqiradi, amalni bajaradi va so'ng to'xtatilgan jarayonni davom ettiradi. Uzilishlar ustuvorlikka ega bo'ladi va tizimning hodisalarga tez javob berishini ta'minlaydi.")

add(83, "Operatsion tizimda I/O qurilmalari bilan ishlash.",
"OT I/O qurilmalari bilan qurilma drayverlari orqali ishlaydi - har bir qurilma uchun maxsus dastur uning tilini biladi. OT qurilmalarni belgili (character), blokli (block) va tarmoq qurilmalariga ajratadi. Ishlash usullari: polling, uzilishlar va DMA. Buferlash, keshlash va spooling I/O ni tezlashtiradi. Bu mexanizmlar dasturlarga qurilmalardan yagona, soddalashtirilgan interfeys orqali foydalanish imkonini beradi.")

add(84, "Operatsion tizimda semaforlar ishlashi va afzalliklari.",
"Semafor - umumiy resursdan foydalanishni boshqaruvchi butun sonli o'zgaruvchi. wait (P) amali resursni egallaganda qiymatni kamaytiradi, signal (V) bo'shatganda oshiradi. Qiymat 0 bo'lsa, jarayon kutadi. Afzalliklari: poyga holatining oldini olish, resurslardan tartibli foydalanish, jarayonlarni sinxronlash va deadlockni kamaytirish. Semaforlar ko'p oqimli va ko'p jarayonli muhitda muhim ahamiyatga ega.")

add(85, "Operatsion tizimlarda tarmoq xavfsizligini ta'minlash usullari.",
"Tarmoq xavfsizligini ta'minlash usullari: tarmoqaro ekran (firewall), ma'lumotlarni shifrlash (TLS/SSL, VPN), kuchli autentifikatsiya (ko'p faktorli), kirishni nazorat qilish, hujumlarni aniqlash tizimlari (IDS/IPS), muntazam yangilanishlar va antivirus. Shuningdek tarmoqni segmentlash va monitoring qo'llaniladi. Bu choralar ma'lumotlarning maxfiyligi, yaxlitligi va xizmatning uzluksizligini himoya qiladi.")

add(86, "Operatsion tizimlarda ko'p oqimli dasturlash va parallel ishlash.",
"Ko'p oqimli dasturlash bir dasturda bir nechta oqimni yaratib, ularni parallel bajarishni ko'zda tutadi. Ko'p yadroli protsessorlarda oqimlar turli yadrolarda haqiqatda bir vaqtda ishlaydi, bu unumdorlikni oshiradi. Parallel ishlashda masala qismlarga bo'linib, bir vaqtda hisoblanadi. Bunda sinxronizatsiya va resurslar nazorati muhim, aks holda poyga holati va deadlock yuzaga kelishi mumkin.")

add(87, "Operatsion tizimlarda fayl tizimi strukturasini tashkil etish.",
"Fayl tizimi strukturasi odatda ierarxik - kataloglar daraxti ko'rinishida tashkil etiladi. U yuklash bloki, superblok (fayl tizimi haqida ma'lumot), inode jadvali (fayl metama'lumotlari) va ma'lumot bloklaridan iborat. Kataloglar fayllarni mantiqiy guruhlaydi, FAT yoki inode esa fayl bloklarining diskdagi joylashuvini kuzatadi. Bu struktura fayllarga tez va tartibli kirishni ta'minlaydi.")

add(88, "Operatsion tizimda jarayonlar orasidagi o'zaro ta'sirni boshqarish.",
"Jarayonlar o'zaro ta'siri IPC mexanizmlari (umumiy xotira, xabar uzatish, quvurlar, soketlar) orqali boshqariladi. OT bu aloqani tartibga soladi, sinxronizatsiya vositalari (semafor, muteks) bilan ziddiyatlarning oldini oladi. To'g'ri boshqaruv jarayonlarning hamkorlik qilishini, ma'lumotlarni xavfsiz almashishini va deadlocksiz, izchil ishlashini ta'minlaydi.")

add(89, "Operatsion tizimlarda tizimli resurslarni boshqarishning asosiy usullari.",
"Tizimli resurslarni boshqarish usullari: rejalashtirish (protsessor vaqti), xotira taqsimlash (sahifalash, segmentlash), resurslarni navbatga qo'yish, kvotalar belgilash, ustuvorlik berish va monitoring. OT resurslarni ajratadi, foydalanishni kuzatadi, ziddiyatlarni hal qiladi va bo'shaganda qaytadan taqsimlaydi. Maqsad - resurslardan adolatli, samarali foydalanish va deadlockning oldini olishdir.")

add(90, "Jarayonlar va fayllar bilan ishlashning asosiy yondashuvlari.",
"Jarayonlar bilan ishlashda OT ularni yaratadi, rejalashtiradi, sinxronlaydi va tugatadi (fork, exec kabi tizim chaqiruvlari). Fayllar bilan ishlashda esa ochish, o'qish, yozish, yopish va kirish huquqlarini boshqarish amallari bajariladi. Ikkala holatda ham OT tizim chaqiruvlari orqali dasturlarga xizmat ko'rsatadi, resurslarni himoya qiladi va ularning izchil, xavfsiz boshqarilishini ta'minlaydi.")

add(91, "Operatsion tizimda tarmoq orqali ma'lumot almashish protokollari.",
"Tarmoq protokollari - ma'lumot almashish qoidalari to'plami. Asosiy protokollar: TCP (ishonchli, ulanishga asoslangan uzatish), UDP (tez, lekin ishonchsiz), IP (manzillash va marshrutlash), HTTP/HTTPS (veb), FTP (fayl uzatish), SMTP (elektron pochta), DNS (nom yechimi). OT ushbu protokollarni TCP/IP steki orqali qo'llab-quvvatlaydi va xavfsizlik uchun shifrlangan variantlardan (HTTPS, TLS) foydalanadi.")

add(92, "Operatsion tizimlar va ularning arxitekturasi.",
"OT arxitekturasi uning ichki tuzilishi va komponentlari tashkil etilish usulini bildiradi. Asosiy turlari: monolit (barcha xizmatlar bitta yadroda - Linux), mikroyadro (minimal yadro, qolgan xizmatlar foydalanuvchi rejimida), qatlamli (layered) va gibrid (Windows NT, macOS). Arxitektura tizim barqarorligi, xavfsizligi, samaradorligi va kengaytiriluvchanligini belgilaydi.")

add(93, "Operatsion tizimlarda fayl boshqaruvchilari.",
"Fayl boshqaruvchisi (file manager) - fayllar va kataloglarni ko'rish, yaratish, nusxalash, ko'chirish, o'chirish va qidirish imkonini beruvchi dastur. Misollar: Windows Explorer, macOS Finder, Linuxda Nautilus, Dolphin. Ular grafik interfeys orqali fayl tizimi bilan qulay ishlashni ta'minlaydi, fayl atributlari va huquqlarini ko'rsatadi hamda resurslarni tartibli boshqarishga yordam beradi.")

add(94, "Operatsion tizimlarda resurslar boshqaruvi va sinxronizatsiyani yaxshilash.",
"Resurslar boshqaruvi va sinxronizatsiyani yaxshilash uchun: samarali rejalashtirish algoritmlari, qulflarni minimallashtirish, lock-free tuzilmalar, ustuvorlikni to'g'ri belgilash, deadlockni aniqlash va oldini olish hamda monitoring qo'llaniladi. To'g'ri sinxronizatsiya (semafor, muteks, monitor) poyga holati va ziddiyatlarni kamaytiradi, resurslardan oqilona foydalanish esa tizim samaradorligini oshiradi.")

add(95, "Operatsion tizimlarda tarmoqni kuzatish va tarmoq trafigini boshqarish.",
"Tarmoqni kuzatish (monitoring) - tarmoq trafigi, qurilmalar holati va xavfsizlikni real vaqtda nazorat qilish. Trafikni boshqarish esa o'tkazuvchanlikni taqsimlash (QoS), yuk muvozanatlash va keraksiz trafikni cheklashni o'z ichiga oladi. Buning uchun Wireshark, netstat, tcpdump kabi vositalar ishlatiladi. Bu tarmoq samaradorligini oshiradi va hujum hamda nosozliklarni o'z vaqtida aniqlashga yordam beradi.")

add(96, "Operatsion tizimda xotira segmentatsiyasining afzalliklari va kamchiliklari.",
"Segmentatsiya afzalliklari: dasturning mantiqiy tuzilishiga mos keladi, kod va ma'lumotlarni alohida himoya qilish hamda ulashish oson, modullashtirishni qo'llab-quvvatlaydi. Kamchiliklari: tashqi fragmentatsiya yuzaga keladi (bo'sh joylar tarqoq bo'lib qoladi), turli o'lchamdagi segmentlarni boshqarish murakkab va manzilni hisoblash qo'shimcha vaqt talab qiladi. Shu sababli ko'pincha sahifalash bilan birga (segmentli-sahifali) qo'llaniladi.")

add(97, "Tizim resurslarini boshqarishning samarali usullari.",
"Tizim resurslarini samarali boshqarish usullari: dinamik resurs taqsimlash, ustuvorlikka asoslangan rejalashtirish, virtuallashtirish, keshlash, yuk muvozanatlash va monitoring. OT resurslardan foydalanishni kuzatib, ehtiyojga qarab moslashtiradi, ziddiyatlarni hal qiladi va deadlockning oldini oladi. Bu resurslardan maksimal foydalanish, tizim barqarorligi va yuqori unumdorlikni ta'minlaydi.")

add(98, "Operatsion tizimda tarmoqni sozlashda xavfsizlik choralari.",
"Tarmoqni sozlashda quyidagi xavfsizlik choralari ko'riladi: tarmoqaro ekran (firewall) sozlash, keraksiz portlarni yopish, kuchli parol va autentifikatsiya, shifrlash (VPN, TLS), kirish huquqlarini cheklash, muntazam yangilanish va antivirus o'rnatish, tarmoqni segmentlash hamda monitoring yuritish. Bu choralar ruxsatsiz kirish, hujum va ma'lumot sizib chiqishining oldini oladi.")

add(99, "Operatsion tizimlarda ma'lumotlar bazasini boshqarishning asosiy prinsiplari.",
"Ma'lumotlar bazasini boshqarish prinsiplari: ma'lumotlar yaxlitligi (integrity), izchillik (consistency), tranzaksiyalarning ACID xususiyatlari (atomarlik, izchillik, izolyatsiya, bardoshlilik), kirish huquqlarini nazorat qilish, zaxira nusxa olish va tiklash hamda bir vaqtda kirishni boshqarish. OT ma'lumotlar bazasi tizimiga (DBMS) fayl, xotira va jarayon resurslarini taqdim etib, ishonchli ishlashni ta'minlaydi.")

add(100, "CLI va GUI o'rtasidagi farqlar.",
"CLI (Command Line Interface) - matnli buyruqlar orqali boshqarish: tezkor, resurs tejamkor, avtomatlashtirish (skript) uchun qulay, lekin buyruqlarni yodlashni talab qiladi. GUI (Graphical User Interface) - oyna, belgi, tugma va sichqoncha orqali boshqarish: ko'rgazmali, o'rganish oson va qulay, lekin ko'proq resurs talab qiladi. CLI tajribali foydalanuvchilar va serverlar uchun, GUI esa oddiy foydalanuvchilar uchun qulaydir.")



# ---------------------------------------------------------------------------
# DOCX qurilishi (python-docx ishlatmasdan, to'g'ridan-to'g'ri OOXML)
# ---------------------------------------------------------------------------

def esc(t):
    return html.escape(t, quote=False)

def run(text, bold=False, size=None, color=None):
    rpr = "<w:rPr>"
    if bold:
        rpr += "<w:b/>"
    if size:
        rpr += f'<w:sz w:val="{size*2}"/>'
    if color:
        rpr += f'<w:color w:val="{color}"/>'
    rpr += "</w:rPr>"
    return f'<w:r>{rpr}<w:t xml:space="preserve">{esc(text)}</w:t></w:r>'

def para(runs_xml, align=None, space_after=120, style_size=None):
    ppr = "<w:pPr>"
    if align:
        ppr += f'<w:jc w:val="{align}"/>'
    ppr += f'<w:spacing w:after="{space_after}"/>'
    ppr += "</w:pPr>"
    return f"<w:p>{ppr}{runs_xml}</w:p>"

body = []
# Sarlavha
body.append(para(run("Operatsion tizimlar fanidan savollarga javoblar", bold=True, size=18, color="1F3864"), align="center", space_after=120))
body.append(para(run("100 ta nazorat savoliga to'liq javoblar", bold=False, size=12, color="595959"), align="center", space_after=360))

for n, q, a in QA:
    body.append(para(run(f"{n}-savol. {q}", bold=True, size=13, color="2E74B5"), space_after=60))
    body.append(para(run("Javob: ", bold=True, size=11) + run(a, size=11), space_after=240))

# Oxirgi bo'lim xossalari (A4)
body.append('<w:sectPr><w:pgSz w:w="11906" w:h="16838"/><w:pgMar w:top="1134" w:bottom="1134" w:left="1134" w:right="1134"/></w:sectPr>')

document_xml = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
    '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
    '<w:body>' + "".join(body) + '</w:body></w:document>'
)

content_types = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
    '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
    '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
    '<Default Extension="xml" ContentType="application/xml"/>'
    '<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
    '</Types>'
)

rels = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
    '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
    '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>'
    '</Relationships>'
)

out_name = "Operatsion_tizimlar_savollar_javoblar.docx"
with zipfile.ZipFile(out_name, "w", zipfile.ZIP_DEFLATED) as z:
    z.writestr("[Content_Types].xml", content_types)
    z.writestr("_rels/.rels", rels)
    z.writestr("word/document.xml", document_xml)

print(f"Tayyor: {out_name} | savollar soni: {len(QA)}")
