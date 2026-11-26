# -*- coding: utf-8 -*-
import json
import os
import sys
import urllib.request
import urllib.parse
from datetime import datetime, timedelta, timezone
from collections import defaultdict

# Add current folder to sys.path so generate_card can be imported
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_card import build_olimpiada_html, render_html_to_jpg, get_fan_color

DATA_URL = "https://umamatov.uz/hududiy-oquvchilar.json"
SITE_URL = "https://umamatov.uz/hududiy-bosqich.html"
FINAL_EXAM_DATE = "2026-12-04"

GH_OWNER = "Umrbek84"
GH_REPO = "olimpiada-portal"
GH_PAT = os.environ.get("GH_PAT", "").strip()

def get_last_sent_date():
    try:
        url = f"https://api.github.com/repos/{GH_OWNER}/{GH_REPO}/actions/variables/LAST_SENT_DATE"
        req = urllib.request.Request(url, headers={
            "Authorization": f"token {GH_PAT}",
            "Accept": "application/vnd.github+json",
            "User-Agent": "OlimpiadaBot"
        })
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode())
            return data.get("value", "").strip()
    except Exception:
        pass
    local_f = os.path.join(os.path.dirname(os.path.abspath(__file__)), "last_sent.txt")
    if os.path.exists(local_f):
        try:
            with open(local_f, "r", encoding="utf-8") as f:
                return f.read().strip()
        except Exception:
            pass
    return ""

def set_last_sent_date(date_str):
    try:
        url = f"https://api.github.com/repos/{GH_OWNER}/{GH_REPO}/actions/variables/LAST_SENT_DATE"
        payload = json.dumps({"name": "LAST_SENT_DATE", "value": date_str}).encode()
        req = urllib.request.Request(url, data=payload, headers={
            "Authorization": f"token {GH_PAT}",
            "Accept": "application/vnd.github+json",
            "User-Agent": "OlimpiadaBot"
        }, method="PATCH")
        with urllib.request.urlopen(req, timeout=10) as resp:
            pass
    except Exception:
        pass
    try:
        local_f = os.path.join(os.path.dirname(os.path.abspath(__file__)), "last_sent.txt")
        with open(local_f, "w", encoding="utf-8") as f:
            f.write(date_str)
    except Exception:
        pass

MONTHS = [
    "yanvar", "fevral", "mart", "aprel", "may", "iyun",
    "iyul", "avgust", "sentabr", "oktabr", "noyabr", "dekabr"
]
WEEKDAYS = [
    "Duşanba", "Seşanba", "Çorşanba", "Payşanba", "Juma", "Şanba", "Yakşanba"
]

def get_tashkent_now():
    tz = timezone(timedelta(hours=5))
    return datetime.now(tz)

def format_date_uz(date_str):
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    wd = WEEKDAYS[dt.weekday()]
    return f"{dt.day}-{MONTHS[dt.month - 1]} ({wd})"

def school_sort_key(school_name):
    import re
    m = re.match(r"^(\d+)", str(school_name))
    if m:
        return (0, int(m.group(1)), str(school_name))
    return (1, 0, str(school_name))

def escape_html(s):
    return (
        str(s)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )

def fetch_students_data():
    req = urllib.request.Request(
        f"{DATA_URL}?_t={int(datetime.now().timestamp())}",
        headers={"User-Agent": "QoshkopirOlimpiadaBot/1.0"}
    )
    with urllib.request.urlopen(req, timeout=20) as resp:
        raw = resp.read().decode("utf-8-sig")
    return json.loads(raw)

