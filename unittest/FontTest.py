#!/usr/bin/env python3.0
# -*- coding: UTF-8 -*-

from os import listdir
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import reportlab.rl_config
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import pdb

reportlab.rl_config.warnOnMissingFontGlyphs = 0
reportlab.rl_config.TTFSearchPath.append("/usr/share/fonts/truetype/freefont/")
reportlab.rl_config.TTFSearchPath.append("/usr/share/fonts/truetype/arphic/")
reportlab.rl_config.TTFSearchPath.append("/usr/share/fonts/truetype/thai")

font_list = []
for i in reportlab.rl_config.TTFSearchPath:
    for j in listdir(i):
        # j: FreeMonoBoldOblique.ttf
        # j.split('.')[0]: FreeMonoBoldOblique
        pdfmetrics.registerFont(TTFont(j.split('.')[0], j))
        font_list.append(j.split('.')[0])

font_size = 12

upper = 810
under = 20
pos_x = 40

def GenPdf(FileName):
    canv = canvas.Canvas(FileName, pagesize = A4 )
    pos_y = upper

    for i in range(len(font_list)):
        if pos_y:
            canv.setFont(font_list[i], font_size)
            canv.drawString(pos_x, pos_y, str(i) + '. ' + font_list[i] + '  ' + 'Style')
            canv.drawString(pos_x, pos_y - 15, "中文字型沒問題的啦")
            canv.drawString(pos_x, pos_y - 15 * 2, "phonetic: " + "[fәu'netik]")
            canv.drawString(pos_x, pos_y - 15 * 3, "iiiiiiiiiiiiiiiiii")
            canv.drawString(pos_x, pos_y - 15 * 4, "TTTTTTTTTTTTTTTTTT")
            canv.drawString(pos_x, pos_y - 15 * 5, "Take honour from me and my life is undone.")
            pos_y -= (15 * 6)
        else:
            pos_y = upper
            canv.showPage()

    canv.showPage()
    canv.save()

if __name__ == "__main__":
    GenPdf("MyPdf.pdf")

