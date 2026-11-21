// "Ixtirochilikka qadam" tanlovi (2-tuman bosqichi) - Rasmiy Nizom va Mezonlar Bazasi
// O'zbekiston Respublikasi Ta'lim va ilm-fan vazirligi xatiga 1-, 2-, 3-ilovalar asosida

const IXTIROCHILIK_CONFIG = {
  competitionName: "“Ixtiroçilikka qadam” tanlovi",
  stage: "Ikkinçi (tuman/şahar) bosqiçi",
  dates: "2026-yil 4–5-dekabr",
  maxScorePerJudge: 100,

  // 1-ILOVA: 5 ta rasmiy baholaş mezoni
  criteria: [
    {
      id: "c1",
      name: "Loyihaning tanlov yönalişlariga mos tayyorlanganligi",
      shortName: "Yönalişga moslik",
      max: 10,
      levels: [
        { score: "1-3", desc: "Loyiha tayyorlangan, lekin yönalişga mos kelmagan, maqsad aks etmagan." },
        { score: "4-6", desc: "Qisman mos, ammo yönaliş çuqur örganilmagan." },
        { score: "7-10", desc: "Töliq mos, çuqur örganilgan va mavjud muammolar töliq körsatilgan." }
      ]
    },
    {
      id: "c2",
      name: "Loyiha taqdimoti (prezentatsiya)",
      shortName: "Taqdimot",
      max: 25,
      levels: [
        { score: "1-6", desc: "Talab darajasida emas, texnik sust, vaqt reglamentiga rioya qilinmagan." },
        { score: "7-12", desc: "Sodda va tuşunarli, ammo savollarga töliq javob berilmagan." },
        { score: "13-18", desc: "Mantiqiy töğri, mazmunli, reglamentga rioya qilingan, ayrim xatoliklar bor." },
        { score: "19-25", desc: "Talab asosida, infografikali, savollarga töliq va aniq javob, reglamentga rioya qilingan." }
      ]
    },
    {
      id: "c3",
      name: "Loyihaning texnik jihatdan sifatli va puxta tayyorlanganligi (model, maket, işlanma)",
      shortName: "Texnik sifat (Model)",
      max: 25,
      levels: [
        { score: "1-6", desc: "Texnik jihatdan sust yoki amaliy işlanma mavjud emas." },
        { score: "7-12", desc: "Qisman yoki yarim tayyor holatda, texnik kamçiliklar mavjud." },
        { score: "13-18", desc: "Deyarli tayyor, işçi holatda, ammo baʼzi kamçiliklar bor." },
        { score: "19-25", desc: "Töliq tayyor, işçi model, barça elementlar puxta işlab çiqilgan." }
      ]
    },
    {
      id: "c4",
      name: "Loyihaning innovatsionligi va ijodiy yondaşuv",
      shortName: "Innovatsionlik",
      max: 20,
      levels: [
        { score: "1-5", desc: "Ijodiy yondaşuv yöq, odatiy usul, yangilik mavjud emas." },
        { score: "6-10", desc: "Qisman ijodiy, yangi texnologiyalar yetarli emas, töliq javob berolmagan." },
        { score: "11-15", desc: "Ijodiy va innovatsion, yangiça ğoya bor, ammo savollarga töliq javob berolmagan." },
        { score: "16-20", desc: "Yangiça ğoya, innovatsion yeçimlar, barça savollarga aniq va töliq javob." }
      ]
    },
    {
      id: "c5",
      name: "Loyihani amalga oşirişda kutilayotgan natijalar va analoglardan afzalligi",
      shortName: "Kutilayotgan natijalar",
      max: 20,
      levels: [
        { score: "1-5", desc: "Real muammolarni hal qilişga qaratilmagan yoki natijalar mavhum." },
        { score: "6-10", desc: "Qisman hal qiladi, ammo tatbiq etiş imkoni mavjud emas." },
        { score: "11-15", desc: "Tatbiq etiş imkoni bor, lekin analoglaridan afzalligi yöq." },
        { score: "16-20", desc: "Real muammolarni hal qiladi, iqtisodiy asoslangan, analoglaridan aniq afzal." }
      ]
    }
  ],

  // 3-ILOVA: Hakamlar hayʼatining tarkibi (7 nafar)
  judges: [
    { id: 1, name: "Abdullayev Rustam Alişeroviç", role: "Informatika fani öqituvçisi", pin: "2001" },
    { id: 2, name: "Karimov Sardor Baxtiyoroviç", role: "Fizika fani öqituvçisi", pin: "2002" },
    { id: 3, name: "Yöldoşeva Nilufar Ikromovna", role: "Biologiya fani öqituvçisi", pin: "2003" },
    { id: 4, name: "Rahimov Jasur Erkinoviç", role: "Kimyo fani öqituvçisi", pin: "2004" },
    { id: 5, name: "Qodirov Elyor Farhodoviç", role: "IT sohasi mutaxassisi", pin: "2005" },
    { id: 6, name: "Sobirov Otabek Uluğbekoviç", role: "Ekologiya va qişloq xöjaligi mutaxassisi", pin: "2006" },
    { id: 7, name: "Mansurov Bekzod Şuhratoviç", role: "Innovatsion işlanmalar mutaxassisi", pin: "2007" }
  ],

  // 2-ILOVA: Taşkiliy qömita tarkibi
  committee: [
    { role: "Taşkiliy qömita raisi", name: "Jumaniyazov Şokir Rözmetoviç", post: "Qöşköpir tuman taʼlim bölimi boşliği" },
    { role: "Taşkiliy qömita aʼzosi", name: "Erjanova Oygul Ilxombek qizi", post: "“Kelajak markazi” direktori" },
    { role: "Taşkiliy qömita aʼzosi", name: "Avezov Jasurbek Ravşanbekoviç", post: "Raqamli taʼlim va sunʼiy intellektni rivojlantiriş şöbasi boş mutaxassisi" },
    { role: "Taşkiliy qömita masʼul kotibi", name: "Mamatov Umrbek Oliquliyeviç", post: "Taşkiliy qömita masʼul kotibi" }
  ],

  // 5 ta rasmiy yönaliş
  directions: [
    "Taʼlim",
    "Axborot texnologiyalari (IT)",
    "Yaşil energiya",
    "Ekologiya va iqlim özgarişi",
    "Qişloq xöjaligi"
  ],

  // Maktablardan namunaviy jamoalar va loyihalar
  projects: [
  {
    "id": 1,
    "siteId": 1709,
    "school": "23-son umumiy örta taʼlim maktabi",
    "projectName": "Harakatlanuvçi qurilma",
    "direction": "Axborot texnologiyalari (IT)",
    "isTeam": true,
    "members": [
      {
        "name": "ABDULLAYEV JAMŞIDBEK DIYOR ÖĞLI",
        "birthDate": "2012-12-28",
        "grade": "8-sinf"
      },
      {
        "name": "OTAJONOV AKROMJON ĞULOMJON ÖĞLI",
        "birthDate": "2011-11-13",
        "grade": "9-sinf"
      }
    ],
    "evaluations": {}
  },
  {
    "id": 2,
    "siteId": 1660,
    "school": "30-son umumiy örta taʼlim maktabi",
    "projectName": "Robot yordamçi",
    "direction": "Axborot texnologiyalari (IT)",
    "isTeam": false,
    "members": [
      {
        "name": "RAVŞANBEKOV MIRJALOL MIRKAMOL ÖĞLI",
        "birthDate": "2014-11-19",
        "grade": "6-sinf"
      }
    ],
    "evaluations": {}
  },
  {
    "id": 3,
    "siteId": 1604,
    "school": "32-son umumiy örta taʼlim maktabi",
    "projectName": "Robototexnika",
    "direction": "Axborot texnologiyalari (IT)",
    "isTeam": false,
    "members": [
      {
        "name": "NORXONOV BUNYODBEK QUVANDIQ ÖĞLI",
        "birthDate": "2014-04-23",
        "grade": "7-sinf"
      }
    ],
    "evaluations": {}
  },
  {
    "id": 4,
    "siteId": 1575,
    "school": "9-IDUM",
    "projectName": "Robot ekskavator",
    "direction": "Axborot texnologiyalari (IT)",
    "isTeam": false,
    "members": [
      {
        "name": "MAŞARIPOV JAVOHIR HASANBOY ÖĞLI",
        "birthDate": "2012-09-07",
        "grade": "7-sinf"
      }
    ],
    "evaluations": {}
  },
  {
    "id": 5,
    "siteId": 1470,
    "school": "25-son umumiy örta taʼlim maktabi",
    "projectName": "Robototexnika",
    "direction": "Axborot texnologiyalari (IT)",
    "isTeam": false,
    "members": [
      {
        "name": "PÖLATOV NURBEK MUXAMMAD ÖĞLI",
        "birthDate": "2014-08-26",
        "grade": "6-sinf"
      }
    ],
    "evaluations": {}
  },
  {
    "id": 6,
    "siteId": 1406,
    "school": "6-son umumiy örta taʼlim maktabi",
    "projectName": "AGRO ROBOT (GROWERX)",
    "direction": "Qişloq xöjaligi",
    "isTeam": false,
    "members": [
      {
        "name": "FAYZULLAYEV BOYMUROD BOBOMUROD ÖĞLI",
        "birthDate": "2009-10-23",
        "grade": "11-sinf"
      }
    ],
    "evaluations": {}
  },
  {
    "id": 7,
    "siteId": 1374,
    "school": "51-son umumiy örta taʼlim maktabi",
    "projectName": "Quyoş energiyasida işlaydigan öt maydalagiç",
    "direction": "Qişloq xöjaligi",
    "isTeam": true,
    "members": [
      {
        "name": "RAJABOV ELMUROD XOLMUROD ÖĞLI",
        "birthDate": "2013-09-21",
        "grade": "7-sinf"
      },
      {
        "name": "BEKÇANOV KAMRONBEK OZODBOY ÖĞLI",
        "birthDate": "2012-08-10",
        "grade": "8-sinf"
      },
      {
        "name": "BAXTIYOROV KAMRONBEK ELDORBEK ÖĞLI",
        "birthDate": "2014-07-21",
        "grade": "6-sinf"
      }
    ],
    "evaluations": {}
  },
  {
    "id": 8,
    "siteId": 1331,
    "school": "20-son umumiy örta taʼlim maktabi",
    "projectName": "Robot yordamçi",
    "direction": "Axborot texnologiyalari (IT)",
    "isTeam": true,
    "members": [
      {
        "name": "OTAMURODOV BILOLBEK BUNYOD ÖĞLI",
        "birthDate": "2015-08-20",
        "grade": "5-sinf"
      },
      {
        "name": "ŞUXRATOV ABDULAZIZ ABDULLA ÖĞLI",
        "birthDate": "2015-07-31",
        "grade": "5-sinf"
      }
    ],
    "evaluations": {}
  },
  {
    "id": 9,
    "siteId": 1256,
    "school": "5-IDUM",
    "projectName": "Energiya tejaydigan uy",
    "direction": "Yaşil energiya",
    "isTeam": true,
    "members": [
      {
        "name": "SANJARBEKOV MIRALI SANJARBEK ÖĞLI",
        "birthDate": "2011-08-27",
        "grade": "9-sinf"
      },
      {
        "name": "QADAMBOYEV JÖŞQINBEK MANSURBEK ÖĞLI",
        "birthDate": "2013-09-20",
        "grade": "7-sinf"
      },
      {
        "name": "RAVŞANBEKOV ASADBEK ISLOMBEK ÖĞLI",
        "birthDate": "2013-08-05",
        "grade": "7-sinf"
      }
    ],
    "evaluations": {}
  },
  {
    "id": 10,
    "siteId": 816,
    "school": "14-son umumiy örta taʼlim maktabi",
    "projectName": "Robot-yordamçi",
    "direction": "Yaşil energiya",
    "isTeam": false,
    "members": [
      {
        "name": "OMONBOYEV NOSIRBEK NODIRBEKOVIÇ",
        "birthDate": "2013-04-12",
        "grade": "7-sinf"
      }
    ],
    "evaluations": {}
  },
  {
    "id": 11,
    "siteId": 198,
    "school": "42-son umumiy örta taʼlim maktabi",
    "projectName": "Aqlli uy",
    "direction": "Axborot texnologiyalari (IT)",
    "isTeam": true,
    "members": [
      {
        "name": "DÖŞÇANOV MURODBEK UMRBEK ÖĞLI",
        "birthDate": "2014-11-19",
        "grade": "6-sinf"
      },
      {
        "name": "SULTONMUROTOV ERKABOY ULUĞBEK ÖĞLI",
        "birthDate": "2014-03-10",
        "grade": "6-sinf"
      }
    ],
    "evaluations": {}
  },
  {
    "id": 12,
    "siteId": 139,
    "school": "19-son umumiy örta taʼlim maktabi",
    "projectName": "Robot maşina",
    "direction": "Axborot texnologiyalari (IT)",
    "isTeam": false,
    "members": [
      {
        "name": "OTANAZAROV XOLMIRZO ERGAŞ ÖĞLI",
        "birthDate": "2011-10-15",
        "grade": "9-sinf"
      }
    ],
    "evaluations": {}
  },
  {
    "id": 13,
    "siteId": 1771,
    "school": "29-son umumiy örta taʼlim maktabi",
    "projectName": "Batareya yordamida harakatlanuvçi maşina",
    "direction": "Axborot texnologiyalari (IT)",
    "isTeam": false,
    "members": [
      {
        "name": "SOBIROV ŞOHJAHON XURMATBEK ÖĞLI",
        "birthDate": "2012-06-10",
        "grade": "8-sinf"
      }
    ],
    "evaluations": {}
  },
  {
    "id": 14,
    "siteId": 1916,
    "school": "2-son umumiy örta taʼlim maktabi",
    "projectName": "Yaşil energiya",
    "direction": "Yaşil energiya",
    "isTeam": false,
    "members": [
      {
        "name": "XAYITBOYEV JAMŞIDBEK NODIRBEK ÖĞLI",
        "birthDate": "2011-05-09",
        "grade": "9-sinf"
      }
    ],
    "evaluations": {}
  },
  {
    "id": 15,
    "siteId": 1831,
    "school": "18-son umumiy örta taʼlim maktabi",
    "projectName": "Ixtiroçilikka qadam",
    "direction": "Ekologiya va iqlim özgarişi",
    "isTeam": true,
    "members": [
      {
        "name": "ARSLONOV MUSTAFO SARDORBEK ÖĞLI",
        "birthDate": "2012-07-27",
        "grade": "7-sinf"
      },
      {
        "name": "YUSUPOV ZEXRIDDIN SARVAR ÖĞLI",
        "birthDate": "2013-01-13",
        "grade": "7-sinf"
      }
    ],
    "evaluations": {}
  },
  {
    "id": 16,
    "siteId": 1814,
    "school": "4-son umumiy örta taʼlim maktabi",
    "projectName": "Foydali texnikalar",
    "direction": "Ekologiya va iqlim özgarişi",
    "isTeam": false,
    "members": [
      {
        "name": "RÖZMATOV RÖZMATBOY XUŞNUDBEK ÖĞLI",
        "birthDate": "2012-08-14",
        "grade": "8-sinf"
      }
    ],
    "evaluations": {}
  },
  {
    "id": 17,
    "siteId": 2050,
    "school": "48-son umumiy örta taʼlim maktabi",
    "projectName": "Bilimscan AI",
    "direction": "Axborot texnologiyalari (IT)",
    "isTeam": true,
    "members": [
      {
        "name": "ATABEKOV XASANBOY MANSURBEK ÖĞLI",
        "birthDate": "2012-08-29",
        "grade": "9-sinf"
      },
      {
        "name": "SABIROV RÖZMAT RASULBEK ÖĞLI",
        "birthDate": "2010-12-09",
        "grade": "10-sinf"
      },
      {
        "name": "OLIMBAYEV YUNUSBEK XURSANDBEK ÖĞLI",
        "birthDate": "2009-11-20",
        "grade": "11-sinf"
      }
    ],
    "evaluations": {}
  }
]
};

