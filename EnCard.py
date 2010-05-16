# -*- coding: UTF-8 -*-
# A4 Size = 210×29
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

__version__ = '0.2'

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
    +-------------------------------------------------------------+
    |                row[vocabulary]:row[classes]                 |
    +-------------------------------------------------------------+
    |                          row[tense]                         |
    +-------------------------------------------------------------+
    |                         row[meaning]                        |
    +-------------------------------------------------------------+
    |                          row[idiom]                         |
    +-------------------------------------------------------------+
    |                         row[sentence]                       |
    +-------------------------------------------------------------+
    |                       row[association]                      |
    +-------------------------------------------------------------+
    |row[translate] |         row[source]      | row[arrange_time]|
    +-------------------------------------------------------------+
        '''

    styleSheet = getSampleStyleSheet()
    style = styleSheet['BodyText']

    #+-------------------------------------------------------------+
    #|                row[vocabulary]:row[classes]                 |
    #+-------------------------------------------------------------+

    if DEBUG:
        Voc_Cla = '<para align=center><font size=26 name=FreeSans>' + 'demonstrators' \
            + '</font><i>' + '   ' + 'Verb'  + '</i></para>'
    else:
        Voc_Cla = '<para align=center><font size=26 name=FreeSans>' + row['vocabulary'] \
            + '</font><i>' + '   ' + row['classes'] + '</i></para>'
    P = Paragraph(Voc_Cla, style)
    P.wrap(9.5 * cm, 1.5 * cm)
    if iOS == 'Linux':
        P.drawOn(c, (0.9 + (x * 9.75))* cm, (28.4 - (y * 7))* cm)
    else:
        P.drawOn(c, (0.9 + (x * 9.75))* cm, (28.2 - (y * 7))* cm)
    #P.drawOn(c, 0.9 * cm, 28.2 * cm)
    #c.drawString(11 * cm, 28 * cm, str(len(Voc_Cla)))
   
    #+-------------------------------------------------------------+
    #|                          row[tense]                         |
    #+-------------------------------------------------------------+

    if DEBUG:
        Tense = '<para align=center><font name=FreeSans>' + "['demәnstreitә]" + '</font></para>'
    else:
        Tense = '<para align=center><font name=FreeSans>' + row['tense'] + '</font></para>'
    P = Paragraph(Tense, style)
    P.wrap(9.5 * cm, 0.5 * cm)
    P.drawOn(c, (0.9 + (x * 9.75))* cm, (27.15- (y * 7))* cm)
    #c.drawString(11 * cm, 27.2 * cm, str(len(Tense)))

    #+-------------------------------------------------------------+
    #|                         row[meaning]                        |
    #+-------------------------------------------------------------+

    if DEBUG:
        string = 'The Mumbai attacks in 2008 left 174 people ' 
    else:
        string = row['meaning']

    Meaning = '<font name = FreeMonoBold size = 9>' + \
        string + \
        '</font>'

    P = Paragraph(Meaning, style)
    P.wrap(9.5 * cm, 0.5 * cm)
    newline = string_verify(string, 50)
    # we can return fail when newline over your layer
    P.drawOn(c, (0.9 + (x * 9.75))* cm, (26.05 - (0.2 * newline) - (y * 7))* cm)

    #P.drawOn(c, 0.9 * cm, 25.35 * cm)
    #c.drawString(11 * cm, 25.45 * cm, str(len(Meaning)))

    #+-------------------------------------------------------------+
    #|                          row[idiom]                         |
    #+-------------------------------------------------------------+
    
    if DEBUG:
        Idiom = '<para align=center>' + 'Demonstrative Evidence' + '</para>'
    else:
        Idiom = '<para align=center>' + row['idiom'] + '</para>'
    P = Paragraph(Idiom, style)
    P.wrap(9.5 * cm, 0.5 * cm)
    P.drawOn(c, (0.9 + (x * 9.75))* cm, (24.97 - (y * 7))* cm)
    #c.drawString(11 * cm, 25 * cm, str(len(Idiom)))
    
    #+-------------------------------------------------------------+
    #|                         row[sentence]                       |
    #+-------------------------------------------------------------+
    
    if DEBUG:
        string = 'They say the militants also to takeers, they ' 
    else:
        string = row['sentence']

    Sentence = '<font name = TlwgMono size = 9>' + \
        string + \
        '</font>'

    P = Paragraph(Sentence, style)
    P.wrap(9.5 * cm, 0.5 * cm)
    newline = string_verify(string, 50)
    P.drawOn(c, (0.9 + (x * 9.75))* cm, (23.9 - (0.2 * newline) - (y * 7))* cm)
    #P.drawOn(c, 0.9 * cm, 23.2 * cm)
    #c.drawString(11 * cm, 23.2 * cm, str(len(Sentence)))
    
    #+-------------------------------------------------------------+
    #|                       row[association]                      |
    #+-------------------------------------------------------------+
    
    if DEBUG:
        string = '1234567890 ' + \
            '1234567890' + \
           '1234567890' + \
            '1234567890' + \
            '1234567890' + \
            '1234567890' 
    else:
        string = row['association']

#    pdb.set_trace()
    newline = string_verify(string, 55)
    if newline > 1:
        string = bubble_by_len(string)
        newline = string_verify(string, 55) #try to decrease the newline
    
    Association = '<para align=center><font name = FreeMonoBold size = 8>' + \
        string + \
        '</font></para>'
    P = Paragraph(Association, style)
    P.wrap(9.5 * cm, 0.5 * cm)
    P.drawOn(c, (0.9 + (x * 9.75))* cm, (22.6 - (0.2 * newline) - (y * 7))* cm)
    
    #+-------------------------------------------------------------+
    #|row[translate] |                          |                  |
    #+-------------------------------------------------------------+
    
    if DEBUG:
        Translate = '<font name=ukai>水銀, 汞</font>'
    else:
        Translate = '<font name=ukai size=8>' + row['translate'] + '</font>'
    P = Paragraph(Translate, style)
    P.wrap(3 * cm, 0.5 * cm)
    P.drawOn(c, (0.9 + (x * 9.75))* cm, (21.85- (y * 7))* cm)
    
    #+-------------------------------------------------------------+
    #|               |         row[source]      |                  |
    #+-------------------------------------------------------------+
    
    if DEBUG:
        Source = '<para align=center>' + "Indonesia 'uncovers plot to kill" + '</para>'
    else:
        Source = '<para align=center>' + row['source'] + '</para>'
    P = Paragraph(Source, style)
    P.wrap(5.75 * cm, 0.5 * cm)
    P.drawOn(c, (2.9 + (x * 9.75))* cm, (21.9 - (y * 7))* cm)
    
    #+-------------------------------------------------------------+
    #|               |                          | row[arrange_time]|
    #+-------------------------------------------------------------+

    if DEBUG:
        Time = '<para align=right spaceb=3>' + '20080109' + '</para>'
    else:
        Time = '<para align=right spaceb=3>' + row['arrange_time'] + '</para>'
    P = Paragraph(Time, style)
    P.wrap(2 * cm, 0.5 * cm)
    P.drawOn(c, (8.3 + (x * 9.75))* cm, (21.9 - (y * 7))* cm)
    
def flash_card(DEBUG = False):
    reportlab.rl_config.TTFSearchPath.append("/usr/share/fonts/truetype/freefont/")
    reportlab.rl_config.TTFSearchPath.append("/usr/share/fonts/truetype/arphic/")
    reportlab.rl_config.TTFSearchPath.append("/usr/share/fonts/truetype/thai")
#    pdfmetrics.registerFont(TTFont('arial_unicode', 'fonts_dir/ARIALUNI.TTF'))
    pdfmetrics.registerFont(TTFont('FreeSans', 'FreeSans.ttf'))
    pdfmetrics.registerFont(TTFont('TlwgMono', 'TlwgMono.ttf'))
    pdfmetrics.registerFont(TTFont('FreeMonoBold', 'FreeMonoBold.ttf'))
    pdfmetrics.registerFont(TTFont('ukai', 'ukai.ttc')) #for chinese
    c = canvas.Canvas("Table_Win.pdf", pagesize = A4)

    if DEBUG:
        reader = iter(range(8))
    else:
        reader = csv.DictReader(open("vocabulary.txt", "rb"), delimiter='\t')

    while reader:
        # 4 Row * 2 column
        for y in range(4):
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

