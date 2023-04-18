from flask import make_response, jsonify
import json
from sqlalchemy import func
from app.models.phrase import Phrase
from app.models.language import Language

from app.utils.english import conjugate_english
from app.utils.spanish import conjugate_spanish

from sqlalchemy import func
from random import randrange

def get_quiz(specifications):
    # accepts a dictionary of specifications for the quiz
    # example: { "length": 10, "unit": 1, "primaryLanguage": "english", "secondaryLanguage": "spanish" }

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
            conjugation_options= ["NEG+3s+PRES+", "1p+IMP+", "3p+PERF+", "NEG+2p+FUT+", "1p+PAS+", "NEG+3s+PAS+" ]
            conjugation_str = conjugation_options[randrange(len(conjugation_options))]



            eng_full_str = conjugation_str + word.primary
            print(eng_full_str)
            english = conjugate_english(eng_full_str)
            print(english)

            secondary_full_str = conjugation_str + word.secondary;
            print(secondary_full_str)
            spanish = conjugate_spanish(secondary_full_str)
            print(spanish)

            new_word_pair = { "primary": english, "secondary": spanish }
            new_quiz["words"].append(new_word_pair)

        return make_response(jsonify(new_quiz), 200)

    except Exception as e:
        return make_response({'message': str(e)}, 500)
    