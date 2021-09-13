import pytest

@pytest.mark.parametrize("hdl_value, expected", [(
    65, "Normal"), (45, "Borderline Low"), (15, "Low"), (70, "Normal")])
def test_hdl_analysis(hdl_value, expected):
	from blood_calculator import hdl_analysis
	answer = hdl_analysis(hdl_value)
	assert answer == expected