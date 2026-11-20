/**
 * "Ixtirochilikka qadam" tanlovi - Google Sheets Jonli Backend Tizimi (Yangilangan)
 * Google Spreadsheet: "Ixtirochilikka qadam - Tuman bosqichi (2026)"
 * ID: 1JwODktbH7i_jEPqeLLtHSgzf_ZiW0wGgih6WjFOjFUw
 */

function doGet(e) {
  var action = (e && e.parameter && e.parameter.action) ? e.parameter.action : "get_data";
  var ss = SpreadsheetApp.getActiveSpreadsheet();

  // 1. Hakam PIN-kodini tekshirish (Kabinetga kirish uchun)
  if (action === "verify_pin") {
    var pin = e.parameter.pin;
    var hakamSheet = ss.getSheetByName("Hakamlar");
    var hakamData = hakamSheet.getDataRange().getValues();
    
    for (var r = 1; r < hakamData.length; r++) {
      if (String(hakamData[r][0]).toUpperCase() === "ADMIN") continue;
      if (String(hakamData[r][3]).trim() === String(pin).trim()) {
        return jsonResponse({
          valid: true,
          judge: {
            id: Number(hakamData[r][0]),
            role: String(hakamData[r][1]),
            name: String(hakamData[r][2]) || String(hakamData[r][1])
          }
        });
      }
    }
    return jsonResponse({ valid: false, message: "PIN-kod topilmadi" });
  }

  // 2. Mas'ul (Admin) PIN-kodini tekshirish (Baholangan loyiha qulfini ochish uchun)
  if (action === "verify_admin_pin") {
    var adminPin = e.parameter.pin;
    var hakamSheet = ss.getSheetByName("Hakamlar");
    var hakamData = hakamSheet.getDataRange().getValues();
    var realAdminPin = "7788";

    for (var r = 1; r < hakamData.length; r++) {
      if (String(hakamData[r][0]).toUpperCase() === "ADMIN") {
        realAdminPin = String(hakamData[r][3]).trim();
        break;
      }
    }

    if (String(adminPin).trim() === String(realAdminPin).trim()) {
      return jsonResponse({ valid: true, message: "Admin ruxsati tasdiqlandi" });
    }
    return jsonResponse({ valid: false, message: "Admin PIN-kodi noto‘g‘ri" });
  }

  // 3. Barcha baholarni olish (Svod uchun)
  if (action === "get_data") {
    var baholarSheet = ss.getSheetByName("Baholar");
    var baholarData = baholarSheet.getDataRange().getValues();
    
    var evaluations = {};
    for (var i = 1; i < baholarData.length; i++) {
      var pId = Number(baholarData[i][0]);
      var jId = Number(baholarData[i][2]);
      var c1 = baholarData[i][3];
      var c2 = baholarData[i][4];
      var c3 = baholarData[i][5];
      var c4 = baholarData[i][6];
      var c5 = baholarData[i][7];
      var tot = baholarData[i][8];

      if (!evaluations[pId]) evaluations[pId] = {};
      
      if (c1 !== "" || c2 !== "" || c3 !== "" || c4 !== "" || c5 !== "") {
        evaluations[pId][jId] = {
          c1: c1 !== "" ? Number(c1) : null,
          c2: c2 !== "" ? Number(c2) : null,
          c3: c3 !== "" ? Number(c3) : null,
          c4: c4 !== "" ? Number(c4) : null,
          c5: c5 !== "" ? Number(c5) : null,
          total: tot !== "" ? Number(tot) : 0
        };
      }
    }

    return jsonResponse({
      status: "success",
      evaluations: evaluations,
      updatedAt: new Date().toISOString()
    });
  }

  return jsonResponse({ status: "unknown_action" });
}

function doPost(e) {
  try {
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    var postData = JSON.parse(e.postData.contents);
    var action = postData.action || "save_score";

    if (action === "save_score") {
      var baholarSheet = ss.getSheetByName("Baholar");
      var baholarData = baholarSheet.getDataRange().getValues();

      var pId = Number(postData.projectId);
      var jId = Number(postData.judgeId);
      var sc = postData.scores || {};

      for (var r = 1; r < baholarData.length; r++) {
        if (Number(baholarData[r][0]) === pId && Number(baholarData[r][2]) === jId) {
          baholarSheet.getRange(r + 1, 4, 1, 5).setValues([[
            sc.c1 !== null && sc.c1 !== undefined && sc.c1 !== "" ? Number(sc.c1) : "",
            sc.c2 !== null && sc.c2 !== undefined && sc.c2 !== "" ? Number(sc.c2) : "",
            sc.c3 !== null && sc.c3 !== undefined && sc.c3 !== "" ? Number(sc.c3) : "",
            sc.c4 !== null && sc.c4 !== undefined && sc.c4 !== "" ? Number(sc.c4) : "",
            sc.c5 !== null && sc.c5 !== undefined && sc.c5 !== "" ? Number(sc.c5) : ""
          ]]);
          break;
        }
      }

      return jsonResponse({ status: "success" });
    }

    return jsonResponse({ status: "error", message: "Noma'lum amaliyot" });
  } catch (err) {
    return jsonResponse({ status: "error", message: err.toString() });
  }
}

function jsonResponse(obj) {
  return ContentService.createTextOutput(JSON.stringify(obj))
    .setMimeType(ContentService.MimeType.JSON);
}
