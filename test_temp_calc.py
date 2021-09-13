import pytest

@pytest.mark.parametrize("input, expected", [([96, 96.5, 103.1, 98.7], False),
    ([96, 96.5, 97.1, 98.7],False)])

def test_detect_fever(input, expected):
	from temp_calc import detect_fever
	input = [96, 96.5, 103.1, 98.7]
	answer = detect_fever(input)
	assert answer == expected
