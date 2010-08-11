# -*- coding: UTF-8 -*-
# A4 Size = 210 x 297
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
import pdb
iOS = platform.system()

__version__ = '0.3'

column = 2
row = 5

paper = {"width":(A4[0]/cm), "height":(A4[1]/cm)}
top = {"x":0.75, "y":(paper.get("height") - 0.85)} #this node is put on the most top-left point.
column_gap = 9.75
row_gap = 5.6

#           {"vac":1, "tense":0.3, "meaning":1.5, "sentence":1.5, "association":1,   "MIX":0.3} # [vac, tense, meaning, sentence, association, MIX]
field_gap = {"vac":1, "tense":1.3, "meaning":2.8, "sentence":4.3, "association":5.3, "MIX":5.6} 
MIX_gap = {"translate":3.5, "source":8.4}

def Table(canvas, DL = False):
	c = canvas

	# accurate issue
	c.grid([(top.get("x") + column_gap * x) * cm for x in range(3)], [(paper.get("height") - top.get("y") + row_gap * y) * cm for y in range(6)])
	#c.grid([0.75 * cm, 10.5 * cm, 20.25 * cm], [0.85 * cm, 6.45 * cm, 12.05 * cm, 17.65 * cm, 23.25 * cm, 28.85 * cm])

	'''
	for a in [(top.get("x") + column_gap * x) * cm for x in range(3)]:
		for b in [(top.get("y") + row_gap * y) * cm for y in range(6)]:
			c.circle(a, b, 0.05 * cm, fill = 1)
	'''

	# Draw Dash Line
	if DL:
		c.setDash(1,2)
		for x in range(column):
			for y in range(row):
				c.line(
					(top.get("x") + (x * column_gap))              * cm, (top.get("y") - field_gap.get("vac") - (y * row_gap)) * cm, 
					(top.get("x") + (x * column_gap) + column_gap) * cm, (top.get("y") - field_gap.get("vac") - (y * row_gap)) * cm)

				c.line(
					(top.get("x") + (x * column_gap))              * cm, (top.get("y") - field_gap.get("tense") - (y * row_gap)) * cm, 
					(top.get("x") + (x * column_gap) + column_gap) * cm, (top.get("y") - field_gap.get("tense") - (y * row_gap)) * cm)

				c.line(
					(top.get("x") + (x * column_gap))              * cm, (top.get("y") - field_gap.get("meaning") - (y * row_gap)) * cm, 
					(top.get("x") + (x * column_gap) + column_gap) * cm, (top.get("y") - field_gap.get("meaning") - (y * row_gap)) * cm)

				c.line(
					(top.get("x") + (x * column_gap))              * cm, (top.get("y") - field_gap.get("sentence") - (y * row_gap)) * cm, 
					(top.get("x") + (x * column_gap) + column_gap) * cm, (top.get("y") - field_gap.get("sentence") - (y * row_gap)) * cm)

				c.line(
					(top.get("x") + (x * column_gap))              * cm, (top.get("y") - field_gap.get("association") - (y * row_gap)) * cm, 
					(top.get("x") + (x * column_gap) + column_gap) * cm, (top.get("y") - field_gap.get("association") - (y * row_gap)) * cm)

				c.line(
					(top.get("x") + MIX_gap.get("translate") + (x * column_gap)) * cm, (top.get("y") - field_gap.get("association") - (y * row_gap)) * cm, 
					(top.get("x") + MIX_gap.get("translate") + (x * column_gap)) * cm, (top.get("y") - field_gap.get("MIX")      - (y * row_gap)) * cm)

				c.line(
					(top.get("x") + MIX_gap.get("source") + (x * column_gap)) * cm, (top.get("y") - field_gap.get("association") - (y * row_gap)) * cm, 
					(top.get("x") + MIX_gap.get("source") + (x * column_gap)) * cm, (top.get("y") - field_gap.get("MIX")      - (y * row_gap)) * cm)

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


def bubble_by_len(String):
	List = String.split(', ')
	max = len(List)
	temp = 0
	for n in range(0,max):
		for i in range(1, max):
			temp = List[i]
			if len(List[i]) < len(List[i-1]):
				List[i] = List[i-1]
				List[i-1] = temp
	return ', '.join(List)

