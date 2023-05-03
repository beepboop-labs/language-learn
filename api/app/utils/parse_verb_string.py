def parse_verb_string(s):
    parts = s.split('+')
    if len(parts) == 4:
        negative, subject, tense, root = parts
    elif len(parts) == 3:
        subject, tense, root = parts
        negative = False
    else:
        raise ValueError('Invalid string format')
    
    if not negative == 'NEG':
        negative = ''       # relying on this to be falsey
    
    # Check if root is a compound verb: Kuwa na
    compound_verb = ""
    if " " in root:
        compound_verb =" " + root.split(" ", 1)[1]
        root = root.split(" ", 1)[0]

    return negative, subject, tense, root, compound_verb