def prepare_day_data(data, target_date_str):
    sets_map = data.get("sets", {})
    students = data.get("students", [])

    groups = defaultdict(list)
    has_it = False
    has_other = False
    unique_students = set()

    for s in students:
        name, school, fan, sinf, set_id = s[0], s[1], s[2], s[3], s[4]
        slots = sets_map.get(set_id, [])
        for sl in slots:
            if sl[0] == target_date_str:
                start_t, end_t, exam_type = sl[1], sl[2], sl[3]
                key = (fan, int(sinf), start_t, end_t, exam_type)
                groups[key].append((school, name))
                unique_students.add((name, school))
                if "informatika" in fan.lower():
                    has_it = True
                else:
                    has_other = True

    if not groups:
        return None

    # Sort groups by subject name, then grade
    sorted_keys = sorted(groups.keys(), key=lambda k: (k[0], k[1], k[2]))

    sections = []
    for fan, sinf, start_t, end_t, exam_type in sorted_keys:
        items = sorted(groups[(fan, sinf, start_t, end_t, exam_type)], key=lambda x: (school_sort_key(x[0]), x[1]))
        st_objs = [{"num": i, "name": n, "school": sch} for i, (sch, n) in enumerate(items, 1)]
        sections.append({
            "fan": fan,
            "sinf": sinf,
            "exam_type": exam_type,
            "time": f"{start_t}–{end_t}",
            "color": get_fan_color(fan),
            "icon": "💻" if "informatika" in fan.lower() else "📘",
            "students": st_objs
        })

    total_count = sum(len(s["students"]) for s in sections)

    return {
        "groups": groups,
        "sections": sections,
        "unique_students": unique_students,
        "has_it": has_it,
        "has_other": has_other,
        "total_count": total_count,
        "total_unique": len(unique_students),
        "total_entries": total_count,
        "date_uz": format_date_uz(target_date_str)
    }

def build_photo_caption(day_info):
    date_uz = day_info["date_uz"]
    total_count = day_info["total_count"]

    venue_lines = []
    if day_info["has_it"]:
        venue_lines.append('• 💻 <b>Informatika:</b> Urganç ş., 15-maktab')
    if day_info["has_other"]:
        venue_lines.append('• 📚 <b>Boşqa fanlar:</b> Urganç ş., 17-maktab')

    venues_str = "\n".join(venue_lines)

    caption = (
        f"📢 <b>ERTANGI HUDUDIY OLIMPIADA EʼLONI</b>\n"
        f"📅 <b>Sana:</b> {date_uz} | 👥 <b>Jami:</b> {total_count} nafar öquvçi\n\n"
        f"Ertaga qatnaşadigan öquvçilar röyxati va imtihon vaqtlari yuqoridagi rasmda keltirilgan.\n\n"
        f"Iştirokçilar ertaga töliq <b>öquvçi formasida</b>, özlari bilan <b>şaxsini tasdiqlovçi hujjati, beydjik va ruçka</b> olib kelişlari talab etiladi. Tegişli hujjatlarsiz kelgan va keçikkanlar kiritilmaydi.\n\n"
        f"❗️<b>Oçiliş marosimi bölişini inobatga olib, barça iştirokçilarni ertalab soat 8:30 dan keç qolmagan holda yetib kelişlarini taʼminlaşingiz va qatʼiy nazoratga olişingiz söraladi.</b>\n\n"
        f"⚠️ <i>Bu yozuvlarni gruppalarga pereslat qilmasdan, iştirokçilar bilan töliq gaplaşib xabardor qilinglar.</i>\n\n"
        f"📍 <b>Manzillar:</b>\n"
        f"{venues_str}\n\n"
        f"🌐 <b>Batafsil:</b> <a href=\"{SITE_URL}\">umamatov.uz/hududiy-bosqich.html</a>"
    )
    return caption

