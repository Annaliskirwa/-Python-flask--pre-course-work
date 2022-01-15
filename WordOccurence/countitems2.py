from string import punctuation
import urllib.request, urllib.error, urllib.parse

# Taking the user input of the webpage input and assigning it as url
url = input("Enter the webpage url: ")

# For example website url = https://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33

# Method for returning the text
def stripTags(pageContents):
    pageContents = str(pageContents)
    startLoc = pageContents.find("<p>")
    endLoc = pageContents.rfind("<br/>")

    pageContents = pageContents[startLoc:endLoc]

    inside = 0
    text = ''

    for char in pageContents:
        if char == '<':
            inside = 1
        elif (inside == 1 and char == '>'):
            inside = 0
        elif inside == 1:
            continue
        else:
            text += char

    return text

# Removing the punctuation marks
def stripNonAlphaNum(text):
    import re
    return re.compile(r'\W+', re.UNICODE).split(text)

# Method for converting the dict to list
def wordListToFreqDict(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(list(zip(wordlist,wordfreq)))

# The sorting method of the list
def sortFreqDict(freqdict):
    aux = [(freqdict[key], key) for key in freqdict]
    aux.sort()
    aux.reverse()
    return aux


response = urllib.request.urlopen(url)
html = response.read().decode('UTF-8')
text = stripTags(html).lower()
wordlist = stripNonAlphaNum(text)
dictionary = wordListToFreqDict(wordlist)
sorteddict = sortFreqDict(dictionary)

# Outputting the list frequencies
for s in sorteddict: print(str(s))