// LocalStorage dan yuklash
function loadIxtirochilikData() {
  let data = null;
  const saved = localStorage.getItem("ixtirochilik_data_v5") || localStorage.getItem("ixtirochilik_data_v4");
  if (saved) {
    try {
      data = JSON.parse(saved);
    } catch (e) {
      data = null;
    }
  }

  if (!data) {
    data = JSON.parse(JSON.stringify(IXTIROCHILIK_CONFIG));
  } else {
    data.judges = IXTIROCHILIK_CONFIG.judges;
    data.committee = IXTIROCHILIK_CONFIG.committee;
    data.directions = IXTIROCHILIK_CONFIG.directions;
    data.criteria = IXTIROCHILIK_CONFIG.criteria;

    if (!Array.isArray(data.projects)) data.projects = [];

    // Barcha yangi loyihalarni saqlangan baholarni yo'qotmagan holda qo'shish
    IXTIROCHILIK_CONFIG.projects.forEach(cp => {
      const existing = data.projects.find(p => p.id === cp.id || p.siteId === cp.siteId);
      if (!existing) {
        data.projects.push(JSON.parse(JSON.stringify(cp)));
      } else {
        existing.school = cp.school;
        existing.projectName = cp.projectName;
        existing.direction = cp.direction;
        existing.members = cp.members;
        existing.isTeam = cp.isTeam;
        existing.siteId = cp.siteId;
      }
    });

    data.projects.sort((a, b) => a.id - b.id);
  }

  saveIxtirochilikData(data);
  return data;
}