def string_verify(string, limite):
	word = 0
	newline = 0;
	tmp = []
	result = []
	for i in string.split(' '):
		if i is '': #avoid many space at string tail.
			continue
		word += len(i)
		tmp.append(i)
		if word > limite:
			newline += 1
			word = len(i) + 1 
			result.append(tmp)
			tmp = []
		word += 1 #space
	result.append(tmp)
	return newline

def Content(c, row, x, y, DEBUG = False): 
	'''
						English Cade's Format
	+---------------------------------------------------------------+
	|				row[vocabulary]:row[classes]					|
	+---------------------------------------------------------------+
	|						row[tense]								|
	+---------------------------------------------------------------+
	|						 row[meaning]							|
	+---------------------------------------------------------------+
	|						 row[sentence]							|
	+---------------------------------------------------------------+
	|					   row[association]							|
	+---------------------------------------------------------------+
	|row[translate] |		row[source]		  |	row[arrange_time]	|
	+---------------------------------------------------------------+
		'''

	styleSheet = getSampleStyleSheet()
	style = styleSheet['BodyText']

	#+-------------------------------------------------------------+
	#|				row[vocabulary]:row[classes]				 |
	#+-------------------------------------------------------------+

	if DEBUG:
		Voc_Cla = '<para align=center><font size=26 name=FreeSans>' + 'demonstrators' \
			+ '</font><i>' + '   ' + 'Verb'  + '</i></para>'
	else:
		Voc_Cla = '<para align=center><font size=26 name=FreeSans>' + row['vocabulary'] \
			+ '</font><i>' + '   ' + row['classes'] + '</i></para>'

	P = Paragraph(Voc_Cla, style)
	P.wrap(column_gap * cm, field_gap.get("vac") * cm)

	P.drawOn(c, (top.get("x") + (x * column_gap)) * cm, (top.get("y") - 0.25 - (y * row_gap)) * cm)

	#P.drawOn(c, 0.9 * cm, 28.2 * cm)
	#c.drawString(11 * cm, 28 * cm, str(len(Voc_Cla)))
   
	#+-----------`--------------------------------------------------+
	#|						  row[tense]						 |
	#+-------------------------------------------------------------+

	if DEBUG:
		Tense = '<para align=center><font name=FreeSans size=10>' + "['demәnstreitә]" + '</font></para>'
	else:
		Tense = '<para align=center><font name=FreeSans size=10>' + row['tense'] + '</font></para>'
	P = Paragraph(Tense, style)
	P.wrap(column_gap * cm, (field_gap.get("tense") - field_gap.get("vac")) * cm)
	P.drawOn(c, (top.get("x") + (x * column_gap)) * cm, (top.get("y") -field_gap.get("tense") - (y * row_gap)) * cm)

	#c.drawString(11 * cm, 27.2 * cm, str(len(Tense)))

	#+-------------------------------------------------------------+
	#|						 row[meaning]						|
	#+-------------------------------------------------------------+

	if DEBUG:
		if y is 0:
			string = 'The Mumbai The Mumbai attacks in 2008 left 174 people The Mumbai attacks people The Mumbai attacks in 2008 left 174 people The Mumbai attacks in 2008 left 174 people he Mumbai attacks in 2008 left 174 people' 
		elif y is 1:
			string = 'in 2008 left 174 people 2008 left The Mumbai attacks in 2008 left 174 people The Mumbai attacks in 2008 left 174 people he Mumbai attacks in 2008 left 174 people' 
		elif y is 2:
			string = '2008mbai attacks in 2008 in 2008 left 174 peopl eleft 174 people he Mumbai attacks in 2008 left 174 people' 
		elif y is 3:
			string = 'e Mumbai attacks in 2008 left 174 people he Mumbai attacks in 2008 left 174 people' 
		elif y is 4:
			string = 'umbai attacks in 2008 left 174 people' 
		else:
			string = ''
	else:
		string = row['meaning']

	Meaning = '<font name = FreeMonoBold size = 9>' + \
		string + \
		'</font>'

	style.leading = 9
	offset = 0.1
	P = Paragraph(Meaning, style)
	P.wrap((column_gap - offset * 2) * cm, (field_gap.get("meaning") - field_gap.get("tense")) * cm)
	newline = string_verify(string, 50)

	# we can return fail when newline over your layout
	P.drawOn(c, (top.get("x") + (x * column_gap) + offset) * cm, (top.get("y") - field_gap.get("meaning") + 0.7  - (0.17 * newline) - (y * row_gap)) * cm)

	#P.drawOn(c, (0.9 + (x * 9.75))* cm, (26.05 - (0.2 * newline) - (y * 7))* cm)

	#P.drawOn(c, 0.9 * cm, 25.35 * cm)
	#c.drawString(11 * cm, 25.45 * cm, str(len(Meaning)))
	'''
	#+-------------------------------------------------------------+
	#|						  row[idiom]						 |
	#+-------------------------------------------------------------+
	
	if DEBUG:
		Idiom = '<para align=center>' + 'Demonstrative Evidence' + '</para>'
	else:
		Idiom = '<para align=center>' + row['idiom'] + '</para>'
	P = Paragraph(Idiom, style)
	P.wrap(9.5 * cm, 0.5 * cm)
	P.drawOn(c, (0.9 + (x * 9.75))* cm, (24.97 - (y * 7))* cm)
	#c.drawString(11 * cm, 25 * cm, str(len(Idiom)))
	'''	
	#+-------------------------------------------------------------+
	#|						 row[sentence]					   |
	#+-------------------------------------------------------------+
	
	if DEBUG:
		if y is 4:
			string = 'The Mumbai The Mumbai attacks in 2008 left 174 people The Mumbai attacks people The Mumbai attacks in 2008 left 174 people The Mumbai attacks in 2008 left 174 people he Mumbai attacks in 2008 left 174 people' 
		elif y is 3:
			string = 'in 2008 left 174 people 2008 left The Mumbai attacks in 2008 left 174 people The Mumbai attacks in 2008 left 174 people he Mumbai attacks in 2008 left 174 people' 
		elif y is 2:
			string = '2008mbai attacks in 2008 in 2008 left 174 peopl eleft 174 people he Mumbai attacks in 2008 left 174 people' 
		elif y is 1:
			string = 'e Mumbai attacks in 2008 left 174 people he Mumbai attacks in 2008 left 174 people' 
		elif y is 0:
			string = 'umbai attacks in 2008 left 174 people' 
		else:
			string = ''
	else:
		string = row['sentence']

	Sentence = '<font name = TlwgMono size = 9>' + \
		string + \
		'</font>'

	P = Paragraph(Sentence, style)

	P.wrap((column_gap - offset * 2) * cm, (field_gap.get("sentence") - field_gap.get("meaning")) * cm)
	newline = string_verify(string, 50)

	# we can return fail when newline over your layout
	P.drawOn(c, (top.get("x") + (x * column_gap) + offset) * cm, (top.get("y") - field_gap.get("sentence") + 0.7  - (0.17 * newline) - (y * row_gap)) * cm)
	
	#+-------------------------------------------------------------+
	#|					   row[association]					  |
	#+-------------------------------------------------------------+
	
	if DEBUG:
		if y is 4:
			string = 'discussion, conference, convention, council, session, seminar, symposium, assembly, rally, workshop, panel discussion'
		elif y is 3:
			string = ' convention, council, session, seminar, symposium, assembly, rally, workshop, panel discussion'
		elif y is 2:
			string = 'n, seminar, symposium, assembly, rally, workshop, panel discussion'
		elif y is 1:
			string = ' assembly, rally, workshop, panel discussion'
		elif y is 0:
			string = 'rkshop, panel discussion'
		else:
			string = ''
	else:
		string = row['association']

