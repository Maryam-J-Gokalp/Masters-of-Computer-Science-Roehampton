#  Unit2

# step one: setting up my basic variables here
student_name = "Charlie"  # my name string
my_current_age = 19       # my age as a whole number
my_exact_height = 1.78    # height in meters as a float decimal

# step two: printing everything nicely together in one go
print("Hey there, my name is " + student_name + ", I am " + str(my_current_age) + " years old, and my height is " + str(my_exact_height) + " meters.")

# step three part one: figure out age in months
months_old = my_current_age * 12  # multiply years by 12 months
print("If you want my age in months, it comes out to:", months_old)

# step three part two: adding ten to height (let's use cm this time)
height_in_centimeters = 178.0  # converted to cm for easier addition
new_tallness = height_in_centimeters + 10  # adding 10 cm
print("Adding ten centimeters gives us:", new_tallness)

# step four: checking if age is greater than eighteen
is_adult_check = my_current_age > 18  # this should give a boolean True or False
print("Is the age greater than eighteen?", is_adult_check)

# step five: turning the float height into a normal integer
whole_number_height = int(my_exact_height)  # strips the decimal part away
print("Changing the float height into an int gives:", whole_number_height)

# step six: making a type error on purpose and then fixing it
# note: doing print("Age next year: " + 20) crashed with a TypeError!
# fixed version below:
print("Next year I will be: " + str(my_current_age + 1))  # wrapped the number in str() so it matches