function saveIxtirochilikData(data) {
  try {
    localStorage.setItem("ixtirochilik_data_v5", JSON.stringify(data));
    localStorage.setItem("ixtirochilik_data_v4", JSON.stringify(data));
  } catch (e) {
    console.warn("Saqlashda xatolik:", e);
  }
}

// Nizom bo'yicha hisoblash va tenglikda ustunlik algoritmi (Tie-breaker)
function calculateIxtirochilikRanking(projects) {
  const calculated = projects.map(proj => {
    let judgeTotalScores = []; // 7 ta hakamning umumiy ballari
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

    let criteriaAverages = { c1: 0, c2: 0, c3: 0, c4: 0, c5: 0 };
    if (judgesCount > 0) {
      criteriaAverages.c1 = Number((criteriaSums.c1 / judgesCount).toFixed(3));
      criteriaAverages.c2 = Number((criteriaSums.c2 / judgesCount).toFixed(3));
      criteriaAverages.c3 = Number((criteriaSums.c3 / judgesCount).toFixed(3));
      criteriaAverages.c4 = Number((criteriaSums.c4 / judgesCount).toFixed(3));
      criteriaAverages.c5 = Number((criteriaSums.c5 / judgesCount).toFixed(3));
    }

    const finalAverage = judgesCount > 0 ? (totalScoreSum / judgesCount).toFixed(2) : "";

    // Jamoa a'zolari soni (kamroq a'zoli jamoaga ustunlik)
    const membersCount = (proj.members && proj.members.length > 0) ? proj.members.length : 1;

    // Jamoa a'zolarining o'rtacha tug'ilgan sanasi va yoshi (yoshroqqa ustunlik)
    let totalBirthTime = 0;
    let validDatesCount = 0;
    if (proj.members && proj.members.length > 0) {
      proj.members.forEach(m => {
        if (m.birthDate) {
          const dt = new Date(m.birthDate);
          if (!isNaN(dt.getTime())) {
            totalBirthTime += dt.getTime();
            validDatesCount++;
          }
        }
      });
    }
    const avgBirthTimestamp = validDatesCount > 0 ? Math.round(totalBirthTime / validDatesCount) : 0;
    const nowMs = new Date("2026-12-04").getTime();
    const avgAgeYears = avgBirthTimestamp > 0 ? Number(((nowMs - avgBirthTimestamp) / (365.25 * 24 * 3600 * 1000)).toFixed(1)) : null;

    return {
      ...proj,
      judgeTotalScores,
      criteriaAverages,
      judgesCount,
      totalScoreSum: judgesCount > 0 ? totalScoreSum : "",
      finalAverage: finalAverage,
      membersCount: membersCount,
      avgBirthTimestamp: avgBirthTimestamp,
      avgAgeYears: avgAgeYears
    };
  });

  // Nizom bo'yicha qat'iy ketma-ketlikda saralash va Tie-breaker (tenglikda ustunlik berish):
  // 0) Umumiy o'rtacha ball (eng yuqori)
  // 1) 3-mezon: Loyihaning texnik jihatdan sifatli va puxta tayyorlanganligi (model/maket/dastur)
  // 2) 2-mezon: Loyiha taqdimoti (prezentatsiya sifati, savol-javob, reglament)
  // 3) 4-mezon: Loyihaning innovatsionligi va ijodiy yondashilganligi
  // 4) 5-mezon: Loyihani amalga oshirishda kutilayotgan natijalar va analoglardan afzalligi
  // 5) 1-mezon: Loyihaning tanlov yönalişlariga mos tayyorlanganligi
  // 6) Iştirokçilar soni: Dastlab individual ishtirokchiga (1 kishi), so‘ngra a’zolari kam bo‘lgan jamoaga ustunlik
  // 7) Tug‘ilgan sanasi bo‘yicha: Yoshroq (jamoaning o‘rtacha yoshi kichikroq, kechroq tug‘ilgan) ishtirokchilarga ustunlik
  calculated.sort((a, b) => {
    const scoreA = a.finalAverage !== "" ? Number(a.finalAverage) : -1;
    const scoreB = b.finalAverage !== "" ? Number(b.finalAverage) : -1;
    if (scoreB !== scoreA) return scoreB - scoreA;

    // Agar ikkalasi ham hali baholanmagan bo'lsa (ball yo'q), dastlabki id tartibida turadi
    if (scoreA === -1 && scoreB === -1) return a.id - b.id;

    // 1-ustunlik: 3-mezon (Texnik jihatdan sifatli va puxta tayyorlanganligi)
    if (b.criteriaAverages.c3 !== a.criteriaAverages.c3) {
      return b.criteriaAverages.c3 - a.criteriaAverages.c3;
    }

    // 2-ustunlik: 2-mezon (Loyiha taqdimoti)
    if (b.criteriaAverages.c2 !== a.criteriaAverages.c2) {
      return b.criteriaAverages.c2 - a.criteriaAverages.c2;
    }

    // 3-ustunlik: 4-mezon (Innovatsionligi va ijodiy yondashilganligi)
    if (b.criteriaAverages.c4 !== a.criteriaAverages.c4) {
      return b.criteriaAverages.c4 - a.criteriaAverages.c4;
    }

    // 4-ustunlik: 5-mezon (Kutilayotgan natijalar va analoglardan afzalligi)
    if (b.criteriaAverages.c5 !== a.criteriaAverages.c5) {
      return b.criteriaAverages.c5 - a.criteriaAverages.c5;
    }

    // 5-ustunlik: 1-mezon (Tanlov yönalişlariga mos tayyorlanganligi)
    if (b.criteriaAverages.c1 !== a.criteriaAverages.c1) {
      return b.criteriaAverages.c1 - a.criteriaAverages.c1;
    }

    // 6-ustunlik: Iştirokçilar soni (individual 1 kishi > kam a'zoli jamoa)
    if (a.membersCount !== b.membersCount) {
      return a.membersCount - b.membersCount;
    }

    // 7-ustunlik: Tug'ilgan sanasi bo'yicha yoshroq ishtirokchilarga ustunlik (kechroq tug'ilgan = timestamp katta)
    if (b.avgBirthTimestamp !== a.avgBirthTimestamp) {
      return b.avgBirthTimestamp - a.avgBirthTimestamp;
    }

    return a.id - b.id;
  });

  // O'rinlarni belgilash (1-, 2-, 3-o'rinlar viloyatga tavsiya etiladi)
  calculated.forEach((proj, idx) => {
    if (proj.finalAverage !== "") {
      proj.rank = idx + 1;
      proj.recommendedToRegion = (idx < 3); // 1-, 2-, 3-o'rinlar viloyat bosqichiga yo'llanma oladi
    } else {
      proj.rank = "-";
      proj.recommendedToRegion = false;
    }
  });

  return calculated;
}


