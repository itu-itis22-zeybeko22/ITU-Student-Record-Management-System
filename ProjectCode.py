                                                            #ITU Student Record Management System
#To save data of students importing csv
import csv
#To visualization importing pandas,seaborn and matplotlib
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#For Alphabetic Order 
import locale
#Creating a list for information fields
fields = ["Roll no.","Name Surname","Age","Gender","Students id","Grade","Email","Phone","Major"]

#Using CSV file for Majors to prevent add non-existing majors (they are all lowercase because it will make it easier to check)
with open("majors.csv","r",encoding="utf-8") as f:
    reader = csv.reader(f)
    itu_majors = list(reader)
#ITU majors was a list in a list so with this line it is one list
itu_majors = itu_majors[0]
#Defining my data storage
database = "dataset.csv"

#Defining a function for console menu
def console_menu():
    print("-----------------------------------------------")
    print("Welcome to ITU Student Record Management System")
    print("-----------------------------------------------")
    print("Which operation do you want to make?")
    print("1. Add New Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Visualization")
    print("7. Student Statistics")
    print("8. Exit")

#Defining a function to print the data of student after save
def print_student_data(student_data):
    print("-------------------------")
    print("Student Information")
    print("-------------------------")
    print("Roll No.:", student_data[0])
    print("Name:", student_data[1])
    print("Age:", student_data[2])
    print("Gender:", student_data[3])
    print("Students ID:", student_data[4])
    print("Grade:", student_data[5])
    print("Email:", student_data[6])
    print("Phone:", student_data[7])
    print("Major:", student_data[8])
    print("-------------------------")

#Defining a function to validate email.
def validate_email(email):
    if not email.endswith("@itu.edu.tr"):
        raise ValueError("Error: Invalid email. Email should end with @itu.edu.tr")
    elif len(email) <= len("@itu.edu.tr"):
        raise ValueError("Error: Invalid Email. There should be at least one character before @itu.edu.tr")
    else:
        #Email should start with lower char
        return email.lower()
#Defining a function to validate name
def validate_name(name):
    #If any character that is not first character is upper this will make it lower.
    name = name.lower()
    # Null name is invalid
    if not name:
        raise ValueError("Error: Invalid name! Name shouldn't be empty")
    #No special characters are allowed or no numbers are allowed in the name
    elif not all(char.isalpha() or char.isspace() for char in name):
        raise ValueError("Error: Invalid name! Name should only include letters or space")
    else:
        formatted_name = ' '.join(word.capitalize() for word in name.split())
        return formatted_name
#Defining a function to validate major
def validate_major(major):
    #Major field is required
    if not major:
        raise ValueError("Error: Invalid major! Major field is required.")
    #No special characters are allowed or no numbers are allowed in the major
    elif not all(char.isalpha() or char.isspace() for char in major):
        raise ValueError("Error: Invalid major! Major should only include letters or spaces.")
    #Major should be in itu_majors
    elif major.lower() not in itu_majors:
        raise ValueError("Error: Invalid major! The major you entered is not in ITU majors list or it is spelled incorrectly.")
    else:
        formatted_major = ' '.join(word.capitalize() for word in major.split())
        return formatted_major
#Defining a function to validate fields
def validation(fields):
    student_data = []
    for field in fields:
        if field == "Major":
            value = input("Enter " + field + " (don't forget to add Engineering end of the major): ")
        else:
            value = input("Enter " + field + ": ")
        # In ITU grades are between 0 and 4 so checking if grade is between 0 and 4
        if field == "Grade":
            while True:
                try:
                    value = float(value)
                    if 0 <= value <= 4:
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print("Error: Please enter a number between 0 and 4 for grade")
                    value = input("Enter " + field + ": ")
        # Age should be >= 17
        elif field == "Age":
            while True:
                try:
                    value = int(value)
                    if 17 <= value <= 30:
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print("Error: Age should be between 17 and 30")
                    value = input("Enter " + field + ": ")
        # Checking if roll no. is bigger than 0
        elif field == "Roll no.":
            while True:
                try:
                    if not all(char.isdigit() for char in value):
                        raise ValueError("Error: Roll no. should be an integer")
                    value = int(value)
                    # Roll no must be bigger or equal to
                    if value < 1:
                        raise ValueError("Error : Roll no. is less than 1")
                    break
                except ValueError as e:
                    print(e)
                    value = input("Enter " + field + ": ")
        elif field == "Students id":
            while True:
                try:

                    #If we convert a number that starts with 0 to integer, its length will be reduced
                    if value.startswith("0"):
                        value = "1" + value[1:]
                    value = int(value)
                    # Student's id length must be 9
                    if not  len(str(value)) == 9:
                        raise ValueError("Error: Student ID length should be 9.")
                    break
                except ValueError as e:
                    print(e)
                    value = input("Enter " + field + ": ")
        # Length of Phone number must be equal to 11
        elif field == "Phone":
            while True:
                try:
                    #If we convert a number that starts with 0 to integer, its length will be reduced
                    if value.startswith("0"):
                        value = "1" + value[1:]
                    value = int(value)
                    #Length of phone number must be 11
                    if len(str(value)) == 11:
                        break
                    else:
                        print("Error: Phone number should be at least 11 characters long.")
                        value = input("Enter " + field + ": ")
                except ValueError:
                    print("Error: Please enter valid", field)
                    value = input("Enter " + field + ": ")
        elif field == "Email":
            while True:
                try:
                    value = validate_email(value)
                    break
                except ValueError as e:
                    print(e)
                    value = input("Enter " + field + ": ")
        elif field == "Gender":
            while True:
                if value.lower() == "male" or value.lower() == "female":
                    break
                else:
                    print("Error: Gender should be Female or Male")
                    value = input("Enter " + field + ": ").lower()
            value = value.title()
        elif field == "Name Surname":
            while True:
                try:
                    value = validate_name(value)
                    break
                except ValueError as e:
                    print(e)
                    value = input("Enter " + field + ": ")
        elif field == "Major":
            while True:
                try:
                    value = validate_major(value)
                    break
                except ValueError as e:
                    print(e)
                    value = input("Enter " + field + ": ")
        student_data.append(value)
    return student_data
