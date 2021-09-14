# Coordinates Classwork by Rini Jayarethinam


def point_inputs():
    print("\nEnter the 2 coordinates separated by a comma")
    print("Example: '(x1,y1),(x2,y2)'")
    input_points = input("Input the 2 coordinates here: ")
    new_x_value = input("\nInput the x-value: ")
    return input_points, new_x_value
    
def input_type_conversion(input_points, new_x_value):
    point_list = list(eval(input_points.replace(',',',').replace(' ',',')))
    x1_value = point_list[0][0]
    y1_value = point_list[0][1]
    x2_value = point_list[1][0]
    y2_value = point_list[1][1]
    new_x_value = int(new_x_value)
    return x1_value, y1_value, x2_value, y2_value, new_x_value

def slope_calculation(x1_value, y1_value, x2_value, y2_value):
    y_diff = y2_value-y1_value
    x_diff = x2_value-x1_value
    slope_m = y_diff/x_diff
    return slope_m
    
def new_y_value_calculation(slope_m, new_x_value, x1_value, y1_value):
    new_y_value = (slope_m * (new_x_value-x1_value))+y1_value
    return new_y_value

def y_value_output(new_y_value):
    print("\nFrom the line created by the 2 inputted points, there is a coordinate on the line with the given x-value and the outputted y-value of {:.2f}.".format(new_y_value))
    
def coordinates_driver():
    input_points, new_x_value = point_inputs()
    x1_value, y1_value, x2_value, y2_value, new_x_value = input_type_conversion(input_points, new_x_value)
    slope_m = slope_calculation(x1_value, y1_value, x2_value, y2_value)
    new_y_value = new_y_value_calculation(slope_m, new_x_value, x1_value, y1_value)
    y_value_output(new_y_value)

if __name__ == "__main__":
    coordinates_driver()