#personal_info.py
#Written by Rini Jayarethinam

def input_info():
    first_name = input("Enter your name: ")
    print("Your name is " + first_name)

    my_age = input("Enter your age: ")
    my_age = int(my_age)
    print("Your age is {}".format(my_age))
    return my_age

def age_next_year(current_age):
    next_year = current_age + 1
    print("Your age next year will be {}".format(next_year))

def age_classification(my_age):
    if my_age<18:
        print("You are a minor.")
        print("Get your parent's permission.")
    elif my_age >=65:
        print("You are a senior.")
    elif my_age==21:
        print("You are turning 21.")
    else:
        print("You are an adult.")  
        
    print("Done")
    
print("Running program...")
age = input_info()
age_next_year(age)
age_classification(age)
print("Finished program...")