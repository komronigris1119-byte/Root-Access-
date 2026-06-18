# VIRTUAL MASHINALAR VA KONTEYNERLAR: ZAMONAVIY DUNYODA FARQLAR VA FOYDALANISH MISOLLARI

## OPERATSION TIZIMLAR FANIDAN MUSTAQIL ISH

---

**Mavzu:** Virtual mashinalar va konteynerlar: zamonaviy dunyoda farqlar va foydalanish misollari

**Fan:** Operatsion tizimlar

**Talaba:** [Ism Familiya]

**Guruh:** [Guruh raqami]

**Ilmiy rahbar:** [Rahbar F.I.O.]

**Toshkent – 2026**

---

## MUNDARIJA

**KIRISH** ............................................................. 3

**1-BOB. VIRTUALIZATSIYA NAZARIY ASOSLARI** .......................... 5
- 1.1. Virtualizatsiya tushunchasi va tarixiy rivojlanishi ........... 5
- 1.2. Virtualizatsiya turlari va tasnifi ........................... 7
- 1.3. Gipervizorlar: Type 1 va Type 2 .............................. 9

**2-BOB. VIRTUAL MASHINALAR** ........................................ 11
- 2.1. Virtual mashina arxitekturasi va ishlash prinsipi ............ 11
- 2.2. Mashhur virtualizatsiya platformalari ........................ 13
- 2.3. Virtual mashinalarning afzalliklari va kamchiliklari ......... 15

**3-BOB. KONTEYNERLAR** .............................................. 17
- 3.1. Konteynerlash texnologiyasi va uning asoslari ................ 17
- 3.2. Docker platformasi ........................................... 19
- 3.3. Kubernetes va konteyner orkestratsiyasi ...................... 21
- 3.4. Konteynerlarning afzalliklari va kamchiliklari ............... 23

**4-BOB. TAQQOSLASH VA AMALIY FOYDALANISH** .......................... 25
- 4.1. Virtual mashina va konteyner o'rtasidagi farqlar ............. 25
- 4.2. Amaliy foydalanish misollari (use cases) ..................... 27
- 4.3. Gibrid yondashuv: birgalikda foydalanish ..................... 29
- 4.4. Kelajak tendentsiyalari ...................................... 31

**XULOSA** ........................................................... 33

**FOYDALANILGAN ADABIYOTLAR RO'YXATI** ............................... 35

---


## KIRISH

Zamonaviy axborot texnologiyalari sohasida hisoblash resurslaridan samarali foydalanish eng dolzarb masalalardan biri hisoblanadi. Bulutli hisoblash (cloud computing), katta ma'lumotlar (big data), mikroservis arxitekturasi va DevOps amaliyotlarining keng tarqalishi bilan dasturiy ta'minotni ishga tushirish, izolyatsiya qilish va boshqarishning yangi usullariga ehtiyoj kuchaydi. Aynan shu ehtiyojlar virtualizatsiya va konteynerlash texnologiyalarining jadal rivojlanishiga turtki bo'ldi.

Virtual mashinalar (Virtual Machines, VM) va konteynerlar (Containers) — bugungi kunda IT-infratuzilmaning ikkita asosiy ustuni hisoblanadi. Ularning har biri bitta jismoniy serverda bir nechta izolyatsiyalangan muhitlarni yaratish imkonini beradi, biroq buni texnik jihatdan butunlay boshqacha usulda amalga oshiradi. Ko'pchilik mutaxassislar va o'quvchilar uchun bu ikki texnologiya o'rtasidagi farqni tushunish murakkab masala bo'lib qolmoqda.

### Mavzuning dolzarbligi

Hozirgi kunda dunyodagi yirik kompaniyalarning aksariyati o'z xizmatlarini bulutli platformalarda joylashtiradi. Amazon Web Services (AWS), Microsoft Azure, Google Cloud Platform kabi yetakchi provayderlar o'z infratuzilmasini virtual mashinalar va konteynerlar asosida quradi. Statistik ma'lumotlarga ko'ra, zamonaviy korxonalarning katta qismi dasturiy ta'minotni yetkazib berishda konteyner texnologiyalaridan, xususan Docker va Kubernetes'dan foydalanmoqda.

O'zbekiston Respublikasida ham "Raqamli O'zbekiston — 2030" strategiyasi doirasida axborot texnologiyalari infratuzilmasi jadal rivojlanmoqda. Davlat xizmatlari, bank tizimlari va xususiy sektor raqamli transformatsiya jarayonini boshidan kechirmoqda. Bu jarayonda virtualizatsiya va konteynerlash texnologiyalarini chuqur tushunish — har bir IT-mutaxassis uchun zaruriy malakaga aylanmoqda.

Operatsion tizimlar fani nuqtai nazaridan bu mavzu ayniqsa muhim, chunki ikkala texnologiya ham operatsion tizimning yadrosi (kernel), jarayonlarni boshqarish, resurslarni taqsimlash va izolyatsiya qilish mexanizmlari bilan bevosita bog'liq. Konteynerlar Linux yadrosining namespaces va cgroups kabi imkoniyatlariga tayanadi, virtual mashinalar esa apparat resurslarini gipervizor orqali virtuallashtiradi.

### Tadqiqotning maqsadi

Ushbu mustaqil ishning asosiy maqsadi — virtual mashinalar va konteynerlar texnologiyalarining nazariy asoslarini, arxitekturasini, ishlash prinsiplarini chuqur o'rganish hamda ular o'rtasidagi farqlarni va zamonaviy dunyodagi amaliy foydalanish misollarini har tomonlama tahlil qilishdir.

### Tadqiqotning vazifalari

Belgilangan maqsadga erishish uchun quyidagi vazifalar qo'yildi:

1. Virtualizatsiya tushunchasi, uning tarixiy rivojlanishi va asosiy turlarini o'rganish;
2. Gipervizorlar va ularning turlarini (Type 1, Type 2) tahlil qilish;
3. Virtual mashina arxitekturasi va mashhur platformalarini ko'rib chiqish;
4. Konteynerlash texnologiyasi, Docker va Kubernetes tizimlarini o'rganish;
5. Virtual mashina va konteyner o'rtasidagi texnik farqlarni aniqlash;
6. Ikkala texnologiyaning amaliy foydalanish misollarini (use cases) tahlil qilish;
7. Gibrid yondashuvlar va kelajak tendentsiyalarini baholash.

