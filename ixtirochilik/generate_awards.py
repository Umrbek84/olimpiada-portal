import os
import sys
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = r"C:\Users\Monitoring\.gemini\antigravity\scratch\olimpiada-portal\ixtirochilik"
THEMES_DIR = os.path.join(BASE_DIR, "assets", "themes")

FONT_TIMES = r"C:\Windows\Fonts\times.ttf"
FONT_TIMES_BD = r"C:\Windows\Fonts\timesbd.ttf"
FONT_TIMES_IT = r"C:\Windows\Fonts\timesi.ttf"

def to_yangi_lotin(text):
    if not text:
        return ""
    t = str(text)
    t = t.replace("Yoʻ", "Yö").replace("yoʻ", "yö")
    t = t.replace("Yo'", "Yö").replace("yo'", "yö")
    t = t.replace("Yo‘", "Yö").replace("yo‘", "yö")
    t = t.replace("YOʻ", "YÖ").replace("YO'", "YÖ").replace("YO‘", "YÖ")
    t = t.replace("Õ", "Ö").replace("õ", "ö")
    t = t.replace("Oʻ", "Ö").replace("oʻ", "ö")
    t = t.replace("O'", "Ö").replace("o'", "ö")
    t = t.replace("O‘", "Ö").replace("o‘", "ö")
    t = t.replace("O`", "Ö").replace("o`", "ö")
    t = t.replace("Oʼ", "Ö").replace("oʼ", "ö")
    t = t.replace("Gʻ", "Ğ").replace("gʻ", "ğ")
    t = t.replace("G'", "Ğ").replace("g'", "ğ")
    t = t.replace("G‘", "Ğ").replace("g‘", "ğ")
    t = t.replace("G`", "Ğ").replace("g`", "ğ")
    t = t.replace("Gʼ", "Ğ").replace("gʼ", "ğ")
    t = t.replace("CH", "Ç").replace("Ch", "Ç").replace("ch", "ç")
    t = t.replace("SH", "Ş").replace("Sh", "Ş").replace("sh", "ş")
    return t

def get_theme_key(direction):
    d = str(direction or "").lower()
    if "axborot" in d or "it" in d or "robot" in d:
        return "it"
    if "yaşil" in d or "yashil" in d or "energiya" in d:
        return "yashil"
    if "ekologiya" in d or "iqlim" in d:
        return "ekologiya"
    if "qişloq" in d or "qishloq" in d or "xöjaligi" in d or "xo'jaligi" in d or "xoʻjaligi" in d or "agro" in d:
        return "qishloq"
    return "talim"

def get_metal_colors(place):
    if place == 1:
        return {"primary": (184, 134, 11), "accent": (212, 175, 55), "name": "Oltin"}
    elif place == 2:
        return {"primary": (100, 116, 139), "accent": (148, 163, 184), "name": "Kumuş"}
    else:
        return {"primary": (154, 80, 40), "accent": (180, 115, 80), "name": "Bronza"}

def draw_common_frame(base, direction, place, box_label, number):
    draw = ImageDraw.Draw(base)
    metal = get_metal_colors(place)

    # 1. Top 3 official logos strip (Vazirlik + Agentlik + Fan Olimpiadalari Markazi)
    logos_path = os.path.join(THEMES_DIR, "top_3_logos.png")
    if os.path.exists(logos_path):
        logos = Image.open(logos_path).convert("RGBA")
        logos = logos.resize((760, 116), Image.Resampling.LANCZOS)
        base.paste(logos, (877 - 380, 132), logos)

    # 2. Top-right rounded number box inside 100% open white safe area
    bx1, by1, bx2, by2 = 1315, 148, 1490, 214
    draw.rounded_rectangle([(bx1, by1), (bx2, by2)], radius=10, fill=(255, 255, 255), outline=metal["accent"], width=3)
    f_lbl = ImageFont.truetype(FONT_TIMES, 14)
    f_num = ImageFont.truetype(FONT_TIMES_BD, 24)
    num_str = f"№ {str(number).zfill(3)}"
    draw.text(((bx1 + bx2 - draw.textlength(box_label, font=f_lbl))/2, by1 + 9), box_label, font=f_lbl, fill=(71, 85, 105))
    draw.text(((bx1 + bx2 - draw.textlength(num_str, font=f_num))/2, by1 + 30), num_str, font=f_num, fill=(12, 26, 48))

    # 3. Bottom official seal + signature (left) & Director title (right)
    seal_path = os.path.join(THEMES_DIR, "seal_signature.png")
    if os.path.exists(seal_path):
        seal = Image.open(seal_path).convert("RGBA")
        seal = seal.resize((345, 214), Image.Resampling.LANCZOS)
        base.paste(seal, (365, 795), seal)

    f_sig_t = ImageFont.truetype(FONT_TIMES_BD, 20)
    f_sig_n = ImageFont.truetype(FONT_TIMES_BD, 32)
    st = "QÖŞKÖPIR TUMAN TAʼLIM BÖLIMI BOŞLIĞI"
    sn = "Ş.R. JUMANIYOZOV"
    cx_r = 1195
    draw.text((cx_r - draw.textlength(st, font=f_sig_t)/2, 872), st, font=f_sig_t, fill=(51, 65, 85))
    draw.text((cx_r - draw.textlength(sn, font=f_sig_n)/2, 914), sn, font=f_sig_n, fill=(12, 26, 48))

    # Date at bottom center
    f_dt = ImageFont.truetype(FONT_TIMES_IT, 18)
    dt = "2026-yil dekabr"
    draw.text(((1754 - draw.textlength(dt, font=f_dt))/2, 1018), dt, font=f_dt, fill=(100, 116, 139))

    return draw, metal

