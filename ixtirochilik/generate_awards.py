import os
import sys
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = r"C:\Users\Monitoring\.gemini\antigravity\scratch\olimpiada-portal\ixtirochilik"
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

FONT_TIMES = r"C:\Windows\Fonts\times.ttf"
FONT_TIMES_BD = r"C:\Windows\Fonts\timesbd.ttf"

def to_yangi_lotin(text):
    if not text:
        return ""
    t = str(text)
    # Multi-char & apostrophe variations
    t = t.replace("Yoʻ", "Yö").replace("yoʻ", "yö")
    t = t.replace("Yo'", "Yö").replace("yo'", "yö")
    t = t.replace("Yo‘", "Yö").replace("yo‘", "yö")
    t = t.replace("YOʻ", "YÖ").replace("YO'", "YÖ").replace("YO‘", "YÖ")
    # All forms of o' / oʻ / õ -> ö (two dots)
    t = t.replace("Õ", "Ö").replace("õ", "ö")
    t = t.replace("Oʻ", "Ö").replace("oʻ", "ö")
    t = t.replace("O'", "Ö").replace("o'", "ö")
    t = t.replace("O‘", "Ö").replace("o‘", "ö")
    t = t.replace("O`", "Ö").replace("o`", "ö")
    t = t.replace("Oʼ", "Ö").replace("oʼ", "ö")
    # All forms of g' / gʻ -> ğ
    t = t.replace("Gʻ", "Ğ").replace("gʻ", "ğ")
    t = t.replace("G'", "Ğ").replace("g'", "ğ")
    t = t.replace("G‘", "Ğ").replace("g‘", "ğ")
    t = t.replace("G`", "Ğ").replace("g`", "ğ")
    t = t.replace("Gʼ", "Ğ").replace("gʼ", "ğ")
    # ch / sh
    t = t.replace("CH", "Ç").replace("Ch", "Ç").replace("ch", "ç")
    t = t.replace("SH", "Ş").replace("Sh", "Ş").replace("sh", "ş")
    return t

def get_diplom_base(place):
    p = place if place in [1, 2, 3] else 1
    path = os.path.join(ASSETS_DIR, f"diplom_base_{p}.jpg")
    if not os.path.exists(path):
        path = os.path.join(ASSETS_DIR, "diplom_base.jpg")
    return Image.open(path).convert("RGB")

def get_tash_base(place):
    p = place if place in [1, 2, 3] else 1
    path = os.path.join(ASSETS_DIR, f"tashakkurnoma_base_{p}.jpg")
    if not os.path.exists(path):
        path = os.path.join(ASSETS_DIR, "tashakkurnoma_base.jpg")
    return Image.open(path).convert("RGB")

def create_diploma(student_name, school, grade, direction, place, number="001"):
    base = get_diplom_base(place)
    draw = ImageDraw.Draw(base)

    font_box_lbl = ImageFont.truetype(FONT_TIMES, 15)
    font_box_num = ImageFont.truetype(FONT_TIMES_BD, 24)
    font_daraja = ImageFont.truetype(FONT_TIMES, 48)
    font_text = ImageFont.truetype(FONT_TIMES, 32)
    font_name = ImageFont.truetype(FONT_TIMES_BD, 52)

    # 1. Box number: centered at x: (1485+1665)/2 = 1575
    lbl = "DIPLOM RAQAMI"
    num_str = f"№ {str(number).zfill(3)}"
    w_lbl = draw.textlength(lbl, font=font_box_lbl)
    w_num = draw.textlength(num_str, font=font_box_num)
    draw.text(((1485 + 1665 - w_lbl)/2, 66), lbl, font=font_box_lbl, fill=(70, 70, 70))
    draw.text(((1485 + 1665 - w_num)/2, 90), num_str, font=font_box_num, fill=(10, 20, 50))

    # 2. Daraja
    daraja_map = {1: "I DARAJALI", 2: "II DARAJALI", 3: "III DARAJALI"}
    daraja_text = daraja_map.get(place, f"{place}-DARAJALI")
    w_daraja = draw.textlength(daraja_text, font=font_daraja)
    draw.text(((1754 - w_daraja)/2, 355), daraja_text, font=font_daraja, fill=(0, 0, 0))

    # 3. Description
    grade_clean = to_yangi_lotin(grade if "sinf" in str(grade) else f"{grade}-sinf")
    dir_clean = to_yangi_lotin(direction)
    school_clean = to_yangi_lotin(school)
    student_clean = to_yangi_lotin(student_name).upper()

    l1 = "2026/2027-öquv yilidagi “Ixtiroçilikka qadam” tanlovining tuman bosqiçida"
    l2 = f"{grade_clean} böyiça {dir_clean} yönalişida {place}-örinni qölga kiritgani uçun"
    l3 = f"Qöşköpir tumani, {school_clean} öquvçisi"

    w1 = draw.textlength(l1, font=font_text)
    w2 = draw.textlength(l2, font=font_text)
    w3 = draw.textlength(l3, font=font_text)

    draw.text(((1754 - w1)/2, 450), l1, font=font_text, fill=(30, 30, 30))
    draw.text(((1754 - w2)/2, 505), l2, font=font_text, fill=(30, 30, 30))
    draw.text(((1754 - w3)/2, 560), l3, font=font_text, fill=(30, 30, 30))

    # 4. Student Name
    w_n = draw.textlength(student_clean, font=font_name)
    if w_n > 1400:
        font_name_smaller = ImageFont.truetype(FONT_TIMES_BD, 42)
        w_n = draw.textlength(student_clean, font=font_name_smaller)
        draw.text(((1754 - w_n)/2, 645), student_clean, font=font_name_smaller, fill=(10, 20, 50))
    else:
        draw.text(((1754 - w_n)/2, 640), student_clean, font=font_name, fill=(10, 20, 50))

    return base

