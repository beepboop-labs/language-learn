from app.utils.english import conjugate_english
import csv
import pytest

file_path = 'tests/test_cases/english.tsv'
data = []
with open(file_path, 'r') as tsvfile:
    reader = csv.reader(tsvfile, delimiter='\t')
    for row in reader:
        data.append((str(row[0]), str(row[1])))


@pytest.mark.parametrize("test_input,expected", data)
def test_conjugate_english(test_input, expected):
     assert conjugate_english(test_input) == expected