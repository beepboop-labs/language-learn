import json
import re
import syllables
from app.utils.parse_verb_string import parse_verb_string

f = open('data/irregular_english_verbs.json')
irregular_verbs = json.load(f)

f = open('data/very_irregular_english_verbs.json')
very_irregular_verbs = json.load(f)

pronouns = {
    '1p': 'we',
    '2p': 'you',
    '3p': 'they',
    '1s': 'I',
    '2s': 'you',
    '3s': '(s)he'
}

def check_irregular(str, tense, subj):
    
    if str in very_irregular_verbs:
        print(str, tense, subj)
        if tense in very_irregular_verbs[str]:
            if subj in very_irregular_verbs[str][tense]:
                return very_irregular_verbs[str][tense][subj]
            else:
                return False
        else:
            return False
    elif str in irregular_verbs:
        print(str, tense, subj)
        if tense in irregular_verbs[str]:
            return irregular_verbs[str][tense]
        else:
            return False
    else:
        return False


def conjugate_english(verbString):
    negative, subject, tense, root, compound_verb = parse_verb_string(verbString)

    if subject not in pronouns:
        raise ValueError('Invalid subject')
    
    # Check if verb is irregular
    irregular = check_irregular(root, tense, subject)
    phrase = irregular if irregular else root 

    syl = syllables.estimate(phrase)
    print(syl)

    if tense == 'IMP':
        return phrase + compound_verb
    
    if tense == 'PAST':
        # NOTES:
        # Issue with double-consonant ending PAST conjugation eg. dragged, hugged, planned

        if not irregular:
            phrase = re.sub(r'e$', 'ed', phrase)
            if re.search(r'[^aeiou]y$', phrase):
                phrase = re.sub(r'y$', 'ied', phrase)
            # the twinning rule, eg. skim -> skimmed
            # 1)ends in a vowel + consonant
            # 2)is monosyllabic
            # 3)is not a verb ending in w, x, or y
            # 4)only has one vowel 
            if re.search(r'^[^aeiou]+[aeiou][^aeiou]$', phrase) and syl == 1 and not phrase.endswith(('w', 'x', 'y')):
                phrase += phrase[-1] + 'ed'
                
            phrase += 'ed' if not phrase.endswith('ed') else ''

        if negative:
            # irregular NEG+PAST takes root instead of past tense
            return pronouns[subject] + ' ' + 'did not ' + root + compound_verb 
        
        return pronouns[subject] + ' ' + phrase + compound_verb
   
    if tense == 'FUT':
        if negative:
            return pronouns[subject] + ' will not ' + phrase + compound_verb
        
        return pronouns[subject] + ' will ' + phrase + compound_verb        
        
    if tense == 'PRES':
        es_suffix = ('ss', 'x', 'ch', 'sh', 'o', 'z')
        helping_verbs = {
            '1p': 'do',
            '2p': 'do',
            '3p': 'do',
            '1s': 'do',
            '2s': 'do',
            '3s': 'does'
        }

        if not irregular:           
            if subject == '3s':
                if phrase.endswith(es_suffix):
                    phrase += 'es'
                elif re.search(r'[^aeiou]y$', phrase):
                    phrase = re.sub(r'y$', 'ies', phrase)
                else:
                    phrase += 's'

        if negative:
            if root == 'be':
                # negative present tense 'to be' inverts negation word order and omits helping verb
                return pronouns[subject] + ' ' + phrase + ' not' + compound_verb
            else:
                return pronouns[subject] + ' ' + helping_verbs[subject] + ' not ' + phrase + compound_verb

        return pronouns[subject] + ' ' + phrase + compound_verb
    
    if tense == 'PERF':
        helping_verbs = {
            '1p': 'have',
            '2p': 'have',
            '3p': 'have',
            '1s': 'have',
            '2s': 'have',
            '3s': 'has'
        }

        # Phrases with irregular past participles will have unique endings
        if not irregular:
            phrase = re.sub(r'e$', 'ed', phrase)
            if re.search(r'[^aeiou]y$', phrase):
                phrase = re.sub(r'y$', 'ied', phrase)
            # the twinning rule, eg. plan -> planned
            if re.search(r'^[^aeiou]+[aeiou][^aeiou]$', phrase) and syl == 1 and not phrase.endswith(('w', 'x', 'y')):
                phrase += phrase[-1] + 'ed'

            phrase += 'ed' if not phrase.endswith('ed') else ''

        if negative:
            return pronouns[subject] + ' ' + helping_verbs[subject] + ' not ' + phrase + compound_verb
        
        return pronouns[subject] + ' ' + helping_verbs[subject] + ' ' + phrase + compound_verb

    else:
        raise ValueError('Invalid tense')
    

