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

  // 3-ILOVA: Hakamlar hay'atining tarkibi (7 nafar)
  judges: [
    { id: 1, name: "Abdullayev Rustam Alisherovich", role: "Informatika fani o‘qituvchisi", pin: "2001" },
    { id: 2, name: "Karimov Sardor Baxtiyorovich", role: "Fizika fani o‘qituvchisi", pin: "2002" },
    { id: 3, name: "Yo‘ldosheva Nilufar Ikromovna", role: "Biologiya fani o‘qituvchisi", pin: "2003" },
    { id: 4, name: "Rahimov Jasur Erkinovich", role: "Kimyo fani o‘qituvchisi", pin: "2004" },
    { id: 5, name: "Qodirov Elyor Farhodovich", role: "IT sohasi mutaxassisi", pin: "2005" },
    { id: 6, name: "Sobirov Otabek Ulug‘bekovich", role: "Ekologiya va qishloq xo‘jaligi mutaxassisi", pin: "2006" },
    { id: 7, name: "Mansurov Bekzod Shuhratovich", role: "Innovatsion ishlanmalar mutaxassisi", pin: "2007" }
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
          "id": 1,
          "siteId": 1709,
          "school": "23-son umumiy o‘rta ta’lim maktabi",
          "projectName": "Harakatlanuvchi qurilma",
          "direction": "Axborot texnologiyalari (IT)",
          "isTeam": true,
          "members": [
              {
                  "name": "ABDULLAYEV JAMSHIDBEK DIYOR O‘G‘LI",
                  "birthDate": "2012-12-28",
                  "grade": "8-sinf"
              },
              {
                  "name": "OTAJONOV AKROMJON G‘ULOMJON O‘G‘LI",
                  "birthDate": "2011-11-13",
                  "grade": "9-sinf"
              }
          ],
          "evaluations": {}
      },
      {
          "id": 2,
          "siteId": 1660,
          "school": "30-son umumiy o‘rta ta’lim maktabi",
          "projectName": "Robot yordamchi",
          "direction": "Axborot texnologiyalari (IT)",
          "isTeam": false,
          "members": [
              {
                  "name": "RAVSHANBEKOV MIRJALOL MIRKAMOL O‘G‘LI",
                  "birthDate": "2014-11-19",
                  "grade": "6-sinf"
              }
          ],
          "evaluations": {}
      },
      {
          "id": 3,
          "siteId": 1604,
          "school": "32-son umumiy o‘rta ta’lim maktabi",
          "projectName": "Robototexnika",
          "direction": "Axborot texnologiyalari (IT)",
          "isTeam": false,
          "members": [
              {
                  "name": "NORXONOV BUNYODBEK QUVANDIQ O‘G‘LI",
                  "birthDate": "2014-04-23",
                  "grade": "7-sinf"
              }
          ],
          "evaluations": {}
      },
      {
          "id": 4,
          "siteId": 1575,
          "school": "9-son ixtisoslashtirilgan maktab",
          "projectName": "Robot ekskavator",
          "direction": "Axborot texnologiyalari (IT)",
          "isTeam": false,
          "members": [
              {
                  "name": "MASHARIPOV JAVOHIR HASANBOY O‘G‘LI",
                  "birthDate": "2012-09-07",
                  "grade": "7-sinf"
              }
          ],
          "evaluations": {}
      },
      {
          "id": 5,
          "siteId": 1470,
          "school": "25-son umumiy o‘rta ta’lim maktabi",
          "projectName": "Robototexnika",
          "direction": "Axborot texnologiyalari (IT)",
          "isTeam": false,
          "members": [
              {
                  "name": "PO‘LATOV NURBEK MUXAMMAD O‘G‘LI",
                  "birthDate": "2014-08-26",
                  "grade": "6-sinf"
              }
          ],
          "evaluations": {}
      },
      {
          "id": 6,
          "siteId": 1406,
          "school": "6-son umumiy o‘rta ta’lim maktabi",
          "projectName": "AGRO ROBOT (GROWERX)",
          "direction": "Qishloq xo‘jaligi",
          "isTeam": false,
          "members": [
              {
                  "name": "FAYZULLAYEV BOYMUROD BOBOMUROD O‘G‘LI",
                  "birthDate": "2009-10-23",
                  "grade": "11-sinf"
              }
          ],
          "evaluations": {}
      },
      {
          "id": 7,
          "siteId": 1374,
          "school": "51-son umumiy o‘rta ta’lim maktabi",
          "projectName": "Quyosh energiyasida ishlaydigan o‘t maydalagich",
          "direction": "Qishloq xo‘jaligi",
          "isTeam": true,
          "members": [
              {
                  "name": "RAJABOV ELMUROD XOLMUROD O‘G‘LI",
                  "birthDate": "2013-09-21",
                  "grade": "7-sinf"
              },
              {
                  "name": "BEKCHANOV KAMRONBEK OZODBOY O‘G‘LI",
                  "birthDate": "2012-08-10",
                  "grade": "8-sinf"
              },
              {
                  "name": "BAXTIYOROV KAMRONBEK ELDORBEK O‘G‘LI",
                  "birthDate": "2014-07-21",
                  "grade": "6-sinf"
              }
          ],
          "evaluations": {}
      },
      {
          "id": 8,
          "siteId": 1331,
          "school": "20-son umumiy o‘rta ta’lim maktabi",
          "projectName": "Robot yordamchi",
          "direction": "Axborot texnologiyalari (IT)",
          "isTeam": true,
          "members": [
              {
                  "name": "OTAMURODOV BILOLBEK BUNYOD O‘G‘LI",
                  "birthDate": "2015-08-20",
                  "grade": "5-sinf"
              },
              {
                  "name": "SHUXRATOV ABDULAZIZ ABDULLA O‘G‘LI",
                  "birthDate": "2015-07-31",
                  "grade": "5-sinf"
              }
          ],
          "evaluations": {}
      },
      {
          "id": 9,
          "siteId": 1256,
          "school": "5-son ixtisoslashtirilgan maktab",
          "projectName": "Energiya tejaydigan uy",
          "direction": "Yashil energiya",
          "isTeam": true,
          "members": [
              {
                  "name": "SANJARBEKOV MIRALI SANJARBEK O‘G‘LI",
                  "birthDate": "2011-08-27",
                  "grade": "9-sinf"
              },
              {
                  "name": "QADAMBOYEV JO‘SHQINBEK MANSURBEK O‘G‘LI",
                  "birthDate": "2013-09-20",
                  "grade": "7-sinf"
              },
              {
                  "name": "RAVSHANBEKOV ASADBEK ISLOMBEK O‘G‘LI",
                  "birthDate": "2013-08-05",
                  "grade": "7-sinf"
              }
          ],
          "evaluations": {}
      },
      {
          "id": 10,
          "siteId": 816,
          "school": "14-son umumiy o‘rta ta’lim maktabi",
          "projectName": "Robot-yordamchi",
          "direction": "Yashil energiya",
          "isTeam": false,
          "members": [
              {
                  "name": "OMONBOYEV NOSIRBEK NODIRBEKOVICH",
                  "birthDate": "2013-04-12",
                  "grade": "7-sinf"
              }
          ],
          "evaluations": {}
      },
      {
          "id": 11,
          "siteId": 198,
          "school": "42-son umumiy o‘rta ta’lim maktabi",
          "projectName": "Aqlli uy",
          "direction": "Axborot texnologiyalari (IT)",
          "isTeam": true,
          "members": [
              {
                  "name": "DO‘SCHANOV MURODBEK UMRBEK O‘G‘LI",
                  "birthDate": "2014-11-19",
                  "grade": "6-sinf"
              },
              {
                  "name": "SULTONMUROTOV ERKABOY ULUG‘BEK O‘G‘LI",
                  "birthDate": "2014-03-10",
                  "grade": "6-sinf"
              }
          ],
          "evaluations": {}
      },
      {
          "id": 12,
          "siteId": 139,
          "school": "19-son umumiy o‘rta ta’lim maktabi",
          "projectName": "Robot mashina",
          "direction": "Axborot texnologiyalari (IT)",
          "isTeam": false,
          "members": [
              {
                  "name": "OTANAZAROV XOLMIRZO ERGASH O‘G‘LI",
                  "birthDate": "2011-10-15",
                  "grade": "9-sinf"
              }
          ],
          "evaluations": {}
      },
      {
          "id": 13,
          "siteId": 1771,
          "school": "29-son umumiy o‘rta ta’lim maktabi",
          "projectName": "Batareya yordamida harakatlanuvchi mashina",
          "direction": "Axborot texnologiyalari (IT)",
          "isTeam": false,
          "members": [
              {
                  "name": "SOBIROV SHOHJAHON XURMATBEK O‘G‘LI",
                  "birthDate": "2012-06-10",
                  "grade": "8-sinf"
              }
          ],
          "evaluations": {}
      }
  ]
};

