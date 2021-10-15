#!/usr/bin/python

#
# This utility will dump out a utf-8 table of characters next to its decimal 
# and hexadecimal value. It works best in a uxterm or a gnome Terminal window 
# set to utf-8 character encoding.
#
# Usage:
#   asc.py [start of range] [end of range]
#
#   It accepts decimal or hexadecimal numbers beginning with 0x.
#   If only a [start of range] is supplied, then that one charater
#   is printed out. If no argument is passed, then the range of printable
#   characters 32-255 is displayed.
#
# Example 1:
#   asc.py 0x1234     <-- prints out unicode character u'\u1234'
# Example 2:
#   asc.py 49 0x7a    <-- prints out characters 49-122
#

import sys

def printasc(start, end):
    n = 0
    for i in range(start, end+1):
        try:
            if i in range(0x80, 0xa0):
                c = ' '
            else:
                c = unichr(i)
            print "%03d" % i + ':' + "0x%02x" % i + ':' + c.encode('utf-8'),
        except:
            print
            print "Can't print character ", i
            return ''
        n += 1
        if (n % 8) == 0:
            print

start_supplied = False

def strtonum(strnum):
    try:
        strnum = int(strnum)
    except ValueError:
        strnum = int(strnum, 16)

    return strnum

try:
    startrange = sys.argv[1]
    start_supplied = True
except IndexError:
    startrange = '32'

startnum = strtonum(startrange)

try:
    endrange   = sys.argv[2]
except IndexError:
    if start_supplied:
        endrange = startnum
    else:
        endrange = '255'

endnum   = strtonum(endrange)

printasc(startnum, endnum)

