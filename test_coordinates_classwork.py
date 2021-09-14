import pytest

@pytest.mark.parametrize("x1_value, y1_value, x2_value, y2_value, expected_m", [(1,2,3,4,1),(1,3,5,5,0.5),(1,2,3,3,0.5)])
def test_slope_calculation(x1_value, y1_value, x2_value, y2_value, expected_m):
    from coordinates_classwork import slope_calculation
    answer = slope_calculation(x1_value, y1_value, x2_value, y2_value)
    assert answer == expected_m
    
@pytest.mark.parametrize("slope_m, new_x_value, x1_value, y1_value, expected_y", [(1,5,1,2,6),(1,6,1,2,7),(1,7,1,2,8)])
def test_y_value_calculation(slope_m, new_x_value, x1_value, y1_value, expected_y):
    from coordinates_classwork import new_y_value_calculation
    answer = new_y_value_calculation(slope_m, new_x_value, x1_value, y1_value)
    assert answer == expected_y