def create_tashakkurnoma(teacher_name, school, role_or_subject, student_name, grade, direction, place, number="001"):
    base = get_tash_base(place)
    draw = ImageDraw.Draw(base)

    font_box_lbl = ImageFont.truetype(FONT_TIMES, 16)
    font_box_num = ImageFont.truetype(FONT_TIMES_BD, 24)
    font_hurmatli = ImageFont.truetype(FONT_TIMES, 44)
    font_teacher = ImageFont.truetype(FONT_TIMES_BD, 52)
    font_sub = ImageFont.truetype(FONT_TIMES, 28)
    font_para = ImageFont.truetype(FONT_TIMES, 28)
    font_close = ImageFont.truetype(FONT_TIMES, 30)

    # 1. Box number
    lbl = "RAQAMI"
    num_str = f"№ {str(number).zfill(3)}"
    w_lbl = draw.textlength(lbl, font=font_box_lbl)
    w_num = draw.textlength(num_str, font=font_box_num)
    draw.text(((1485 + 1665 - w_lbl)/2, 66), lbl, font=font_box_lbl, fill=(70, 70, 70))
    draw.text(((1485 + 1665 - w_num)/2, 90), num_str, font=font_box_num, fill=(10, 20, 50))

    # 2. Hurmatli
    h_text = "Hurmatli"
    w_h = draw.textlength(h_text, font=font_hurmatli)
    draw.text(((1754 - w_h)/2, 315), h_text, font=font_hurmatli, fill=(30, 30, 30))

    # 3. Ustoz F.I.SH.
    teacher_clean = to_yangi_lotin(teacher_name)
    w_tn = draw.textlength(teacher_clean, font=font_teacher)
    if w_tn > 1400:
        font_teacher_sm = ImageFont.truetype(FONT_TIMES_BD, 42)
        w_tn = draw.textlength(teacher_clean, font=font_teacher_sm)
        draw.text(((1754 - w_tn)/2, 385), teacher_clean, font=font_teacher_sm, fill=(10, 20, 50))
    else:
        draw.text(((1754 - w_tn)/2, 380), teacher_clean, font=font_teacher, fill=(10, 20, 50))

    # 4. Maktab va fan/lavozim
    school_clean = to_yangi_lotin(school)
    role_clean = to_yangi_lotin(role_or_subject or "tögarak rahbari")
    sub_text = f"({school_clean}, {role_clean})"
    w_sub = draw.textlength(sub_text, font=font_sub)
    draw.text(((1754 - w_sub)/2, 455), sub_text, font=font_sub, fill=(60, 60, 60))

    # 5. Metallic separator line is already in base template at y=520

    # 6. Minnatdorchilik matni
    grade_clean = to_yangi_lotin(grade if "sinf" in str(grade) else f"{grade}-sinf")
    student_clean = to_yangi_lotin(student_name)
    dir_clean = to_yangi_lotin(direction)

    p1 = f"Siz tayyorlagan {grade_clean} öquvçisi {student_clean} 2026/2027-öquv"
    p2 = f"yilidagi “Ixtiroçilikka qadam” tanlovining tuman bosqiçida {dir_clean} yönalişida {place}-örinni egalladi."
    p3 = "Öquvçilarni yuksak natijalarga yetaklagan fidokorona mehnatingiz, kasbiy mahoratingiz va"
    p4 = "ilhomlantiruvçi ustozligingiz uçun Sizga çuqur minnatdorçilik bildiramiz."

    w_p1 = draw.textlength(p1, font=font_para)
    w_p2 = draw.textlength(p2, font=font_para)
    w_p3 = draw.textlength(p3, font=font_para)
    w_p4 = draw.textlength(p4, font=font_para)

    draw.text(((1754 - w_p1)/2, 555), p1, font=font_para, fill=(30, 30, 30))
    draw.text(((1754 - w_p2)/2, 595), p2, font=font_para, fill=(30, 30, 30))
    draw.text(((1754 - w_p3)/2, 635), p3, font=font_para, fill=(30, 30, 30))
    draw.text(((1754 - w_p4)/2, 675), p4, font=font_para, fill=(30, 30, 30))

    # 7. Tilak
    close_text = "İş faoliyatingizda yangi zafarlar tilaymiz!"
    w_cl = draw.textlength(close_text, font=font_close)
    draw.text(((1754 - w_cl)/2, 735), close_text, font=font_close, fill=(30, 30, 30))

    return base

