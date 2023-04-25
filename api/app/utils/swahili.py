import json

f = open('data/irregular_swahili_verbs.json')
irregular_verbs = json.load(f)

subject_prefix = {
    '1p': 'tu',
    '2p': 'm',
    '3p': 'wa',
    '1s': 'ni',
    '2s': 'u',
    '3s': 'a'
}

subject_prefix_negative = {
    '1p': 'ha',
    '2p': 'ha',
    '3p': 'ha',
    '1s': 'si',
    '2s': 'hu',
    '3s': 'ha'
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
    
    return negative, subject, tense, root

def conjugate_swahili(verbString):
    # negative: True, False
    # subject: 1p, 2p, 3p, 1s, 2s, 3s
    # tense: IMP, PAST, FUT, PRES, PERF

    negative, subject, tense, root = parse_string(verbString)

    # keep or remove 'ku' from the root
    if root in irregular_verbs and not negative:
        phrase = root
    elif root in irregular_verbs and negative and tense == 'FUT':
        phrase = root
    else:
        phrase = root[2:]
        


    if tense == 'IMP':
        return phrase
    
    if tense == 'PAST':
        # NOTES:
    
        if negative:
            tense_marker = 'ku'
            phrase = subject_prefix_negative[subject] + tense_marker + phrase
            return phrase
        
        tense_marker = 'li'
        phrase = subject_prefix[subject] + tense_marker + phrase
        return phrase
    
    if tense == 'FUT':
        if negative:
            tense_marker = 'ta'
            phrase = subject_prefix_negative[subject] + tense_marker + phrase
            return phrase
        
        tense_marker = 'ta'
        phrase = subject_prefix[subject] + tense_marker + phrase
        return phrase
    
    if tense == 'PRES':
        if negative:
            tense_marker = 'ha'
            if phrase[-1] == 'a':
                phrase = phrase[:-1] + 'i'
            phrase = subject_prefix_negative[subject] + phrase
            return phrase
        
        tense_marker = 'na'
        phrase = subject_prefix[subject] + tense_marker + phrase
        return phrase
    
    if tense == 'PERF':
        if negative:
            tense_marker = 'ja'
            phrase = subject_prefix_negative[subject] + tense_marker + phrase
            return phrase
        
        tense_marker = 'me';
        phrase = subject_prefix[subject] + tense_marker + phrase
        return phrase
        
    else:
        raise ValueError('Invalid tense')