### Tadqiqot obyekti va predmeti

**Tadqiqot obyekti:** Zamonaviy hisoblash infratuzilmasida resurslarni virtuallashtirish va izolyatsiya qilish texnologiyalari.

**Tadqiqot predmeti:** Virtual mashinalar va konteynerlarning arxitekturasi, ishlash prinsiplari, farqlari va amaliy qo'llanilishi.

### Tadqiqot metodlari

Ishni amalga oshirishda nazariy tahlil, qiyosiy tahlil (comparative analysis), tizimli yondashuv va amaliy misollarni o'rganish metodlaridan foydalanildi.

### Ishning tuzilishi

Mustaqil ish kirish, to'rtta asosiy bob, xulosa va foydalanilgan adabiyotlar ro'yxatidan iborat. Birinchi bobda virtualizatsiyaning nazariy asoslari, ikkinchi bobda virtual mashinalar, uchinchi bobda konteynerlar, to'rtinchi bobda esa ikkala texnologiyaning taqqoslanishi va amaliy foydalanishi yoritilgan.

---


## 1-BOB. VIRTUALIZATSIYA NAZARIY ASOSLARI

### 1.1. Virtualizatsiya tushunchasi va tarixiy rivojlanishi

**Virtualizatsiya** — bu jismoniy hisoblash resurslarini (protsessor, operativ xotira, disk, tarmoq) dasturiy ta'minot yordamida abstraktlashtirib, ulardan bir nechta mustaqil, mantiqiy (virtual) resurslar yaratish texnologiyasidir. Virtualizatsiya tufayli bitta jismoniy server bir vaqtning o'zida bir nechta operatsion tizim yoki ilovani izolyatsiyalangan holda ishlatishi mumkin.

Virtualizatsiyaning asosiy g'oyasi — apparat (hardware) va dasturiy ta'minot (software) o'rtasiga abstraktsiya qatlamini qo'shishdir. Bu qatlam jismoniy resurslarni virtual resurslarga aylantiradi va ularni turli foydalanuvchilar yoki ilovalar o'rtasida taqsimlaydi.

#### 1.1.1. Tarixiy rivojlanish bosqichlari

Virtualizatsiya g'oyasi yangi emas — uning ildizlari XX asrning 60-yillariga borib taqaladi:

**1960-yillar.** Virtualizatsiyaning dastlabki shakllari IBM kompaniyasining mainframe (yirik universal) kompyuterlarida paydo bo'ldi. IBM System/360 va keyinchalik CP/CMS tizimlari bir nechta foydalanuvchining bitta qimmatbaho kompyuter resurslaridan bir vaqtda foydalanishiga imkon berdi. Bu davrda "virtual mashina" atamasi birinchi marta ishlatildi.

**1970-yillar.** 1974-yilda Gerald Popek va Robert Goldberg "Uchinchi avlod arxitekturalarini virtuallashtirish uchun rasmiy talablar" nomli ilmiy ishida virtualizatsiyaning nazariy asoslarini ishlab chiqdilar. Ular gipervizor uchun zarur bo'lgan uchta asosiy xususiyatni belgilab berdilar: ekvivalentlik, resurslar ustidan nazorat va samaradorlik.

**1990-yillar.** Shaxsiy kompyuterlarning keng tarqalishi bilan virtualizatsiyaga qiziqish susaydi, chunki har bir foydalanuvchi o'z kompyuteriga ega bo'ldi. Biroq 1998-yilda VMware kompaniyasi tashkil etilib, x86 arxitekturasi uchun virtualizatsiyani amalga oshirdi. Bu yo'nalishda inqilob bo'ldi, chunki x86 protsessorlari dastlab virtualizatsiya uchun mo'ljallanmagan edi.

**2000-yillar.** Serverlarning kam yuklanishi muammosi (server underutilization) tufayli kompaniyalar bitta serverda bir nechta xizmatni birlashtirishga ehtiyoj sezdi. 2006-yilda Intel (VT-x) va AMD (AMD-V) apparat darajasida virtualizatsiyani qo'llab-quvvatlashni joriy etdi, bu esa virtualizatsiya samaradorligini sezilarli oshirdi.

**2010-yillardan hozirgacha.** Bulutli hisoblash davri boshlandi. Amazon EC2, Microsoft Azure kabi platformalar virtual mashinalarni asosiy xizmat sifatida taklif eta boshladi. 2013-yilda Docker konteyner texnologiyasini ommalashtirib, virtualizatsiyaning yangi, yengilroq paradigmasini olib keldi.

#### 1.1.2. Virtualizatsiyaning asosiy maqsadlari

Virtualizatsiya texnologiyasi quyidagi muhim maqsadlarga xizmat qiladi:

1. **Resurslardan samarali foydalanish.** Bitta jismoniy serverning quvvatidan to'liq foydalanish, bo'sh turgan resurslarni kamaytirish.
2. **Izolyatsiya.** Har bir virtual muhit boshqalaridan ajratilgan bo'lib, bittasidagi nosozlik boshqalariga ta'sir qilmaydi.
3. **Moslashuvchanlik (flexibility).** Virtual muhitlarni tez yaratish, ko'chirish va o'chirish imkoniyati.
4. **Xarajatlarni kamaytirish.** Kamroq jismoniy server xarid qilish, energiya va joy tejash.
5. **Tez tiklanish (disaster recovery).** Zaxira nusxalarni olish va tizimni tez tiklash.

### 1.2. Virtualizatsiya turlari va tasnifi

Virtualizatsiya bir necha turga bo'linadi va har biri o'ziga xos vazifani bajaradi:

#### 1.2.1. Server virtualizatsiyasi

Eng keng tarqalgan tur bo'lib, bitta jismoniy serverni bir nechta virtual serverga bo'lish imkonini beradi. Har bir virtual server o'z operatsion tizimiga va ilovalariga ega bo'ladi. Bu data-markazlarda (data center) keng qo'llaniladi.

