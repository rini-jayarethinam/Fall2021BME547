import pytest

@pytest.mark.parametrize("x1_value, y1_value, x2_value, y2_value, expected_m", [(1,2,3,4,1),(1,2,3,4,5),(1,2,3,3,0.5)])
def test_slope_calculation(x1_value, y1_value, x2_value, y2_value, expected_m):
    from coordinates_classwork import slope_calculation
    answer = slope_calculation(x1_value, y1_value, x2_value, y2_value)
    assert answer == expected_m