#Defining a function for Add New Student operation
def add_student():
    #Fields and database are global we can access them
    global fields
    global database

    #Add Information
    print("-------------------------")
    print("Add Student Information")
    print("-------------------------")
    operation = "Add Student operation"
    while True:
        value = input(f"Enter 1 to continue {operation} or 2 to exit: ")
        if value == "2":
            break
        elif value == "1":
            #Creating a list to store inputs
            student_data = validation(fields)
            #Checking if students id , email , roll no or phone in database
            if len(student_data) == 9:
                new_id = student_data[4]
                new_email = student_data[6]
                new_phone = student_data[7]
                new_roll = student_data[0]
                #Opening csv file in reading mode
                with open(database, "r", encoding="utf-8") as f:
                    reader = csv.reader(f)
                    for row in reader:
                        if str(new_id) in row:
                            print("A student with the same student id already exists.")
                            return
                        elif str(new_email) in row:
                            print("A student with the same email already exists.")
                            return
                        elif str(new_roll) in row:
                            print("A student with the same roll no. already exists.")
                            return
                        elif str(new_phone) in row:
                            print("A student with the same phone number already exists")
                            return

            #Opening csv file in writing mode (appending end of the dataset)
            with open("dataset.csv", "a", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerows([student_data])

            print_student_data(student_data)

            print("Data saved successfully")
        else:
            print("Invalid input. Please enter 1 to continue or 2 to exit.")
#Defining a function for View Students Operation
def view_students():
    #Fields and database ara global we can access them
    global fields
    global database

    print("--- Student Records ---")
    operation = "View Students operation"
    while True:
        value = input(f"Enter 1 to continue {operation} or 2 to exit: ")
        if value == "2":
            break
        elif value == "1":
            while True:
                #Asking user to how they want to see datas
                print("Which way do you want to see students?")
                print("1. As It is in Database")
                print("2. By their Roll Numbers")
                print("3. By their Gender")
                print("4. By their Major")
                print("5. By their Grades")
                print("6. By Alphabetic Order")
                print("7. By their Gender in a specific Major")
                print("8. By their Grades in a specific Major")

                choice = input("Enter your choice (0 to exit): ")
                choice = choice.strip()
                if not choice == "0":
                    #For choice 1
                    if choice == "1":
                        #Opening csv file in reading mode
                        with open("dataset.csv", "r", encoding="utf-8") as f:
                            reader = csv.reader(f)

                            for row in reader:
                                print(" | ".join(row))
                        break
                    #For choice 2
                    elif choice == "2":
                        #Opens file and read each line
                        with open(database, 'r',encoding="utf-8") as file:
                            lines = file.readlines()

                        #Adjusts header line and append to output_lines
                        header = ' | '.join(map(str.strip, lines[0].split(',')))
                        output_lines = [header]

                        #Sorting values by their roll numbers
                        data_lines = [line.split(',') for line in lines[1:]]
                        sorted_data = sorted(data_lines, key=lambda x: int(x[0]))

                        #Appending each data with " | "
                        for line in sorted_data:
                            formatted_line = ' | '.join(map(str.strip, line))
                            output_lines.append(formatted_line)

                        #Writing the outputs
                        for line in output_lines:
                            print(line)
                        print("\n")
                        break
                    #For choice 3
                    elif choice == "3":
                        print("Which gender students do you want to see?")
                        print("1. Male")
                        print("2. Female")
                        while True:
                            gen = input("Enter your choice (0 to exit): ")
                            if not gen == "0":
                                if gen == "1":
                                    print(" | ".join(fields))
                                    with open("dataset.csv", "r", encoding="utf-8") as f:
                                        reader = csv.reader(f)
                                        #Writing Male Students
                                        for row in reader:
                                            if "Male" in row:
                                                print(" | ".join(row))
                                    break
                                elif gen == "2":
                                    print(" | ".join(fields))
                                    with open("dataset.csv", "r", encoding="utf-8") as f:
                                        reader = csv.reader(f)
                                        #Writing female students
                                        for row in reader:
                                            if "Female" in row:
                                                print(" | ".join(row))
                                    break
                                else:
                                    print("Invalid Input! Enter 1 or 2.")
                            else:
                                break
                        break
                    #By their Major
                    elif choice == "4":

                        print("Which major students do you want to see?")

                        # Gets unique major values from the dataset
                        with open(database, 'r', encoding="utf-8") as file:
                            lines = file.readlines()
                        majors = set([line.split(',')[-1].strip() for line in lines[1:]])

                        # Printing major options
                        for idx, major in enumerate(majors, start=1):
                            print(f"{idx}. {major}")

                        # Asking which major they want to see
                        major_choice = input("Enter the number of the major you want to see (0 to exit): ")
                        while True:
                            if not major_choice == "0":
                                #User selects a number
                                if major_choice.isdigit() and 1 <= int(major_choice) <= len(majors):
                                    selected_major = list(majors)[int(major_choice) - 1]

                                    #Opening csv file in reading mode
                                    with open(database, 'r', encoding="utf-8") as file:
                                        lines = file.readlines()

                                    #Adjusting header line and appends to output_lines
                                    header = ' | '.join(map(str.strip, lines[0].split(',')))
                                    output_lines = [header]

                                    #Filtering data by major
                                    data_lines = [line.split(',') for line in lines[1:]]
                                    filtered_data = [line for line in data_lines if line[-1].strip() == selected_major]

                                    #Appending each data with " | "
                                    for line in filtered_data:
                                        formatted_line = ' | '.join(map(str.strip, line))
                                        output_lines.append(formatted_line)

                                    #Writing the outputs
                                    for line in output_lines:
                                        print(line)
                                    print("\n")
                                    break
                                else:
                                    print("Invalid Input! Please enter a valid number.")
                            else:
                                break
                        break
                    #Sorting By Grade
                    elif choice == "5":
                        while True:
                            print("How do you want to sort students by grades?")
                            print("1. Ascending Order")
                            print("2. Descending Order")
                            sort_choice = input("Enter your choice (0 to exit): ")
                            if not sort_choice == "0":

                                if sort_choice == "1":
                                    #Opening CSV file in reading mode
                                    with open(database, 'r', encoding="utf-8") as file:
                                        lines = file.readlines()

                                    #Adjusting header line and appends to output_lines
                                    header = ' | '.join(map(str.strip, lines[0].split(',')))
                                    output_lines = [header]

                                    #Sorting data by grades (Ascending Order)
                                    data_lines = [line.split(',') for line in lines[1:]]
                                    sorted_data = sorted(data_lines, key=lambda x: float(x[5]))

                                    #Appending each data with " | "
                                    for line in sorted_data:
                                        formatted_line = ' | '.join(map(str.strip, line))
                                        output_lines.append(formatted_line)

                                    #Writing the outputs
                                    for line in output_lines:
                                        print(line)
                                    print("\n")
                                    break
                                elif sort_choice == "2":
                                    #Opening CSV file in reading mode
                                    with open(database, 'r', encoding="utf-8") as file:
                                        lines = file.readlines()

                                    #Adjusting header line and appends to output_lines
                                    header = ' | '.join(map(str.strip, lines[0].split(',')))
                                    output_lines = [header]

                                    #Sorting data by grades (Descending Order)
                                    data_lines = [line.split(',') for line in lines[1:]]
                                    sorted_data = sorted(data_lines, key=lambda x: float(x[5]), reverse=True)

                                    #Appending each data with " | "
                                    for line in sorted_data:
                                        formatted_line = ' | '.join(map(str.strip, line))
                                        output_lines.append(formatted_line)

                                    #Writing the outputs
                                    for line in output_lines:
                                        print(line)
                                    print("\n")
                                    break
                                #If choice is not equal to 1 or 2
                                else:
                                    print("Invalid Input! Enter 1 or 2.")
                            else:
                                break
                        break
                    #Sorting by Alphabetic Order
                    elif choice == "6":
                        while True:
                            print("Which Alphabet Ordering Do You Want?")
                            print("1.Turkish")
                            print("2.English")
                            w = input("Enter your choice (0 to exit): ")
                            if not w == "0":
                                if w == "1":
                                    #Setting the locale to Turkish for sorting
                                    locale.setlocale(locale.LC_ALL, "tr_TR.UTF-8")
                                        # Opening CSV file in reading mode
                                    with open(database, 'r', encoding="utf-8") as file:
                                        lines = file.readlines()

                                    # Adjusting header line and appends to output_lines
                                    header = ' | '.join(map(str.strip, lines[0].split(',')))
                                    output_lines = [header]

                                    # Sorting data by student names (Alphabetic Order with Turkish locale)
                                    data_lines = [line.split(',') for line in lines[1:]]

                                    # Define a custom sorting function based on Turkish locale
                                    def turkish_sort(item):
                                        return locale.strxfrm(item[1])  # Assuming student names are in the second column

                                    sorted_data = sorted(data_lines, key=turkish_sort)

                                    # Appending each data with " | "
                                    for line in sorted_data:
                                        formatted_line = ' | '.join(map(str.strip, line))
                                        output_lines.append(formatted_line)

                                    # Writing the outputs
                                    for line in output_lines:
                                        print(line)
                                    print("\n")
                                    break
                                elif w == "2":
                                    #Opening CSV file in reading mode
                                    with open(database, 'r', encoding="utf-8") as file:
                                        lines = file.readlines()

                                    #Adjusting header line and appends to output_lines
                                    header = ' | '.join(map(str.strip, lines[0].split(',')))
                                    output_lines = [header]

                                    #Sorting data by student names (Alphabetic Order)
                                    data_lines = [line.split(',') for line in lines[1:]]
                                    sorted_data = sorted(data_lines, key=lambda x: x[1])  # Assuming student names are in the second column

                                    #Appending each data with " | "
                                    for line in sorted_data:
                                        formatted_line = ' | '.join(map(str.strip, line))
                                        output_lines.append(formatted_line)

                                    #Writing the outputs
                                    for line in output_lines:
                                        print(line)
                                    print("\n")
                                    break
                                else:
                                    print("Invalid Input! Enter 1 or 2")
                            else:
                                break
                        break
                    #By their Gender in a Specific Major
                    elif choice == "7":
                        print("Which major students do you want to see?")
                        with open(database, 'r', encoding="utf-8") as file:
                            lines = file.readlines()
                        #Selecting Majors and printing them
                        majors = set([line.split(",")[-1].strip() for line in lines[1:]])

                        for idx, major in enumerate(majors, start=1):
                            print(f"{idx}. {major}")

                        major_choice = input("Enter the number of the major you want to see (0 to exit): ")
                        if major_choice == "0":
                            continue
                        elif major_choice.isdigit() and 1 <= int(major_choice) <= len(majors):
                            selected_major = list(majors)[int(major_choice) - 1]
                        else:
                            print("Invalid Input! Enter a valid number.")
                            continue
                        #Asking user for input
                        print("Which Gender Students Do You Want to See?")
                        print("1. Male")
                        print("2. Female")
                        gen_choice = input("Enter your choice (0 to exit): ")
                        #Choosing the gender
                        if gen_choice == "0":
                            continue
                        elif gen_choice == "1":
                            selected_gender = "Male"
                        elif gen_choice == "2":
                            selected_gender = "Female"
                        else:
                            print("Invalid Input! Enter 1 or 2.")
                            continue
                        with open(database, 'r', encoding="utf-8") as file:
                            lines = file.readlines()

                        #Appending Header
                        header = ' | '.join(map(str.strip, lines[0].split(',')))
                        output_lines = [header]
                        #Filtering Data with selected major
                        data_lines = [line.split(',') for line in lines[1:]]
                        data_major = [line for line in data_lines if line[-1].strip() == selected_major]
                        #Filtering data with selected gender
                        sorted_data = sorted(data_major, key=lambda x: x == selected_gender)
                        #Writing Output
                        for line in sorted_data:
                            formatted_line = ' | '.join(map(str.strip, line))
                            output_lines.append(formatted_line)
                        for line in output_lines:
                            print(line)
                        print("\n")
                        break
                    #By Grades in Specific Major
                    elif choice == "8":
                        print("Which major students do you want to see?")
                        #Opening file as reading mode
                        with open(database, 'r', encoding="utf-8") as file:
                            lines = file.readlines()
                        #Selecting Majors
                        majors = set([line.split(",")[-1].strip() for line in lines[1:]])
                        #Printing majors starting with 1
                        for idx, major in enumerate(majors, start=1):
                            print(f"{idx}. {major}")
                        #Asking user for input
                        major_choice = input("Enter the number of the major you want to see (0 to exit): ")
                        if major_choice == "0":
                            continue
                        elif major_choice.isdigit() and 1 <= int(major_choice) <= len(majors):
                            selected_major = list(majors)[int(major_choice) - 1]
                        else:
                            print("Invalid Input! Enter a valid number.")
                            continue
                        #Asking user for input
                        print("How do you want to sort students by grades?")
                        print("1. Ascending Order")
                        print("2. Descending Order")
                        sort_choice = input("Enter your choice (0 to exit): ")
                        #Choosing the sort_choice
                        if sort_choice == "0":
                            continue
                        elif sort_choice == "1":
                            order = False
                        elif sort_choice == "2":
                            order = True
                        else:
                            print("Invalid Input! Enter 1 or 2.")
                            continue
                        #Reading the CSV file
                        with open(database, 'r', encoding="utf-8") as file:
                            lines = file.readlines()
                        #Appending Header line
                        header = ' | '.join(map(str.strip, lines[0].split(',')))
                        output_lines = [header]
                        #Filtering data with selected_major after sorting with grade
                        data_lines = [line.split(',') for line in lines[1:]]
                        filtered_data = [line for line in data_lines if line[-1].strip() == selected_major]
                        sorted_data = sorted(filtered_data, key=lambda x: float(x[5]), reverse=order)
                        #Writing Output
                        for line in sorted_data:
                            formatted_line = ' | '.join(map(str.strip, line))
                            output_lines.append(formatted_line)
                        for line in output_lines:
                            print(line)
                        print("\n")
                        break
                    else:
                        print("Invalid Input! Choose a number between 1-8")
                else:
                    break
    else:
        print("Invalid Input! Choose 1 or 2")

 #Defining a function for Search Student Operation
def search_student():
    #Fields and database ara global we can access them
    global fields
    global database

    operation = "Search Student operation"
    #Offering options to user
    print("--- Search Student ---")
    while True:
        value = input(f"Enter 1 to continue {operation} or 2 to exit: ")
        if value == "2":
            break
        elif value == "1":
            print("1. Search by Students Id")
            print("2. Search by Name Surname (There may be more than one student with same name surname)")
            print("3. Search by Roll No.")

            #Getting input
            choice = input("Enter your choice: ")

            while choice not in ["1", "2", "3"]:
                print("Invalid input. Please enter 1, 2 or 3.")
                print("1. Search by Students Id")
                print("2. Search by Name Surname (There may be more than one student with same name surname)")
                print("3. Search by Roll No.")
                choice = input("Enter your choice: ")

            if choice == "1":
                while True:
                    id = input("Enter students id you want to search (0 to exit): ")
                    if not id == "0":
                        #Checking length of id
                        if len(id) != 9:
                            print("Error: Students ids length must be 9")
                            continue
                        #Opening csv file in reading mode
                        with open("dataset.csv", "r", encoding="utf-8") as f:
                            reader = csv.reader(f)
                            a = 0
                            #Checking if id in rows
                            for row in reader:
                                if str(id) in row:
                                    a += 1
                                    data = row
                            if a == 1:
                            #Writing students info
                                print(" | ".join(fields))
                                print(" | ".join(data))
                                break
                            else:
                                #If student not found in our database
                                print(f"Student with students id {id} not found in our database!")
                    else:
                        break

            elif choice == "2":
                # Using same function in add_student to validate name
                while True:
                    name = input("Enter students name surname (0 to exit): ")
                    if not name == "0":
                        try:
                            name = validate_name(name)
                            #Opening csv file in reading mode
                            with open("dataset.csv", "r", encoding="utf-8") as f:
                                reader = csv.reader(f)
                                a = 0
                                data = []
                                #Checking if name surname in rows
                                for row in reader:
                                    if name in row:
                                        a += 1
                                        data.append(row)
                                if a > 0:
                                #Writing students info
                                    print(" | ".join(fields))
                                    print(" | ".join(data))
                                    break
                                else:
                                    #If student not found in our database
                                    print(f"Student with name surname {name} not found in our database!")

                        except ValueError as e:
                            print(e)
                            break
                    else:
                        break
            else:
                while True:
                    roll = input("Enter students roll no (0 to exit): ")
                    if not all(char.isdigit() for char in roll):
                        print("Error: Students roll no must be all digits")
                        roll = input("Enter students roll no (0 to exit): ")
                    if not roll == "0":
                        with open("dataset.csv", "r", encoding="utf-8") as f:
                            reader = csv.reader(f)
                            a = 0
                            #Checking if roll no in rows
                            for row in reader:
                                if str(roll) in row:
                                    a += 1
                                    data = row
                            #If student is in our database
                            if a == 1:
                                #Writing students info
                                print(" | ".join(fields))
                                print(" | ".join(data))
                                break
                            else:
                                #If student not found in our database
                                print(f"Student with roll no. {roll} not found in our database!")
                    else:
                        break
        else:
            print("Invalid Input! Enter 1 or 2")

#Defining a function for Update Operation
def update_student():
    #Fields and database are global we can access them
    global fields
    global database

    operation = "Update Student operation"
    while True:
        value = input(f"Enter 1 to continue {operation} or 2 to exit: ")
        if value == "2":
            break
        elif value == "1":
            print("--- Update Student ---")
            while True:
                student_id = input("Enter student's student id to update (0 to exit): ")
                if len(student_id) != 9 and student_id != "0":
                    print("Error: Students ids length must be 9")
                    student_id = input("Enter student's student id to update (0 to exit): ")

                if student_id != "0":
                    found_student = False

                    with open(database, "r", encoding="utf-8") as file:
                        reader = csv.reader(file)
                        rows = list(reader)
                        for i, row in enumerate(rows):
                            if row[4] == str(student_id):
                                found_student = True
                                print("Student Found at index", i)
                                #Using validation function
                                updated_data = validation(fields)

                                # Checking if updated data is already in our database
                                new_id = updated_data[4]
                                new_email = updated_data[6]
                                new_phone = updated_data[7]
                                new_roll = updated_data[0]
                                for row in rows:
                                    if row != rows[i]:  # Skip the row we are updating
                                        if str(new_id) == row[4]:
                                            print("\nA student with the same student id already exists.")
                                            return
                                        elif str(new_email) == row[6]:
                                            print("\nA student with the same email already exists.")
                                            return
                                        elif str(new_roll) == row[0]:
                                            print("\nA student with the same roll no. already exists.")
                                            return
                                        elif str(new_phone) == row[7]:
                                            print("\nA student with the same phone number already exists.")
                                            return

                                # Update the data
                                rows[i] = updated_data

                                with open(database, 'w', newline='', encoding="utf-8") as file:
                                    writer = csv.writer(file)
                                    writer.writerows(rows)
                                print("Student Record Updated Successfully")

                                print("New data of student with id ", str(student_id), " is")
                                print(" | ".join(fields))
                                updated_data = [str(i) for i in updated_data]
                                print(" | ".join(updated_data))
                                break

                    if not found_student:
                        print("\nStudent not found in the database")
                else:
                    break
        else:
            print("Invalid Input! Enter 1 or 2")



#Creating a function for Delete Student Operation
def delete_student():
    #Fields and database ara global we can access them
    global fields
    global database

    operation = "Delete Student operation"
    print("--- Delete Student ---")
    while True:
        value = input(f"Enter 1 to continue {operation} or 2 to exit: ")
        if value == "2":
            break
        elif value == "1":
            while True:
                id = input("Enter students id to delete (0 to exit): ")
                if len(id) != 9 and id != "0":
                    print("Error: Students ids length must be 9")
                    id = input("Enter students id to delete (0 to exit): ")
                if id != "0":
                    #Will check if student found or not
                    student_found = False

                    #To append updated data
                    updated_data = []

                    #Opening csv file in reading mode
                    with open("dataset.csv", "r", encoding="utf-8") as f:
                        reader = csv.reader(f)
                        counter = 0

                        #Checking if student in our database
                        for row in reader:#Appending row if students roll no is not equal to users input
                                if str(id) != row[4]:
                                    updated_data.append(row)
                                    counter += 1
                                else:
                                    student_found = True

                    #Updating our csv file without deleted student

                    if student_found is True:
                        #Opening csv file in writing mode
                        with open(database, "w", newline="",encoding="utf-8") as f:
                            writer = csv.writer(f)
                            writer.writerows(updated_data)
                        print("Students id", id, "deleted successfully")

                    #If student not in our database
                    else:
                        print("Students id not found in our database")
                else:
                    break

        else:
            print("Invalid Input! Enter 1 or 2")


#Defining a function for Visualization Operation (Using Pandas Library)
def visualization():
    #Fields and database ara global we can access them
    global fields
    global database
    operation = "Visualization operation"
    print("--- Visualization ---")
    while True:
        value = input(f"Enter 1 to continue {operation} or 2 to exit: ")
        if value == "2":
            break
        elif value == "1":
            while True:
                #Asking user to which visualization they want
                print("Which visualization do you want to make?")
                print("1. Gender - Major (Recommended) ")
                print("2. Grade - Major (Recommended)")
                print("3. Gender - Grade (Recommended)")
                print("4. Age - Major (Recommended)")
                print("5. Average Grades and Success Graph by Majors (Recommended)")
                print("6. Average Grades and Success Graph by Gender (Recommended)")
                print("7. Male and Female Percentage (Recommended)")
                print("8. Major Percentage (Recommended)")
                print("9. Gender - Age Distribution (Recommended)")
                print("10. Gender and Major - Grade Distribution (Recommended)")
                print("11. Gender and Major - Age Distribution (Recommended)")
                print("12. Age Percentage (Recommended)")
                print("13. I want to choose fields and chart type (Warning! Visualizations may be meaningless)")


                choice = input("Enter your choice (0 to exit): ")
                if not choice == "0":
                    #Reading csv file with pandas
                    df = pd.read_csv(database)
                    #Removing Engineering part because it causes mess
                    df["Major"] = df["Major"].str.replace("Engineering","")
                    #Adjust figsize
                    plt.figure(figsize=(30,26))
                    #Adjusts the gap between the graphs and prevents them from intertwining.
                    plt.tight_layout()

                    #Adjusting x labels
                    plt.xticks(rotation=90)
                    plt.gca().tick_params(axis="x", length=0)

                    if choice == "1":
                        sns.countplot(x='Major', hue='Gender', data=df)
                        plt.title("Gender Distribution Across Majors",fontsize=24, fontweight='bold')
                        plt.xlabel("Major",fontsize=24, fontweight='bold')
                        plt.ylabel("Count",fontsize=24, fontweight='bold')
                        #Saves plot to your desktop or the file your .py file is in , dpi effects quality
                        plt.savefig("Gender_Major_Plot.png", dpi=300)
                        plt.show()
                    elif choice == "2":
                        sns.violinplot(x='Major', y='Grade', data=df)
                        plt.title("Grade Distribution Across Majors",fontsize=24, fontweight='bold')
                        plt.xlabel("Major",fontsize=24, fontweight='bold')
                        plt.ylabel("Grade",fontsize=24, fontweight='bold')
                        # Saves plot to your desktop or the file your .py file is in , dpi effects quality
                        plt.savefig('Grade_Major_Plot.png',dpi=300)
                        plt.show()
                    elif choice == "3":
                        sns.violinplot(x='Gender', y='Grade', data=df, palette="coolwarm")
                        plt.title("Grade Distribution by Gender",fontsize=24, fontweight='bold')
                        plt.xlabel("Gender",fontsize=24, fontweight='bold')
                        plt.ylabel("Grade",fontsize=24, fontweight='bold')
                        #Saves plot to your desktop or the file your .py file is in , dpi effects quality
                        plt.savefig('Gender_Grade_Plot.png',dpi=300)
                        plt.show()
                    elif choice == "4":
                        sns.boxplot(x='Major', y='Age', data=df)
                        plt.title("Age Distribution Across Majors",fontsize=24, fontweight='bold')
                        plt.xlabel("Major",fontsize=24, fontweight='bold')
                        plt.ylabel("Age",fontsize=24, fontweight='bold')
                        # Saves plot to your desktop or the file your .py file is in , dpi effects quality
                        plt.savefig('Age_Major_Plot.png')
                        plt.show()

                    elif choice == "5":
                        #Grouping by Major and we need Grades
                        major_averages = df.groupby(['Major'])['Grade'].mean().reset_index()

                        #Creating success graph
                        sns.violinplot(x="Major", y="Grade", data=df, palette="coolwarm")
                        plt.title("Average Grades and Success Graph by Majors",fontsize=24, fontweight='bold')
                        plt.xlabel("Major",fontsize=24, fontweight='bold')
                        plt.ylabel("Grade",fontsize=24, fontweight='bold')

                        #Shows average grades on the graph
                        for index, row in major_averages.iterrows():
                            plt.text(index, row['Grade'], f"{row['Grade']:.2f}", ha='center', va='bottom')
                        plt.savefig('average_grade_by_major.png')
                        plt.show()

                    elif choice == "6":
                        #Grouping by gender and we need Grades
                        gender_averages = df.groupby(["Gender"])['Grade'].mean().reset_index()

                        #Creating success graph
                        sns.violinplot(x="Gender", y="Grade", data=df, palette="coolwarm")
                        plt.title("Average Grades and Success Graph by Gender",fontsize=24, fontweight='bold')
                        plt.xlabel("Gender",fontsize=24, fontweight='bold')
                        plt.ylabel("Grade",fontsize=24, fontweight='bold')

                        #Shows average grades on the graph
                        for index, row in gender_averages.iterrows():
                            plt.text(index, row["Grade"], f"{row['Grade']:.2f}", ha='center', va='bottom')

                        plt.savefig('average_grade_by_gender.png')
                        plt.show()

                    elif choice == "7":
                        #Counting genders
                        gender_counts = df["Gender"].value_counts()

                        #Creating pie plot
                        plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.2f%%', startangle=140, colors=sns.color_palette("pastel"))

                        plt.title("Gender Distribution",fontsize=24, fontweight='bold')
                        plt.savefig('gender_distribution.png')
                        plt.show()

                    elif choice == "8":
                        #Counting Majors
                        major_counts = df["Major"].value_counts()

                        #Creating pie plot
                        plt.pie(major_counts, labels = major_counts.index, autopct='%1.2f%%', startangle=140, colors=sns.color_palette("pastel"))

                        plt.title("Major Distribution",fontsize=24, fontweight='bold')
                        plt.savefig("major_distribution.png")
                        plt.show()
                    elif choice == "9":
                        #Creating plot
                        sns.violinplot(x="Gender",y = "Age", data=df)
                        plt.title("Gender - Age Distribution",fontsize=24, fontweight='bold')
                        plt.xlabel("Gender",fontsize=24, fontweight='bold')
                        plt.ylabel("Age",fontsize=24, fontweight='bold')
                        plt.savefig("gender_age_distribution.png")
                        plt.show()
                    elif choice == "10":
                        #Creating plot
                        sns.violinplot(x = "Major", y = "Age", data=df, hue="Gender", palette="pastel")
                        plt.title('Major - Age and Gender Distribution',fontsize=24, fontweight='bold')
                        plt.xlabel("Major",fontsize=24, fontweight='bold')
                        plt.ylabel("Age",fontsize=24, fontweight='bold')
                        plt.savefig("major_age_gender_distribution.png")
                        plt.show()
                    elif choice == "11":
                        #Creating plot
                        sns.violinplot(x="Major", y = "Grade", hue="Gender", data=df, palette="pastel")
                        plt.title('Gender and Major - Grade Distribution',fontsize=24, fontweight='bold')
                        plt.xlabel("Major",fontsize=24, fontweight='bold')
                        plt.ylabel("Grade",fontsize=24, fontweight='bold')
                        plt.savefig("major_grade_gender_distribution.png")
                        plt.show()
                    #Age Percentage
                    elif choice == "12":
                        age = df["Age"].value_counts()
                        plt.title("Age Percentage",fontsize=24, fontweight='bold')
                        plt.pie(age,labels = age.index,autopct='%1.2f%%', startangle=140, colors=sns.color_palette("pastel"))
                        plt.savefig("age_percentage.png")
                        plt.show()
                    #User chooses fields and chart type
                    elif choice == "13":
                        #Asking user to choose fields
                        print("Choose fields for visualization:")
                        #Taking index and value and starting it with 1
                        for index, field in enumerate(fields,start=1):
                            print(f"{index}. {field}")

                        selected_fields = []
                        while True:
                            try:
                                choice = int(input("Enter 2 field number to visualize: "))
                                if choice == 0:
                                    #There should be 2 fields
                                    if len(selected_fields) != 2:
                                        raise ValueError("You must select exactly two fields.")
                                    else:
                                        break
                                #You can not select 0 or 1 field and more than in fields list
                                elif choice < 1 or choice > len(fields):
                                    raise ValueError("Invalid field number")

                                selected_field = fields[choice-1]
                                selected_fields.append(selected_field)
                                if len(selected_fields) == 2:
                                    break
                            except ValueError as e:
                                print(f"Error: {e}")

                        while True:
                            #Asking user select a chart type
                            print("Choose chart type:")
                            print("1. Count Plot")
                            print("2. Bar Plot")
                            print("3. Box Plot")
                            print("4. Violin Plot")
                            print("5. Scatter Plot")
                            print("6. Histogram")
                            print("7. Distribution Plot")
                            print("8. Line Plot")
                            chart_type = input("Enter chart type number: ")
                            #Adjusting the figure size
                            plt.figure(figsize=(12, 8))


                            if chart_type == "1":
                                if len(selected_fields) == 2:
                                    #Creating a countplot selected fields
                                    plt.subplot(2,1,1)
                                    sns.countplot(x=selected_fields[0], hue=selected_fields[1], data=df)
                                    plt.title(f"Count Plot of {selected_fields[0]} by {selected_fields[1]}",fontsize=24, fontweight='bold')
                                    plt.xlabel(selected_fields[0],fontsize=24, fontweight='bold')
                                    plt.ylabel("Count",fontsize=24, fontweight='bold')

                                    #Creating a countplot selected fields
                                    plt.subplot(2,1,2)
                                    sns.countplot(x=selected_fields[1], hue=selected_fields[0], data=df)
                                    plt.title(f"Count Plot of {selected_fields[1]} by {selected_fields[0]}",fontsize=24, fontweight='bold')
                                    plt.xlabel(selected_fields[1],fontsize=24, fontweight='bold')
                                    plt.ylabel("Count",fontsize=24, fontweight='bold')

                                    # Saves plot to your desktop or the file your .py file is in , dpi effects quality
                                    plt.savefig(f'{field[0]}_{field[1]}_cplot.png')
                                    plt.tight_layout()
                                    # Show the plot
                                    plt.show()
                                    break
                            elif chart_type == "2":
                                if len(selected_fields) == 2:
                                    #Creating a barplot selected fields 0 to 1
                                    plt.subplot(2,1,1)
                                    sns.barplot(x=selected_fields[0], y=selected_fields[1], data=df)
                                    plt.title(f"Bar Plot of {selected_fields[1]} by {selected_fields[0]}",fontsize=24, fontweight='bold')
                                    plt.xlabel(selected_fields[0],fontsize=24, fontweight='bold')
                                    plt.ylabel(selected_fields[1],fontsize=24, fontweight='bold')

                                    #Creating a barplot selected fields 1 to 0
                                    plt.subplot(2,1,2)
                                    sns.barplot(x=selected_fields[1], y=selected_fields[0], data=df)
                                    plt.title(f"Bar Plot of {selected_fields[0]} by {selected_fields[1]}",fontsize=24, fontweight='bold')
                                    plt.xlabel(selected_fields[1],fontsize=24, fontweight='bold')
                                    plt.ylabel(selected_fields[0],fontsize=24, fontweight='bold')

                                    # Saves plot to your desktop or the file your .py file is in , dpi effects quality
                                    plt.savefig(f'{field[0]}_{field[1]}_barplot.png')
                                    plt.tight_layout()
                                    # Show the plot
                                    plt.show()
                                    break
                            elif chart_type == "3":
                                if len(selected_fields) == 2:
                                    #Creating a boxplot selected fields 0 to 1
                                    plt.subplot(2,1,1)
                                    sns.boxplot(x=selected_fields[0], y=selected_fields[1], data=df)
                                    plt.title(f"Box Plot of {selected_fields[1]} by {selected_fields[0]}",fontsize=24, fontweight='bold')
                                    plt.xlabel(selected_fields[0],fontsize=24, fontweight='bold')
                                    plt.ylabel(selected_fields[1],fontsize=24, fontweight='bold')

                                    #Creating a boxplot selected fields 1 to 0
                                    plt.subplot(2,1,2)
                                    sns.boxplot(x=selected_fields[1], y=selected_fields[0], data=df)
                                    plt.title(f"Box Plot of {selected_fields[0]} by {selected_fields[1]}",fontsize=24, fontweight='bold')
                                    plt.xlabel(selected_fields[1],fontsize=24, fontweight='bold')
                                    plt.ylabel(selected_fields[0],fontsize=24, fontweight='bold')

                                    # Saves plot to your desktop or the file your .py file is in , dpi effects quality
                                    plt.savefig(f'{field[0]}_{field[1]}_boxplot.png')
                                    plt.tight_layout()
                                    # Show the plot
                                    plt.show()
                                    break
                            elif chart_type == "4":
                                if len(selected_fields) == 2:
                                    #Creating a violinplot with selected fields 0 to 1
                                    plt.subplot(2,1,1)
                                    sns.violinplot(x=selected_fields[0], y=selected_fields[1], data=df)
                                    plt.title(f"Violin Plot of {selected_fields[1]} by {selected_fields[0]}",fontsize=24, fontweight='bold')
                                    plt.xlabel(selected_fields[0],fontsize=24, fontweight='bold')
                                    plt.ylabel(selected_fields[1],fontsize=24, fontweight='bold')

                                    #Creating a violinplot with selected fields 1 to 0
                                    plt.subplot(2,1,2)
                                    sns.violinplot(x=selected_fields[1], y=selected_fields[0], data=df)
                                    plt.title(f"Violin Plot of {selected_fields[0]} by {selected_fields[1]}",fontsize=24, fontweight='bold')
                                    plt.xlabel(selected_fields[1],fontsize=24, fontweight='bold')
                                    plt.ylabel(selected_fields[0],fontsize=24, fontweight='bold')

                                    # Saves plot to your desktop or the file your .py file is in , dpi effects quality
                                    plt.savefig(f'{field[0]}_{field[1]}_violinplot.png')
                                    plt.tight_layout()
                                    # Show the plot
                                    plt.show()
                                    break
                            elif chart_type == "5":
                                if len(selected_fields) == 2:
                                    #Creating a scatterplot with selected fields 0 to 1
                                    plt.subplot(2, 1, 1)
                                    sns.scatterplot(x=selected_fields[0], y=selected_fields[1], data=df)
                                    plt.title(f"Scatter Plot of {selected_fields[1]} by {selected_fields[0]}",fontsize=24, fontweight='bold')
                                    plt.xlabel(selected_fields[0],fontsize=24, fontweight='bold')
                                    plt.ylabel(selected_fields[1],fontsize=24, fontweight='bold')

                                    #Creating a scatterplot with selected fields 1 to 0
                                    plt.subplot(2, 1, 2)
                                    sns.scatterplot(x=selected_fields[1], y=selected_fields[0], data=df)
                                    plt.title(f"Scatter Plot of {selected_fields[0]} by {selected_fields[1]}",fontsize=24, fontweight='bold')
                                    plt.xlabel(selected_fields[1],fontsize=24, fontweight='bold')
                                    plt.ylabel(selected_fields[0],fontsize=24, fontweight='bold')

                                    # Saves plot to your desktop or the file your .py file is in , dpi effects quality
                                    plt.savefig(f'{field[0]}_{field[1]}_scatterplot.png')
                                    plt.tight_layout()
                                    # Show the plot
                                    plt.show()
                                    break
                            elif chart_type == "6":
                                if len(selected_fields) == 2:
                                    #For first field
                                    #Creating a histplot
                                    plt.subplot(2, 1, 1)
                                    plt.hist(df[selected_fields[0]], bins=20)
                                    plt.title(f"Histogram of {selected_fields[0]}",fontsize=24, fontweight='bold')
                                    plt.xlabel(selected_fields[0],fontsize=24, fontweight='bold')
                                    plt.ylabel("Frequency",fontsize=24, fontweight='bold')

                                    #For second field
                                    #Creating a histplot
                                    plt.subplot(2, 1, 2)
                                    plt.hist(df[selected_fields[1]], bins=20)
                                    plt.title(f"Histogram of {selected_fields[1]}",fontsize=24, fontweight='bold')
                                    plt.xlabel(selected_fields[1],fontsize=24, fontweight='bold')
                                    plt.ylabel("Frequency",fontsize=24, fontweight='bold')

                                    plt.tight_layout()
                                    # Saves plot to your desktop or the file your .py file is in , dpi effects quality
                                    plt.savefig(f'{field[0]}_{field[1]}_histplot.png')
                                    # Show the plot
                                    plt.show()
                                    break
                            elif chart_type == "7":
                                if len(selected_fields) == 2:
                                    #For first field
                                    #Creating a dist plot
                                    plt.subplot(2, 1, 1)
                                    sns.histplot(df[selected_fields[0]], kde=True)
                                    plt.title(f"Distribution Plot of {selected_fields[0]}",fontsize=24, fontweight='bold')
                                    plt.xlabel(selected_fields[0],fontsize=24, fontweight='bold')
                                    plt.ylabel("Density",fontsize=24, fontweight='bold')

                                    plt.subplot(2, 1, 2)
                                    sns.histplot(df[selected_fields[1]], kde=True)
                                    plt.title(f"Distribution Plot of {selected_fields[1]}",fontsize=24, fontweight='bold')
                                    plt.xlabel(selected_fields[1],fontsize=24, fontweight='bold')
                                    plt.ylabel("Density",fontsize=24, fontweight='bold')

                                    # Saves plot to your desktop or the file your .py file is in , dpi effects quality
                                    plt.savefig(f'{field[0]}_{field[1]}_distplot.png')
                                    plt.tight_layout()
                                    # Show the plot
                                    plt.show()
                                    break
                            elif chart_type == "8":
                                if len(selected_fields) == 2:
                                    #Creating a line plot with selected fields 0 to 1
                                    plt.subplot(2, 1, 1)
                                    sns.lineplot(x=selected_fields[0], y=selected_fields[1], data=df)
                                    plt.title(f"Line Plot of {selected_fields[1]} by {selected_fields[0]}",fontsize=24, fontweight='bold')
                                    plt.xlabel(selected_fields[0],fontsize=24, fontweight='bold')
                                    plt.ylabel(selected_fields[1],fontsize=24, fontweight='bold')

                                    #Creating a line plot with selected fields 1 to 0
                                    plt.subplot(2, 1, 2)
                                    sns.lineplot(x=selected_fields[1], y=selected_fields[0], data=df)
                                    plt.title(f"Line Plot of {selected_fields[0]} by {selected_fields[1]}",fontsize=24, fontweight='bold')
                                    plt.xlabel(selected_fields[1],fontsize=24, fontweight='bold')
                                    plt.ylabel(selected_fields[0],fontsize=24, fontweight='bold')

                                    # Saves plot to your desktop or the file your .py file is in , dpi effects quality
                                    plt.savefig(f'{field[0]}_{field[1]}_lineplot.png')
                                    plt.tight_layout()
                                    # Show the plot
                                    plt.show()
                                    break
                            else:
                                print("Error: Invalid chart type.")
                    else:
                        print("Error: Invalid Input! Please enter a number between 1-12")
                else:
                    break
        else:
            print("Invalid Input! Enter 1 or 2")



#Defining a function for Student Statistics (Using Pandas library)
def student_statistics():
    #Fields and database ara global we can access them
    global fields
    global database

    operation = "Student Statistics"
    #Reading database with pandas
    data = pd.read_csv(database)
    print("--- Student Statistics ---")
    while True:
        value = input(f"Enter 1 to see {operation} or 2 to exit: ")
        if value == "2":
            break
        elif value == "1":
            while True:
                #Asking user to select a statistic
                print("Which statistics do you want to see?")
                print("1. Number of Students")
                print("2. Number of Male-Female Students")
                print("3. Number of Students in a Specific Major")
                print("4. Number of Male-Female Students in a Specific Major")
                print("5. Average Grade of Students")
                print("6. Average Grade of Students by their Gender")
                print("7. Average Grade of Students in a Specific Major")
                print("8. Average Grade of Male-Female Students in a Specific Major")
                print("9. Average Age of Students")
                print("10. Average Age of Male-Female Students")
                print("11. Average Age of Students in Specific Major")
                print("12. Average Age of Male-Female Students in Specific Major")

                choice = input("Enter your choice (0 to exit): ")
                if not choice == "0":

                    #Num of studetns
                    if choice == "1":
                        num_students = len(data)
                        print("Number of Students: ",num_students)
                        break
                    #Num of male-female students
                    elif choice == "2":
                        male_students = len(data[data["Gender"] == "Male"])
                        female_students = len(data[data["Gender"] == "Female"])
                        print("Number of Male Students: ",male_students)
                        print("Number of Female Students: ",female_students)
                        break
                    #Num of students in specific major
                    elif choice == "3":
                        print("Which major students do you want to see?")

                        # Gets unique major values from the dataset
                        with open(database, 'r', encoding="utf-8") as file:
                            lines = file.readlines()
                        majors = set([line.split(',')[-1].strip() for line in lines[1:]])

                        # Printing major options
                        for idx, major in enumerate(majors, start=1):
                            print(f"{idx}. {major}")
                        # Asking which major they want to see
                        major_choice = input("Enter the number of the major you want to see: ")

                        # User selects a number
                        if major_choice.isdigit() and 1 <= int(major_choice) <= len(majors):
                            selected_major = list(majors)[int(major_choice) - 1]
                        #Number of students in selected major
                        major_students = len(data[data["Major"] == selected_major])

                        print(f"Number of students in {selected_major}: ",major_students)
                        break
                    #Num of female-male students in specific major
                    elif choice == "4":
                        print("Which major students do you want to see? (Male Female Students)")
                        # Gets unique major values from the dataset
                        with open(database, 'r', encoding="utf-8") as file:
                            lines = file.readlines()
                        majors = set([line.split(',')[-1].strip() for line in lines[1:]])

                        # Printing major options
                        for idx, major in enumerate(majors, start=1):
                            print(f"{idx}. {major}")
                        # Asking which major they want to see
                        major_choice = input("Enter the number of the major you want to see: ")

                        # User selects a number
                        if major_choice.isdigit() and 1 <= int(major_choice) <= len(majors):
                            selected_major = list(majors)[int(major_choice) - 1]


                        number_male = len(data[(data["Gender"] == "Male") & (data["Major"] == selected_major)])
                        number_female = len(data[(data["Gender"] == "Female") & (data["Major"] == selected_major)])

                        print(f"Number of Male Students in {selected_major}: ", number_male)
                        print(f"Number of Female Students in {selected_major}: ", number_female)
                        break
                    #Average Grade
                    elif choice == "5":
                        av_grade = data["Grade"].mean()
                        print("Average Grade of Students: ", f"{av_grade:.2f}")
                        break
                    #Average grade of male-female students
                    elif choice == "6":
                        av_grade_male = data[data["Gender"] == "Male"]["Grade"].mean()
                        av_grade_female = data[data["Gender"] == "Female"]["Grade"].mean()
                        print("Average Grade of Male Students: ", f"{av_grade_male:.2f}")
                        print("Average Grade of Female Students: ",f"{av_grade_female:.2f}")
                        break
                    #Average Grade in specific major
                    elif choice == "7":
                        print("Which major students do you want to see?")

                        # Gets unique major values from the dataset
                        with open(database, 'r', encoding="utf-8") as file:
                            lines = file.readlines()
                        majors = set([line.split(',')[-1].strip() for line in lines[1:]])

                        # Printing major options
                        for idx, major in enumerate(majors, start=1):
                            print(f"{idx}. {major}")
                        # Asking which major they want to see
                        major_choice = input("Enter the number of the major you want to see: ")

                        # User selects a number
                        if major_choice.isdigit() and 1 <= int(major_choice) <= len(majors):
                            selected_major = list(majors)[int(major_choice) - 1]

                        major_average = data[data["Major"] == selected_major]["Grade"].mean()
                        print(f"Average Grade of Students in {selected_major}: {major_average:.2f}")
                        break
                    #Average Grade of Male-Female Students in Specific Major
                    elif choice == "8":
                        print("Which major students do you want to see?")

                        # Gets unique major values from the dataset
                        with open(database, 'r', encoding="utf-8") as file:
                            lines = file.readlines()
                        majors = set([line.split(',')[-1].strip() for line in lines[1:]])

                        # Printing major options
                        for idx, major in enumerate(majors, start=1):
                            print(f"{idx}. {major}")
                        # Asking which major they want to see
                        major_choice = input("Enter the number of the major you want to see: ")

                        # User selects a number
                        if major_choice.isdigit() and 1 <= int(major_choice) <= len(majors):
                            selected_major = list(majors)[int(major_choice) - 1]

                        avg_male = data[(data["Major"] == selected_major) & (data["Gender"] == "Male")]["Grade"].mean()
                        avg_female = data[(data["Major"] == selected_major) & (data["Gender"] == "Female")]["Grade"].mean()
                        #If avg_female == nan
                        if not avg_female >= 0:
                            avg_female = "No Female Student"
                            print(f"Average Grade of Male Students in {selected_major}: {avg_male:.2f} ")
                            print(f"Average Grade of Female Students in {selected_major}: {avg_female}")
                        elif not avg_male >= 0:
                            avg_male = "No Male Student"
                            print(f"Average Grade of Male Students in {selected_major}: {avg_male} ")
                            print(f"Average Grade of Female Students in {selected_major}: {avg_female:.2f}")
                        else:
                            print(f"Average Grade of Male Students in {selected_major}: {avg_male:.2f} ")
                            print(f"Average Grade of Female Students in {selected_major}: {avg_female:.2f}")
                        break
                    #Average age
                    elif choice == "9":
                        avg_age = data["Age"].mean()
                        print("Average Age of Students: ", f"{avg_age:.2f}")
                        break
                    #Average age of female-male students
                    elif choice == "10":
                        avg_age_male = data[data["Gender"] == "Male"]["Age"].mean()
                        avg_age_female = data[data["Gender"] == "Female"]["Age"].mean()
                        print("Average Age of Male Students: ", f"{avg_age_male:.2f}")
                        print("Average Age of Female Students: ", f"{avg_age_female:.2f}")
                        break
                    #Average age in specific major
                    elif choice == "11":
                        print("Which major students do you want to see?")

                        # Gets unique major values from the dataset
                        with open(database, 'r', encoding="utf-8") as file:
                            lines = file.readlines()
                        majors = set([line.split(',')[-1].strip() for line in lines[1:]])

                        # Printing major options
                        for idx, major in enumerate(majors, start=1):
                            print(f"{idx}. {major}")
                        # Asking which major they want to see
                        major_choice = input("Enter the number of the major you want to see: ")

                        # User selects a number
                        if major_choice.isdigit() and 1 <= int(major_choice) <= len(majors):
                            selected_major = list(majors)[int(major_choice) - 1]

                        avg_age_major = data[data["Major"] == selected_major]["Age"].mean()
                        print(f"Average Age of Students in {selected_major}:", f"{avg_age_major:.2f}")
                        break
                    #Average age of male-female students in specific major
                    elif choice == "12":
                        print("Which major students do you want to see?")

                        with open(database, 'r', encoding="utf-8") as file:
                            lines = file.readlines()
                        majors = set([line.split(',')[-1].strip() for line in lines[1:]])

                        # Printing major options
                        for idx, major in enumerate(majors, start=1):
                            print(f"{idx}. {major}")
                        # Asking which major they want to see
                        major_choice = input("Enter the number of the major you want to see: ")
                        # User selects a number
                        if major_choice.isdigit() and 1 <= int(major_choice) <= len(majors):
                            selected_major = list(majors)[int(major_choice) - 1]

                        avg_m_major = data[(data["Major"] == selected_major) & (data["Gender"] == "Male")]["Age"].mean()
                        avg_f_major = data[(data["Major"] == selected_major) & (data["Gender"] == "Female")]["Age"].mean()

                        print(f"Average Age of Male students in {selected_major}: {avg_m_major:.2f} ")
                        print(f"Average Age of Female students in {selected_major}: {avg_f_major:.2f}")
                        break
                    else:
                        print("Invlaid Input! Choose a number between 1 and 12")
                else:
                    break
        else:
            print("Invalid Input! Choose 1 or 2")
#Offers choices to user while
while True:
    console_menu()

    choice = input("Enter your choice: ")
    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    elif choice == "6":
        visualization()
    elif choice == "7":
        student_statistics()
    elif choice == "8":
        break
    else:
        print("--- Invalid input ---")
print("-------------------------------")
print(" Thank you for using our system")
print("-------------------------------")
