# -*- coding: utf-8 -*-
"""
"Iqtidorlilikka qadam" tanlovi - Rasmiy Excel Bayonnomasi Generator
jadval-standartlari bo'yicha to'liq A4 Landshaft pechatga tayyor holatda yaratadi.
"""

import os
import json
from datetime import datetime
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

def generate_bayonnoma_excel():
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Baholash_Qaydnoması"

    # Fontlar (Standart: Times New Roman)
    font_title = Font(name="Times New Roman", size=14, bold=True)
    font_subtitle = Font(name="Times New Roman", size=11, italic=True)
    font_header = Font(name="Times New Roman", size=11, bold=True)
    font_data = Font(name="Times New Roman", size=10)
    font_bold = Font(name="Times New Roman", size=10, bold=True)
    font_sign = Font(name="Times New Roman", size=10)

    # Chiziqlar (Borders)
    thin = Side(border_style="thin", color="000000")
    double_bottom = Side(border_style="double", color="000000")
    border_cell = Border(left=thin, right=thin, top=thin, bottom=thin)
    border_header = Border(left=thin, right=thin, top=thin, bottom=thin)

    # Ranglar
    fill_header = PatternFill(start_color="F2F2F2", end_color="F2F2F2", fill_type="solid")
    fill_zebra = PatternFill(start_color="F8FAFC", end_color="F8FAFC", fill_type="solid")
    fill_rank1 = PatternFill(start_color="FEF08A", end_color="FEF08A", fill_type="solid")

    # Alignments
    align_center = Alignment(horizontal="center", vertical="center", wrap_text=True)
    align_left = Alignment(horizontal="left", vertical="center")
    align_right = Alignment(horizontal="right", vertical="center")

    # 1. Sarlavha
    ws.merge_cells("A1:N1")
    ws["A1"] = "QO‘SHKO‘PIR TUMANI MAKTABGACHA VA MAKTAB TA'LIMI BO‘LIMI"
    ws["A1"].font = font_title
    ws["A1"].alignment = align_center

    ws.merge_cells("A2:N2")
    ws["A2"] = "\"Iqtidorlilikka qadam\" tanlovi 1-bosqich yakuniy baholash QAYDNOMASI"
    ws["A2"].font = Font(name="Times New Roman", size=13, bold=True)
    ws["A2"].alignment = align_center

    ws.merge_cells("A3:N3")
    sana_str = datetime.now().strftime("%d.%m.%Y, soat %H:%M holatiga")
    ws["A3"] = f"Sana: 2026-yil 20-noyabr | Shakllantirilgan vaqt: {sana_str} | Joy: Qo‘shko‘pir tumani"
    ws["A3"].font = font_subtitle
    ws["A3"].alignment = align_center

    # 2. Ustunlar sarlavhasi
    headers = [
        "T/r", "O‘quvchining familiyasi, ismi, otasining ismi", "Ta'lim muassasasi", "Sinf",
        "1-Hakam\n(Mantiq)", "2-Hakam\n(Ijod)", "3-Hakam\n(Aniq)", "4-Hakam\n(Tabiiy)",
        "5-Hakam\n(Til)", "6-Hakam\n(Nutq)", "Jami\nball", "O‘rtacha\nball", "O‘rni", "Hakam\nimzosi"
    ]

    ws.row_dimensions[5].height = 28
    for col_idx, h in enumerate(headers, 1):
        cell = ws.cell(row=5, column=col_idx, value=h)
        cell.font = font_header
        cell.fill = fill_header
        cell.alignment = align_center
        cell.border = border_header

    # 3. Namunaviy ma'lumotlar
    students_data = [
        ("Karimova Mohinur Sanjar qizi", "4-son IDUM", "9-sinf", [98, 96, 95, 94, 97, 99]),
        ("Bekchanov Sardorbek Otabek o‘g‘li", "2-son IDUM", "8-sinf", [96, 95, 94, 92, 95, 97]),
        ("O‘rozboyev Doniyorbek Alisher o‘g‘li", "1-son umumta'lim maktabi", "8-sinf", [95, 92, 98, 90, 94, 96]),
        ("Ro‘zmetova Dilnoza Mansur qizi", "32-son umumta'lim maktabi", "9-sinf", [92, 94, 89, 91, 93, 90]),
        ("Matyoqubova Sabina Farhod qizi", "12-son umumta'lim maktabi", "9-sinf", [90, 88, 92, 85, 91, 89]),
        ("Quryozov Sherzod Ilhom o‘g‘li", "15-son umumta'lim maktabi", "8-sinf", [88, 85, 87, 84, 86, 89]),
        ("Yo‘ldoshev Jasurbek Bobur o‘g‘li", "25-son umumta'lim maktabi", "8-sinf", [85, 80, 88, 82, 84, 86]),
        ("Otajonova Madina Komil qizi", "7-son umumta'lim maktabi", "9-sinf", [84, 82, 85, 80, 83, 85]),
        ("Xudoyberganova Sevara Azamat qizi", "29-son umumta'lim maktabi", "9-sinf", [82, 80, 84, 79, 81, 83]),
        ("Jumaniyozov Bobur Davron o‘g‘li", "18-son umumta'lim maktabi", "8-sinf", [78, 75, 80, 76, 79, 82]),
    ]

    start_row = 6
    for idx, (name, school, grade, scores) in enumerate(students_data, 1):
        row_num = start_row + idx - 1
        ws.row_dimensions[row_num].height = 20
        is_zebra = (idx % 2 == 0)

        total_sum = sum(scores)
        avg_score = round(total_sum / len(scores), 2)
        rank = f"{idx}-o‘rin"

        row_vals = [idx, name, school, grade] + scores + [total_sum, avg_score, rank, ""]

        for col_idx, val in enumerate(row_vals, 1):
            cell = ws.cell(row=row_num, column=col_idx, value=val)
            cell.font = font_bold if col_idx in [1, 11, 12, 13] else font_data
            cell.border = border_cell

            # 0 larni bo'sh qoldirish qoidasi
            if val == 0:
                cell.value = ""

            # Tekislash
            if col_idx == 2:
                cell.alignment = align_left
            elif col_idx in [1, 4, 13, 14]:
                cell.alignment = align_center
            else:
                cell.alignment = align_center

            # Rang
            if idx == 1 and col_idx == 13:
                cell.fill = fill_rank1
            elif is_zebra:
                cell.fill = fill_zebra

    # 4. Imzolar bloki
    sign_row = start_row + len(students_data) + 2
    ws.merge_cells(f"A{sign_row}:N{sign_row}")
    ws[f"A{sign_row}"] = "HAKAMLAR HAY'ATI A'ZOLARI:"
    ws[f"A{sign_row}"].font = Font(name="Times New Roman", size=11, bold=True)

    judges_signatures = [
        ("1. Hakamlar hay'ati raisi:", "_________________ ( U. Mamatov )", "2. 1-Hakam (Mantiq):", "_________________ ( ___________ )"),
        ("3. 2-Hakam (Ijodiy fikrlash):", "_________________ ( ___________ )", "4. 3-Hakam (Aniq fanlar):", "_________________ ( ___________ )"),
        ("5. 4-Hakam (Tabiiy fanlar):", "_________________ ( ___________ )", "6. 5-Hakam (Til va adabiyot):", "_________________ ( ___________ )"),
        ("7. 6-Hakam (Taqdimot):", "_________________ ( ___________ )", "Kotib (Mas'ul xodim):", "_________________ ( ___________ )")
    ]

    for s_idx, (j1_title, j1_line, j2_title, j2_line) in enumerate(judges_signatures):
        curr = sign_row + 1 + s_idx
        ws.row_dimensions[curr].height = 22
        
        ws[f"B{curr}"] = j1_title
        ws[f"B{curr}"].font = font_bold
        ws.merge_cells(f"C{curr}:F{curr}")
        ws[f"C{curr}"] = j1_line
        ws[f"C{curr}"].font = font_sign

        ws[f"H{curr}"] = j2_title
        ws[f"H{curr}"].font = font_bold
        ws.merge_cells(f"I{curr}:M{curr}")
        ws[f"I{curr}"] = j2_line
        ws[f"I{curr}"].font = font_sign

    # 5. Ustun kengliklari
    col_widths = {
        "A": 5, "B": 38, "C": 24, "D": 9,
        "E": 11, "F": 11, "G": 11, "H": 11,
        "I": 11, "J": 11, "K": 11, "L": 11,
        "M": 10, "N": 12
    }
    for col_letter, width in col_widths.items():
        ws.column_dimensions[col_letter].width = width

    # =========================================================================
    # CHOP ETISH / PECHAT SOZLAMALARI (jadval-standartlari bo'yicha)
    # =========================================================================
    ws.page_setup.paperSize = ws.PAPERSIZE_A4
    ws.page_setup.orientation = ws.ORIENTATION_LANDSCAPE
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0
    ws.print_title_rows = "5:5"

    ws.page_margins.left = 0.4
    ws.page_margins.right = 0.4
    ws.page_margins.top = 0.5
    ws.page_margins.bottom = 0.5

    ws.print_options.horizontalCentered = True
    ws.print_options.gridLines = True
    ws.views.sheetView[0].showGridLines = True

    output_path = os.path.join(r"C:\Users\Monitoring\.gemini\antigravity\scratch\olimpiada\iqtidorlilikka-qadam", "Iqtidorlilikka_qadam_Bayonnoma.xlsx")
    wb.save(output_path)
    print(f"Muvaffaqiyatli yaratildi: {output_path}")

if __name__ == "__main__":
    generate_bayonnoma_excel()
