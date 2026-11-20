# -*- coding: utf-8 -*-
"""
"Ixtirochilikka qadam" tanlovi (2-tuman bosqichi) - Rasmiy Excel Bayonnomasi
jadval-standartlari bo'yicha A4 Landshaft, Times New Roman, pechatga 100% tayyor.
"""

import os
from datetime import datetime
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

def generate_ixtirochilik_excel():
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Ixtirochilik_Bayonnoma"

    font_title = Font(name="Times New Roman", size=13, bold=True)
    font_subtitle = Font(name="Times New Roman", size=10, italic=True)
    font_header = Font(name="Times New Roman", size=10, bold=True)
    font_data = Font(name="Times New Roman", size=9.5)
    font_bold = Font(name="Times New Roman", size=9.5, bold=True)
    font_small = Font(name="Times New Roman", size=8.5)

    thin = Side(border_style="thin", color="000000")
    border_cell = Border(left=thin, right=thin, top=thin, bottom=thin)

    fill_header = PatternFill(start_color="F2F2F2", end_color="F2F2F2", fill_type="solid")
    fill_zebra = PatternFill(start_color="F8FAFC", end_color="F8FAFC", fill_type="solid")
    fill_winner = PatternFill(start_color="DCFCE7", end_color="DCFCE7", fill_type="solid")

    align_center = Alignment(horizontal="center", vertical="center", wrap_text=True)
    align_left = Alignment(horizontal="left", vertical="center", wrap_text=True)

    # 1. Sarlavha
    ws.merge_cells("A1:O1")
    ws["A1"] = "QO‘SHKO‘PIR TUMANI MAKTABGACHA VA MAKTAB TA'LIMI BO‘LIMI"
    ws["A1"].font = font_title
    ws["A1"].alignment = align_center

    ws.merge_cells("A2:O2")
    ws["A2"] = "“Ixtirochilikka qadam” tanlovining ikkinchi (tuman) bosqichi yakuniy baholash QAYDNOMASI (BAYONNOMA)"
    ws["A2"].font = Font(name="Times New Roman", size=11.5, bold=True)
    ws["A2"].alignment = align_center

    ws.merge_cells("A3:O3")
    sana_str = datetime.now().strftime("%d.%m.%Y, %H:%M")
    ws["A3"] = f"Sana: 2026-yil 4-5-dekabr | Qo‘shko‘pir tumani | Shakllantirilgan vaqt: {sana_str}"
    ws["A3"].font = font_subtitle
    ws["A3"].alignment = align_center

    # 2. Ustunlar sarlavhasi
    headers = [
        "T/r", "Ta'lim muassasasi", "Loyiha nomi", "Yo‘nalish", "Mualliflar (Jamoa)",
        "1-H\n(IT)", "2-H\n(Fizika)", "3-H\n(Bio)", "4-H\n(Kimyo)",
        "5-H\n(Soha)", "6-H\n(Eko)", "7-H\n(Innov)", "O‘rtacha\nball", "O‘rni", "Qaror / Tavsiya"
    ]

    ws.row_dimensions[5].height = 30
    for col_idx, h in enumerate(headers, 1):
        cell = ws.cell(row=5, column=col_idx, value=h)
        cell.font = font_header
        cell.fill = fill_header
        cell.alignment = align_center
        cell.border = border_cell

    # 3. Namunaviy ma'lumotlar
    projects = [
        ("4-son IDUM", "AI-EkoDron: Ekinlar kasalliklarini aniqlash", "Qishloq xo‘jaligi", "Karimova Mohinur Sanjar qizi", [100, 98, 98, 98, 100, 100, 97], 98.71, "1-o‘rin", "Viloyatga tavsiya"),
        ("1-son maktab", "Aqlli quyosh panellari orientatsiya tizimi", "Yashil energiya", "O‘rozboyev Doniyorbek, Yo‘ldoshev Jasurbek", [96, 94, 91, 96, 94, 95, 92], 94.00, "2-o‘rin", "Viloyatga tavsiya"),
        ("2-son IDUM", "Avtomatlashtirilgan tomchilatib sug‘orish", "Ekologiya", "Bekchanov Sardorbek Otabek o‘g‘li", [95, 94, 92, 95, 94, 93, 94], 93.86, "3-o‘rin", "Viloyatga tavsiya"),
        ("12-son maktab", "Virtual kimyo laboratoriyasi", "Ta‘lim", "Matyoqubova S., Ro‘zmetova D., Otajonova M.", [88, 87, 89, 84, 89, 86, 88], 87.29, "4-o‘rin", "Ishtirokchi"),
        ("18-son maktab", "Bio-plastik qadoqlash materiali", "Ekologiya", "Jumaniyozov Bobur, Quryozov Sherzod", [80, 82, 82, 85, 78, 84, 79], 81.43, "5-o‘rin", "Ishtirokchi")
    ]

    start_row = 6
    for idx, (school, pname, direction, authors, scores, avg_val, rank_str, decision) in enumerate(projects, 1):
        row_num = start_row + idx - 1
        ws.row_dimensions[row_num].height = 24
        is_zebra = (idx % 2 == 0)
        is_winner = (idx <= 3)

        row_vals = [idx, school, pname, direction, authors] + scores + [avg_val, rank_str, decision]

        for col_idx, val in enumerate(row_vals, 1):
            cell = ws.cell(row=row_num, column=col_idx, value=val)
            cell.font = font_bold if col_idx in [1, 13, 14, 15] else font_data
            cell.border = border_cell

            if val == 0:
                cell.value = ""

            if col_idx in [2, 3, 5]:
                cell.alignment = align_left
            else:
                cell.alignment = align_center

            if is_winner and col_idx == 15:
                cell.fill = fill_winner
            elif is_zebra:
                cell.fill = fill_zebra

    # 4. Qaror matni
    dec_row = start_row + len(projects) + 1
    ws.merge_cells(f"A{dec_row}:O{dec_row}")
    ws[f"A{dec_row}"] = "HAKAMLAR HAY'ATI QARORI: Nizomga muvofiq, eng yuqori ball to‘plagan 1-, 2- va 3-o‘rin sohiblari tanlovning viloyat bosqichiga tavsiya etilsin."
    ws[f"A{dec_row}"].font = font_bold
    ws[f"A{dec_row}"].alignment = align_left

    # 5. Imzolar (2-ILOVA: Tashkiliy qo'mita + 3-ILOVA: Hakamlar hay'ati)
    sign_start = dec_row + 2
    ws.merge_cells(f"A{sign_start}:G{sign_start}")
    ws[f"A{sign_start}"] = "TASHKILIY QO‘MITA A'ZOLARI:"
    ws[f"A{sign_start}"].font = font_bold

    ws.merge_cells(f"I{sign_start}:O{sign_start}")
    ws[f"I{sign_start}"] = "HAKAMLAR HAY'ATI A'ZOLARI (7 NAFAR):"
    ws[f"I{sign_start}"].font = font_bold

    committee_sigs = [
        "1. Tuman MMTB bo‘limi boshlig‘i, rais: ___________",
        "2. Barkamol avlod direktori, a'zo: ___________",
        "3. Ishlab chiqarish sohasi vakili, a'zo: ___________",
        "4. IT sohasiga oid mutaxassis, a'zo: ___________",
        "5. Bosh mutaxassis, kotib: ___________"
    ]

    judge_sigs = [
        "1. Informatika o‘qituvchisi: ___________",
        "2. Fizika o‘qituvchisi: ___________",
        "3. Biologiya o‘qituvchisi: ___________",
        "4. Kimyo o‘qituvchisi: ___________",
        "5. Sohaga oid mutaxassis (IT): ___________",
        "6. Sohaga oid mutaxassis (Eko): ___________",
        "7. Sohaga oid mutaxassis (Innov): ___________"
    ]

    max_lines = max(len(committee_sigs), len(judge_sigs))
    for l_idx in range(max_lines):
        curr_row = sign_start + 1 + l_idx
        ws.row_dimensions[curr_row].height = 18

        if l_idx < len(committee_sigs):
            ws.merge_cells(f"A{curr_row}:G{curr_row}")
            ws[f"A{curr_row}"] = committee_sigs[l_idx]
            ws[f"A{curr_row}"].font = font_small

        if l_idx < len(judge_sigs):
            ws.merge_cells(f"I{curr_row}:O{curr_row}")
            ws[f"I{curr_row}"] = judge_sigs[l_idx]
            ws[f"I{curr_row}"].font = font_small

    # Ustun kengliklari
    col_widths = {
        "A": 4, "B": 18, "C": 28, "D": 16, "E": 24,
        "F": 7, "G": 7, "H": 7, "I": 7, "J": 7, "K": 7, "L": 7,
        "M": 10, "N": 9, "O": 16
    }
    for col_letter, width in col_widths.items():
        ws.column_dimensions[col_letter].width = width

    # Pechat / Chop etish sozlamalari (A4 Landshaft, jadval-standartlari)
    ws.page_setup.paperSize = ws.PAPERSIZE_A4
    ws.page_setup.orientation = ws.ORIENTATION_LANDSCAPE
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0
    ws.print_title_rows = "5:5"

    ws.page_margins.left = 0.35
    ws.page_margins.right = 0.35
    ws.page_margins.top = 0.45
    ws.page_margins.bottom = 0.45

    ws.print_options.horizontalCentered = True
    ws.print_options.gridLines = True
    ws.views.sheetView[0].showGridLines = True

    out_file = os.path.join(r"C:\Users\Monitoring\.gemini\antigravity\scratch\olimpiada\ixtirochilik", "Ixtirochilikka_qadam_Tuman_bosqichi_Bayonnoma.xlsx")
    wb.save(out_file)
    print(f"Yaratildi: {out_file}")

if __name__ == "__main__":
    generate_ixtirochilik_excel()
