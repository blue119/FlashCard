# -*- coding: UTF-8 -*-
# A4 Size = 210×297
#
import csv
import sys
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib.colors import pink, black, red, blue, green
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import reportlab.rl_config
import platform
iOS = platform.system()

pdfmetrics.registerFont(TTFont('arial_unicode', 'ARIALUNI.TTF'))

__version__ = '0.1'

	#c.setStrokeColor(red)
	#c.setFont("Times-Roman", 20)
	#c.drawString(1*cm, 1*cm, "(1,1) * cm ..... ")
#global Debug = 0

def Table(canvas):
	c = canvas
	c.grid([0.75 * cm, 10.5 * cm, 20.25 * cm], [0.85 * cm, 7.85 * cm, 14.85 * cm, 21.85 * cm, 28.85 * cm])

	# Draw Dash Line
	c.setDash(1,2)
	for x in range(2):
		for y in range(4):
			c.line((0.75 + (x * 9.75)) * cm, (27.6 - (y * 7)) * cm, (10.5 + (x * 9.75)) * cm, (27.6 - (y * 7)) * cm)
			c.line((0.75 + (x * 9.75)) * cm, (27.1 - (y * 7)) * cm, (10.5 + (x * 9.75)) * cm, (27.1 - (y * 7)) * cm)
			
			c.line((0.75 + (x * 9.75)) * cm, (25.4 - (y * 7)) * cm, (10.5 + (x * 9.75)) * cm, (25.4 - (y * 7)) * cm)
			#c.line((0.75 + (x * 9.75)) * cm, (24.35 - (y * 7)) * cm, (10.5 + (x * 9.75)) * cm, (24.35 - (y * 7)) * cm)
			c.line((0.75 + (x * 9.75)) * cm, (24.9 - (y * 7)) * cm, (10.5 + (x * 9.75)) * cm, (24.9 - (y * 7)) * cm)
			c.line((0.75 + (x * 9.75)) * cm, (23.3 - (y * 7)) * cm, (10.5 + (x * 9.75)) * cm, (23.3 - (y * 7)) * cm)
			c.line((0.75 + (x * 9.75)) * cm, (22.35 - (y * 7)) * cm, (10.5 + (x * 9.75)) * cm, (22.35 - (y * 7)) * cm)

			c.line((3.75 + (x * 9.75)) * cm, (22.35 - (y * 7)) * cm, (3.75 + (x * 9.75)) * cm, (21.85 - (y * 7)) * cm)
			c.line((8.5 + (x * 9.75)) * cm, (22.35 - (y * 7)) * cm, (8.5 + (x * 9.75)) * cm, (21.85 - (y * 7)) * cm)
	
	#iString = "I am a string......."
	#c.drawCentredString(5.625 * cm, 28.1 * cm, "X XXX XXX XXX XXX XXX XXX X")
	#c.drawString(0.75 * cm, 27.35 * cm, iString)
	#c.setFillColor(green)
	# column 2
	#c.circle(0.75 * cm, 0.85 * cm, 0.05 * cm, fill = 1)
	#c.circle(0.75 * cm, 7.85 * cm, 0.05 * cm, fill = 1)
	#c.circle(0.75 * cm, 14.85 * cm, 0.05 * cm, fill = 1)
	#c.circle(0.75 * cm, 21.85 * cm, 0.05 * cm, fill = 1)
	#c.circle(0.75 * cm, 28.85 * cm, 0.05 * cm, fill = 1)
	# column 3
	#c.circle(10.5 * cm, 0.85 * cm, 0.05 * cm, fill = 1)
	#c.circle(10.5 * cm, 7.85 * cm, 0.05 * cm, fill = 1)
	#c.circle(10.5 * cm, 14.85 * cm, 0.05 * cm, fill = 1)
	#c.circle(10.5 * cm, 21.85 * cm, 0.05 * cm, fill = 1)
	#c.circle(10.5 * cm, 28.85 * cm, 0.05 * cm, fill = 1)
	# column 4
	#c.circle(20.25 * cm, 0.85 * cm, 0.05 * cm, fill = 1)
	#c.circle(20.25 * cm, 7.85 * cm, 0.05 * cm, fill = 1)
	#c.circle(20.25 * cm, 14.85 * cm, 0.05 * cm, fill = 1)
	#c.circle(20.25 * cm, 21.85 * cm, 0.05 * cm, fill = 1)
	#c.circle(20.25 * cm, 28.85 * cm, 0.05 * cm, fill = 1)