def create_diploma(student_name, school, grade, direction, place, number="001"):
    theme_key = get_theme_key(direction)
    bg_path = os.path.join(THEMES_DIR, f"bg_{theme_key}.jpg")
    base = Image.open(bg_path).convert("RGB")
    draw, metal = draw_common_frame(base, direction, place, "DIPLOM RAQAMI", number)

    f_title = ImageFont.truetype(FONT_TIMES_BD, 78)
    f_daraja = ImageFont.truetype(FONT_TIMES_BD, 44)
    f_text = ImageFont.truetype(FONT_TIMES, 30)
    f_name = ImageFont.truetype(FONT_TIMES_BD, 48)
    f_taqdir = ImageFont.truetype(FONT_TIMES_BD, 32)

    # Title
    t_str = "D I P L O M"
    draw.text(((1754 - draw.textlength(t_str, font=f_title))/2, 272), t_str, font=f_title, fill=(12, 26, 48))

    # Daraja in metallic Gold/Silver/Bronze
    daraja_map = {1: "I DARAJALI", 2: "II DARAJALI", 3: "III DARAJALI"}
    daraja_text = daraja_map.get(place, f"{place}-DARAJALI")
    draw.text(((1754 - draw.textlength(daraja_text, font=f_daraja))/2, 368), daraja_text, font=f_daraja, fill=metal["primary"])

    # Description
    grade_clean = to_yangi_lotin(grade if "sinf" in str(grade) else f"{grade}-sinf")
    dir_clean = to_yangi_lotin(direction)
    school_clean = to_yangi_lotin(school)
    student_clean = to_yangi_lotin(student_name).upper()

    l1 = "2026/2027-öquv yilidagi “Ixtiroçilikka qadam” tanlovining tuman bosqiçida"
    l2 = f"{grade_clean} böyiça {dir_clean} yönalişida {place}-örinni qölga kiritgani uçun"
    l3 = f"Qöşköpir tumani, {school_clean} öquvçisi"

    draw.text(((1754 - draw.textlength(l1, font=f_text))/2, 440), l1, font=f_text, fill=(30, 41, 59))
    draw.text(((1754 - draw.textlength(l2, font=f_text))/2, 488), l2, font=f_text, fill=(30, 41, 59))
    draw.text(((1754 - draw.textlength(l3, font=f_text))/2, 536), l3, font=f_text, fill=(30, 41, 59))

    # Student Name
    w_n = draw.textlength(student_clean, font=f_name)
    if w_n > 1250:
        f_name = ImageFont.truetype(FONT_TIMES_BD, 38)
        w_n = draw.textlength(student_clean, font=f_name)
    draw.text(((1754 - w_n)/2, 608), student_clean, font=f_name, fill=(12, 26, 48))

    # Metallic divider line
    draw.line([(420, 682), (1334, 682)], fill=metal["accent"], width=3)

    # TAQDIRLANADI
    taq = "T A Q D I R L A N A D I"
    draw.text(((1754 - draw.textlength(taq, font=f_taqdir))/2, 706), taq, font=f_taqdir, fill=(30, 41, 59))

    return base

