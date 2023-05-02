from flask import make_response, jsonify
import json
from sqlalchemy import func
from app.models.phrase import Phrase
from app.models.language import Language

from app.utils.english import conjugate_english
from app.utils.spanish import conjugate_spanish
from app.utils.swahili import conjugate_swahili

from sqlalchemy import func
from random import randrange, choice

def get_quiz(specifications):
    # accepts a dictionary of specifications for the quiz
    # example: { "length": 10, "unit": 1, "primaryLanguage": "english", "secondaryLanguage": "spanish" }
    negative = ["NEG", ""]
    subjects = ["1s", "2s", "3s", "1p", "2p", "3p"]
    unit_tenses = {
        "1": ["PRES", "IMP"],
        "2": ["PAST", "FUT"],
        "3": ["PAST", "PERF", "FUT"]
    }
    #TODO: add logic for different kinds of quiz data based on specifications
    try:
        
        new_quiz = {
            "words": [],
        }

        new_word_pair = {}

        # get requested language
        language = Language.query.filter_by(name=specifications['secondaryLanguage']).first()

        # Get list of verbs from the database of specified length
        word_pairs = Phrase.query.filter_by(secondary_language=language).order_by(func.random()).limit(specifications['length']).all()


        for word in word_pairs:
            tense = "PRES"
            if specifications['unit'] == 1:
                tense = choice(unit_tenses["1"])
            elif specifications['unit'] == 2:
                tense = choice(unit_tenses["2"])
            elif specifications['unit'] == 3:
                tense = choice(unit_tenses["3"])
            else:
                raise Exception("Unit not found")

            conjugation_str = choice(negative) + "+" + choice(subjects) + "+" + tense + "+"



            eng_full_str = conjugation_str + word.primary
            print(eng_full_str)
            english = conjugate_english(eng_full_str)
            print(english)

            secondary_full_str = conjugation_str + word.secondary;
            print(secondary_full_str)

            conjugation = ""
            if specifications['secondaryLanguage'] == 'spanish':
                conjugation = conjugate_spanish(secondary_full_str)

            elif specifications['secondaryLanguage'] == 'swahili':
                conjugation = conjugate_swahili(secondary_full_str)

            new_word_pair = { "primary": english, "secondary": conjugation }
            new_quiz["words"].append(new_word_pair)

        return make_response(jsonify(new_quiz), 200)

    except Exception as e:
        return make_response({'message': str(e)}, 500)