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
      name: "Loyihaning tanlov yõnalişlariga mos tayyorlanganligi",
      shortName: "Yõnalişga moslik",
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
      name: "Loyihaning innovacionligi va ijodiy yondaşuv",
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

  // 2-ILOVA: Tashkiliy qõmita tarkibi
  committee: [
    { role: "Tashkiliy qõmita raisi", name: "Jumaniyazov Şokir Rõzmetoviç", post: "Qõşkõpir tuman maktabgaça va maktab taʼlimi bõlimi başliğõ" },
    { role: "Tashkiliy qõmita aʼzosi", name: "Erjanova Oygul Ilxombek qizi", post: "«Kelajak markazi» direktori" },
    { role: "Tashkiliy qõmita aʼzosi", name: "Avezov Jasurbek Ravşanbekoviç", post: "Raqamli taʼlim va sunʼiy intellektni rivojlantiriş şõbasi baş mutaxassisi" },
    { role: "Tashkiliy qõmita masʼul kotibi", name: "Mamatov Umrbek Oliquliyeviç", post: "Tashkiliy qõmita masʼul kotibi" }
  ],

  // 5 ta rasmiy yo'nalish
  directions: [
    "Taʼlim",
    "Axborot texnologiyalari (IT)",
    "Yaşil energiya",
    "Ekologiya va iqlim õzgarişi",
    "Qişloq xõjaligi"
  ],

  // Maktablardan namunaviy jamoalar va loyihalar
  projects: [
      {
          "id": 1,
          "siteId": 1709,
          "school": "23-son umumiy õrta taʼlim maktabi",
          "projectName": "Harakatlanuvchi qurilma",
          "direction": "Axborot texnologiyalari (IT)",
          "isTeam": true,
          "members": [
              {
                  "name": "ABDULLAYEV JAMŞIDBEK DIYOR ÕĞLI",
                  "birthDate": "2012-12-28",
                  "grade": "8-sinf"
              },
              {
                  "name": "OTAJONOV AKROMJON ĞULOMJON ÕĞLI",
                  "birthDate": "2011-11-13",
                  "grade": "9-sinf"
              }
          ],
          "evaluations": {}
      },
      {
          "id": 2,
          "siteId": 1660,
          "school": "30-son umumiy õrta taʼlim maktabi",
          "projectName": "Robot yordamchi",
          "direction": "Axborot texnologiyalari (IT)",
          "isTeam": false,
          "members": [
              {
                  "name": "RAVŞANBEKOV MIRJALOL MIRKAMOL ÕĞLI",
                  "birthDate": "2014-11-19",
                  "grade": "6-sinf"
              }
          ],
          "evaluations": {}
      },
      {
          "id": 3,
          "siteId": 1604,
          "school": "32-son umumiy õrta taʼlim maktabi",
          "projectName": "Robototexnika",
          "direction": "Axborot texnologiyalari (IT)",
          "isTeam": false,
          "members": [
              {
                  "name": "NORXONOV BUNYODBEK QUVANDIQ ÕĞLI",
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
                  "name": "MASHARIPOV JAVOHIR HASANBOY ÕĞLI",
                  "birthDate": "2012-09-07",
                  "grade": "7-sinf"
              }
          ],
          "evaluations": {}
      },
      {
          "id": 5,
          "siteId": 1470,
          "school": "25-son umumiy õrta taʼlim maktabi",
          "projectName": "Robototexnika",
          "direction": "Axborot texnologiyalari (IT)",
          "isTeam": false,
          "members": [
              {
                  "name": "PO‘LATOV NURBEK MUXAMMAD ÕĞLI",
                  "birthDate": "2014-08-26",
                  "grade": "6-sinf"
              }
          ],
          "evaluations": {}
      },
      {
          "id": 6,
          "siteId": 1406,
          "school": "6-son umumiy õrta taʼlim maktabi",
          "projectName": "AGRO ROBOT (GROWERX)",
          "direction": "Qişloq xõjaligi",
          "isTeam": false,
          "members": [
              {
                  "name": "FAYZULLAYEV BOYMUROD BOBOMUROD ÕĞLI",
                  "birthDate": "2009-10-23",
                  "grade": "11-sinf"
              }
          ],
          "evaluations": {}
      },
      {
          "id": 7,
          "siteId": 1374,
          "school": "51-son umumiy õrta taʼlim maktabi",
          "projectName": "Quyosh energiyasida ishlaydigan o‘t maydalagich",
          "direction": "Qişloq xõjaligi",
          "isTeam": true,
          "members": [
              {
                  "name": "RAJABOV ELMUROD XOLMUROD ÕĞLI",
                  "birthDate": "2013-09-21",
                  "grade": "7-sinf"
              },
              {
                  "name": "BEKCHANOV KAMRONBEK OZODBOY ÕĞLI",
                  "birthDate": "2012-08-10",
                  "grade": "8-sinf"
              },
              {
                  "name": "BAXTIYOROV KAMRONBEK ELDORBEK ÕĞLI",
                  "birthDate": "2014-07-21",
                  "grade": "6-sinf"
              }
          ],
          "evaluations": {}
      },
      {
          "id": 8,
          "siteId": 1331,
          "school": "20-son umumiy õrta taʼlim maktabi",
          "projectName": "Robot yordamchi",
          "direction": "Axborot texnologiyalari (IT)",
          "isTeam": true,
          "members": [
              {
                  "name": "OTAMURODOV BILOLBEK BUNYOD ÕĞLI",
                  "birthDate": "2015-08-20",
                  "grade": "5-sinf"
              },
              {
                  "name": "SHUXRATOV ABDULAZIZ ABDULLA ÕĞLI",
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
          "direction": "Yaşil energiya",
          "isTeam": true,
          "members": [
              {
                  "name": "SANJARBEKOV MIRALI SANJARBEK ÕĞLI",
                  "birthDate": "2011-08-27",
                  "grade": "9-sinf"
              },
              {
                  "name": "QADAMBOYEV JO‘SHQINBEK MANSURBEK ÕĞLI",
                  "birthDate": "2013-09-20",
                  "grade": "7-sinf"
              },
              {
                  "name": "RAVŞANBEKOV ASADBEK ISLOMBEK ÕĞLI",
                  "birthDate": "2013-08-05",
                  "grade": "7-sinf"
              }
          ],
          "evaluations": {}
      },
      {
          "id": 10,
          "siteId": 816,
          "school": "14-son umumiy õrta taʼlim maktabi",
          "projectName": "Robot-yordamchi",
          "direction": "Yaşil energiya",
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
          "school": "42-son umumiy õrta taʼlim maktabi",
          "projectName": "Aqlli uy",
          "direction": "Axborot texnologiyalari (IT)",
          "isTeam": true,
          "members": [
              {
                  "name": "DO‘SCHANOV MURODBEK UMRBEK ÕĞLI",
                  "birthDate": "2014-11-19",
                  "grade": "6-sinf"
              },
              {
                  "name": "SULTONMUROTOV ERKABOY ULUG‘BEK ÕĞLI",
                  "birthDate": "2014-03-10",
                  "grade": "6-sinf"
              }
          ],
          "evaluations": {}
      },
      {
          "id": 12,
          "siteId": 139,
          "school": "19-son umumiy õrta taʼlim maktabi",
          "projectName": "Robot mashina",
          "direction": "Axborot texnologiyalari (IT)",
          "isTeam": false,
          "members": [
              {
                  "name": "OTANAZAROV XOLMIRZO ERGASH ÕĞLI",
                  "birthDate": "2011-10-15",
                  "grade": "9-sinf"
              }
          ],
          "evaluations": {}
      },
      {
          "id": 13,
          "siteId": 1771,
          "school": "29-son umumiy õrta taʼlim maktabi",
          "projectName": "Batareya yordamida harakatlanuvchi mashina",
          "direction": "Axborot texnologiyalari (IT)",
          "isTeam": false,
          "members": [
              {
                  "name": "SOBIROV SHOHJAHON XURMATBEK ÕĞLI",
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
      parsed.committee = IXTIROCHILIK_CONFIG.committee;
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
  // 5) 1-mezon: Loyihaning tanlov yo‘nalishlariga mos tayyorlanganligi
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

    // 5-ustunlik: 1-mezon (Tanlov yo‘nalishlariga mos tayyorlanganligi)
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