def Content(c, row, x, y): 
	'''
	+-------------------------------------------------------------+
	|                row[vocabulary]:row[classes]                 |
	+-------------------------------------------------------------+
	|                          row[tense]
	+-------------------------------------------------------------+
	|                         row[meaning] 
	+-------------------------------------------------------------+
	|                          row[idiom]
	+-------------------------------------------------------------+
	|                         row[sentence]
	+-------------------------------------------------------------+
	|                       row[association]
	+-------------------------------------------------------------+
	|row[translate] |         row[source]      | row[arrange_time]|
	+-------------------------------------------------------------+				 
		'''
	styleSheet = getSampleStyleSheet()
	style = styleSheet['BodyText']
	Voc_Cla = '<para align=center><font size=26 name=arial_unicode>' + row['vocabulary'] \
		+ '</font><i>' + '   ' + row['classes'] + '</i></para>'
	P = Paragraph(Voc_Cla, style)
	P.wrap(9.5 * cm, 1.5 * cm)
	if iOS == 'Linux':
		P.drawOn(c, (0.9 + (x * 9.75))* cm, (28.4 - (y * 7))* cm)
	else:
		P.drawOn(c, (0.9 + (x * 9.75))* cm, (28.2 - (y * 7))* cm)
	#P.drawOn(c, 0.9 * cm, 28.2 * cm)
	#c.drawString(11 * cm, 28 * cm, str(len(Voc_Cla)))
	
	Tense = '<para align=center><font name=arial_unicode>' + row['tense'] + '</font></para>'
	#Tense = '<para align=center>6 7 8 9 0 a b c e f g h i j k l m n o p q A B C</para>'
	P = Paragraph(Tense, style)
	P.wrap(9.5 * cm, 0.5 * cm)
	P.drawOn(c, (0.9 + (x * 9.75))* cm, (27.15- (y * 7))* cm)
	#c.drawString(11 * cm, 27.2 * cm, str(len(Tense)))

	Meaning = row['meaning']
	#Meaning = 'a statue of a woman on Liberty Island, in New York Harbour, given to \
#the US by France in 1884 to celebrate the American and French revolutions. \
#The woman is holding up a.'
	P = Paragraph(Meaning, style)
	P.wrap(9.5 * cm, 0.5 * cm)
	P.drawOn(c, (0.9 + (x * 9.75))* cm, (25.8 - (y * 7))* cm)
	#P.drawOn(c, 0.9 * cm, 25.35 * cm)
	#c.drawString(11 * cm, 25.45 * cm, str(len(Meaning)))
	
	#Idiom = 'a b c d e f g h i j k l m n o p q r s t u v w x y z | A B C D E F G H I'
	Idiom = '<para align=center>' + row['idiom'] + '</para>'
	P = Paragraph(Idiom, style)
	P.wrap(9.5 * cm, 0.5 * cm)
	P.drawOn(c, (0.9 + (x * 9.75))* cm, (24.93- (y * 7))* cm)
	#c.drawString(11 * cm, 25 * cm, str(len(Idiom)))
	
	Sentence = row['sentence']
	#Sentence = 'A pharmacist is someone who prepares and sells medicines. \
#This is the usual word in American English, but in British English pharmacist \
#is slightly technical and it is more  '
	P = Paragraph(Sentence, style)
	P.wrap(9.5 * cm, 0.5 * cm)
	#P.drawOn(c, 0.9 * cm, 23.2 * cm)
	P.drawOn(c, (0.9 + (x * 9.75))* cm, (23.6 - (y * 7))* cm)
	#c.drawString(11 * cm, 23.2 * cm, str(len(Sentence)))
	
	Association = '<para align=center>' + row['association'] + '</para>'
	#Association = '<para align=center>0 1 2 3 4 5 6 7 8 9 0 a b c d e f g h i j k l m n o p q r s t u v w x y z | A B C D E F G H I</para>'
	P = Paragraph(Association, style)
	P.wrap(9.5 * cm, 0.5 * cm)
	P.drawOn(c, (0.9 + (x * 9.75))* cm, (22.4 - (y * 7))* cm)
	
	Translate = '<font name=arial_unicode size=8>' + row['translate'] + '</font>'
	#Translate = '<font name=arial_unicode>水銀, 汞, [羅神]墨丘利神(眾神的信使)</font>'
	P = Paragraph(Translate, style)
	P.wrap(3 * cm, 0.5 * cm)
	P.drawOn(c, (0.9 + (x * 9.75))* cm, (21.85- (y * 7))* cm)
	
	Source = '<para align=center>' + row['source'] + '</para>'
	#Source = '<para align=center>a b c d e f g h i j k l m n o p q r s t u v</para>'
	P = Paragraph(Source, style)
	P.wrap(5.75 * cm, 0.5 * cm)
	P.drawOn(c, (2.9 + (x * 9.75))* cm, (21.9 - (y * 7))* cm)
	
	Time = row['arrange_time']
	#Time = '20080109'
	iTime = "<para align=right spaceb=3>" + Time + "</para>"
	P = Paragraph(iTime, style)
	P.wrap(2 * cm, 0.5 * cm)
	P.drawOn(c, (8.3 + (x * 9.75))* cm, (21.9 - (y * 7))* cm)
	
if __name__ == "__main__":
	c = canvas.Canvas("Table_Win.pdf", pagesize = A4)
	reader = csv.DictReader(open("vocabulary.txt", "rb"), delimiter='\t')
	while reader:
		for y in range(4):
			for x in range(2):
				try:
					row = reader.next()
					Content(c, row, x, y)
				except StopIteration:
					if x == y == 0:
						pass
					else:
						Table(c)
						c.showPage()
					c.save()
					sys.exit(2)
					#break
		Table(c)
		c.showPage()
	#c.save()
