// "Ixtirochilikka qadam" tanlovi (2-tuman bosqichi) - Rasmiy Nizom va Mezonlar Bazasi
// O'zbekiston Respublikasi Ta'lim va ilm-fan vazirligi xatiga 1-, 2-, 3-ilovalar asosida

const IXTIROCHILIK_CONFIG = {
  competitionName: "\"Ixtirochilikka qadam\" tanlovi",
  stage: "Ikkinchi (tuman/shahar) bosqichi",
  dates: "2026-yil 4-5-dekabr",
  maxScorePerJudge: 100,

  // 1-ILOVA: 5 ta rasmiy baholash mezoni
  criteria: [
    {
      id: "c1",
      name: "Loyihaning tanlov yo‘nalishlariga mos tayyorlanganligi",
      shortName: "Yo‘nalishga moslik",
      max: 10,
      levels: [
        { score: "1-3", desc: "Loyiha tayyorlangan, lekin yo‘nalishga mos kelmagan, maqsad aks etmagan." },
        { score: "4-6", desc: "Qisman mos, ammo yo‘nalish chuqur o‘rganilmagan." },
        { score: "7-10", desc: "To‘liq mos, chuqur o‘rganilgan va mavjud muammolar to‘liq ko‘rsatilgan." }
      ]
    },
    {
      id: "c2",
      name: "Loyiha taqdimoti (prezentatsiya)",
      shortName: "Taqdimot",
      max: 25,
      levels: [
        { score: "1-6", desc: "Talab darajasida emas, texnik sust, vaqt reglamentiga rioya qilinmagan." },
        { score: "7-12", desc: "Sodda va tushunarli, ammo savollarga to‘liq javob berilmagan." },
        { score: "13-18", desc: "Mantiqiy to‘g‘ri, mazmunli, reglamentga rioya qilingan, ayrim xatoliklar bor." },
        { score: "19-25", desc: "Talab asosida, infografikali, savollarga to‘liq va aniq javob, reglamentga rioya qilingan." }
      ]
    },
    {
      id: "c3",
      name: "Loyihaning texnik jihatdan sifatli va puxta tayyorlanganligi (model, maket, ishlanma)",
      shortName: "Texnik sifat (Model)",
      max: 25,
      levels: [
        { score: "1-6", desc: "Texnik jihatdan sust yoki amaliy ishlanma mavjud emas." },
        { score: "7-12", desc: "Qisman yoki yarim tayyor holatda, texnik kamchiliklar mavjud." },
        { score: "13-18", desc: "Deyarli tayyor, ishchi holatda, ammo ba'zi kamchiliklar bor." },
        { score: "19-25", desc: "To‘liq tayyor, ishchi model, barcha elementlar puxta ishlab chiqilgan." }
      ]
    },
    {
      id: "c4",
      name: "Loyihaning innovatsionligi va ijodiy yondashuv",
      shortName: "Innovatsionlik",
      max: 20,
      levels: [
        { score: "1-5", desc: "Ijodiy yondashuv yo‘q, odatiy usul, yangilik mavjud emas." },
        { score: "6-10", desc: "Qisman ijodiy, yangi texnologiyalar yetarli emas, to‘liq javob berolmagan." },
        { score: "11-15", desc: "Ijodiy va innovatsion, yangicha g‘oya bor, ammo savollarga to‘liq javob berolmagan." },
        { score: "16-20", desc: "Yangicha g‘oya, innovatsion yechimlar, barcha savollarga aniq va to‘liq javob." }
      ]
    },
    {
      id: "c5",
      name: "Loyihani amalga oshirishda kutilayotgan natijalar va analoglardan afzalligi",
      shortName: "Kutilayotgan natijalar",
      max: 20,
      levels: [
        { score: "1-5", desc: "Real muammolarni hal qilishga qaratilmagan yoki natijalar mavhum." },
        { score: "6-10", desc: "Qisman hal qiladi, ammo tatbiq etish imkoni mavjud emas." },
        { score: "11-15", desc: "Tatbiq etish imkoni bor, lekin analoglaridan afzalligi yo‘q." },
        { score: "16-20", desc: "Real muammolarni hal qiladi, iqtisodiy asoslangan, analoglaridan aniq afzal." }
      ]
    }
  ],

  // 3-ILOVA: Hakamlar hay'atining namunaviy tarkibi (7 nafar)
  judges: [
    { id: 1, name: "1-Hakam: Informatika fani o‘qituvchisi", role: "Informatika fani o‘qituvchisi", pin: "2001" },
    { id: 2, name: "2-Hakam: Fizika fani o‘qituvchisi", role: "Fizika fani o‘qituvchisi", pin: "2002" },
    { id: 3, name: "3-Hakam: Biologiya fani o‘qituvchisi", role: "Biologiya fani o‘qituvchisi", pin: "2003" },
    { id: 4, name: "4-Hakam: Kimyo fani o‘qituvchisi", role: "Kimyo fani o‘qituvchisi", pin: "2004" },
    { id: 5, name: "5-Hakam: Sohaga oid mutaxassis (IT)", role: "IT sohasi mutaxassisi", pin: "2005" },
    { id: 6, name: "6-Hakam: Sohaga oid mutaxassis (Ekologiya/Qishloq xo‘jaligi)", role: "Ekologiya/Agrar mutaxassis", pin: "2006" },
    { id: 7, name: "7-Hakam: Sohaga oid mutaxassis (Innovatsiya)", role: "Innovatsion ishlanmalar mutaxassisi", pin: "2007" }
  ],

  // 2-ILOVA: Tashkiliy qo'mita tarkibi
  committee: [
    { role: "Tashkiliy qo‘mita raisi", name: "Tuman maktabgacha va maktab ta’limi bo‘limi boshlig‘i" },
    { role: "A'zo", name: "Tuman Barkamol avlod bolalar maktabi direktori" },
    { role: "A'zo", name: "Tuman ishlab chiqarish / xizmat ko‘rsatish sohasi vakili" },
    { role: "A'zo", name: "IT sohasi mutaxassisi" },
    { role: "Mas'ul kotib", name: "Tarbiyaviy ishlarni muvofiqlashtirish bo‘limi bosh mutaxassisi" }
  ],

  // 5 ta rasmiy yo'nalish
  directions: [
    "Ta‘lim",
    "Axborot texnologiyalari (IT)",
    "Yashil energiya",
    "Ekologiya va iqlim o‘zgarishi",
    "Qishloq xo‘jaligi"
  ],

  // Maktablardan namunaviy jamoalar va loyihalar
  projects: [
    {
      id: 1,
      school: "1-son umumta'lim maktabi",
      projectName: "Aqlli quyosh panellari orientatsiya tizimi",
      direction: "Yashil energiya",
      isTeam: true,
      members: [
        { name: "O‘rozboyev Doniyorbek Alisher o‘g‘li", birthDate: "2010-04-12" },
        { name: "Yo‘ldoshev Jasurbek Bobur o‘g‘li", birthDate: "2010-08-25" }
      ],
      // Hakamlar qo'ygan mezon ballari: { judgeId: { c1: 9, c2: 23, c3: 24, c4: 18, c5: 19 } }
      evaluations: {
        1: { c1: 10, c2: 24, c3: 24, c4: 19, c5: 19 },
        2: { c1: 9, c2: 23, c3: 25, c4: 18, c5: 18 },
        3: { c1: 9, c2: 22, c3: 23, c4: 18, c5: 19 },
        4: { c1: 10, c2: 24, c3: 24, c4: 19, c5: 19 },
        5: { c1: 9, c2: 23, c3: 25, c4: 19, c5: 18 },
        6: { c1: 10, c2: 24, c3: 24, c4: 18, c5: 19 },
        7: { c1: 9, c2: 23, c3: 24, c4: 18, c5: 18 }
      }
    },
    {
      id: 2,
      school: "4-son IDUM",
      projectName: "AI-EkoDron: Ekinlarni masofadan kasalliklarini aniqlash",
      direction: "Qishloq xo‘jaligi",
      isTeam: false,
      members: [
        { name: "Karimova Mohinur Sanjar qizi", birthDate: "2010-02-15" }
      ],
      evaluations: {
        1: { c1: 10, c2: 25, c3: 25, c4: 20, c5: 20 },
        2: { c1: 10, c2: 24, c3: 25, c4: 20, c5: 19 },
        3: { c1: 10, c2: 25, c3: 24, c4: 19, c5: 20 },
        4: { c1: 10, c2: 24, c3: 25, c4: 20, c5: 19 },
        5: { c1: 10, c2: 25, c3: 25, c4: 20, c5: 20 },
        6: { c1: 10, c2: 25, c3: 25, c4: 20, c5: 20 },
        7: { c1: 10, c2: 24, c3: 24, c4: 19, c5: 19 }
      }
    },
    {
      id: 3,
      school: "12-son umumta'lim maktabi",
      projectName: "Maktab laboratoriyalari uchun arzon virtual simulyator",
      direction: "Ta‘lim",
      isTeam: true,
      members: [
        { name: "Matyoqubova Sabina Farhod qizi", birthDate: "2009-11-05" },
        { name: "Ro‘zmetova Dilnoza Mansur qizi", birthDate: "2010-01-20" },
        { name: "Otajonova Madina Komil qizi", birthDate: "2010-06-18" }
      ],
      evaluations: {
        1: { c1: 9, c2: 22, c3: 22, c4: 17, c5: 18 },
        2: { c1: 8, c2: 21, c3: 23, c4: 18, c5: 17 },
        3: { c1: 9, c2: 23, c3: 22, c4: 17, c5: 18 },
        4: { c1: 8, c2: 20, c3: 22, c4: 16, c5: 17 },
        5: { c1: 9, c2: 22, c3: 23, c4: 17, c5: 18 },
        6: { c1: 8, c2: 21, c3: 22, c4: 18, c5: 17 },
        7: { c1: 9, c2: 22, c3: 22, c4: 17, c5: 18 }
      }
    },
    {
      id: 4,
      school: "2-son IDUM",
      projectName: "Suvni tejovchi avtomatlashtirilgan tomchilatib sug‘orish datchigi",
      direction: "Ekologiya va iqlim o‘zgarishi",
      isTeam: false,
      members: [
        { name: "Bekchanov Sardorbek Otabek o‘g‘li", birthDate: "2010-09-10" }
      ],
      evaluations: {
        1: { c1: 9, c2: 24, c3: 24, c4: 19, c5: 19 },
        2: { c1: 10, c2: 23, c3: 24, c4: 18, c5: 19 },
        3: { c1: 9, c2: 23, c3: 23, c4: 19, c5: 18 },
        4: { c1: 10, c2: 24, c3: 24, c4: 18, c5: 19 },
        5: { c1: 9, c2: 24, c3: 24, c4: 19, c5: 18 },
        6: { c1: 9, c2: 23, c3: 24, c4: 18, c5: 19 },
        7: { c1: 10, c2: 24, c3: 23, c4: 19, c5: 18 }
      }
    },
    {
      id: 5,
      school: "18-son umumta'lim maktabi",
      projectName: "Bio-plastik: Organik chiqindilardan qadoqlash materiali olish",
      direction: "Ekologiya va iqlim o‘zgarishi",
      isTeam: true,
      members: [
        { name: "Jumaniyozov Bobur Davron o‘g‘li", birthDate: "2010-07-14" },
        { name: "Quryozov Sherzod Ilhom o‘g‘li", birthDate: "2010-12-01" }
      ],
      evaluations: {
        1: { c1: 8, c2: 19, c3: 20, c4: 16, c5: 17 },
        2: { c1: 8, c2: 20, c3: 21, c4: 17, c5: 16 },
        3: { c1: 9, c2: 20, c3: 20, c4: 16, c5: 17 },
        4: { c1: 9, c2: 21, c3: 21, c4: 17, c5: 17 },
        5: { c1: 8, c2: 19, c3: 20, c4: 16, c5: 16 },
        6: { c1: 9, c2: 20, c3: 21, c4: 17, c5: 17 },
        7: { c1: 8, c2: 19, c3: 20, c4: 16, c5: 16 }
      }
    }
  ]
};

