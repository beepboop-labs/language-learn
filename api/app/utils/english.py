
pronouns = {
    '1p': 'we',
    '2p': 'you',
    '3p': 'they',
    '1s': 'I',
    '2s': 'you',
    '3s': '(s)he'
}

consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']

vowels = ['a', 'e', 'i', 'o', 'u']

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
    

def build_english(verbString):
    # negative: True, False
    # subject: 1p, 2p, 3p, 1s, 2s, 3s
    # tense: IMP, PAS, FUT, PRES, PERF

    negative, subject, tense, root = parse_string(verbString)

    phrase = root

    if tense == 'IMP':
        return root
    
    if tense == 'PAS':
        # NOTES:

        # "to be <verb>" form phrases are irregular and dont work yet
        # 1p+PAST+kufurahi	we were happy
        # 1s+PAST+kushtuka	I was shocked

        # Issue with double-consonant ending past conjugation noted below eg. dragged, hugged, planned

        # need to check for past tenst ends in 't' like 'slept'

        helping_verbs = {
            '1p': 'did',
            '2p': 'did',
            '3p': 'did',
            '1s': 'did',
            '2s': 'did',
            '3s': 'did'
        }

        if negative == False:
            if root.endswith('e'):
                phrase = root + 'd'
            elif root.endswith('y'):
                if root[-1] in consonants:
                    phrase = root[:-1] + 'ied'
                elif root[-1] in vowels:
                    phrase = root + 'ed'

            # This works for 1 syllable words but
            # the rules are more complex for 2 syllable words
            elif (root[-3] in consonants and
                    root[-2] in vowels and
                      root[-1] in consonants):
                phrase = root + root[-1] + 'ed'            
            else:
                phrase = root + 'ed'
            
            phrase = pronouns[subject] + ' ' + phrase

        # negative past tense gets helping verb
        else:
            phrase = pronouns[subject] + ' ' + helping_verbs[subject] + ' not ' + phrase
            
        return phrase
    
    if tense == 'FUT':
        helping_verbs = {
            '1p': 'will',
            '2p': 'will',
            '3p': 'will',
            '1s': 'will',
            '2s': 'will',
            '3s': 'will'
        }

        if negative == False:
            phrase = pronouns[subject] + ' ' + helping_verbs[subject] + ' ' + phrase
        else:
            phrase = pronouns[subject] + ' ' + helping_verbs[subject] + ' not ' + phrase
        
        return phrase
    
    if tense == 'PRES':
        print("entering PRESENT CONJUGATION")
        es_suffix = ('ss', 'x', 'ch', 'sh', 'o', 'z')
        helping_verbs = {
            '1p': 'do',
            '2p': 'do',
            '3p': 'do',
            '1s': 'do',
            '2s': 'do',
            '3s': 'does'
        }

        if negative == False:
            
            if phrase.endswith(es_suffix) and subject == '3s':
                phrase = pronouns[subject] + ' ' + phrase + 'es'
            elif phrase[-2] in consonants and phrase.endswith('y') and subject == '3s':
                phrase = pronouns[subject] + ' ' + phrase[:-1] + 'ies'
            else:
                phrase = pronouns[subject] + ' ' + phrase + 's'
        else:
            phrase = pronouns[subject] + ' ' + helping_verbs[subject] + ' not ' + phrase

        return phrase
    
    if tense == 'PERF':
        helping_verbs = {
            '1p': 'have',
            '2p': 'have',
            '3p': 'have',
            '1s': 'have',
            '2s': 'have',
            '3s': 'has'
        }

        if negative == False:
            if root.endswith('e'):
                phrase = root + 'd'
            elif root.endswith('y'):
                if root[-1] in consonants:
                    phrase = root[:-1] + 'ied'
                elif root[-1] in vowels:
                    phrase = root + 'ed'

            # This works for 1 syllable words but
            # the rules are more complex for 2 syllable words
            elif (root[-3] in consonants and
                    root[-2] in vowels and
                      root[-1] in consonants):
                phrase = root + root[-1] + 'ed'            
            else:
                phrase = root + 'ed'
            
            phrase = pronouns[subject] + ' ' + helping_verbs[subject] + ' ' + phrase

        # negative past tense gets helping verb
        else:
            phrase = pronouns[subject] + ' ' + helping_verbs[subject] + ' not ' + phrase

       
        return phrase
        
    
    else:
        raise ValueError('Invalid tense')
    

