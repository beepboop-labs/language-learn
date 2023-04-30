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

def conjugate_spanish(verbString):
    # negative: True, False
    # subject: 1p, 2p, 3p, 1s, 2s, 3s
    # tense: IMP, PAST, FUT, PRES, PERF

    negative, subject, tense, root = parse_string(verbString)

    phrase = root


    #IMP TENSE
    
    if tense == 'IMP':


        if phrase.endswith('ar'):
            affirmative_endings = {
                '1s':'',
                '2s':'a',
                '3s':'e',
                '1p':'emos',
                '2p':'ad',
                '3p':'en'

            }
            negative_endings =  {
                '1s':'no',
                '2s':'no',
                '3s':'no',
                '1p':'no',
                '2p':'no',
                '3p':'no'

            }

            if negative:
                return "no " + phrase[:-2] + endings[subject]
            return phrase[:-2] + endings[subject]
        

        elif phrase.endswith('er') or phrase.endswith('ir'):
             affirmative_endings = {
                '1s':'',
                '2s':'e',
                '3s':'a',
                '1p':'amos',
                '2p':'ed',
                '3p':'an'

            }
             negative_endings =  {
                '1s':'no',
                '2s':'no',
                '3s':'no',
                '1p':'no',
                '2p':'no',
                '3p':'no'

            }
        else:
            phrase = "ENDING NOT FOUND"
            return phrase
             
        if negative:
            return "no " + phrase[:-2] + endings[subject]
        return phrase[:-2] + endings[subject]
    
    
    
            
        
    

    #PAST TENSE
    if tense == 'PAST':
        
        if phrase.endswith('ar'):
            endings = {
                '1s':'é',
                '2s':'aste',
                '3s':'ó',
                '1p':'amos',
                '2p':'asteis',
                '3p':'aron'
            }

            if negative:
                return "no " + phrase[:-2] + endings[subject]
            return phrase[:-2] + endings[subject]

        elif phrase.endswith('er') or phrase.endswith('ir'):
            endings={
                '1s':'í',
                '2s':'iste',
                '3s':'ió',
                '1p':'imos',
                '2p':'isteis',
                '3p':'ieron'

            }
        else:
            phrase = "ENDING NOT FOUND"
            return phrase  
        
        if negative:
                return "no " + phrase[:-2] + endings[subject]
        return phrase[:-2] + endings[subject]
            
       



    #FUTURE TENSE
    if tense == 'FUT':
        if phrase.endswith('ar'):
            endings = {
                 '1s':'é',
                '2s':'ás',
                '3s':'á',
                '1p':'emos',
                '2p':'éis',
                '3p':'án'
            }

            if negative:
                return "no " + phrase[:-2] + endings[subject]
            return phrase[:-2] + endings[subject]
        

        elif phrase.endswith('er') or phrase.endswith('ir'):
             endings = {
                 '1s':'é',
                '2s':'ás',
                '3s':'á',
                '1p':'emos',
                '2p':'éis',
                '3p':'án'
            }

        else:
            phrase = "ENDING NOT FOUND"
            return phrase 
            
        if negative:
                return "no " + phrase[:-2] + endings[subject]
        return phrase[:-2] + endings[subject]  
    
    
        
    


    #PRESENT TENSE
    # phrase = "hablar"
    if tense == 'PRES':
        if phrase.endswith('ar'):
            endings = {
                '1s':'o',
                '2s':'as',
                '3s':'a',
                '1p':'amos',
                '2p':'áis',
                '3p':'an'
            }

            if negative:
                return "no " + phrase[:-2] + endings[subject]
            return phrase[:-2] + endings[subject]

        elif phrase.endswith('er'):
            endings ={
                '1s':'o',
                '2s':'es',
                '3s':'e',
                '1p':'emos',
                '2p':'éis',
                '3p':'en'

            } 

            if negative:
                return "no " + phrase[:-2] + endings[subject]
            return phrase[:-2] + endings[subject]

        elif phrase.endswith('ir'):  # verb.endswith('ir')
            endings ={
                '1s':'o',
                '2s':'es',
                '3s':'e',
                '1p':'imos',
                '2p':'ís',
                '3p':'en'
            } 

        else:
            phrase = "ENDING NOT FOUND"
            return phrase
        

        if negative:
                return "no " + phrase[:-2] + endings[subject]
        return phrase[:-2] + endings[subject]
           
    


    #PERFECT TENSE
    
    if tense == 'PERF':
        if phrase.endswith('ar'):
            past_participle = phrase[:-2] + 'ado'
            endings = {
                '1s':'o',
                '2s':'as',
                '3s':'a',
                '1p':'amos',
                '2p':'áis',
                '3p':'an'
            }

            

            if negative:
                return "no " + phrase[:-2] + endings[subject]
            return phrase[:-2] + endings[subject]


        elif phrase.endswith('er') or phrase.endswith('ir'):
            past_participle = phrase[:-2] + 'ido'
            
            endings ={
                '1s':'o',
                '2s':'es',
                '3s':'e',
                '1p':'emos',
                '2p':'éis',
                '3p':'en'

            } 

            if negative:
                return "no " + phrase[:-2] + endings[subject]
            return phrase[:-2] + endings[subject]

        elif phrase.endswith('ir'):  # verb.endswith('ir')
            past_participle = phrase[:-2] + 'ido'
            endings ={
                '1s':'o',
                '2s':'es',
                '3s':'e',
                '1p':'imos',
                '2p':'ís',
                '3p':'en'
            }

        else:
            phrase = "ENDING NOT FOUND"
            return phrase

        if negative:
                return "no " + phrase[:-2] + endings[subject]
        return phrase[:-2] + endings[subject] 

        
    