#	pdb.set_trace()
	newline = string_verify(string, 55)
	if newline > 1:
		string = bubble_by_len(string)
		newline = string_verify(string, 55) #try to decrease the newline
	
	Association = '<para align=center><font name = FreeMonoBold size = 8>' + \
		string + \
		'</font></para>'

	P = Paragraph(Association, style)
	P.wrap((column_gap - offset * 2) * cm, (field_gap.get("association") - field_gap.get("sentence")) * cm)
	P.drawOn(c, (top.get("x") + (x * column_gap) + offset) * cm, (top.get("y") - field_gap.get("association") + 0.4  - (0.17 * newline) - (y * row_gap)) * cm)
	
	#+-------------------------------------------------------------+
	#|row[translate] |						  |				  |
	#+-------------------------------------------------------------+
	
	if DEBUG:
		Translate = '<font name=ukai size=8>水銀, 汞</font>'
	else:
		Translate = '<font name=ukai size=8>' + row['translate'] + '</font>'
	P = Paragraph(Translate, style)

	P.wrap(MIX_gap.get("translate") * cm, (field_gap.get("MIX") - field_gap.get("association")) * cm)
	P.drawOn(c, (top.get("x") + (x * column_gap) + offset) * cm, (top.get("y") -field_gap.get("MIX") - (y * row_gap)) * cm)
	
	#+-------------------------------------------------------------+
	#|			   |		 row[source]	  |				  |
	#+-------------------------------------------------------------+
	
	if DEBUG:
		Source = '<para align=center><font size=8>' + "Indonesia 'uncovers plot to kill" + '</font></para>'
	else:
		Source = '<para align=center><font size=8>' + row['source'] + '</font></para>'
	P = Paragraph(Source, style)
	P.wrap((MIX_gap.get("source") - MIX_gap.get("translate")) * cm, (field_gap.get("MIX") - field_gap.get("association")) * cm)
	P.drawOn(c, (top.get("x") + (x * column_gap) + MIX_gap.get("translate")) * cm, (top.get("y") -field_gap.get("MIX") - (y * row_gap)) * cm)
	
	#+-------------------------------------------------------------+
	#|			   |						  | row[arrange_time]|
	#+-------------------------------------------------------------+

	if DEBUG:
		Time = '<para align=right spaceb=3><font size=8>' + '20080109' + '</font></para>'
	else:
		Time = '<para align=right spaceb=3><font size=8>' + row['arrange_time'] + '</font></para>'
	P = Paragraph(Time, style)
	P.wrap((column_gap - MIX_gap.get("source")) * cm, (field_gap.get("MIX") - field_gap.get("association")) * cm)
	P.drawOn(c, (top.get("x") + (x * column_gap) + MIX_gap.get("source") - offset) * cm, (top.get("y") -field_gap.get("MIX") - (y * row_gap)) * cm)
	
