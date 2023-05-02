## This script runs conjugations from the command line

import sys
import csv
from app import create_app, db
from app.models.language import Language
from app.models.phrase import Phrase
from app.utils.english import conjugate_english
from app.utils.spanish import conjugate_spanish
from app.utils.swahili import conjugate_swahili
from app.utils.parse_verb_string import parse_verb_string

# Accepting an app instance as an optional argument is useful for testing
# because we can pass in the app object from the test
# When not testing, we dont pass an object and the function will create one
# This allows the script to be run from the command line
def conjugate(language, filename, app=None):

    if not app:
        print("Creating app object from create_app function")
        app = create_app()

    if not filename:
        raise Exception("No filename provided")
    
    if not language:
        raise Exception("No language provided")
    
    secondary_language = Language.query.filter_by(name=language.lower()).first()
    if not secondary_language:
        raise Exception("Language not found")
    


    # Read the contents of the TSV file
    with open(filename, 'r') as file:
        reader = csv.reader(file, delimiter='\t')


        conjugations = [];

        for row in reader:
            negative, subject, tense, root, compound_verb = parse_verb_string(row[0])
            print(negative, subject, tense, root, compound_verb)

            # get english translation
            phrase_pair = Phrase.query.filter_by(secondary=root+compound_verb).first()

            if not phrase_pair:
                raise Exception("Translation not found")
            
            # build verb string
            primary_verb_string = negative + "+" + subject + "+" + tense + "+" + phrase_pair.primary
            secondary_verb_string = row[0]

            # get conjugation
            if language == 'spanish':
                conjugation = (conjugate_english(primary_verb_string), conjugate_spanish(secondary_verb_string))
            elif language == 'swahili':
                conjugation = (conjugate_english(primary_verb_string), conjugate_swahili(secondary_verb_string))
            else:
                raise Exception("Language not found")
            
            conjugations.append(conjugation)

        output_filename = 'tests/test_cases/output_file.tsv'

        with open(output_filename, 'w', newline='') as file:
            writer = csv.writer(file, delimiter='\t')
            for row in conjugations:
                writer.writerow(row)

        print(f"Data has been written to {output_filename}")


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python insert_phrases.py <langauge> <filename>')
        sys.exit(1)

    language = sys.argv[1]
    filename = sys.argv[2]
    conjugate(language, filename)