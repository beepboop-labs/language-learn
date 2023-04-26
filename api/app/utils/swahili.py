import json

f = open('data/irregular_swahili_verbs.json')
irregular_verbs = json.load(f)

f = open('data/very_irregular_swahili_verbs.json')
very_irregular_verbs = json.load(f)

vowels = ['a', 'e', 'i', 'o', 'u']

subject_prefix = {
    '1p': 'tu',
    '2p': 'm',
    '3p': 'wa',
    '1s': 'ni',
    '2s': 'u',
    '3s': 'a'
}

subject_prefix_negative = {
    '1p': 'hatu',
    '2p': 'ham',
    '3p': 'hawa',
    '1s': 'si',
    '2s': 'hu',
    '3s': 'ha'
}

tense_marker = {
    'IMP': '',
    'PAST': 'li',
    'FUT': 'ta',
    'PRES': 'na',
    'PERF': 'me'
}

tense_marker_negative = {
    'IMP': 'si',
    'PAST': 'ku',
    'FUT': 'ta',
    'PRES': 'ha',
    'PERF': 'ja'
}


def parse_string(s):
    parts = s.split('+')
    if len(parts) == 4:
        negative, subject, tense, root = parts
    elif len(parts) == 3:
        subject, tense, root = parts
        negative = False
    else:
        raise ValueError('Invalid string format')
    
    if negative == 'NEG':
        negative = True
    else:
        negative = False
    
    # Check if root is a compound verb: Kuwa na
    compound_verb = ""
    if " " in root:
        compound_verb = " " + root.split(" ")[1]
        root = root.split(" ")[0]

    return negative, subject, tense, root, compound_verb

def check_irregular(str, tense, negative):
    # verbs that are irregular within a tense.
    if str in very_irregular_verbs:
        if tense in very_irregular_verbs[str]:
            return very_irregular_verbs[str][tense]
        else:
            print("tense not found in very_irregular_verbs")
            return False
    # monosyllabic verbs keep the ku- prefix in these cases
    elif str in irregular_verbs and (not negative or (negative and tense == 'FUT')):
        return irregular_verbs[str] 
    else:
        return False

def conjugate_swahili(verbString):
    # negative: True, False
    # root: ku + verb
    # subject: 1p, 2p, 3p, 1s, 2s, 3s
    # tense: IMP, PAST, FUT, PRES, PERF

    negative, subject, tense, root, compound_verb = parse_string(verbString)

    # Remove 'ku' from root
    phrase = root[2:]

    # Check if verb is irregular
    irregular = check_irregular(root + compound_verb, tense, negative)
    if irregular:
        phrase = irregular

    if tense not in tense_marker:
        raise ValueError('Invalid tense')        
    
    #TODO: write negative imperative
    if tense == 'IMP':
        if subject.endswith('p'):   # plural
            if phrase[-1] == 'a':
                phrase = phrase[:-1] + 'e'
            phrase = phrase + 'ni'
            return phrase
        return phrase
    
    if tense == 'PRES' and negative:
        if phrase != 'na': # kuwa na is the only verb that doesn't change in the negative
            if phrase[-1] == 'a':
                phrase = phrase[:-1] + 'i'
        phrase = subject_prefix_negative[subject] + phrase
        return phrase
    
    # specific case for kuwa na: No present tense marker
    if tense == 'PRES' and phrase == 'na':
        phrase = subject_prefix[subject] + phrase
        return phrase
    
    # specific case for kuwa: No present tense marker or subject prefix
    if tense == 'PRES' and phrase == 'ni':
        return phrase
    

    # no special cases
    if negative:
        return subject_prefix_negative[subject] + tense_marker_negative[tense] + phrase + compound_verb
    
    return subject_prefix[subject] + tense_marker[tense] + phrase + compound_verb