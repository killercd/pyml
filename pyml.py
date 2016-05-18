#!/usr/bin/env python

from bs4 import BeautifulSoup
import argparse
import sys
import fileinput


def stdOutPrint(data):
    sys.stdout.write(data+"\n")

parser = argparse.ArgumentParser()
'''
parser.add_argument("-dbserver", dest="dbserver", required=False, help="db servername")
parser.add_argument("-dbuser", dest="dbuser", required=False, help="db username")
parser.add_argument("-dbpass", dest="dbpass", required=False, help="db password")
parser.add_argument("-dbport", dest="dbport", required=False, help="db port")
parser.add_argument("-dbname", dest="dbname", required=False, help="dbname")
parser.add_argument("-trusted", dest="trusted", required=False, default=True, help="Enable windows Authentication")
parser.add_argument("-conffile", dest="conffile", required=False, help="Set configuration file")
parser.add_argument("-colsep", dest="column_separator", required=False, help="result column separator",default='\t')
'''

parser.add_argument("-e", dest="html_element", required=False, help="Html element")

parser.add_argument("infile",metavar="FILE", nargs="?", type=str )
args = parser.parse_args()


htmlStream = ""

if args.infile:
    for line in fileinput.input(args.infile):
        htmlStream = htmlStream+line
    
    soup = BeautifulSoup(htmlStream, 'html.parser')
    if args.html_element:
        elems = soup.find_all(args.html_element)
        for elem in elems:
           print(elem)
    else:
        print(soup.prettify())