#### 1.2.2. Tarmoq virtualizatsiyasi (Network Virtualization)

Jismoniy tarmoq resurslarini dasturiy ta'minot yordamida virtuallashtirishni anglatadi. Bunga Software-Defined Networking (SDN) va virtual mahalliy tarmoqlar (VLAN) misol bo'la oladi.

#### 1.2.3. Saqlash virtualizatsiyasi (Storage Virtualization)

Bir nechta jismoniy saqlash qurilmalarini yagona mantiqiy saqlash resursiga birlashtirib, ularni markazlashgan holda boshqarish imkonini beradi. SAN (Storage Area Network) va NAS texnologiyalari bunga misoldir.

#### 1.2.4. Desktop virtualizatsiyasi (Desktop Virtualization)

Foydalanuvchining ish stoli muhitini markaziy serverda ishlatib, uni uzoqdan turib boshqarish. VDI (Virtual Desktop Infrastructure) texnologiyasi bunga yorqin misol.

#### 1.2.5. Ilova virtualizatsiyasi (Application Virtualization)

Ilovalarni operatsion tizimdan ajratilgan holda, izolyatsiyalangan muhitda ishlatish. Konteynerlash texnologiyasi aynan shu yo'nalishga yaqin turadi.

#### 1.2.6. Virtualizatsiya darajasiga ko'ra tasnif

| Tur | Tavsifi | Misol |
|-----|---------|-------|
| To'liq virtualizatsiya (Full Virtualization) | Mehmon OT o'zgartirilmasdan ishlaydi, gipervizor barcha apparat so'rovlarini emulyatsiya qiladi | VMware ESXi, KVM |
| Paravirtualizatsiya (Paravirtualization) | Mehmon OT virtualizatsiyadan xabardor bo'lib, gipervizor bilan to'g'ridan-to'g'ri ishlaydi | Xen |
| Apparat yordamidagi virtualizatsiya | Protsessor darajasidagi qo'llab-quvvatlash (Intel VT-x, AMD-V) | Zamonaviy barcha gipervizorlar |
| OT darajasidagi virtualizatsiya | Bitta yadro bir nechta izolyatsiyalangan foydalanuvchi muhitini boshqaradi | Docker, LXC |

### 1.3. Gipervizorlar: Type 1 va Type 2

**Gipervizor** (hypervisor yoki Virtual Machine Monitor, VMM) — bu virtual mashinalarni yaratish, ishga tushirish va boshqarishni ta'minlovchi dasturiy ta'minot qatlamidir. Gipervizor jismoniy apparat resurslarini virtual mashinalar o'rtasida taqsimlaydi va ularning izolyatsiyasini ta'minlaydi. Gipervizorlar ikki asosiy turga bo'linadi.

#### 1.3.1. Type 1 gipervizor (Bare-Metal)

Type 1 gipervizor to'g'ridan-to'g'ri jismoniy apparatga (bare-metal) o'rnatiladi va u bilan bevosita ishlaydi. Bunda asosiy operatsion tizim mavjud bo'lmaydi — gipervizorning o'zi operatsion tizim vazifasini bajaradi.

**Xususiyatlari:**
- Yuqori samaradorlik va tezlik, chunki qo'shimcha qatlam yo'q;
- Yuqori xavfsizlik va barqarorlik;
- Asosan korporativ data-markazlarda va serverlarda ishlatiladi.

**Misollar:** VMware ESXi, Microsoft Hyper-V, Citrix XenServer, KVM (Linux).

#### 1.3.2. Type 2 gipervizor (Hosted)

Type 2 gipervizor mavjud operatsion tizim (host OS) ustiga oddiy dastur sifatida o'rnatiladi. Virtual mashinalar host OT orqali apparat resurslariga murojaat qiladi.

**Xususiyatlari:**
- O'rnatish va foydalanish oson;
- Samaradorligi Type 1'ga nisbatan pastroq, chunki qo'shimcha qatlam mavjud;
- Asosan shaxsiy kompyuterlarda, test va o'quv maqsadlarida ishlatiladi.

**Misollar:** Oracle VirtualBox, VMware Workstation, VMware Fusion, Parallels Desktop.

#### 1.3.3. Ikkala turning taqqoslanishi

| Xususiyat | Type 1 (Bare-Metal) | Type 2 (Hosted) |
|-----------|---------------------|-----------------|
| O'rnatish joyi | To'g'ridan-to'g'ri apparatga | Host OT ustiga |
| Samaradorlik | Yuqori | O'rtacha |
| Xavfsizlik | Yuqori | Pastroq |
| Foydalanish sohasi | Serverlar, data-markazlar | Shaxsiy kompyuterlar, test |
| Misol | VMware ESXi, Hyper-V | VirtualBox, VMware Workstation |

Birinchi bobda virtualizatsiyaning nazariy asoslari, tarixi, turlari va gipervizorlar ko'rib chiqildi. Keyingi bobda virtual mashinalar batafsil o'rganiladi.

---


## 2-BOB. VIRTUAL MASHINALAR

### 2.1. Virtual mashina arxitekturasi va ishlash prinsipi

**Virtual mashina (Virtual Machine, VM)** — bu jismoniy kompyuterning to'liq dasturiy emulyatsiyasi bo'lib, o'z operatsion tizimiga, virtual protsessoriga, xotirasiga, diskiga va tarmoq interfeysiga ega bo'ladi. Foydalanuvchi nuqtai nazaridan virtual mashina haqiqiy kompyuterdan deyarli farq qilmaydi.

#### 2.1.1. Virtual mashina arxitekturasi

Virtual mashina arxitekturasi qatlamli tuzilishga ega:

```
┌─────────────────────────────────────────────────┐
│   Ilova A    │   Ilova B    │   Ilova C          │
├─────────────────────────────────────────────────┤
│  Mehmon OT 1 │  Mehmon OT 2 │  Mehmon OT 3       │ (Guest OS)
│  (Linux)     │  (Windows)   │  (Linux)           │
├─────────────────────────────────────────────────┤
│       Virtual apparat (vCPU, vRAM, vDisk)         │
├─────────────────────────────────────────────────┤
│              GIPERVIZOR (Hypervisor)              │
├─────────────────────────────────────────────────┤
│     Host operatsion tizimi (Type 2 uchun)         │
├─────────────────────────────────────────────────┤
│   Jismoniy apparat (CPU, RAM, Disk, Tarmoq)       │
└─────────────────────────────────────────────────┘
```