// =========================================================================
// GOOGLE SHEETS JONLI SINXRONLASH VA PIN TEKSHIRISH
// =========================================================================
function getGoogleSheetsApiUrl() {
  return localStorage.getItem("ixtirochilik_sheets_api_url") || "https://script.google.com/macros/s/AKfycbzaL-LBrctvYGw_NxpSZ9IyfbH2zK_oP106ZzYIXEEE-GT-nk1Lzb8-oMQATs0tFdtofQ/exec";
}

function setGoogleSheetsApiUrl(url) {
  localStorage.setItem("ixtirochilik_sheets_api_url", url ? url.trim() : "");
}

async function syncScoreToGoogleSheets(projectId, judgeId, scores) {
  const url = getGoogleSheetsApiUrl();
  if (!url) return { ok: false, localOnly: true };

  try {
    await fetch(url, {
      method: "POST",
      mode: "no-cors",
      headers: { "Content-Type": "text/plain;charset=utf-8" },
      body: JSON.stringify({
        action: "save_score",
        projectId: projectId,
        judgeId: judgeId,
        scores: scores
      })
    });
    return { ok: true };
  } catch (err) {
    console.warn("Google Sheetga yuborishda xatolik:", err);
    return { ok: false, error: err };
  }
}

async function fetchLiveScoresFromGoogleSheets() {
  const url = getGoogleSheetsApiUrl();
  if (!url) return null;

  try {
    const sep = url.includes("?") ? "&" : "?";
    const res = await fetch(`${url}${sep}action=get_data&_t=${Date.now()}`, { cache: "no-store" });
    const json = await res.json();
    if (json && json.status === "success" && json.evaluations && typeof json.evaluations === "object") {
      // Faqat haqiqiy (0 dan katta) baholarni qoldiramiz; Sheet'da o'chirilgan/bo'shatilgan baholar saytda ham o'chadi
      const cleaned = {};
      Object.keys(json.evaluations).forEach(projId => {
        const projEvals = json.evaluations[projId] || {};
        const cleanProj = {};
        Object.keys(projEvals).forEach(jId => {
          const ev = projEvals[jId];
          if (ev) {
            const total = (Number(ev.c1) || 0) + (Number(ev.c2) || 0) + (Number(ev.c3) || 0) + (Number(ev.c4) || 0) + (Number(ev.c5) || 0);
            if (total > 0) {
              cleanProj[jId] = {
                c1: Number(ev.c1) || 0,
                c2: Number(ev.c2) || 0,
                c3: Number(ev.c3) || 0,
                c4: Number(ev.c4) || 0,
                c5: Number(ev.c5) || 0
              };
            }
          }
        });
        if (Object.keys(cleanProj).length > 0) {
          cleaned[projId] = cleanProj;
        }
      });
      return cleaned;
    }
  } catch (err) {
    console.warn("Google Sheetdan o'qishda xatolik:", err);
  }
  return null;
}