def main():
    target_dir = r"C:\Users\Monitoring\Desktop\ОЛИМПИАДАЛАР\2026\Ихтирочиликка қадам\туман босқичи\туман босқичи ғолибларни тақдирлаш"
    output_pdf = os.path.join(target_dir, "Goliblar_Diplom_va_Tashakkurnoma_2026.pdf")
    output_img_dir = os.path.join(target_dir, "Goliblar_Rasmlar_2026")
    # Clear previous image files in output_img_dir to ensure no duplicates
    for f in os.listdir(output_img_dir):
        fp = os.path.join(output_img_dir, f)
        if os.path.isfile(fp):
            os.remove(fp)

    winners = [
        {
            "place": 1, # OLTIN (GOLD)
            "school": "6-son umumiy oʻrta taʼlim maktabi",
            "project": "AGRO ROBOT (GROWERX)",
            "direction": "Qishloq xoʻjaligi",
            "students": [
                {"name": "FAYZULLAYEV BOYMUROD BOBOMUROD OʻGʻLI", "grade": "11-sinf"}
            ],
            "teacher": "Ollaberganova Laylo Rözimbayevna",
            "teacher_role": "Informatika va axborot texnologiyalari fani öqituvçisi"
        },
        {
            "place": 2, # KUMUSH (SILVER)
            "school": "23-son umumiy oʻrta taʼlim maktabi",
            "project": "Harakatlanuvchi qurilma",
            "direction": "Axborot texnologiyalari (IT)",
            "students": [
                {"name": "ABDULLAYEV JAMSHIDBEK DIYOR OʻGʻLI", "grade": "8-sinf"},
                {"name": "OTAJONOV AKROMJON GʻULOMJON OʻGʻLI", "grade": "9-sinf"}
            ],
            "teacher": "Madaminov Jasurbek Baxtiyorovich",
            "teacher_role": "Fizika va robototexnika tögaragi rahbari"
        },
        {
            "place": 3, # BRONZA (BRONZE)
            "school": "9-son ixtisoslashtirilgan maktab",
            "project": "Robot ekskavator",
            "direction": "Axborot texnologiyalari (IT)",
            "students": [
                {"name": "MASHARIPOV JAVOHIR HASANBOY OʻGʻLI", "grade": "7-sinf"}
            ],
            "teacher": "Bobojonov Shavkat Rustamovich",
            "teacher_role": "Informatika fani öqituvçisi"
        }
    ]

    all_pages = []
    cert_counter = 1

    for w in winners:
        place = w["place"]
        metal_name = "Oltin" if place == 1 else "Kumush" if place == 2 else "Bronza"
        # Generate diplomas for all team members
        for st in w["students"]:
            dip_img = create_diploma(
                student_name=st["name"],
                school=w["school"],
                grade=st["grade"],
                direction=w["direction"],
                place=place,
                number=str(cert_counter).zfill(3)
            )
            clean_name = to_yangi_lotin(st["name"]).replace(" ", "_").replace("'", "").replace("ʻ", "").replace("ʼ", "")
            dip_path = os.path.join(output_img_dir, f"Diplom_{place}-orin_{metal_name}_{clean_name}.jpg")
            dip_img.save(dip_path, quality=95)
            all_pages.append(dip_img)
            cert_counter += 1

        # Generate teacher Tashakkurnoma
        if w.get("teacher"):
            tash_img = create_tashakkurnoma(
                teacher_name=w["teacher"],
                school=w["school"],
                role_or_subject=w["teacher_role"],
                student_name=", ".join([to_yangi_lotin(s["name"]) for s in w["students"]]),
                grade=", ".join([to_yangi_lotin(s["grade"]) for s in w["students"]]),
                direction=w["direction"],
                place=place,
                number=str(cert_counter).zfill(3)
            )
            clean_tname = to_yangi_lotin(w["teacher"]).replace(" ", "_").replace("'", "").replace("ʻ", "").replace("ʼ", "")
            tash_path = os.path.join(output_img_dir, f"Tashakkurnoma_{place}-orin_{metal_name}_ustoz_{clean_tname}.jpg")
            tash_img.save(tash_path, quality=95)
            all_pages.append(tash_img)
            cert_counter += 1

    # Save all into one unified PDF
    if all_pages:
        all_pages[0].save(
            output_pdf,
            save_all=True,
            append_images=all_pages[1:],
            resolution=150.0
        )
        print(f"SUCCESS: Generated {len(all_pages)} award documents with Gold, Silver, Bronze metals!")
        print(f"Unified PDF: {output_pdf}")
        print(f"Image files in: {output_img_dir}")

if __name__ == "__main__":
    main()