Eng pastki qatlamda jismoniy apparat joylashadi. Uning ustida gipervizor turadi, u apparat resurslarini virtual mashinalar o'rtasida taqsimlaydi. Har bir virtual mashina o'zining to'liq mehmon operatsion tizimini (guest OS) ishlatadi va uning ustida ilovalar bajariladi.

#### 2.1.2. Ishlash prinsipi

Virtual mashinaning asosiy xususiyati shundaki, u **to'liq operatsion tizimni** o'z ichiga oladi, jumladan yadro (kernel), drayverlar, kutubxonalar va foydalanuvchi muhiti. Bu uni juda izolyatsiyalangan, ammo nisbatan "og'ir" (resurs talab qiluvchi) qiladi.

Gipervizor virtual mashinadan kelgan apparat so'rovlarini ushlab oladi va ularni jismoniy apparatga uzatadi yoki emulyatsiya qiladi. Zamonaviy protsessorlarda apparat yordamidagi virtualizatsiya (Intel VT-x, AMD-V) tufayli bu jarayon juda samarali bajariladi.

Virtual mashinaning yana bir muhim tushunchasi — **snapshot** (vaqt kesimi). Bu virtual mashinaning ma'lum bir paytdagi to'liq holatini saqlash imkonini beradi, keyinchalik kerak bo'lganda shu holatga qaytish mumkin.

#### 2.1.3. Virtual mashina fayllari

Virtual mashina jismoniy diskda fayllar to'plami sifatida saqlanadi:
- **Virtual disk fayli** (.vmdk, .vdi, .qcow2) — mehmon OT va ma'lumotlarni saqlaydi;
- **Konfiguratsiya fayli** — VM sozlamalari (xotira hajmi, protsessorlar soni);
- **Snapshot fayllari** — saqlangan holatlar.

### 2.2. Mashhur virtualizatsiya platformalari

#### 2.2.1. VMware

VMware — virtualizatsiya bozorining yetakchilaridan biri. Kompaniya bir nechta mahsulot taklif etadi:
- **VMware ESXi** — Type 1 gipervizor, korporativ data-markazlar uchun;
- **VMware Workstation** — Type 2 gipervizor, ish stoli kompyuterlari uchun;
- **VMware vSphere** — virtual infratuzilmani markazlashgan boshqarish platformasi.

VMware o'zining barqarorligi, keng funksionalligi va korporativ qo'llab-quvvatlashi bilan ajralib turadi.

#### 2.2.2. Oracle VirtualBox

VirtualBox — bepul va ochiq kodli (open-source) Type 2 gipervizor. U Windows, macOS, Linux operatsion tizimlarida ishlaydi. O'rnatish va foydalanish soddaligi tufayli o'quv maqsadlarida va dasturchilar orasida juda mashhur.

#### 2.2.3. Microsoft Hyper-V

Hyper-V — Microsoft kompaniyasining Type 1 gipervizori bo'lib, Windows Server va Windows 10/11 Pro versiyalariga o'rnatilgan. U Windows muhitida ishlovchi korxonalar uchun qulay yechim hisoblanadi.

#### 2.2.4. KVM (Kernel-based Virtual Machine)

KVM — Linux yadrosiga o'rnatilgan virtualizatsiya texnologiyasi. U Linux yadrosini to'liq funksional Type 1 gipervizorga aylantiradi. KVM ochiq kodli bo'lib, ko'plab bulutli platformalar (jumladan OpenStack) tomonidan ishlatiladi. KVM ko'pincha QEMU emulyatori bilan birgalikda qo'llaniladi.

#### 2.2.5. Platformalarning taqqoslanishi

| Platforma | Turi | Litsenziya | Asosiy foydalanish |
|-----------|------|------------|--------------------|
| VMware ESXi | Type 1 | Tijoriy | Korporativ serverlar |
| VirtualBox | Type 2 | Bepul/ochiq kod | O'quv, test, dasturlash |
| Hyper-V | Type 1 | Windows bilan | Windows muhitidagi korxonalar |
| KVM | Type 1 | Ochiq kod | Linux serverlar, bulut |

### 2.3. Virtual mashinalarning afzalliklari va kamchiliklari

#### 2.3.1. Afzalliklari

1. **To'liq izolyatsiya.** Har bir VM o'z yadrosi va OT'siga ega bo'lgani uchun ular o'rtasidagi izolyatsiya juda kuchli. Bittasidagi xavfsizlik buzilishi yoki nosozlik boshqalariga ta'sir qilmaydi.

2. **Turli operatsion tizimlarni ishlatish.** Bitta jismoniy serverda Windows, Linux, va boshqa OT'larni bir vaqtda ishlatish mumkin.

3. **Yetuk va sinovdan o'tgan texnologiya.** VM texnologiyasi o'n yillar davomida rivojlangan, barqaror va ishonchli.

4. **Kuchli xavfsizlik.** To'liq izolyatsiya tufayli xavfsizlik darajasi yuqori.

5. **Snapshot va migratsiya.** VM holatini saqlash va ishlab turgan VM'ni bir serverdan boshqasiga ko'chirish (live migration) imkoniyati.

#### 2.3.2. Kamchiliklari

1. **Resurs sarfi yuqori.** Har bir VM to'liq OT'ni ishlatgani uchun ko'p xotira (RAM), disk maydoni va protsessor quvvatini talab qiladi.

2. **Sekin ishga tushish.** Virtual mashinani ishga tushirish (boot) bir necha daqiqa vaqt olishi mumkin, chunki butun OT yuklanadi.

3. **Cheklangan zichlik (density).** Bitta serverda chegaralangan miqdordagi VM'ni ishlatish mumkin, chunki har biri katta resurs talab qiladi.

4. **Boshqarish murakkabligi.** Ko'plab VM'larni va ularning OT'larini yangilash, xavfsizlik tuzatishlarini o'rnatish murakkab bo'lishi mumkin.

