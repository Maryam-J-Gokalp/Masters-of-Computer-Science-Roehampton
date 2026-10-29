
"""
Task: Unit 3 - Task 1 - File I/O Task
File name: Unit_3_Task_1_File_IO_Task.py

This program asks the user for their name and age.
It saves the information in a text file and reads it back.
It also shows how to handle a missing file.
"""

from pathlib import Path


def main():
    # Ask the user for their name
    name = input("Enter your name: ")

    # Ask the user for their age
    try:
        age = int(input("Enter your age: "))
    except ValueError:
        print("Please enter a valid age using numbers.")
        return

    # Welcome the user
    print(f"Hello, {name}! You are {age} years old.")

    # Create the file path
    file_path = Path("user_data.txt")

    try:
        # Save the name and age in the file
        with file_path.open("w", encoding="utf-8") as file:
            file.write(f"Name: {name}\n")
            file.write(f"Age: {age}\n")

        # Add a confirmation message
        with file_path.open("a", encoding="utf-8") as file:
            file.write("Data successfully saved.\n")

        # Read the information from the file
        with file_path.open("r", encoding="utf-8") as file:
            print("\nInformation in the file:")
            print(file.read(), end="")

    except FileNotFoundError as error:
        print(f"File not found: {error}")
    except OSError as error:
        print(f"An error occurred: {error}")

    # Test what happens when a file is missing
    print("\nTesting a missing file:")

    missing_file = Path("missing_file.txt")

    try:
        with missing_file.open("r", encoding="utf-8") as file:
            print(file.read())

    except FileNotFoundError as error:
        # Display the error message
        print(f"Error message: {error}")

        # Create the missing file to fix the problem
        try:
            with missing_file.open("w", encoding="utf-8") as file:
                file.write("The file has been created.")

            print("The missing file has now been created.")

            # Open the file again and read it
            with missing_file.open("r", encoding="utf-8") as file:
                print(file.read())

        except OSError as fix_error:
            print(f"Could not create the file: {fix_error}")


if __name__ == "__main__":
    main()