def build_fallback_text_messages(day_info):
    groups = day_info["groups"]
    date_uz = day_info["date_uz"]
    total_unique = day_info["total_unique"]
    total_entries = day_info["total_entries"]
    has_it = day_info["has_it"]
    has_other = day_info["has_other"]

    header_lines = [
        f"📢 <b>ERTANGI HUDUDIY (VILOYAT) OLIMPIADA EʼLONI</b>",
        f"📅 <b>Sana:</b> {date_uz} | 👥 <b>Jami:</b> {total_unique} nafar öquvçi ({total_entries} ta sinov)",
        "",
        "Ertaga olimpiadaga qatnaşadigan öquvçilar röyxati yuborilmoqda. Uşbu iştirokçilar ertaga töliq <b>öquvçi formasida</b> kelişlari talab etiladi. Bundan taşqari özlari bilan <b>şaxsini tasdiqlovçi hujjati, beydjik va ruçka</b> olib kelişlari söraladi. Tegişli hujjatlarsiz kelgan va keçikib kelgan iştirokçilar kiritilmaydi.",
        "",
        "❗️<b>Ertaga oçiliş marosimi bölişini inobatga olib, röyxatdagi barça iştirokçilarni ertalab soat 8:30 dan keç qolmagan holda yetib kelişlarini taʼminlaşingiz söraladi va qatʼiy nazoratga olinglar.</b>",
        "",
        "⚠️ <i>Bu yozuvlarni gruppalarga pereslat qilmasdan, röyxatdagi iştirokçilar bilan töliq gaplaşib xabardor qilinglar.</i>",
        "",
        "📍 <b>Ötkaziliş manzillari:</b>",
    ]
    if has_it:
        header_lines.append('• 💻 <b>Informatika fani:</b> Urganç şahri, 15-sonli maktab (<a href="https://maps.app.goo.gl/s2o7CmybZpJMU5a38">Xaritada köriş</a>)')
    if has_other:
        header_lines.append('• 📚 <b>Qolgan barça fanlar:</b> Urganç şahri, 17-sonli maktab (<a href="https://goo.gl/maps/V5cFN5Js9mBWoSHa7">Xaritada köriş</a>)')

    header_lines.append("")
    header_lines.append("📋 <b>ERTANGI FANLAR VA ÖQUVÇILAR RÖYXATI:</b>")

    sorted_keys = sorted(groups.keys(), key=lambda k: (k[0], k[1], k[2]))
    blocks = []
    for fan, sinf, start_t, end_t, exam_type in sorted_keys:
        items = sorted(groups[(fan, sinf, start_t, end_t, exam_type)], key=lambda x: (school_sort_key(x[0]), x[1]))
        icon = "💻" if "informatika" in fan.lower() else "📘"
        b_lines = [
            f"\n{icon} <b>{escape_html(fan)} — {sinf}-sinf</b> ({escape_html(exam_type)}, ⏰ {start_t}–{end_t})"
        ]
        for idx, (school, name) in enumerate(items, 1):
            b_lines.append(f"  {idx}. <b>{escape_html(name)}</b> — {escape_html(school)}")
        blocks.append("\n".join(b_lines))

    footer = f'\n\n🌐 <b>Töliq grafik va manzillar:</b> <a href="{SITE_URL}">umamatov.uz/hududiy-bosqich.html</a>'

    messages = []
    current = "\n".join(header_lines)
    for blk in blocks:
        if len(current) + len(blk) + 20 > 3850:
            messages.append(current)
            current = f"📋 <b>DAVOMI ({date_uz}):</b>\n" + blk
        else:
            current += "\n" + blk

    if len(current) + len(footer) > 4000:
        messages.append(current)
        messages.append(footer.strip())
    else:
        current += footer
        messages.append(current)

    return messages

def send_telegram_photo(token, chat_id, photo_path, caption):
    import requests
    url = f"https://api.telegram.org/bot{token}/sendPhoto"
    with open(photo_path, "rb") as f:
        resp = requests.post(
            url,
            data={
                "chat_id": str(chat_id),
                "caption": caption,
                "parse_mode": "HTML"
            },
            files={"photo": f},
            timeout=30
        )
    res = resp.json()
    if not res.get("ok"):
        raise RuntimeError(f"Telegram API sendPhoto error: {res}")
    return res

def send_telegram_message(token, chat_id, text):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = urllib.parse.urlencode({
        "chat_id": str(chat_id),
        "text": text,
        "parse_mode": "HTML",
        "disable_web_page_preview": "true"
    }).encode("utf-8")
    req = urllib.request.Request(url, data=payload, method="POST")
    with urllib.request.urlopen(req, timeout=20) as resp:
        res = json.loads(resp.read().decode("utf-8"))
        if not res.get("ok"):
            raise RuntimeError(f"Telegram API error: {res}")
        return res