Ikkinchi bobda virtual mashinalarning arxitekturasi, platformalari hamda afzallik va kamchiliklari batafsil ko'rib chiqildi. Keyingi bobda konteynerlash texnologiyasi o'rganiladi.

---


## 3-BOB. KONTEYNERLAR

### 3.1. Konteynerlash texnologiyasi va uning asoslari

**Konteyner (Container)** — bu ilovani va uning barcha bog'liqliklarini (kutubxonalar, konfiguratsiya fayllari, ish vaqti muhiti) yagona, yengil va ko'chma paketga jamlangan izolyatsiyalangan muhitdir. Virtual mashinadan farqli o'laroq, konteyner o'z operatsion tizim yadrosiga ega emas — u host (asosiy) operatsion tizimning yadrosini boshqa konteynerlar bilan birgalikda ishlatadi.

#### 3.1.1. Konteyner arxitekturasi

Konteyner arxitekturasi virtual mashinadan tubdan farq qiladi:

```
┌─────────────────────────────────────────────────┐
│   Ilova A    │   Ilova B    │   Ilova C          │
├──────────────┼──────────────┼────────────────────┤
│ Kutubxonalar │ Kutubxonalar │ Kutubxonalar       │ (Bog'liqliklar)
├──────────────┴──────────────┴────────────────────┤
│   Konteyner A │ Konteyner B │ Konteyner C         │
├─────────────────────────────────────────────────┤
│      Konteyner dvigateli (Docker Engine)          │
├─────────────────────────────────────────────────┤
│         Host operatsion tizimi (yadro)            │ (umumiy kernel)
├─────────────────────────────────────────────────┤
│   Jismoniy yoki virtual apparat                   │
└─────────────────────────────────────────────────┘
```

Bu yerda asosiy farq shundaki, barcha konteynerlar **bitta umumiy yadroni** (shared kernel) ishlatadi. Bu konteynerlarni juda yengil va tez qiladi.

#### 3.1.2. Konteynerlashning texnik asoslari

Konteynerlash texnologiyasi asosan Linux yadrosining ikki muhim mexanizmiga tayanadi:

**1. Namespaces (nom maydonlari).** Bu mexanizm jarayonlar uchun izolyatsiyalangan muhit yaratadi. Har bir konteyner o'zining alohida nom maydoniga ega bo'lib, u quyidagilarni izolyatsiya qiladi:
- PID namespace — jarayonlar identifikatorlari;
- NET namespace — tarmoq interfeyslari;
- MNT namespace — fayl tizimi nuqtalari;
- UTS namespace — host nomi;
- IPC namespace — jarayonlararo aloqa;
- USER namespace — foydalanuvchi identifikatorlari.

**2. Control Groups (cgroups).** Bu mexanizm konteynerga ajratiladigan resurslarni (protsessor, xotira, disk I/O, tarmoq) cheklash va boshqarish imkonini beradi. Cgroups tufayli bitta konteyner barcha resurslarni "o'zlashtirib olmaydi".

Bundan tashqari, **Union File System** (masalan, OverlayFS) texnologiyasi konteyner obrazlarini qatlamli tuzilishda saqlash va samarali boshqarish imkonini beradi.

#### 3.1.3. Konteyner va obraz tushunchalari

Konteynerlashda ikki muhim tushuncha mavjud:

- **Obraz (Image)** — ilovani ishga tushirish uchun zarur bo'lgan barcha narsalarni o'z ichiga olgan o'zgarmas (read-only) shablon. Obraz qatlamlardan iborat bo'ladi.
- **Konteyner (Container)** — obrazning ishlab turgan namunasi (instance). Bir obrazdan bir nechta konteyner yaratish mumkin.

Buni obyektga yo'naltirilgan dasturlashdagi sinf (class) va obyekt (object) munosabatiga o'xshatish mumkin: obraz — bu sinf, konteyner — uning namunasi.

### 3.2. Docker platformasi

**Docker** — konteynerlash texnologiyasini ommalashtirgan eng mashhur platforma. 2013-yilda taqdim etilgan Docker konteynerlarni yaratish, tarqatish va ishga tushirishni standartlashtirib, dasturiy ta'minotni yetkazib berish jarayonini tubdan o'zgartirdi.

#### 3.2.1. Docker arxitekturasi

Docker mijoz-server (client-server) arxitekturasiga asoslanadi:
- **Docker Client** — foydalanuvchi buyruqlarni kiritadigan buyruq qatori interfeysi (CLI);
- **Docker Daemon (dockerd)** — konteynerlar, obrazlar va tarmoqlarni boshqaruvchi fon jarayoni;
- **Docker Registry** — obrazlarni saqlash ombori (masalan, Docker Hub).

#### 3.2.2. Dockerfile

**Dockerfile** — konteyner obrazini avtomatik yaratish uchun ko'rsatmalar to'plamini o'z ichiga olgan matnli fayl. Misol:

```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package.json ./
RUN npm install
COPY . .
EXPOSE 3000
CMD ["npm", "start"]
```

Bu Dockerfile Node.js ilovasi uchun obraz yaratadi: bazaviy obrazni oladi, ish katalogini belgilaydi, bog'liqliklarni o'rnatadi va ilovani ishga tushiradi.

#### 3.2.3. Docker asosiy buyruqlari

| Buyruq | Vazifasi |
|--------|----------|
| `docker build` | Dockerfile'dan obraz yaratish |
| `docker pull` | Registry'dan obraz yuklab olish |
| `docker run` | Obrazdan konteyner ishga tushirish |
| `docker ps` | Ishlab turgan konteynerlar ro'yxati |
| `docker stop` | Konteynerni to'xtatish |
| `docker images` | Mavjud obrazlar ro'yxati |

#### 3.2.4. Docker Compose

**Docker Compose** — bir nechta konteynerdan iborat ilovalarni yagona konfiguratsiya fayli (docker-compose.yml) orqali boshqarish vositasi. Masalan, veb-server, ma'lumotlar bazasi va kesh xizmatini bitta buyruq bilan ishga tushirish mumkin.

### 3.3. Kubernetes va konteyner orkestratsiyasi

