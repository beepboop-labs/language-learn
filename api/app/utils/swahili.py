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

    phrase = root

    if tense == 'IMP':
        return root
    
    if tense == 'PAST':
        # NOTES:
            
        return phrase
    
    if tense == 'FUT':

        return phrase
    
    if tense == 'PRES':

        return phrase
    
    if tense == 'PERF':
       
        return phrase
        
    else:
        raise ValueError('Invalid tense')