// LocalStorage dan yuklash
function loadIxtirochilikData() {
  const saved = localStorage.getItem("ixtirochilik_data_v4");
  if (saved) {
    try {
      const parsed = JSON.parse(saved);
      parsed.judges = IXTIROCHILIK_CONFIG.judges;
      return parsed;
    } catch (e) {
      console.error(e);
    }
  }
  saveIxtirochilikData(IXTIROCHILIK_CONFIG);
  return IXTIROCHILIK_CONFIG;
}

function saveIxtirochilikData(data) {
  localStorage.setItem("ixtirochilik_data_v4", JSON.stringify(data));
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
      headers: { "Content-Type": "application/json" },
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
    const res = await fetch(url + (url.includes("?") ? "&" : "?") + "action=get_data");
    const json = await res.json();
    if (json && json.status === "success" && json.evaluations) {
      return json.evaluations;
    }
  } catch (err) {
    console.warn("Google Sheetdan o'qishda xatolik:", err);
  }
  return null;
}

// Mas'ul (Admin) PIN-kodini tekshirish (Qulfni ochish uchun)
async function verifyAdminPin(enteredPin) {
  if (!enteredPin) return false;
  const cleanPin = String(enteredPin).trim();
  const url = getGoogleSheetsApiUrl();

  if (url) {
    // 1-urinish: verify_admin_pin amaliyoti
    try {
      const res = await fetch(url + (url.includes("?") ? "&" : "?") + "action=verify_admin_pin&pin=" + encodeURIComponent(cleanPin));
      const json = await res.json();
      if (json && json.valid) {
        return true;
      }
    } catch (err) {
      // Davom etamiz
    }

    // 2-urinish: verify_pin orqali (Hakamlar sheetidagi ADMIN qatori)
    try {
      const res2 = await fetch(url + (url.includes("?") ? "&" : "?") + "action=verify_pin&pin=" + encodeURIComponent(cleanPin));
      const json2 = await res2.json();
      if (json2 && json2.valid && json2.judge) {
        const role = String(json2.judge.role || "");
        const name = String(json2.judge.name || "");
        if (role.toLowerCase().includes("admin") || name.toLowerCase().includes("mamatov") || json2.judge.id === null) {
          return true;
        }
      }
    } catch (err2) {
      // Davom etamiz
    }
  }

  // 3-urinish: Zaxira doimiy admin PIN-kodi
  return cleanPin === "7788";
}
