#!/usr/bin/python3

#
# This utility will dump out a unicode table of characters next to ones decimal 
# and hexadecimal value.  It works best in a uxterm or a Terminal window that's
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
#   asc.py 0x2623     <-- prints out unicode character u'\u2623'
# Example 2:
#   asc.py 49 0x7a    <-- prints out characters 49-122
#

import sys

# Function to print a range of characters along with their decimal and 
# hexadecimal values.  Wraps around every 8.  Unprintable characters
# are replaced with spaces.
def printasc(start, end):
    n = 0
    for i in range(start, end+1):
        try:
            if i in range(0x80, 0x9f):
                c = chr(' ')
            else:
                c = chr(i)
            print("%03d" % i + ':' + "0x%02x" % i + ':' + c, end=' ')
        except:
            print("%03d" % i + ':' + "0x%02x" % i + ':' + ' ', end=' ')
        n += 1
        if (n % 8) == 0:
            print()

start_supplied = False

# Function to convert a string to a numeric.
# Accepts hexadecimal number if prefixed by 0x, decimal otherwise.
def strtonum(strnum):
    try:
        strnum = int(strnum)
    except ValueError:
        strnum = int(strnum, 16)

    return strnum

# Did the user provide a 1st arguemnt?
# If so use it as a starting range, otherwise start at <SPACE>=32.
try:
    startrange = sys.argv[1]
    start_supplied = True
except IndexError:
    startrange = '32'

# Convert the starting character to a numeric.
startnum = strtonum(startrange)

# Did the user provide a 2nd argument?
# If so use it as an ending range, otherwise:
# - end at startnum if available; or
# - end at 255 as default.
try:
    endrange   = sys.argv[2]
except IndexError:
    if start_supplied:
        endrange = startrange
    else:
        endrange = '255'

# Convert the ending character to a numeric.
endnum   = strtonum(endrange)

#sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8')
# Print the range of characters.
printasc(startnum, endnum)
