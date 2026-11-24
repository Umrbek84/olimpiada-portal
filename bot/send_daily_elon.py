import json
import os
import sys
import urllib.request
import urllib.parse
from datetime import datetime, timedelta, timezone
from collections import defaultdict

DATA_URL = "https://umamatov.uz/hududiy-oquvchilar.json"
SITE_URL = "https://umamatov.uz/hududiy-bosqich.html"

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

def build_tomorrow_messages(data, target_date_str):
    sets_map = data.get("sets", {})
    students = data.get("students", [])

    # Collect all participations for target_date_str
    # Group by (fan, sinf, start, end, exam_type)
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
        return []

    date_uz = format_date_uz(target_date_str)
    total_entries = sum(len(v) for v in groups.values())
    total_unique = len(unique_students)

    # Header + Official Warning Text requested by user
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

    # Sort groups by subject name, then grade, then start time
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

    # Assemble into <= 3900 char Telegram messages cleanly (never splitting mid-block)
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

    if not target_date:
        now_tash = get_tashkent_now()
        target_date = (now_tash + timedelta(days=1)).strftime("%Y-%m-%d")

    print(f"Checking Olympiad schedule for tomorrow: {target_date}")
    data = fetch_students_data()
    messages = build_tomorrow_messages(data, target_date)

    if not messages:
        print(f"No Olympiad exams scheduled for {target_date}. Skipping notification.")
        return

    if dry_run:
        print("=== DRY RUN PREVIEW ===")
        for i, m in enumerate(messages, 1):
            print(f"--- Message {i} ({len(m)} chars) ---")
            print(m)
        return

    if not token or not chat_id:
        print("ERROR: TG_BOT_TOKEN or TG_CHAT_ID environment variable is missing!", file=sys.stderr)
        sys.exit(1)

    for i, m in enumerate(messages, 1):
        res = send_telegram_message(token, chat_id, m)
        print(f"Sent message {i}/{len(messages)} successfully! message_id={res['result']['message_id']}")

if __name__ == "__main__":
    main()