def create_tashakkurnoma(teacher_name, school, role_or_subject, student_name, grade, direction, place, number="001"):
    theme_key = get_theme_key(direction)
    bg_path = os.path.join(THEMES_DIR, f"bg_{theme_key}.jpg")
    base = Image.open(bg_path).convert("RGB")
    draw, metal = draw_common_frame(base, direction, place, "RAQAMI", number)

    f_title = ImageFont.truetype(FONT_TIMES_BD, 62)
    f_hurmatli = ImageFont.truetype(FONT_TIMES_IT, 38)
    f_teacher = ImageFont.truetype(FONT_TIMES_BD, 46)
    f_sub = ImageFont.truetype(FONT_TIMES, 26)
    f_para = ImageFont.truetype(FONT_TIMES, 27)
    f_close = ImageFont.truetype(FONT_TIMES_BD, 28)

    # Title
    t_str = "T A Ş A K K U R N O M A"
    draw.text(((1754 - draw.textlength(t_str, font=f_title))/2, 272), t_str, font=f_title, fill=(12, 26, 48))

    # Hurmatli
    h_str = "Hurmatli"
    draw.text(((1754 - draw.textlength(h_str, font=f_hurmatli))/2, 348), h_str, font=f_hurmatli, fill=(51, 65, 85))

    # Teacher Name
    teacher_clean = to_yangi_lotin(teacher_name)
    w_tn = draw.textlength(teacher_clean, font=f_teacher)
    if w_tn > 1250:
        f_teacher = ImageFont.truetype(FONT_TIMES_BD, 38)
        w_tn = draw.textlength(teacher_clean, font=f_teacher)
    draw.text(((1754 - w_tn)/2, 398), teacher_clean, font=f_teacher, fill=(12, 26, 48))

    # School & Role
    school_clean = to_yangi_lotin(school)
    role_clean = to_yangi_lotin(role_or_subject or "tögarak rahbari")
    sub_text = f"({school_clean}, {role_clean})"
    draw.text(((1754 - draw.textlength(sub_text, font=f_sub))/2, 456), sub_text, font=f_sub, fill=(71, 85, 105))

    # Metallic divider line
    draw.line([(420, 502), (1334, 502)], fill=metal["accent"], width=3)

    # Body paragraph
    grade_clean = to_yangi_lotin(grade if "sinf" in str(grade) else f"{grade}-sinf")
    student_clean = to_yangi_lotin(student_name)
    dir_clean = to_yangi_lotin(direction)

    p1 = f"Siz tayyorlagan {grade_clean} öquvçisi {student_clean} 2026/2027-öquv"
    p2 = f"yilidagi “Ixtiroçilikka qadam” tanlovining tuman bosqiçida {dir_clean} yönalişida {place}-örinni egalladi."
    p3 = "Öquvçilarni yuksak natijalarga yetaklagan fidokorona mehnatingiz, kasbiy mahoratingiz va"
    p4 = "ilhomlantiruvçi ustozligingiz uçun Sizga çuqur minnatdorçilik bildiramiz."

    for idx, line in enumerate([p1, p2, p3, p4]):
        f_use = f_para
        if draw.textlength(line, font=f_use) > 1250:
            f_use = ImageFont.truetype(FONT_TIMES, 22)
        draw.text(((1754 - draw.textlength(line, font=f_use))/2, 526 + idx * 40), line, font=f_use, fill=(30, 41, 59))

    # Closing
    cl = "İş faoliyatingizda yangi zafarlar tilaymiz!"
    draw.text(((1754 - draw.textlength(cl, font=f_close))/2, 708), cl, font=f_close, fill=metal["primary"])

    return base

def generate_all_5_directions_samples(target_dir):
    samples_root = os.path.join(target_dir, "Namuna_5_Yonalish_2026")
    os.makedirs(samples_root, exist_ok=True)

    directions_meta = [
        ("01_Talim", "Taʼlim", "14-son umumiy örta taʼlim maktabi", "9-sinf", "NAMUNA ÖQUVÇI F.I.Ş.", "Namuna Ustoz F.I.Ş.", "Informatika fani öqituvçisi"),
        ("02_Axborot_texnologiyalari_IT", "Axborot texnologiyalari (IT)", "23-son umumiy örta taʼlim maktabi", "8-sinf", "ABDULLAYEV JAMŞIDBEK DIYOR ÖĞLI", "Madaminov Jasurbek Baxtiyoroviç", "Fizika va robototexnika tögaragi rahbari"),
        ("03_Yashil_energiya", "Yaşil energiya", "5-son ixtisoslaştirilgan maktab", "9-sinf", "SANJARBEKOV MIRALI SANJARBEK ÖĞLI", "Namuna Ustoz F.I.Ş.", "Fizika fani öqituvçisi"),
        ("04_Ekologiya_va_iqlim_ozgarishi", "Ekologiya va iqlim özgarişi", "4-son umumiy örta taʼlim maktabi", "8-sinf", "RÖZMATOV RÖZMATBOY XUŞNUDBEK ÖĞLI", "Namuna Ustoz F.I.Ş.", "Biologiya va ekologiya fani öqituvçisi"),
        ("05_Qishloq_xojaligi", "Qişloq xöjaligi", "6-son umumiy örta taʼlim maktabi", "11-sinf", "FAYZULLAYEV BOYMUROD BOBOMUROD ÖĞLI", "Ollaberganova Laylo Rözimbayevna", "Informatika va axborot texnologiyalari fani öqituvçisi"),
    ]

    all_diploms = []
    all_tashakkurs = []
    dip_num = 1
    tash_num = 1

    for folder_name, dir_label, school, grade, student, teacher, role in directions_meta:
        dir_folder = os.path.join(samples_root, folder_name)
        os.makedirs(dir_folder, exist_ok=True)
        for f in os.listdir(dir_folder):
            fp = os.path.join(dir_folder, f)
            if os.path.isfile(fp):
                os.remove(fp)

        for place in [1, 2, 3]:
            metal_name = get_metal_colors(place)["name"]
            # Diplom sample
            dip_img = create_diploma(student, school, grade, dir_label, place, str(dip_num).zfill(3))
            dip_file = os.path.join(dir_folder, f"Diplom_{place}-orin_{metal_name}_{folder_name}.jpg")
            dip_img.save(dip_file, quality=95)
            all_diploms.append(dip_img)
            dip_num += 1

            # Tashakkurnoma sample
            tash_img = create_tashakkurnoma(teacher, school, role, student, grade, dir_label, place, str(tash_num).zfill(3))
            tash_file = os.path.join(dir_folder, f"Tashakkurnoma_{place}-orin_{metal_name}_{folder_name}.jpg")
            tash_img.save(tash_file, quality=95)
            all_tashakkurs.append(tash_img)
            tash_num += 1

    # Save 2 unified print-ready PDFs for all 15 Diploms and all 15 Tashakkurnomas
    pdf_dips = os.path.join(samples_root, "Namuna_15_ta_Diplom_5_yonalish.pdf")
    all_diploms[0].save(pdf_dips, save_all=True, append_images=all_diploms[1:], resolution=150.0)

    pdf_tash = os.path.join(samples_root, "Namuna_15_ta_Tashakkurnoma_5_yonalish.pdf")
    all_tashakkurs[0].save(pdf_tash, save_all=True, append_images=all_tashakkurs[1:], resolution=150.0)

    print(f"SUCCESS: Generated 15 Diplom + 15 Tashakkurnoma samples across all 5 directions in {samples_root}")