Bir nechta konteynerni boshqarish oson, ammo yuzlab yoki minglab konteynerni boshqarish murakkab vazifaga aylanadi. Aynan shu yerda **konteyner orkestratsiyasi** zarur bo'ladi.

#### 3.3.1. Kubernetes nima?

**Kubernetes (K8s)** — konteynerlashtirilgan ilovalarni avtomatik joylashtirish, masshtablash va boshqarish uchun mo'ljallangan ochiq kodli orkestratsiya platformasi. U dastlab Google tomonidan ishlab chiqilgan va hozirda Cloud Native Computing Foundation (CNCF) tomonidan qo'llab-quvvatlanadi.

#### 3.3.2. Kubernetes asosiy komponentlari

- **Pod** — Kubernetes'dagi eng kichik birlik, bir yoki bir nechta konteynerni o'z ichiga oladi;
- **Node** — konteynerlar ishlaydigan ishchi mashina (jismoniy yoki virtual);
- **Cluster** — node'lar to'plami;
- **Deployment** — ilovaning kerakli holatini (replikalar soni) belgilaydi;
- **Service** — konteynerlarga tarmoq orqali kirishni ta'minlaydi;
- **Control Plane** — klasterni boshqaruvchi markaz.

#### 3.3.3. Kubernetes imkoniyatlari

1. **Avtomatik masshtablash (auto-scaling)** — yuklamaga qarab konteynerlar sonini ko'paytirish yoki kamaytirish;
2. **O'z-o'zini tiklash (self-healing)** — ishlamay qolgan konteynerlarni avtomatik qayta ishga tushirish;
3. **Yuklamani taqsimlash (load balancing)** — so'rovlarni konteynerlar o'rtasida teng taqsimlash;
4. **To'xtovsiz yangilash (rolling updates)** — xizmatni to'xtatmasdan yangilash.

### 3.4. Konteynerlarning afzalliklari va kamchiliklari

#### 3.4.1. Afzalliklari

1. **Yengillik (lightweight).** Konteynerlar OT yadrosini ulashgani uchun juda kam resurs talab qiladi (megabaytlar darajasida).

2. **Tez ishga tushish.** Konteyner soniyalar, hatto millisekundlar ichida ishga tushadi, chunki OT yuklanishi shart emas.

3. **Yuqori zichlik (density).** Bitta serverda yuzlab konteynerni ishlatish mumkin.

4. **Ko'chuvchanlik (portability).** "Mening mashinamda ishlayapti" muammosini hal qiladi — konteyner har qanday muhitda bir xil ishlaydi.

5. **DevOps va CI/CD bilan integratsiya.** Konteynerlar uzluksiz integratsiya va yetkazib berish jarayonlariga ideal mos keladi.

#### 3.4.2. Kamchiliklari

1. **Zaifroq izolyatsiya.** Umumiy yadro ishlatilgani uchun izolyatsiya VM'ga nisbatan kuchsizroq. Yadroda zaiflik bo'lsa, barcha konteynerlar xavf ostida qoladi.

2. **OT bog'liqligi.** Konteyner host OT yadrosiga bog'liq. Masalan, Linux konteynerlarini to'g'ridan-to'g'ri Windows yadrosida ishlatib bo'lmaydi (qo'shimcha qatlamsiz).

3. **Xavfsizlik masalalari.** Yadroni ulashish qo'shimcha xavfsizlik choralarini talab qiladi.

4. **Holatni saqlash (stateful) murakkabligi.** Konteynerlar tabiatan vaqtinchalik (ephemeral) bo'lgani uchun doimiy ma'lumotlarni saqlash qo'shimcha yechimlar (volume) talab qiladi.

Uchinchi bobda konteynerlash texnologiyasi, Docker va Kubernetes platformalari hamda konteynerlarning xususiyatlari o'rganildi. Keyingi bobda ikkala texnologiya taqqoslanadi.

---


## 4-BOB. TAQQOSLASH VA AMALIY FOYDALANISH

### 4.1. Virtual mashina va konteyner o'rtasidagi farqlar

Virtual mashinalar va konteynerlar bir xil maqsadga — izolyatsiyalangan muhit yaratishga xizmat qilsa-da, ular texnik jihatdan tubdan farq qiladi. Asosiy farq quyidagicha: **virtual mashina apparatni virtuallashtirsa, konteyner operatsion tizimni virtuallashtiradi.**

#### 4.1.1. Arxitektura jihatidan farq

Virtual mashinada gipervizor jismoniy apparatni virtuallashtiradi va har bir VM o'zining to'liq mehmon operatsion tizimini ishlatadi. Konteynerda esa konteyner dvigateli host OT yadrosini bo'lishadi va har bir konteyner faqat ilova hamda uning bog'liqliklarini o'z ichiga oladi.

#### 4.1.2. Batafsil taqqoslash jadvali