// LocalStorage dan yuklash
function loadIxtirochilikData() {
  const saved = localStorage.getItem("ixtirochilik_data");
  if (saved) {
    try {
      return JSON.parse(saved);
    } catch (e) {
      console.error(e);
    }
  }
  saveIxtirochilikData(IXTIROCHILIK_CONFIG);
  return IXTIROCHILIK_CONFIG;
}

function saveIxtirochilikData(data) {
  localStorage.setItem("ixtirochilik_data", JSON.stringify(data));
}

// Nizom bo'yicha hisoblash va tenglikda ustunlik algoritmi
function calculateIxtirochilikRanking(projects) {
  const calculated = projects.map(proj => {
    let judgeTotalScores = []; // 7 ta hakamning umumiy ballari
    let criteriaAverages = { c1: 0, c2: 0, c3: 0, c4: 0, c5: 0 };
    let criteriaSums = { c1: 0, c2: 0, c3: 0, c4: 0, c5: 0 };
    let totalScoreSum = 0;
    let judgesCount = 0;

    for (let jId = 1; jId <= 7; jId++) {
      const ev = proj.evaluations ? proj.evaluations[jId] : null;
      if (ev) {
        const sumJ = (ev.c1 || 0) + (ev.c2 || 0) + (ev.c3 || 0) + (ev.c4 || 0) + (ev.c5 || 0);
        judgeTotalScores.push(sumJ > 0 ? sumJ : null);
        if (sumJ > 0) {
          totalScoreSum += sumJ;
          judgesCount++;
          criteriaSums.c1 += (ev.c1 || 0);
          criteriaSums.c2 += (ev.c2 || 0);
          criteriaSums.c3 += (ev.c3 || 0);
          criteriaSums.c4 += (ev.c4 || 0);
          criteriaSums.c5 += (ev.c5 || 0);
        }
      } else {
        judgeTotalScores.push(null);
      }
    }

    if (judgesCount > 0) {
      criteriaAverages.c1 = criteriaSums.c1 / judgesCount;
      criteriaAverages.c2 = criteriaSums.c2 / judgesCount;
      criteriaAverages.c3 = criteriaSums.c3 / judgesCount;
      criteriaAverages.c4 = criteriaSums.c4 / judgesCount;
      criteriaAverages.c5 = criteriaSums.c5 / judgesCount;
    }

    const finalAverage = judgesCount > 0 ? (totalScoreSum / judgesCount).toFixed(2) : "";

    return {
      ...proj,
      judgeTotalScores,
      criteriaAverages,
      judgesCount,
      totalScoreSum: judgesCount > 0 ? totalScoreSum : "",
      finalAverage: finalAverage,
      membersCount: proj.members ? proj.members.length : 1
    };
  });

  // Nizom bo'yicha saralash va Tie-breaker (tenglikda ustunlik berish):
  // 1) O'rtacha umumiy ball;
  // 2) 3-mezon (Texnik sifat);
  // 3) 2-mezon (Taqdimot);
  // 4) 4-mezon (Innovatsiya);
  // 5) 5-mezon (Kutilayotgan natijalar);
  // 6) 1-mezon (Yo'nalishga moslik);
  // 7) A'zolar soni kamligi (individual > kichik jamoa)
  calculated.sort((a, b) => {
    const scoreA = a.finalAverage !== "" ? Number(a.finalAverage) : -1;
    const scoreB = b.finalAverage !== "" ? Number(b.finalAverage) : -1;
    if (scoreB !== scoreA) return scoreB - scoreA;

    // 1-ustunlik: 3-mezon (Texnik sifat)
    if (b.criteriaAverages.c3 !== a.criteriaAverages.c3) {
      return b.criteriaAverages.c3 - a.criteriaAverages.c3;
    }
    // 2-ustunlik: 2-mezon (Taqdimot)
    if (b.criteriaAverages.c2 !== a.criteriaAverages.c2) {
      return b.criteriaAverages.c2 - a.criteriaAverages.c2;
    }
    // 3-ustunlik: 4-mezon (Innovatsiya)
    if (b.criteriaAverages.c4 !== a.criteriaAverages.c4) {
      return b.criteriaAverages.c4 - a.criteriaAverages.c4;
    }
    // 4-ustunlik: 5-mezon (Kutilayotgan natijalar)
    if (b.criteriaAverages.c5 !== a.criteriaAverages.c5) {
      return b.criteriaAverages.c5 - a.criteriaAverages.c5;
    }
    // 5-ustunlik: 1-mezon (Yo'nalish)
    if (b.criteriaAverages.c1 !== a.criteriaAverages.c1) {
      return b.criteriaAverages.c1 - a.criteriaAverages.c1;
    }
    // 6-ustunlik: a'zolar soni kamligi
    return a.membersCount - b.membersCount;
  });

  // O'rinlarni belgilash (1-, 2-, 3-o'rinlar viloyatga tavsiya etiladi)
  calculated.forEach((proj, idx) => {
    if (proj.finalAverage !== "") {
      proj.rank = idx + 1;
      proj.recommendedToRegion = (idx < 3); // 1-, 2-, 3-o'rinlar
    } else {
      proj.rank = "-";
      proj.recommendedToRegion = false;
    }
  });

  return calculated;
}
