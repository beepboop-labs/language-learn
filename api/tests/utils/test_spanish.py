# -*- coding: utf-8 -*-

from app.utils.spanish import conjugate_spanish
import csv
import pytest

file_path = 'tests/test_cases/spanish.tsv'
data = []
with open(file_path, 'r') as tsvfile:
    reader = csv.reader(tsvfile, delimiter='\t')
    for row in reader:
        data.append((str(row[0]), str(row[1])))


@pytest.mark.parametrize("test_input,expected", data)
def test_conjugate_spanish(test_input, expected):
     assert conjugate_spanish(test_input) == expected