from bs4 import BeautifulSoup
from glob import glob
import re
import pickle
import time
import math
import copy

def sentiment(document, Path):
    filenameAFINN = Path
    afinn = dict(map(lambda (w, s): (w, int(s)), [
            ws.strip().split('\t') for ws in open(filenameAFINN) ]))
    pattern_split = re.compile(r"\W+")
    words = pattern_split.split(document.lower())
    sentiments = map(lambda word: afinn.get(word, 0), words)
    if sentiments:
        sentiment = float(sum(sentiments))/math.sqrt(len(sentiments))
    else:
        sentiment = 0
    return sentiment
def parseHTML(html):
    soup = BeautifulSoup(html, "html.parser")
    [s.extract() for s in soup('script')]
    return soup.get_text()
    
def visitSubdir(ParentDir):
    result = []
    for name in glob(ParentDir + "/*"):
        partition = name.split("/")
        if "." not in partition[-1]:
            result += visitSubdir(name)
        else:
            result.append(name)
    return result
