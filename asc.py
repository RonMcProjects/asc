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

ctrl_codes = [ # Control characters 0-31
'NUL', 'SOH', 'STX', 'ETX', 'EOT', 'ENQ', 'ACK', 'BEL',
'BS ', 'TAB', 'LF ', 'VT ', 'FF ', 'CR ', 'S0 ', 'S1 ',
'DLE', 'DC1', 'DC2', 'DC3', 'DC4', 'NAK', 'SYN', 'ETB',
'CAN', 'EM ', 'SUB', 'ESC', 'FS ', 'GS ', 'RS ', 'US ' ]

# Function to print a range of characters along with their decimal and 
# hexadecimal values.  Wraps around every 8.  Unprintable characters
# are replaced with spaces.
def printasc(start, end):
    n = 0
    for i in range(start, end+1):
        try:
            if i in range(0x80, 0xa0):
                c = ' '
            elif i in range(0, 32):
                c = ctrl_codes[i]
            elif i == 127:
                c = 'DEL'
            else:
                c = chr(i)
            print("%03d" % i + ':' + "0x%02x" % i + ':' + c, end=' ')
        except:
            print("%03d" % i + ':' + "0x%02x" % i + ':' + ' ', end=' ')
        n += 1
        if (n % 8) == 0:
            print()
    return n

start_supplied = False

# Function to convert a string to a numeral.
# Accepts hexadecimal number if prefixed by 0x, decimal otherwise.
def strtonum(strnum):
    try:
        strnum = int(strnum)
    except ValueError:
        try:
            strnum = int(strnum, 16)
        except ValueError:
            print("Invalid numeral '" + strnum + "'", end='. ')
            print("Use decimal or hexadecimal numbers.")
            exit()

    return strnum

# Did the user provide a 1st arguemnt?
# If so use it as a starting range, otherwise start at <SPACE>=32.
try:
    startrange = sys.argv[1]
    start_supplied = True
except IndexError:
    startrange = '0'

# Convert the starting character to a numeral.
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

# Convert the ending character to a numeral.
endnum   = strtonum(endrange)

#sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8')
# Print the range of characters.
numchars = printasc(startnum, endnum)
if (numchars % 8) != 0:
    # add a <CR> terminator where needed
    print() 