| Mezon | Virtual mashina | Konteyner |
|-------|-----------------|-----------|
| **Virtualizatsiya darajasi** | Apparat darajasida | OT darajasida |
| **Operatsion tizim** | Har birida to'liq mehmon OT | Host OT yadrosini ulashadi |
| **Hajmi** | Gigabaytlar (GB) | Megabaytlar (MB) |
| **Ishga tushish vaqti** | Daqiqalar | Soniyalar / millisekundlar |
| **Resurs sarfi** | Yuqori | Past |
| **Izolyatsiya** | Kuchli (to'liq) | O'rtacha (yadro ulashilgan) |
| **Zichlik (bir serverda)** | O'nlab | Yuzlab / minglab |
| **Ko'chuvchanlik** | Cheklangan | Yuqori |
| **Xavfsizlik** | Yuqori | Qo'shimcha choralar talab qiladi |
| **Turli OT ishlatish** | Mumkin (Windows, Linux) | Faqat host yadrosi turi bilan cheklangan |
| **Asosiy texnologiya** | Gipervizor (ESXi, KVM) | Docker, containerd, LXC |

#### 4.1.3. Samaradorlik jihatidan farq

Konteynerlar yengilligi va tez ishga tushishi tufayli resurslardan ancha samarali foydalanadi. Masalan, bitta serverda 10-20 ta virtual mashina ishlatish mumkin bo'lsa, xuddi shu serverda yuzlab konteynerni ishlatish mumkin. Bu konteynerlarni mikroservis arxitekturasi uchun ideal qiladi.

Biroq samaradorlik har doim ham asosiy mezon emas. Ba'zi hollarda kuchli izolyatsiya va xavfsizlik muhimroq bo'ladi — bunda virtual mashinalar afzalroq.

### 4.2. Amaliy foydalanish misollari (use cases)

#### 4.2.1. Virtual mashinalar qachon afzal?

**1. Turli operatsion tizimlarni ishlatish.** Agar bitta serverda ham Windows, ham Linux ilovalarini ishlatish kerak bo'lsa, virtual mashinalar yagona yechim hisoblanadi.

**2. Kuchli izolyatsiya va xavfsizlik talab qilinadigan holatlar.** Bank tizimlari, davlat tashkilotlari va maxfiy ma'lumotlar bilan ishlovchi tizimlarda to'liq izolyatsiya muhim.

**3. Legacy (eski) ilovalarni ishlatish.** Eski operatsion tizimlarni yoki maxsus muhit talab qiladigan ilovalarni ishlatishda VM qulay.

**4. Test va sinov muhitlari.** Turli OT versiyalarida dasturlarni sinab ko'rish uchun virtual mashinalar ishlatiladi.

**5. Desktop virtualizatsiyasi (VDI).** Korxonalarda xodimlar uchun markazlashgan ish stoli muhitlarini ta'minlash.

**Amaliy misol:** Bank o'zining asosiy bank tizimini (core banking) virtual mashinalarda ishlatadi, chunki bu yerda maksimal izolyatsiya, barqarorlik va xavfsizlik talab qilinadi.

#### 4.2.2. Konteynerlar qachon afzal?

**1. Mikroservis arxitekturasi.** Katta ilovani kichik, mustaqil xizmatlarga bo'lishda konteynerlar ideal. Har bir mikroservis o'z konteynerida ishlaydi.

**2. DevOps va CI/CD jarayonlari.** Dasturni avtomatik test qilish, qurish va joylashtirishda konteynerlar tezlik va izchillikni ta'minlaydi.

**3. Bulutli va masshtablanuvchi ilovalar.** Yuklamaga qarab tez masshtablanishi kerak bo'lgan veb-ilovalar uchun konteynerlar va Kubernetes ideal yechim.

**4. Ilovalarni tez yetkazib berish.** "Bir marta yarat, hamma joyda ishlat" prinsipi tufayli konteynerlar dasturchining mahalliy mashinasidan ishlab chiqarish (production) muhitiga muammosiz ko'chiriladi.

**Amaliy misol:** Netflix, Spotify, Google kabi yirik kompaniyalar o'z xizmatlarini minglab mikroservislar shaklida konteynerlarda ishlatadi va Kubernetes orqali boshqaradi. Bu ularga millionlab foydalanuvchilarga uzluksiz xizmat ko'rsatish imkonini beradi.

#### 4.2.3. Sohalar bo'yicha foydalanish

| Soha | Tavsiya etiladigan texnologiya | Sababi |
|------|-------------------------------|--------|
| Bank va moliya | Virtual mashinalar | Kuchli izolyatsiya va xavfsizlik |
| Veb-ilovalar (startaplar) | Konteynerlar | Tez masshtablash, arzon |
| E-tijorat platformalari | Konteynerlar + Kubernetes | Yuqori yuklamaga moslashish |
| Test laboratoriyalari | Virtual mashinalar | Turli OT muhitlari |
| Mikroservislar | Konteynerlar | Yengillik, mustaqillik |
| Davlat tizimlari | Virtual mashinalar | Maxfiylik, barqarorlik |

### 4.3. Gibrid yondashuv: birgalikda foydalanish

Amaliyotda virtual mashinalar va konteynerlar ko'pincha **bir-biriga qarama-qarshi emas, balki bir-birini to'ldiruvchi** texnologiyalar sifatida ishlatiladi. Eng keng tarqalgan yondashuv — konteynerlarni virtual mashinalar ichida ishga tushirish.

#### 4.3.1. Konteynerlar VM ichida

Ko'pchilik bulutli platformalarda Kubernetes klasteri virtual mashinalar ustida quriladi. Bu yondashuv ikkala texnologiyaning afzalliklarini birlashtiradi:
- Virtual mashinalar kuchli izolyatsiya va xavfsizlikni ta'minlaydi;
- Konteynerlar VM ichida yengillik, tezlik va ko'chuvchanlikni beradi.

Masalan, Google Kubernetes Engine (GKE), Amazon EKS va Azure AKS kabi boshqariladigan Kubernetes xizmatlari aynan shu printsip asosida ishlaydi — konteynerlar bulutdagi virtual mashinalar ustida ishlaydi.

#### 4.3.2. Gibrid yondashuvning afzalliklari

1. **Ko'p qatlamli xavfsizlik.** VM izolyatsiyasi va konteyner izolyatsiyasi birgalikda kuchliroq himoya beradi.
2. **Moslashuvchanlik.** Turli ehtiyojlarga mos resurslarni taqsimlash.
3. **Mavjud infratuzilmadan foydalanish.** Korxonalar mavjud VM infratuzilmasini saqlab qolgan holda konteyner texnologiyasiga o'tishi mumkin.

### 4.4. Kelajak tendentsiyalari

Virtualizatsiya va konteynerlash texnologiyalari doimiy rivojlanmoqda. Kelajakdagi asosiy yo'nalishlar:

#### 4.4.1. Serverless (server'siz) hisoblash

**Serverless** yondashuvida dasturchi serverni boshqarish haqida o'ylamaydi — u faqat kodni yozadi, infratuzilma esa avtomatik boshqariladi. AWS Lambda, Azure Functions kabi xizmatlar konteyner texnologiyasiga asoslanadi va talab bo'yicha (on-demand) ishlaydi.

#### 4.4.2. Yengil VM va xavfsiz konteynerlar

VM va konteyner o'rtasidagi chegarani yo'qotishga qaratilgan yangi texnologiyalar paydo bo'lmoqda. Masalan, **Firecracker** (AWS tomonidan ishlab chiqilgan) microVM texnologiyasi VM xavfsizligini konteyner tezligi bilan birlashtiradi. **Kata Containers** ham xuddi shunday maqsadni ko'zlaydi.

#### 4.4.3. Edge computing (chekka hisoblash)

Ma'lumotlarni manbaga yaqin joyda qayta ishlash uchun yengil konteynerlar edge qurilmalarida keng qo'llanilmoqda. Bu IoT (Internet of Things) tizimlarida ayniqsa muhim.

#### 4.4.4. WebAssembly (Wasm)

WebAssembly konteynerlarga muqobil yengil ish vaqti muhiti sifatida rivojlanmoqda. U konteynerlardan ham yengilroq va tezroq ishga tushish imkonini beradi.

To'rtinchi bobda virtual mashinalar va konteynerlar batafsil taqqoslandi, ularning amaliy foydalanish misollari, gibrid yondashuv va kelajak tendentsiyalari ko'rib chiqildi.

---


## XULOSA

Ushbu mustaqil ishda "Virtual mashinalar va konteynerlar: zamonaviy dunyoda farqlar va foydalanish misollari" mavzusi har tomonlama o'rganildi. Tadqiqot natijasida quyidagi xulosalar shakllantirildi:

**Birinchidan,** virtualizatsiya — jismoniy hisoblash resurslarini abstraktlashtirib, ulardan bir nechta mustaqil mantiqiy resurslar yaratish texnologiyasi bo'lib, uning ildizlari XX asrning 60-yillariga borib taqaladi. Bugungi kunda virtualizatsiya zamonaviy IT-infratuzilmaning asosini tashkil etadi. Gipervizorlar (Type 1 va Type 2) virtual mashinalarni yaratish va boshqarishni ta'minlaydi.

**Ikkinchidan,** virtual mashinalar apparat darajasida virtualizatsiyani amalga oshiradi va har bir VM o'zining to'liq operatsion tizimiga ega bo'ladi. Bu ularga kuchli izolyatsiya, yuqori xavfsizlik va turli OT'larni bir vaqtda ishlatish imkoniyatini beradi. Biroq ular ko'p resurs talab qiladi va sekin ishga tushadi.

**Uchinchidan,** konteynerlar operatsion tizim darajasida virtualizatsiyani amalga oshiradi va host OT yadrosini ulashadi. Linux yadrosining namespaces va cgroups mexanizmlariga tayanadigan konteynerlar yengilligi, tez ishga tushishi va yuqori ko'chuvchanligi bilan ajralib turadi. Docker va Kubernetes platformalari konteyner texnologiyasini ommalashtirdi.

**To'rtinchidan,** ikkala texnologiya o'rtasidagi asosiy farq shundaki, virtual mashina apparatni, konteyner esa operatsion tizimni virtuallashtiradi. Bu farq ularning hajmi, ishga tushish vaqti, izolyatsiya darajasi va resurs sarfida o'z aksini topadi.

**Beshinchidan,** virtual mashinalar kuchli izolyatsiya va xavfsizlik talab qilinadigan holatlarda (bank, davlat tizimlari, legacy ilovalar), konteynerlar esa mikroservis arxitekturasi, DevOps jarayonlari va masshtablanuvchi bulutli ilovalarda afzal hisoblanadi.

**Oltinchidan,** amaliyotda bu ikki texnologiya ko'pincha gibrid yondashuvda — konteynerlar virtual mashinalar ichida ishlatiladi. Bu yondashuv ikkala texnologiyaning afzalliklarini birlashtiradi va zamonaviy bulutli platformalarning asosini tashkil etadi.

**Umumiy xulosa:** Virtual mashinalar va konteynerlar bir-biriga raqobatchi emas, balki turli vazifalarni hal qiluvchi, bir-birini to'ldiruvchi texnologiyalardir. To'g'ri texnologiyani tanlash konkret loyihaning talablariga — xavfsizlik, samaradorlik, masshtablash va izolyatsiya darajasiga bog'liq. Serverless hisoblash, microVM va WebAssembly kabi yangi tendentsiyalar bu sohaning yanada rivojlanishidan dalolat beradi. IT-mutaxassis uchun har ikki texnologiyani chuqur tushunish zamonaviy infratuzilmani samarali loyihalash va boshqarishning zaruriy sharti hisoblanadi.

---

## FOYDALANILGAN ADABIYOTLAR RO'YXATI

1. Tanenbaum A. S., Bos H. *Modern Operating Systems*. 4th Edition. — Pearson, 2015. — 1136 p.

2. Silberschatz A., Galvin P. B., Gagne G. *Operating System Concepts*. 10th Edition. — Wiley, 2018. — 1280 p.

3. Popek G. J., Goldberg R. P. *Formal Requirements for Virtualizable Third Generation Architectures* // Communications of the ACM. — 1974. — Vol. 17, No. 7. — pp. 412–421.

4. Turnbull J. *The Docker Book: Containerization is the new virtualization*. — 2014. — 320 p.

5. Burns B., Beda J., Hightower K. *Kubernetes: Up and Running*. 3rd Edition. — O'Reilly Media, 2022. — 278 p.

6. Smith J., Nair R. *Virtual Machines: Versatile Platforms for Systems and Processes*. — Morgan Kaufmann, 2005. — 656 p.

7. Docker rasmiy hujjatlari [Elektron resurs]. — Kirish manzili: https://docs.docker.com

8. Kubernetes rasmiy hujjatlari [Elektron resurs]. — Kirish manzili: https://kubernetes.io/docs

9. VMware rasmiy hujjatlari [Elektron resurs]. — Kirish manzili: https://docs.vmware.com

10. Red Hat. *What's the difference between containers and VMs?* [Elektron resurs]. — Kirish manzili: https://www.redhat.com/en/topics/containers

11. Linux Kernel hujjatlari: Namespaces va Control Groups [Elektron resurs]. — Kirish manzili: https://www.kernel.org/doc

12. "Raqamli O'zbekiston — 2030" strategiyasi. O'zbekiston Respublikasi Prezidentining Farmoni, 2020-yil.

---

*Mustaqil ish · Operatsion tizimlar fani · Toshkent — 2026*
