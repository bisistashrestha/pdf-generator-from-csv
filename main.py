# ================================================================
# File: main.py
# Author: Bisista Shrestha
# Date: 2025-09-30
# License: MIT License (See LICENSE file)
# Description:
#     This script generates a PDF document based on topics and their
#     corresponding number of pages listed in 'topics.csv'. 
#     
#     - Each topic's first page includes a header with the topic title.
#     - All pages include a footer with the topic name and page number.
#     - The final output is saved as 'output.pdf'.
# ================================================================


from fpdf import FPDF
import pandas as pd

pdf=FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)
df=pd.read_csv("topics.csv")
page_no=0
for index,row in df.iterrows():
    for i in range(row["Pages"]):
        page_no+=1
        if i==0:
            pdf.add_page()
            #Set Header
            pdf.set_font(family = "Times",style = "B", size=24)
            pdf.set_text_color(100, 100, 100)
            pdf.set_line_width(0.5)
            pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
            pdf.line(10,22,200,22)

            #Set Footer
            pdf.ln(260)
            pdf.set_font(family = "Times",style = "I", size=8)
            pdf.set_text_color(180, 180, 180)
            pdf.cell(w=0, h=10, txt=row["Topic"], align="R", ln=1)
            pdf.cell(w=185, h=0.5, txt=str(page_no), align="R", ln=1)

        else:
            pdf.add_page()

            #Set Footer
            pdf.ln(272)
            pdf.set_font(family = "Times",style = "I", size=8)
            pdf.set_text_color(180, 180, 180)
            pdf.cell(w=0, h=10, txt=row["Topic"], align="R", ln=1)
            pdf.cell(w=185, h=0.5, txt=str(page_no), align="R", ln=1)

pdf.output('output.pdf')