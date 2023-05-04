from string import *
from secrets import *
import utils

codes = {'l': ascii_lowercase, 'u':ascii_uppercase, 'd': digits, 'p': punctuation}

def ch_aggr(code: str): # Returns a list of possible characters
    l = []
    for c in codes: #chars
        if c in codes: #Avoid None
            l.append(codes[c])
    return utils.flatten(l)

def gen(code, l): # gen the password
    pw = ""
    for _ in range(l):
        pw+=choice(ch_aggr(code))
    return pw