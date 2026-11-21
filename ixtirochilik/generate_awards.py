import os
import sys
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = r"C:\Users\Monitoring\.gemini\antigravity\scratch\olimpiada-portal\ixtirochilik"
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
THEMES_DIR = os.path.join(ASSETS_DIR, "themes")

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
        return {"primary": (90, 105, 125), "accent": (158, 170, 184), "name": "Kumuş"}
    else:
        return {"primary": (154, 80, 40), "accent": (180, 115, 80), "name": "Bronza"}

def load_metallic_base(doc_type, place, direction):
    p = place if place in [1, 2, 3] else 1
    prefix = "diplom_base" if doc_type == "diplom" else "tashakkurnoma_base"
    base_path = os.path.join(ASSETS_DIR, f"{prefix}_{p}.jpg")
    base = Image.open(base_path).convert("RGBA")

    # Subtle direction watermark inside the white interior (bilinar-bilinmas orqa fon)
    theme_key = get_theme_key(direction)
    wm_path = os.path.join(THEMES_DIR, f"wm_{theme_key}.png")
    if os.path.exists(wm_path):
        wm = Image.open(wm_path).convert("RGBA")
        wm = wm.resize((540, 540), Image.Resampling.LANCZOS)
        # Position softly centered behind the body text area
        y_pos = 270 if doc_type == "diplom" else 260
        base.alpha_composite(wm, (877 - 270, y_pos))

    return base.convert("RGB")

def create_diploma(student_name, school, grade, direction, place, number="001"):
    base = load_metallic_base("diplom", place, direction)
    draw = ImageDraw.Draw(base)
    metal = get_metal_colors(place)

    font_box_lbl = ImageFont.truetype(FONT_TIMES, 15)
    font_box_num = ImageFont.truetype(FONT_TIMES_BD, 24)
    font_daraja = ImageFont.truetype(FONT_TIMES_BD, 46)
    font_text = ImageFont.truetype(FONT_TIMES, 32)
    font_name = ImageFont.truetype(FONT_TIMES_BD, 50)

    # 1. Top-right number box (cleanly centered inside official metallic box)
    lbl = "DIPLOM RAQAMI"
    num_str = f"№ {str(number).zfill(3)}"
    draw.text(((1485 + 1665 - draw.textlength(lbl, font=font_box_lbl))/2, 66), lbl, font=font_box_lbl, fill=(70, 70, 70))
    draw.text(((1485 + 1665 - draw.textlength(num_str, font=font_box_num))/2, 90), num_str, font=font_box_num, fill=(10, 20, 50))

    # 2. Daraja in Gold / Silver / Bronze
    daraja_map = {1: "I DARAJALI", 2: "II DARAJALI", 3: "III DARAJALI"}
    daraja_text = daraja_map.get(place, f"{place}-DARAJALI")
    draw.text(((1754 - draw.textlength(daraja_text, font=font_daraja))/2, 355), daraja_text, font=font_daraja, fill=metal["primary"])

    # 3. Description
    grade_clean = to_yangi_lotin(grade if "sinf" in str(grade) else f"{grade}-sinf")
    dir_clean = to_yangi_lotin(direction)
    school_clean = to_yangi_lotin(school)
    student_clean = to_yangi_lotin(student_name).upper()

    l1 = "2026/2027-öquv yilidagi “Ixtiroçilikka qadam” tanlovining tuman bosqiçida"
    l2 = f"{grade_clean} böyiça {dir_clean} yönalişida {place}-örinni qölga kiritgani uçun"
    l3 = f"Qöşköpir tumani, {school_clean} öquvçisi"

    draw.text(((1754 - draw.textlength(l1, font=font_text))/2, 448), l1, font=font_text, fill=(30, 30, 30))
    draw.text(((1754 - draw.textlength(l2, font=font_text))/2, 503), l2, font=font_text, fill=(30, 30, 30))
    draw.text(((1754 - draw.textlength(l3, font=font_text))/2, 558), l3, font=font_text, fill=(30, 30, 30))

    # 4. Student Name
    w_n = draw.textlength(student_clean, font=font_name)
    if w_n > 1360:
        font_name = ImageFont.truetype(FONT_TIMES_BD, 40)
        w_n = draw.textlength(student_clean, font=font_name)
    draw.text(((1754 - w_n)/2, 642), student_clean, font=font_name, fill=(10, 20, 50))

    return base

