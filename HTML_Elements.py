# Author: Rafal Kukolowicz
# Solution for HTML Elements challange from CoderByte
# Description:
# Have the function HTMLElements(str) read the str parameter being passed which will
# be a string of HTML DOM elements and plain text. The elements that will be used are
# b, i, em, div, p. For example if str is '<div><b><p>hello world</p></b></div>' then
# this string DOM elements is nested corectly so your program should return the string
# true.
# If string is not nested correctly, return the first element encountered where, if
# changed into a different element, would result in a properly formated string.
#
# In mine solution I've add the check for the number of opening and closing DOM elements.

import re

def GetModParameters(splittedStr):

    # Create list of HTML MODs with properties as mod-type and is opening or closing mod
    for i, htmlmod in enumerate(splittedStr):
        if htmlmod[1] == '/':
            splittedStr[i] = {
                'htmlmod' : splittedStr[i],
                'type': splittedStr[i][2:-1],
                'opening': False
            }
        else:
            splittedStr[i] = {
                'htmlmod': splittedStr[i],
                'type': splittedStr[i][1: -1],
                'opening': True
            }
    return splittedStr


def CheckForProperClosing(htmlmod, splittedStr):

    # Check if given HTML MOD is properly closed. Considers appearance of multiple HTML MODs of the same type
    totalOpening = 1
    totalClosing = 0
    sameTypeOpening = 1 # counters for the same type HTML MODs
    sameTypeClosing = 0 # counters for the same type HTML MODs
    closedProperly = True
    k = 0

    while totalOpening != totalClosing and sameTypeOpening != sameTypeClosing:
        nextHtmlmod = splittedStr[k]
        if nextHtmlmod['opening']:
            totalOpening += 1
            if nextHtmlmod['type'] == htmlmod['type']:
                sameTypeOpening += 1
        else:
            totalClosing += 1
            if nextHtmlmod['type'] == htmlmod['type']:
                sameTypeClosing += 1

        if totalOpening == totalClosing and sameTypeOpening != sameTypeClosing:
            closedProperly = False
            break
        k += 1
    return closedProperly


def HTMLElements(str):

    # Regular expresions used to find any appearing HTML DOM
    splittedStr = re.findall('<[^<>]{1,4}>', str)
    # print(splittedStr)

    # Create dictionary for found HTML MODs
    splittedStr = GetModParameters(splittedStr)

    # Counters for checking if the number of openings and closings is the same
    openingSum = 0
    closingSum = 0

    for i, htmlmod in enumerate(splittedStr):
        if not htmlmod['opening']:
            closingSum += 1
            continue
        openingSum += 1

        closedProperly = CheckForProperClosing(htmlmod, splittedStr[i+1:])

        if not closedProperly:
            str = htmlmod['htmlmod']
            return str

    if openingSum != closingSum:
        str = 'Uneven number of opening and closing brackets'
    else:
        str = True

    return str

str = '<div><b><p>hello world</p></b></div>'
#str = '<div><div><b></b></div></p>'
print(HTMLElements(str))