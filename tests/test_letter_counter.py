from lib.letter_counter import *

def test_calculate_more_common():
    rcounter = LetterCounter("Digital Punk")
    result = counter.calculate_most_common()
    assert result == [2, "i"]