@pytest.mark.parametrize("first_point, second_point, expected",[
    ((1,2),(3,4),1)])
def test_coordinates_plane(input_points, expected_m):
    from coordinates_plane import slope_calculation
    answer = slope_calculation(input_points)
    assert answer == expected_m
    
@pytest.mark.parametrize("x_value, expected_y",[
    (4,1)])
def test_coordinates_plane(x_value, expected_y):
    from coordinates_plane import y_value_calculation
    answer = y_value_calculation(x_value)
    assert answer == expected_y