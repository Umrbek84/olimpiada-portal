# -*- coding: utf-8 -*-
import os
import sys
import json
import base64
import shutil
import subprocess
from datetime import datetime
from PIL import Image

FAN_COLORS = {
    "matematika": "#2563eb",
    "fizika": "#7c3aed",
    "kimyo": "#059669",
    "biologiya": "#16a34a",
    "informatika": "#0284c7",
    "ingliz": "#d97706",
    "nemis": "#ea580c",
    "fransuz": "#c2410c",
    "ona tili": "#b91c1c",
    "rus tili": "#be123c",
    "özbek tili": "#e11d48",
    "o'zbek tili": "#e11d48",
    "tarix": "#4f46e5",
    "geografiya": "#0d9488",
    "davlat va huquq": "#6366f1",
}

def get_fan_color(fan_name):
    low = fan_name.lower()
    for k, v in FAN_COLORS.items():
        if k in low:
            return v
    return "#3b82f6"

def find_chrome():
    if os.name == "nt":
        candidates = [
            r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
            r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            r"C:\Users\Monitoring\AppData\Local\Google\Chrome\Application\chrome.exe"
        ]
        for c in candidates:
            if os.path.exists(c):
                return c
    for b in ["google-chrome", "google-chrome-stable", "chromium", "chrome"]:
        p = shutil.which(b)
        if p:
            return p
    return None

def shorten_exam_type(exam_type):
    if not exam_type:
        return "Sinov"
    if "Tinglab" in exam_type:
        return "Tinglab/öqib tuşuniş, test"
    if "Esse" in exam_type:
        return "Esse va test"
    return exam_type

