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
    
def coordinates_driver():
    input_points, new_x_value = point_inputs()
    x1_value, y1_value, x2_value, y2_value, new_x_value = input_type_conversion(input_points, new_x_value)

if __name__ == "__main__":
    coordinates_driver()