
# My Python practice script for Unit Two

# Step 1: Store my name as text
student_name = "Charlie"

# Store my age as a whole number
my_current_age = 19

# Store my height as a decimal number in metres
my_exact_height = 1.78


# Step 2: Display my personal information
# str() converts numbers into text so they can be joined together
print("Hello, my name is " + student_name
      + ", I am " + str(my_current_age)
      + " years old, and my height is "
      + str(my_exact_height) + " metres.")


# Step 3: Calculate my age in months
# There are 12 months in one year
months_old = my_current_age * 12

# Display my age in months
print("My age in months is:", months_old)


# Step 4: Convert my height from metres to centimetres
# Multiply the height in metres by 100
height_in_centimeters = my_exact_height * 100

# Add 10 centimetres to my height
new_tallness = height_in_centimeters + 10

# Display the new height in centimetres
print("My height plus 10 cm is:", new_tallness, "cm")


# Step 5: Check whether I am older than 18
# The result will be either True or False
is_adult_check = my_current_age > 18

# Display the result of the age check
print("Is my age greater than 18?", is_adult_check)


# Step 6: Convert my height into a whole number
# int() removes the decimal part; it does not round the number
whole_number_height = int(my_exact_height)

# Display the converted height value
print("My height converted to an integer is:",
      whole_number_height)


# Step 7: Calculate my age next year
# Add 1 to my current age
next_year_age = my_current_age + 1

# Display my age next year
print("Next year I will be:", next_year_age)


# Step 8: Practise converting a number into text
# Joining text and a number directly causes a TypeError
# Example of incorrect code: "My age is " + my_current_age

# Convert my age into text using str()
print("My age as text is " + str(my_current_age))
