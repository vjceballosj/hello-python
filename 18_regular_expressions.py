"""
Regular Expressions
A regular expression or RegEx is a special text string that helps to find patterns in data. A RegEx can be used to check if some pattern exists in a different data type. To use RegEx in python first we should import the RegEx module which is called re.

The re Module
After importing the module we can use it to detect or find patterns.
"""
import re

"""
Methods in re Module
To find a pattern we use different set of re character sets that allows to search for a match in a string.

re.match(): searches only in the beginning of the first line of the string and returns matched objects if found, else returns None.
re.search: Returns a match object if there is one anywhere in the string, including multiline strings.
re.findall: Returns a list containing all matches
re.split: Takes a string, splits it at the match points, returns a list
re.sub: Replaces one or many matches within a string

Match
"""
# syntac
re.match(substring, string, re.I)
# substring is a string or a pattern, string is the text we look for a pattern , re.I is case ignore
import re

txt = 'I love to teach python and javaScript'
# It returns an object with span, and match
match = re.match('I love to teach', txt, re.I)
print(match)  # <re.Match object; span=(0, 15), match='I love to teach'>
# We can get the starting and ending position of the match as tuple using span
span = match.span()
print(span)     # (0, 15)
# Lets find the start and stop position from the span
start, end = span
print(start, end)  # 0, 15
substring = txt[start:end]
print(substring)       # I love to teach