def flash_card(DEBUG = False):
	reportlab.rl_config.TTFSearchPath.append("/usr/share/fonts/truetype/freefont/")
	reportlab.rl_config.TTFSearchPath.append("/usr/share/fonts/truetype/arphic/")
	reportlab.rl_config.TTFSearchPath.append("/usr/share/fonts/truetype/thai")
#	pdfmetrics.registerFont(TTFont('arial_unicode', 'fonts_dir/ARIALUNI.TTF'))
	pdfmetrics.registerFont(TTFont('FreeSans', 'FreeSans.ttf'))
	pdfmetrics.registerFont(TTFont('TlwgMono', 'TlwgMono.ttf'))
	pdfmetrics.registerFont(TTFont('FreeMonoBold', 'FreeMonoBold.ttf'))
	pdfmetrics.registerFont(TTFont('ukai', 'ukai.ttc')) #for chinese
	c = canvas.Canvas("Table_Win.pdf", pagesize = A4)

	if DEBUG:
		reader = iter(range(10))
	else:
		reader = csv.DictReader(open("vocabulary.txt", "rb"), delimiter='\t')

	while reader:
		# 5 of Row * 2 of column
		for y in range(5):
			for x in range(2):
				try:
					row = reader.next()
					Content(c, row, x, y, DEBUG)
				except StopIteration:
					if x == y == 0:
						pass
					else:
						Table(c) #Create table
						c.showPage() #draw to pdf
					c.save()
					sys.exit(2)
					#break
		Table(c) #Create table
		c.showPage() #draw to pdf
	#c.save()

if __name__ == "__main__":
	flash_card()

