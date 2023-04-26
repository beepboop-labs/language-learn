import json
import re
from app.utils.parse_verb_string import parse_verb_string

f = open('data/irregular_swahili_verbs.json')
irregular_verbs = json.load(f)

f = open('data/very_irregular_swahili_verbs.json')
very_irregular_verbs = json.load(f)

subject_prefix = {
    '1p': 'tu',
    '2p': 'm',
    '3p': 'wa',
    '1s': 'ni',
    '2s': 'u',
    '3s': 'a',
    'NEG1p': 'hatu',
    'NEG2p': 'ham',
    'NEG3p': 'hawa',
    'NEG1s': 'si',
    'NEG2s': 'hu',
    'NEG3s': 'ha'
}

tense_marker = {
    'IMP': '',
    'PAST': 'li',
    'FUT': 'ta',
    'PRES': 'na',
    'PERF': 'me',
    'NEGIMP': 'si',
    'NEGPAST': 'ku',
    'NEGFUT': 'ta',
    'NEGPRES': 'ha',
    'NEGPERF': 'ja'
}

def check_irregular(str, tense, negative):
    if str in very_irregular_verbs:
        if tense in very_irregular_verbs[str]:
            return very_irregular_verbs[str][tense]
        else:
            return False
    # monosyllabic verbs are irregular in these cases:
    elif str in irregular_verbs and (not negative or (negative and tense == 'FUT')):
        return irregular_verbs[str] 
    else:
        return False

def conjugate_swahili(verbString):

    negative, subject, tense, root, compound_verb = parse_verb_string(verbString)

    if tense not in tense_marker:
        raise ValueError('Invalid tense')
    if subject not in subject_prefix:
        raise ValueError('Invalid subject')

    # Check if verb is irregular, else remove 'ku' from root
    irregular = check_irregular(root + compound_verb, tense, negative)
    phrase = irregular if irregular else root[2:]   
    
    if tense == 'IMP':
        if subject.endswith('p'):   # plural
            return re.sub(r'a$', 'e', phrase) + "ni"
        return phrase
    
    if tense == 'PRES':
        # special case for 'kuwa na': No present tense marker
        if root + compound_verb == 'kuwa na':
            return subject_prefix[negative + subject] + phrase
    
        # special case for 'kuwa': No present tense marker or subject prefix
        if root == 'kuwa':
            return "si" if negative else phrase
    
        if negative:
            return subject_prefix[negative + subject] + re.sub(r'a$', 'i', phrase)

    # no special cases
    return subject_prefix[negative + subject] + tense_marker[negative + tense] + phrase + compound_verb