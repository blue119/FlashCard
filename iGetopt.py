#!/usr/bin/python
#-*- coding: utf-8 -*-
#http://docs.python.org/library/getopt.html

import getopt
import sys

def usage():
	print """
	filteralig : filter sites in alignments

	filteralig [-ch] [-t <threshold>] [-f <frames>] [-i <cols>] <alignment>

	-h                  print this message
	-c                  print colum numbers of the original alignment
	-t <threshold>      filter all colums with a conservation above <threshold>
	-f <frames>         filter all codonpositions of frames
	                    possible values 1, 2, 3 
	                    for more than one use syntaxe: '1,2'
	-i <cols>           filter this columns
	                    syntaxe: give a string with the column numbers separated by
	','

	<alignment>         the file has to be in clustalw format
 	"""

def main():
	try:
		options, args = getopt.getopt(sys.argv[1:], 'c:h', ['command=','help'])
	except getopt.GetoptError:
		usage()
		sys.exit(2)

	if len(options) < 1:
		usage()
		sys.exit(0)

	opts = {}

	for o, a in options:
	    opts[o] = a
	
	if '-h' in opts or '--help' in opts:
		usage()
		sys.exit(0)

	if '-c' in opts or '--command' in opts:
		cmd = opts.get('-c', opts.get('--command'))
		print 'you command is ', cmd

	if len(a) < 1:
		usage(); sys.exit("alignment file missing")


main()

