from flask import make_response, jsonify
import json
from app.models.phrase import Phrase
from app.models.language import Language
from sqlalchemy import func

def get_quiz(specifications):
    # specifications is a dictionary of specifications for the quiz
    # {"length": 10, "unit": 1, "primaryLanguage": "English",
    #  "secondaryLanguage": "Spanish"} for example

    #TODO: add logic for different kinds of quiz data based on specifications
    try:
        # SAMPLE QUIZ DATA
        f = open('data/sample_data.json')
        quiz_data = json.load(f)

        newQuiz = {};


        print(specifications)
        print(specifications['length'])

        # get requested language
        language = Language.query.filter_by(name=specifications['secondaryLanguage']).first()
        print(language.id)
        # Get list of verbs from the database of specified length
        word_pairs = Phrase.query.filter_by(secondary_language=language).order_by(func.random()).limit(specifications['length']).all()
        print(language)
        print(word_pairs)

        return make_response(jsonify(quiz_data), 200)

    except Exception as e:
        return make_response({'message': str(e)}, 500)
    