// Mas'ul (Admin) PIN-kodini tekshirish (Google Sheet'dagi ADMIN qatoridan jonli tekshiradi)
async function verifyAdminPin(enteredPin) {
  if (!enteredPin) return false;
  const cleanPin = String(enteredPin).trim();
  const url = getGoogleSheetsApiUrl();

  if (url) {
    let sheetResponded = false;
    const sep = url.includes("?") ? "&" : "?";

    // 1-urinish: verify_admin_pin amaliyoti
    try {
      const res = await fetch(`${url}${sep}action=verify_admin_pin&pin=${encodeURIComponent(cleanPin)}&_t=${Date.now()}`, { cache: "no-store" });
      const json = await res.json();
      if (json && typeof json.valid === "boolean") {
        sheetResponded = true;
        if (json.valid) return true;
      }
    } catch (err) {
      // Davom etamiz
    }

    // 2-urinish: verify_pin orqali (Hakamlar sheetidagi ADMIN qatori)
    try {
      const res2 = await fetch(`${url}${sep}action=verify_pin&pin=${encodeURIComponent(cleanPin)}&_t=${Date.now()}`, { cache: "no-store" });
      const json2 = await res2.json();
      if (json2 && typeof json2.valid === "boolean") {
        sheetResponded = true;
        if (json2.valid && json2.judge) {
          const role = String(json2.judge.role || "");
          const name = String(json2.judge.name || "");
          if (role.toLowerCase().includes("admin") || name.toLowerCase().includes("mamatov") || json2.judge.id === null) {
            return true;
          }
        }
      }
    } catch (err2) {
      // Davom etamiz
    }

    // Agar Google Sheet javob bergan bo'lsa va PIN mos kelmasa — qat'iy rad etamiz!
    if (sheetResponded) {
      return false;
    }
  }

  // Faqat internet/Sheet umuman ulanmagan holatda zaxira tekshiruv
  return cleanPin === "7788";
}