def main():
    token = os.environ.get("TG_BOT_TOKEN", "").strip()
    chat_id = os.environ.get("TG_CHAT_ID", "").strip()
    target_date = os.environ.get("TARGET_DATE", "").strip()
    dry_run = os.environ.get("DRY_RUN", "0") == "1"

    now_tash = get_tashkent_now()
    today_str = now_tash.strftime("%Y-%m-%d")

    # 4-dekabr kuni va undan keyin avtomatik o'chish nazorati
    if today_str > FINAL_EXAM_DATE:
        print(f"Hududiy olimpiada jadvali {FINAL_EXAM_DATE} kuni to'liq yakunlangan. Bot avtomatik o'chirilgan.")
        return

    # VAQT QALQONI: E'lon faqat soat 17:00 atrofida (16:50 - 18:00) yuborilishi shart!
    # Tunda yoki boshqa soatda adashib xabar ketishining oldi olinadi.
    is_force = (os.environ.get("FORCE_SEND", "0") == "1") or dry_run or bool(target_date)
    cur_minutes = now_tash.hour * 60 + now_tash.minute
    if not (1010 <= cur_minutes <= 1080) and not is_force:
        print(f"VAQT QALQONI: Hozirgi Toshkent vaqti {now_tash.strftime('%H:%M')}. Ruxsat etilgan vaqt: 16:50 - 18:00. Noto'g'ri vaqtdagi chaqiruv bekor qilindi.")
        return

    # 3. Dublikatdan himoya: Agar bugungi e'lon allaqachon yuborilgan bo'lsa, qayta yuborilmaydi
    if not dry_run and not bool(target_date):
        last_sent = get_last_sent_date()
        if last_sent == today_str:
            print(f"DUBLIKAT HIMOYA: Bugungi e'lon ({today_str}) allaqachon muvaffaqiyatli yuborilgan. Qayta yuborilmaydi.")
            return

    if not target_date:
        target_date = (now_tash + timedelta(days=1)).strftime("%Y-%m-%d")

    if target_date > FINAL_EXAM_DATE:
        print(f"Ertangi sana ({target_date}) oxirgi olimpiada kuni ({FINAL_EXAM_DATE}) dan keyinda. Yangi e'lon yo'q, bot to'xtatildi.")
        return

    print(f"Checking Olympiad schedule for tomorrow: {target_date}")
    data = fetch_students_data()
    day_info = prepare_day_data(data, target_date)

    if not day_info:
        print(f"No Olympiad exams scheduled for {target_date}. Skipping notification.")
        return

    # 1. Generate JPG infographic card
    card_html = build_olimpiada_html(
        day_info["date_uz"],
        day_info["total_count"],
        day_info["sections"],
        day_info["has_it"],
        day_info["has_other"]
    )
    jpg_path = os.path.abspath(f"olimpiada_{target_date}.jpg")
    photo_rendered = render_html_to_jpg(card_html, jpg_path)

    caption = build_photo_caption(day_info)

    if dry_run:
        print("=== DRY RUN PREVIEW ===")
        print(f"Card rendered: {photo_rendered} -> {jpg_path} ({os.path.getsize(jpg_path) if photo_rendered else 0} bytes)")
        print(f"--- Caption ({len(caption)} chars) ---")
        print(caption)
        return

    if not token or not chat_id:
        print("ERROR: TG_BOT_TOKEN or TG_CHAT_ID environment variable is missing!", file=sys.stderr)
        sys.exit(1)

    # 2. Send via Telegram sendPhoto
    if photo_rendered and os.path.exists(jpg_path):
        try:
            print(f"Sending photo card to chat {chat_id} with caption ({len(caption)} chars)...")
            res = send_telegram_photo(token, chat_id, jpg_path, caption)
            print(f"✓ Photo announcement sent successfully! message_id={res['result']['message_id']}")
            set_last_sent_date(today_str)
            return
        except Exception as e:
            print(f"WARNING: Photo sending failed ({e}), falling back to text messages...", file=sys.stderr)

    # Fallback: Text messages
    fallback_messages = build_fallback_text_messages(day_info)
    for i, m in enumerate(fallback_messages, 1):
        res = send_telegram_message(token, chat_id, m)
        print(f"Sent fallback text message {i}/{len(fallback_messages)} successfully! message_id={res['result']['message_id']}")
    set_last_sent_date(today_str)

if __name__ == "__main__":
    main()
