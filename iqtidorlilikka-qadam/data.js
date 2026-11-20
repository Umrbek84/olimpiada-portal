// "Iqtidorlilikka qadam" tanlovi - Namunaviy ma'lumotlar bazasi va sozlamalar

const DEFAULT_CONFIG = {
  competitionName: "\"Iqtidorlilikka qadam\" tanlovi",
  stage: "1-bosqich yakuniy baholash qaydnomasi",
  date: "2026-yil 20-noyabr",
  maxScore: 100,
  judges: [
    { id: 1, name: "1-Hakam (Mantiqiy tafakkur)", pin: "1101", subject: "Mantiqiy savollar" },
    { id: 2, name: "2-Hakam (Ijodiy fikrlash)", pin: "1102", subject: "Ijodiy topshiriq" },
    { id: 3, name: "3-Hakam (Aniq fanlar)", pin: "1103", subject: "Matematika/Fizika" },
    { id: 4, name: "4-Hakam (Tabiiy fanlar)", pin: "1104", subject: "Biologiya/Kimyo" },
    { id: 5, name: "5-Hakam (Til va adabiyot)", pin: "1105", subject: "Ona tili va nutq" },
    { id: 6, name: "6-Hakam (Taqdimot va faollik)", pin: "1106", subject: "Loyiha himoyasi" }
  ],
  students: [
    { id: 1, name: "O‘rozboyev Doniyorbek Alisher o‘g‘li", school: "1-son umumta'lim maktabi", grade: "8-sinf", scores: { 1: 95, 2: 92, 3: 98, 4: 90, 5: 94, 6: 96 } },
    { id: 2, name: "Matyoqubova Sabina Farhod qizi", school: "12-son umumta'lim maktabi", grade: "9-sinf", scores: { 1: 90, 2: 88, 3: 92, 4: 85, 5: 91, 6: 89 } },
    { id: 3, name: "Yo‘ldoshev Jasurbek Bobur o‘g‘li", school: "25-son umumta'lim maktabi", grade: "8-sinf", scores: { 1: 85, 2: 80, 3: 88, 4: 82, 5: 84, 6: 86 } },
    { id: 4, name: "Karimova Mohinur Sanjar qizi", school: "4-son IDUM", grade: "9-sinf", scores: { 1: 98, 2: 96, 3: 95, 4: 94, 5: 97, 6: 99 } },
    { id: 5, name: "Jumaniyozov Bobur Davron o‘g‘li", school: "18-son umumta'lim maktabi", grade: "8-sinf", scores: { 1: 78, 2: 75, 3: 80, 4: 76, 5: 79, 6: 82 } },
    { id: 6, name: "Ro‘zmetova Dilnoza Mansur qizi", school: "32-son umumta'lim maktabi", grade: "9-sinf", scores: { 1: 92, 2: 94, 3: 89, 4: 91, 5: 93, 6: 90 } },
    { id: 7, name: "Quryozov Sherzod Ilhom o‘g‘li", school: "15-son umumta'lim maktabi", grade: "8-sinf", scores: { 1: 88, 2: 85, 3: 87, 4: 84, 5: 86, 6: 89 } },
    { id: 8, name: "Otajonova Madina Komil qizi", school: "7-son umumta'lim maktabi", grade: "9-sinf", scores: { 1: 84, 2: 82, 3: 85, 4: 80, 5: 83, 6: 85 } },
    { id: 9, name: "Bekchanov Sardorbek Otabek o‘g‘li", school: "2-son IDUM", grade: "8-sinf", scores: { 1: 96, 2: 95, 3: 94, 4: 92, 5: 95, 6: 97 } },
    { id: 10, name: "Xudoyberganova Sevara Azamat qizi", school: "29-son umumta'lim maktabi", grade: "9-sinf", scores: { 1: 82, 2: 80, 3: 84, 4: 79, 5: 81, 6: 83 } }
  ]
};

// LocalStorage dan yuklash yoki standartni olish
function loadAppData() {
  const saved = localStorage.getItem("iqtidor_qadam_data");
  if (saved) {
    try {
      return JSON.parse(saved);
    } catch (e) {
      console.error("Ma'lumotlarni o'qishda xatolik:", e);
    }
  }
  saveAppData(DEFAULT_CONFIG);
  return DEFAULT_CONFIG;
}

function saveAppData(data) {
  localStorage.setItem("iqtidor_qadam_data", JSON.stringify(data));
}

// O'quvchilar reytingini hisoblash (Jami ball, o'rtacha ball, o'rni)
function calculateRanking(students) {
  const calculated = students.map(st => {
    let sum = 0;
    let count = 0;
    const judgeScores = [];
    
    for (let i = 1; i <= 6; i++) {
      const val = st.scores && st.scores[i] !== undefined && st.scores[i] !== null && st.scores[i] !== "" 
        ? Number(st.scores[i]) 
        : null;
      judgeScores.push(val);
      if (val !== null && !isNaN(val)) {
        sum += val;
        count++;
      }
    }
    
    const avg = count > 0 ? (sum / count).toFixed(2) : "";
    return {
      ...st,
      judgeScores,
      totalSum: count > 0 ? sum : "",
      averageScore: avg,
      scoreCount: count
    };
  });

  // Ball bo'yicha kamayish tartibida saralash
  calculated.sort((a, b) => {
    const valB = b.totalSum !== "" ? Number(b.totalSum) : -1;
    const valA = a.totalSum !== "" ? Number(a.totalSum) : -1;
    return valB - valA;
  });

  // O'rinlarni belgilash (1, 2, 3...)
  let currentRank = 1;
  for (let i = 0; i < calculated.length; i++) {
    if (calculated[i].totalSum === "") {
      calculated[i].rank = "-";
    } else {
      if (i > 0 && calculated[i].totalSum === calculated[i - 1].totalSum) {
        calculated[i].rank = calculated[i - 1].rank;
      } else {
        calculated[i].rank = currentRank;
      }
      currentRank++;
    }
  }

  return calculated;
}
