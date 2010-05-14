from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import cm

styleSheet = getSampleStyleSheet()
style = styleSheet['BodyText']

canv = Canvas('c.pdf')

P=Paragraph('This is a very silly example',style)
P.wrap(1*cm, 1*cm)     # find required space
P.drawOn(canv,5*cm,20*cm)

P=Paragraph('This is a little guide on how you can create your own code swarm. \
	Code swarm shows the history of commits in a software project. \
	The visualization looks something like this', style)
P.wrap(8*cm, 5*cm)     # find required space
P.drawOn(canv,10*cm,20*cm)

styleSheet.add(ParagraphStyle(name='iBodyText',
	spaceBefore = 6, fontName = 'Times-Roman' , bulletFontName = 'Times-Roman', \
	borderRadius = None, firstLineIndent = 0, leftIndent = 0, rightIndent = 0, \
	wordWrap = None, allowWidows = 1, backColor = None, textTransform = None, \
	alignment = 0, borderColor = None, leading = 26, bulletIndent = 0, \
	allowOrphans = 0, bulletFontSize = 10, fontSize = 10, borderWidth = 1, \
	borderPadding = 0, spaceAfter = 6))
	
istyle = styleSheet['iBodyText']
P=Paragraph('This is a little guide on how you can create your own code swarm. \
	Code swarm shows the history of commits in a software project. \
	The visualization looks something like this', istyle)
P.wrap(8*cm, 5*cm)     # find required space
P.drawOn(canv,10*cm,15*cm)

canv.save()