def create_tashakkurnoma(teacher_name, school, role_or_subject, student_name, grade, direction, place, number="001"):
    base = load_metallic_base("tashakkur", place, direction)
    draw = ImageDraw.Draw(base)
    metal = get_metal_colors(place)

    font_box_lbl = ImageFont.truetype(FONT_TIMES, 16)
    font_box_num = ImageFont.truetype(FONT_TIMES_BD, 24)
    font_hurmatli = ImageFont.truetype(FONT_TIMES_IT, 42)
    font_teacher = ImageFont.truetype(FONT_TIMES_BD, 50)
    font_sub = ImageFont.truetype(FONT_TIMES, 28)
    font_para = ImageFont.truetype(FONT_TIMES, 28)
    font_close = ImageFont.truetype(FONT_TIMES_BD, 30)

    # 1. Box number
    lbl = "RAQAMI"
    num_str = f"№ {str(number).zfill(3)}"
    draw.text(((1485 + 1665 - draw.textlength(lbl, font=font_box_lbl))/2, 66), lbl, font=font_box_lbl, fill=(70, 70, 70))
    draw.text(((1485 + 1665 - draw.textlength(num_str, font=font_box_num))/2, 90), num_str, font=font_box_num, fill=(10, 20, 50))

    # 2. Hurmatli
    h_text = "Hurmatli"
    draw.text(((1754 - draw.textlength(h_text, font=font_hurmatli))/2, 315), h_text, font=font_hurmatli, fill=(45, 55, 72))

    # 3. Teacher Name
    teacher_clean = to_yangi_lotin(teacher_name)
    w_tn = draw.textlength(teacher_clean, font=font_teacher)
    if w_tn > 1360:
        font_teacher = ImageFont.truetype(FONT_TIMES_BD, 40)
        w_tn = draw.textlength(teacher_clean, font=font_teacher)
    draw.text(((1754 - w_tn)/2, 380), teacher_clean, font=font_teacher, fill=(10, 20, 50))

    # 4. School & Role
    school_clean = to_yangi_lotin(school)
    role_clean = to_yangi_lotin(role_or_subject or "tögarak rahbari")
    sub_text = f"({school_clean}, {role_clean})"
    draw.text(((1754 - draw.textlength(sub_text, font=font_sub))/2, 455), sub_text, font=font_sub, fill=(60, 60, 60))

    # 5. Body paragraph
    grade_clean = to_yangi_lotin(grade if "sinf" in str(grade) else f"{grade}-sinf")
    student_clean = to_yangi_lotin(student_name)
    dir_clean = to_yangi_lotin(direction)

    p1 = f"Siz tayyorlagan {grade_clean} öquvçisi {student_clean} 2026/2027-öquv"
    p2 = f"yilidagi “Ixtiroçilikka qadam” tanlovining tuman bosqiçida {dir_clean} yönalişida {place}-örinni egalladi."
    p3 = "Öquvçilarni yuksak natijalarga yetaklagan fidokorona mehnatingiz, kasbiy mahoratingiz va"
    p4 = "ilhomlantiruvçi ustozligingiz uçun Sizga çuqur minnatdorçilik bildiramiz."

    for idx, line in enumerate([p1, p2, p3, p4]):
        f_use = font_para
        if draw.textlength(line, font=f_use) > 1340:
            f_use = ImageFont.truetype(FONT_TIMES, 23)
        draw.text(((1754 - draw.textlength(line, font=f_use))/2, 552 + idx * 42), line, font=f_use, fill=(30, 30, 30))

    # 6. Closing
    cl = "İş faoliyatingizda yangi zafarlar tilaymiz!"
    draw.text(((1754 - draw.textlength(cl, font=font_close))/2, 742), cl, font=font_close, fill=metal["primary"])

    return base

def generate_all_5_directions_samples(target_dir):
    samples_root = os.path.join(target_dir, "Namuna_5_Yonalish_2026")
    os.makedirs(samples_root, exist_ok=True)

    directions_meta = [
        ("01_Talim", "Taʼlim", "14-son umumiy örta taʼlim maktabi", "9-sinf", "NAMUNA ÖQUVÇI F.I.Ş.", "Namuna Ustoz F.I.Ş.", "Informatika fani öqituvçisi"),
        ("02_Axborot_texnologiyalari_IT", "Axborot texnologiyalari (IT)", "23-son umumiy örta taʼlim maktabi", "8-sinf", "ABDULLAYEV JAMŞIDBEK DIYOR ÖĞLI", "Madaminov Jasurbek Baxtiyoroviç", "Fizika va robototexnika tögaragi rahbari"),
        ("03_Yashil_energiya", "Yaşil energiya", "5-IDUM", "9-sinf", "SANJARBEKOV MIRALI SANJARBEK ÖĞLI", "Namuna Ustoz F.I.Ş.", "Fizika fani öqituvçisi"),
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
            dip_img = create_diploma(student, school, grade, dir_label, place, str(dip_num).zfill(3))
            dip_file = os.path.join(dir_folder, f"Diplom_{place}-orin_{metal_name}_{folder_name}.jpg")
            dip_img.save(dip_file, quality=95)
            all_diploms.append(dip_img)
            dip_num += 1

            tash_img = create_tashakkurnoma(teacher, school, role, student, grade, dir_label, place, str(tash_num).zfill(3))
            tash_file = os.path.join(dir_folder, f"Tashakkurnoma_{place}-orin_{metal_name}_{folder_name}.jpg")
            tash_img.save(tash_file, quality=95)
            all_tashakkurs.append(tash_img)
            tash_num += 1

    pdf_dips = os.path.join(samples_root, "Namuna_15_ta_Diplom_5_yonalish.pdf")
    all_diploms[0].save(pdf_dips, save_all=True, append_images=all_diploms[1:], resolution=150.0)

    pdf_tash = os.path.join(samples_root, "Namuna_15_ta_Tashakkurnoma_5_yonalish.pdf")
    all_tashakkurs[0].save(pdf_tash, save_all=True, append_images=all_tashakkurs[1:], resolution=150.0)

    print(f"SUCCESS: Generated 15 Diplom + 15 Tashakkurnoma (Gold/Silver/Bronze frames + 5 direction watermarks) in {samples_root}")

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
            "school": "9-IDUM",
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

    generate_all_5_directions_samples(target_dir)

if __name__ == "__main__":
    main()