def build_olimpiada_html(date_title, total_students, sections, has_it, has_other):
    cards_html = []
    for sec in sections:
        color = sec["color"]
        fan = sec["fan"]
        sinf = sec["sinf"]
        exam_type = shorten_exam_type(sec["exam_type"])
        tm = sec["time"]
        icon = sec.get("icon", "📘")
        st_list = sec["students"]

        rows_html = []
        for s in st_list:
            rows_html.append(f"""
            <div class="st-row">
              <div class="st-left">
                <span class="st-num" style="background:{color};">{s['num']}</span>
                <span class="st-name">{s['name']}</span>
              </div>
              <span class="st-sch">{s['school']}</span>
            </div>
            """)

        cards_html.append(f"""
        <div class="sec-card">
          <div class="sec-head" style="background: linear-gradient(135deg, {color} 0%, {color}dd 100%);">
            <div class="sh-left">
              <span class="sh-icon">{icon}</span>
              <div class="sh-title-box">
                <span class="sh-fan">{fan}</span>
                <span class="sh-sinf">— {sinf}-sinf</span>
              </div>
            </div>
            <div class="sh-badges">
              <span class="badge badge-exam">{exam_type}</span>
              <span class="badge badge-time">⏰ {tm}</span>
              <span class="badge badge-count">👥 {len(st_list)} nafar</span>
            </div>
          </div>
          <div class="sec-body">
            {''.join(rows_html)}
          </div>
        </div>
        """)

    venue_items = []
    if has_it:
        venue_items.append("""
        <div class="v-item">
          <span class="v-icon">💻</span>
          <div>
            <b>Informatika fani:</b> Urganç şahri, 15-sonli umumiy örta taʼlim maktabi
          </div>
        </div>
        """)
    if has_other:
        venue_items.append("""
        <div class="v-item">
          <span class="v-icon">📚</span>
          <div>
            <b>Boşqa barça fanlar:</b> Urganç şahri, 17-sonli umumiy örta taʼlim maktabi
          </div>
        </div>
        """)

    html = f"""<!DOCTYPE html>
<html lang="uz">
<head>
<meta charset="utf-8">
<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  background: #f1f5f9;
  padding: 16px;
  width: 900px;
  color: #0f172a;
}}
.banner {{
  background: linear-gradient(135deg, #09132b 0%, #172554 45%, #1e3a8a 100%);
  border-radius: 16px;
  padding: 20px 24px;
  color: #ffffff;
  margin-bottom: 14px;
  box-shadow: 0 6px 18px rgba(15, 23, 42, 0.25);
  position: relative;
  overflow: hidden;
}}
.banner::after {{
  content: "";
  position: absolute;
  top: -40px;
  right: -40px;
  width: 140px;
  height: 140px;
  background: radial-gradient(circle, rgba(251, 191, 36, 0.2) 0%, transparent 70%);
  border-radius: 50%;
}}
.top-org {{
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: #fbbf24;
  margin-bottom: 6px;
}}
.banner h1 {{
  font-size: 24px;
  font-weight: 800;
  letter-spacing: -0.02em;
  line-height: 1.25;
  margin-bottom: 8px;
}}
.banner-sub {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 4px;
  padding-top: 8px;
  border-top: 1px solid rgba(255, 255, 255, 0.15);
}}
.sub-date {{
  font-size: 14.5px;
  color: #e2e8f0;
  font-weight: 600;
}}
.sub-badge {{
  background: #dc2626;
  color: #ffffff;
  padding: 4px 14px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.02em;
  box-shadow: 0 2px 8px rgba(220, 38, 38, 0.4);
}}
.sec-card {{
  background: #ffffff;
  border-radius: 14px;
  overflow: hidden;
  margin-bottom: 12px;
  border: 1px solid #e2e8f0;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.04);
}}
.sec-head {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 9px 16px;
  color: #ffffff;
}}
.sh-left {{
  display: flex;
  align-items: center;
  gap: 10px;
  min-width: 0;
}}
.sh-icon {{
  font-size: 18px;
}}
.sh-title-box {{
  display: flex;
  align-items: baseline;
  gap: 6px;
  white-space: nowrap;
}}
.sh-fan {{
  font-size: 16px;
  font-weight: 800;
  letter-spacing: -0.01em;
}}
.sh-sinf {{
  font-size: 13.5px;
  font-weight: 600;
  opacity: 0.95;
}}
.sh-badges {{
  display: flex;
  align-items: center;
  gap: 6px;
  flex-shrink: 0;
}}
.badge {{
  background: rgba(255, 255, 255, 0.22);
  border: 1px solid rgba(255, 255, 255, 0.4);
  padding: 3px 10px;
  border-radius: 20px;
  font-size: 11px;
  font-weight: 700;
  white-space: nowrap;
}}
.sec-body {{
  padding: 6px 12px;
  background: #ffffff;
}}
.st-row {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 6px 4px;
  border-bottom: 1px solid #f1f5f9;
}}
.st-row:last-child {{
  border-bottom: none;
}}
.st-left {{
  display: flex;
  align-items: center;
  flex: 1;
  min-width: 0;
  margin-right: 12px;
}}
.st-num {{
  width: 22px;
  height: 22px;
  border-radius: 50%;
  color: #ffffff;
  font-size: 11px;
  font-weight: 800;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  margin-right: 10px;
}}
.st-name {{
  font-size: 13px;
  font-weight: 700;
  color: #0f172a;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}}
.st-sch {{
  background: #f8fafc;
  border: 1px solid #cbd5e1;
  color: #334155;
  font-size: 11px;
  font-weight: 700;
  padding: 3px 10px;
  border-radius: 12px;
  flex-shrink: 0;
  white-space: nowrap;
}}
.footer-venues {{
  background: #ffffff;
  border: 1px solid #cbd5e1;
  border-radius: 14px;
  padding: 12px 16px;
  margin-top: 12px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}}
.v-head {{
  font-size: 11.5px;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: #475569;
}}
.v-item {{
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 12.5px;
  color: #1e293b;
}}
.v-icon {{
  font-size: 15px;
}}
.v-item b {{
  color: #0f172a;
}}
.warning-box {{
  background: #fffbeb;
  border: 1px solid #fde68a;
  border-radius: 12px;
  padding: 10px 14px;
  margin-top: 10px;
  font-size: 11.5px;
  color: #92400e;
  line-height: 1.45;
  font-weight: 600;
}}
.warning-box b {{
  color: #b45309;
}}
.source-box {{
  text-align: center;
  font-size: 11px;
  color: #64748b;
  margin-top: 10px;
  margin-bottom: 2px;
}}
</style>
</head>
<body id="container">
  <div class="banner">
    <div class="top-org">🏛️ QÖŞKÖPIR TUMANI MAKTABGAÇA VA MAKTAB TAʼLIMI BÖLIMI</div>
    <h1>ASOSIY FAN OLIMPIADASI · HUDUDIY (VILOYAT) BOSQICHI</h1>
    <div class="banner-sub">
      <div class="sub-date">📅 <b>{date_title}</b> &nbsp;|&nbsp; 👥 Jami: <b>{total_students} nafar</b> öquvçi</div>
      <div class="sub-badge">⏰ Ertalab soat 8:30 da yetib keliş şart!</div>
    </div>
  </div>

  {''.join(cards_html)}

  <div class="footer-venues">
    <div class="v-head">📍 Imtihon topşiriladigan manzillar:</div>
    {''.join(venue_items)}
  </div>

  <div class="warning-box">
    ❗️ <b>Eslatma:</b> Barça iştirokçilar <b>töliq öquvçi formasida</b>, şaxsini tasdiqlovçi hujjat, beydjik va ruçka bilan <b>ertalab soat 8:30 dan keç qolmasdan</b> yetib kelişlari şart!
  </div>

  <div class="source-box">
    🌐 Rasmiy portal: <b>umamatov.uz/hududiy-bosqich.html</b>
  </div>
</body>
</html>"""
    return html

def render_html_to_jpg(html_content, output_jpg_path, width=900):
    chrome = find_chrome()
    if not chrome:
        print("Chrome executable not found!", file=sys.stderr)
        return False

    b64 = base64.b64encode(html_content.encode("utf-8")).decode("ascii")
    data_uri = f"data:text/html;base64,{b64}"

    temp_png = output_jpg_path.replace(".jpg", ".png")
    cmd = [
        chrome,
        "--headless=new",
        "--no-sandbox",
        "--disable-gpu",
        "--hide-scrollbars",
        f"--screenshot={temp_png}",
        f"--window-size={width},4000",
        data_uri
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)

    if os.path.exists(temp_png):
        img = Image.open(temp_png)
        w, h = img.size
        pixels = img.load()
        bg = pixels[w // 2, h - 1]

        bottom = h
        found = False
        for y in range(h - 1, 0, -5):
            for x in range(20, w - 20, 20):
                px = pixels[x, y]
                if abs(px[0] - bg[0]) > 10 or abs(px[1] - bg[1]) > 10 or abs(px[2] - bg[2]) > 10:
                    bottom = min(h, y + 25)
                    found = True
                    break
            if found:
                break

        cropped = img.crop((0, 0, width, bottom))
        cropped.convert("RGB").save(output_jpg_path, "JPEG", quality=95)
        try:
            os.remove(temp_png)
        except Exception:
            pass
        return True

    return False