def main():
    target_dir = r"C:\Users\Monitoring\Desktop\ОЛИМПИАДАЛАР\2026\Ихтирочиликка қадам\туман босқичи\туман босқичи ғолибларни тақдирлаш"
    output_pdf = os.path.join(target_dir, "Goliblar_Diplom_va_Tashakkurnoma_2026.pdf")
    output_img_dir = os.path.join(target_dir, "Goliblar_Rasmlar_2026")
    os.makedirs(output_img_dir, exist_ok=True)

    for f in os.listdir(output_img_dir):
        fp = os.path.join(output_img_dir, f)
        if os.path.isfile(fp):
            os.remove(fp)

    winners = [
        {
            "place": 1,
            "school": "6-son umumiy örta taʼlim maktabi",
            "project": "AGRO ROBOT (GROWERX)",
            "direction": "Qişloq xöjaligi",
            "students": [
                {"name": "FAYZULLAYEV BOYMUROD BOBOMUROD ÖĞLI", "grade": "11-sinf"}
            ],
            "teacher": "Ollaberganova Laylo Rözimbayevna",
            "teacher_role": "Informatika va axborot texnologiyalari fani öqituvçisi"
        },
        {
            "place": 2,
            "school": "23-son umumiy örta taʼlim maktabi",
            "project": "Harakatlanuvçi qurilma",
            "direction": "Axborot texnologiyalari (IT)",
            "students": [
                {"name": "ABDULLAYEV JAMŞIDBEK DIYOR ÖĞLI", "grade": "8-sinf"},
                {"name": "OTAJONOV AKROMJON ĞULOMJON ÖĞLI", "grade": "9-sinf"}
            ],
            "teacher": "Madaminov Jasurbek Baxtiyoroviç",
            "teacher_role": "Fizika va robototexnika tögaragi rahbari"
        },
        {
            "place": 3,
            "school": "9-son ixtisoslaştirilgan maktab",
            "project": "Robot ekskavator",
            "direction": "Axborot texnologiyalari (IT)",
            "students": [
                {"name": "MAŞARIPOV JAVOHIR HASANBOY ÖĞLI", "grade": "7-sinf"}
            ],
            "teacher": "Bobojonov Şavkat Rustamoviç",
            "teacher_role": "Informatika fani öqituvçisi"
        }
    ]

    all_pages = []
    cert_counter = 1

    for w in winners:
        place = w["place"]
        metal_name = get_metal_colors(place)["name"]
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

    if all_pages:
        all_pages[0].save(
            output_pdf,
            save_all=True,
            append_images=all_pages[1:],
            resolution=150.0
        )
        print(f"SUCCESS: Generated {len(all_pages)} current winner award documents!")

    # Also generate full 5 directions x 3 places (15 Diploms + 15 Tashakkurnomas) ready sample pack!
    generate_all_5_directions_samples(target_dir)

if __name__ == "__main__":
    main()
