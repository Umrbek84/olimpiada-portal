/**
 * "Iqtidorlilikka qadam" tanlovi - Google Sheets Avtomatik Sinxronlash Skripti
 * 
 * Ushbu skriptni Google Sheet ichidagi "Extensions" (Kengaytmalar) -> "Apps Script" ga qo'yib,
 * "Deploy" -> "New deployment" -> "Web app" qilib ishga tushirasiz.
 */

function doPost(e) {
  try {
    var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
    var data = JSON.parse(e.postData.contents);
    
    // Agar jadval bo'sh bo'lsa, ustun nomlarini yozish
    if (sheet.getLastRow() === 0) {
      sheet.appendRow([
        "T/r", "O'quvchi F.I.SH", "Ta'lim muassasasi", "Sinf",
        "1-Hakam", "2-Hakam", "3-Hakam", "4-Hakam", "5-Hakam", "6-Hakam",
        "Jami ball", "O'rtacha ball", "O'rni", "Oxirgi yangilanish"
      ]);
      
      // Standart format: Times New Roman, qalin sarlavha
      var headerRange = sheet.getRange(1, 1, 1, 14);
      headerRange.setFontFamily("Times New Roman");
      headerRange.setFontWeight("bold");
      headerRange.setBackground("#e2e8f0");
    }
    
    var students = data.students;
    if (students && students.length > 0) {
      // 2-qatordan boshlab eski ma'lumotlarni tozalash
      if (sheet.getLastRow() > 1) {
        sheet.getRange(2, 1, sheet.getLastRow() - 1, 14).clearContent();
      }
      
      // O'quvchilarni saralash va ballarini yozish
      var rows = [];
      for (var i = 0; i < students.length; i++) {
        var st = students[i];
        var s = st.scores || {};
        
        var j1 = (s[1] !== null && s[1] !== undefined && s[1] !== 0) ? s[1] : "";
        var j2 = (s[2] !== null && s[2] !== undefined && s[2] !== 0) ? s[2] : "";
        var j3 = (s[3] !== null && s[3] !== undefined && s[3] !== 0) ? s[3] : "";
        var j4 = (s[4] !== null && s[4] !== undefined && s[4] !== 0) ? s[4] : "";
        var j5 = (s[5] !== null && s[5] !== undefined && s[5] !== 0) ? s[5] : "";
        var j6 = (s[6] !== null && s[6] !== undefined && s[6] !== 0) ? s[6] : "";
        
        var sum = 0;
        var count = 0;
        [j1, j2, j3, j4, j5, j6].forEach(function(val) {
          if (val !== "") { sum += Number(val); count++; }
        });
        
        var total = count > 0 ? sum : "";
        var avg = count > 0 ? (sum / count).toFixed(2) : "";
        
        rows.push([
          i + 1,
          st.name,
          st.school,
          st.grade,
          j1, j2, j3, j4, j5, j6,
          total,
          avg,
          "", // O'rni formulada yoki quyida
          new Date().toLocaleString("uz-UZ")
        ]);
      }
      
      if (rows.length > 0) {
        var dataRange = sheet.getRange(2, 1, rows.length, 14);
        dataRange.setValues(rows);
        dataRange.setFontFamily("Times New Roman");
        dataRange.setFontSize(10);
      }
    }
    
    return ContentService.createTextOutput(JSON.stringify({ status: "success" }))
      .setMimeType(ContentService.MimeType.JSON);
      
  } catch (err) {
    return ContentService.createTextOutput(JSON.stringify({ status: "error", message: err.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}
