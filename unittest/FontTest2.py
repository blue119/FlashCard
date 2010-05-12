#!/usr/bin/env python3.0
# -*- coding: UTF-8 -*-

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import reportlab.rl_config
reportlab.rl_config.warnOnMissingFontGlyphs = 0
reportlab.rl_config.TTFSearchPath.append("/usr/share/fonts/truetype/arphic/")

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont('uming', 'uming.ttc'))
pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))

def GenPdf(FileName):
	canv = canvas.Canvas(FileName, pagesize = A4 )
	canv.setFont('uming', 32)
	canv.drawString(10, 350, "中文勒")
	#canv.drawString(10, 150, "Some text encoded in UTF-8")
	canv.drawString(10, 320, "In the Vera TT Font!")
	canv.setFont('Vera', 32)
	canv.drawString(10, 290, "In the Vera TT Font!")
	canv.setFont('Times-Italic', 32)
	canv.drawString(10, 260, "In the Vera TT Font!")
	#canv.drawString(100, 100, "!!Hello World!!")
	canv.showPage()
	canv.save()

if __name__ == "__main__":
	GenPdf("MyPdf.pdf")

