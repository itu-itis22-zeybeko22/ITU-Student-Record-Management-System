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

#Listing Majors to prevent add non-existing majors (they are all lowercase because it will make it easier to check)
itu_majors = ["computer engineering","composing","mineral processing engineering","instrument training","environmental engineering","maritime transportation management engineering",
          "economy","electrical engineering","chemical engineering","electronics and communications engineering","industrial engineering","industrial products engineering",
          "physics engineering","naval construction and ship machinery engineering","ship machinery management engineering","ship and marine technology engineering",
          "geomatic engineering","food engineering","interior architecture","manufacturing engineering","civil engineering","management engineering","geophysical engineering",
          "geological engineering","chemical","control and automation engineering","mining engineering","mechanical engineering","mathematics engineering","metallurgy and materials engineering",
          "meteorological engineering","architecture","molecular biology and genetics","fashion design","music technology","music theory","musicology","petroleum and natural gas engineering",
          "landscape architecture","voice training","city and region planning","textile engineering","textile development and marketing","turkish folk dances","aircraft engineering",
          "astronautical engineering","artificial intelligence and data engineering"]
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
    print("7. Quit")

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
    # Null name is invalid
    if not major:
        raise ValueError("Error: Invalid name! Major shouldn't be empty")
    #No special characters are allowed or no numbers are allowed in the major
    elif not all(char.isalpha() or char.isspace() for char in major):
        raise ValueError("Error: Invalid name! Major should only include letters or space")
    #Major should be in itu_majors
    elif major.lower() not in itu_majors:
        raise ValueError("Error: Invalid major! The Major you entered not in ITU or it's written wrong")
    else:
        formatted_major = ' '.join(word.capitalize() for word in major.split())
        return formatted_major
#Defining a function for Add New Student operation
def add_student():
    #Fields and database ara global we can access them
    global fields
    global database

    #Add Information
    print("-------------------------")
    print("Add Student Information")
    print("-------------------------")
    #Creating a list to store inputs

    student_data = []
    while True:
        for field in fields:
            value = input("Enter " + field + ": ")
            #In ITU grades are between 0 and 4 so checking if grade is between 0 and 4
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
            #Age should be >= 17
            elif field == "Age":
                while True:
                    try:
                        value = int(value)
                        if 17 <= value <= 100:
                            break
                        else:
                            raise ValueError
                    except ValueError:
                        print("Error: Age should be between 17 and 100")
                        value = input("Enter " + field + ": ")
            #Checking if roll no. and students id is integer
            elif field == "Roll no." or field == "Students id":
                while True:
                    try:
                        value = int(value)
                        #Roll no must be bigger or equal to 1
                        if field == "Roll no.":
                            if value < 1:
                                raise ValueError("Error : Roll no. is less than 1")
                        #Students id length must be 9
                        if field == "students id" and len(str(value)) != 9:
                            raise ValueError("Error: Student ID length should be 9.")
                        break
                    except ValueError as e:
                        print(e)
                        value = input("Enter " + field + ": ")
            #Length of Phone number must be equal to 11
            elif field == "Phone":
                while True:
                    try:
                        value = int(value)
                        if len(str(value)) == 10:
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
            #Appending Data
            student_data.append(value)
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
        input("Press any key to continue")
        return

#Defining a function for View Students Operation
def view_students():
    #Fields and database ara global we can access them
    global fields
    global database

    print("--- Student Records ---")
    #Asking user to how they want to see datas
    print("Which way do you want to see students?")
    print("1. As It is in Database")
    print("2. By their Roll Numbers")
    print("3. By their Gender")
    print("4. By their Major")
    print("5. By their Grades")
    print("6. By Alphabetic Order")

    while True:
        choice = input("Enter your choice: ")

        #For choice 1
        if choice == "1":
            #Opening csv file in reading mode
            with open("dataset.csv", "r", encoding="utf-8") as f:
                reader = csv.reader(f)

                for row in reader:
                    for item in row:
                        print(item, end=" | ")
                    print("\n")
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
        #For choice 3
        elif choice == "3":
            print("Which gender students do you want to see?")
            print("1. Male")
            print("2. Female")
            print("\n")
            gen = input("Enter your choice: ")
            
            if gen == "1":
                for item in fields:
                    print(item, end=" | ")
                print("\n")
                with open("dataset.csv", "r", encoding="utf-8") as f:
                    reader = csv.reader(f)
                    #Writing Male Students
                    for row in reader:
                        if "Male" in row:
                            for item in row:
                                print(item, end=" | ")
                            print("\n")
            elif gen == "2":
                for item in fields:
                    print(item, end=" | ")
                print("\n")
                with open("dataset.csv", "r", encoding="utf-8") as f:
                    reader = csv.reader(f)
                    #Writing female students
                    for row in reader:
                        if "Female" in row:
                            for item in row:
                                print(item, end=" | ")
                            print("\n")
            else:
                print("Invalid Input! Enter 1 or 2.")
                continue
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

            #Asking which major they want to see
            major_choice = input("Enter the number of the major you want to see: ")
            
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
            else:
                print("Invalid Input! Please enter a valid number.")
                continue
        #Sorting By Grade
        elif choice == "5":

            print("How do you want to sort students by grades?")
            print("1. Ascending Order")
            print("2. Descending Order")
            sort_choice = input("Enter your choice: ")

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
            #If choice is not equal to 1 or 2
            else:
                print("Invalid Input! Enter 1 or 2.")
                continue
        #Sorting by Alphabetic Order
        
        elif choice == "6":
            print("Which Alphabet Ordering Do You Want?")
            print("1.Turkish")
            print("2.English")
            w = input("Enter your choice: ")

            if w == "1":
                print("\n")
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
            elif w == "2":
                print("\n")
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
            else:
                print("Invalid Input! Enter 1 or 2")
                continue
        else:
            print("Invalid Input! Choose 1, 2, 3, 4, 5 or 6")
            continue
        break
        
    input("Press any key to continue")
 
 #Defining a function for Search Student Operation
def search_student():
    #Fields and database ara global we can access them
    global fields
    global database

    #Offering options to user
    print("\n")
    print("--- Search Student ---")
    print("1. Search by Students Id")
    print("2. Search by Name Surname (There may be more than one student with same name surname)")
    print("3. Search by Roll No.")

    #Getting input
    choice = input("Enter your choice: ")

    while choice not in ["1", "2", "3"]:
        print("Invalid input. Please enter 1, 2 or 3.")
        choice = input("Enter your choice: ")

    if choice == "1":

        while True:
            id = input("Enter students id: ")

            #Checking length of id
            if len(id) != 9:
                print("Error: Students ids length must be 9")
                continue
            #It must start with 1 or 9
            elif not str(id).startswith(('1', '9')):
                print("Error: Students id must start with 1 or 9 (9 for foreigner students)")
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
                    print("\n")     
                #Writing students info
                    for field in fields:
                        if field == fields[-1]:
                            print(str(field) + "|")
                        else:
                            print(str(field), end="|")
                    for i in data:
                        print(i, end="|")
                    print("\n")
                    break
                else:
                    #If student not found in our database
                    print(f"Student with students id {id} not found in our database!")
                    continue

    elif choice == "2":
        while True:
            #Using same function in add_student to validate name
            name = input("Enter students name surname: ")
            try:
                name = validate_name(name)
                break
            except ValueError as e:
                print(e)
            #Opening csv file in reading mode
            with open("dataset.csv", "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                a = 0
                #Checking if name surname in rows
                for row in reader:
                    if str(name) in row:
                        a += 1
                        data = row
                if a == 1:     
                    print("\n")
                #Writing students info
                    for field in fields:
                        if field == fields[-1]:
                            print(str(field) + "|")
                        else:
                            print(str(field), end="|")
                    for i in data:
                        print(i, end="|")
                    print("\n")
                    break
                else:
                    #If student not found in our database
                    print(f"Student with name surname {name} not found in our database!")
                    continue
    else:
        roll = input("Enter students roll no: ")
        while True:
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
                    print("\n")     
                #Writing students info
                    for field in fields:
                        if field == fields[-1]:
                            print(str(field) + "|")
                        else:
                            print(str(field), end="|")
                    for i in data:
                        print(i, end="|")
                    print("\n")
                    break
                else:
                    #If student not found in our database
                    print(f"Student with roll no. {roll} not found in our database!")
                    continue

    input("Press any key to continue")

#Defining a function for Update Operation
def update_student():
    #Fields and database ara global we can access them
    global fields
    global database

    while True:
        print("\n")
        print("--- Update Student ---")
        #Roll no. of
        student_id = input("Enter student's students id to update or enter 1 to break: ")
        #New data of student
        updated_data = []
        # Will use at if student found or not
        found_student = False

        #To break
        if student_id == "1":
            break
        #Opening dataset in writing mode
        with open(database, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            #Checking student and doing the same operations add_student does
            for row in reader:
                    if row[4] == str(student_id):
                        found_student = True
                        print("Student Found at index", reader.line_num-1)
                        x = reader.line_num-1
                        for field in fields:
                            value = input("Enter " + field + ": ")
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
                            elif field == "Age":
                                while True:
                                    try:
                                        value = int(value)
                                        if value >= 17:
                                            break
                                        else:
                                            raise ValueError
                                    except ValueError:
                                        print("Error: Please enter an integer greater than or equal to 17")
                                        value = input("Enter " + field + ": ")
                            elif field == "Roll no." or field == "Students id":
                                while True:
                                    try:
                                        value = int(value)
                                        if field == "students id" and len(str(value)) != 9:
                                            raise ValueError("Error: Student ID length should be 9.")
                                        break
                                    except ValueError:
                                        print("Error: Please enter a valid", field)
                                        value = input("Enter " + field + ": ")
                            elif field == "Phone":
                                while len(value) != 11:
                                    print("Error: Phone number should be 11 characters long.")
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
                                while value.lower() not in ["male", "female"]:
                                    print("Error: Gender should be Male or Female")
                                    value = input("Enter " + field + ": ").lower()
                                value = value.title()
                            elif field == "Name":
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
                            updated_data.append(value)

                    #Checking if updated data in our database
                    if len(updated_data) == 9:
                        new_id = updated_data[4]
                        new_email = updated_data[6]
                        new_phone = updated_data[7]
                        new_roll = updated_data[0]
                        #Opening csv file in reading mode
                        with open(database, "r", encoding="utf-8") as f:
                            reader = csv.reader(f)
                            for row in reader:
                                #We should skip the row that we update
                                if str(student_id) not in row:
                                    if str(new_id) in row:
                                        print("\n")
                                        print("A student with the same student id already exists.")
                                        return
                                    elif str(new_email) in row:
                                        print("\n")
                                        print("A student with the same email already exists.")
                                        return
                                    elif str(new_roll) in row:
                                        print("\n")
                                        print("A student with the same roll no. already exists.")
                                        return
                                    elif str(new_phone) in row:
                                        print("\n")
                                        print("A student with the same phone number already exists")
                                        return


        #If student is in our database
        if found_student:
            print("\n")
            with open(database, 'r', newline='',encoding="utf-8") as file:
                reader = csv.reader(file)
                rows = list(reader)
                #Changing the old data to new data
                rows[x] = updated_data
                with open(database, 'w', newline='',encoding="utf-8") as file:
                    writer = csv.writer(file)
                    writer.writerows(rows)
            print("Student Record Updated Successfully")
            updated_data = [str(i) for i in updated_data]

            print("New data of student with id ", str(student_id), " is")
            for i in fields:
                print(i,end=" | ")
            print("\n")
            print(" | ".join(updated_data))
        #If student is not in our database
        else:
            print("\n")
            print("Student not found in the database")
            continue
        break
    input("Press any key to continue")



#Creating a function for Delete Student Operation
def delete_student():
    #Fields and database ara global we can access them
    global fields
    global database

    while True:
        print("--- Delete Student ---")
        id = input("Enter students id to delete: ")

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
                    if str(id) not in row:
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
            continue
        break
    input("Press any key to continue")

#Defining a function for Visualization Operation
def visualization():
    #Fields and database ara global we can access them
    global fields
    global database
    #Asking user to which visualization they want
    print("Which visualization do you want to make?")
    print("1. Gender - Major (Recommended) ")
    print("2. Grade - Major (Recommended)")
    print("3. Gender - Grade (Recommended)")
    print("4. Age - Major (Recommended)")
    print("5. Average Grades and Success Graph by Majors")
    print("6. Average Grades and Success Graph by Gender")
    print("7. I want to choose fields and chart type (Warning! Visualizations may be meaningless)")

    while True:
        choice = input("Enter your choice: ")

        #Reading csv file with pandas
        df = pd.read_csv(database)
        #Adjust figsize
        plt.figure(figsize=(24,18))
        #Adjusts the gap between the graphs and prevents them from intertwining.
        plt.tight_layout()
        if choice == "1":
            sns.countplot(x='Major', hue='Gender', data=df)
            plt.title("Gender Distribution Across Majors")
            plt.xlabel("Major")
            plt.ylabel("Count")
            #Saves plot to your desktop or the file your .py file is in , dpi effects quality
            plt.savefig("Gender_Major_Plot.png", dpi=300)
            plt.show()
        elif choice == "2":
            sns.violinplot(x='Major', y='Grade', data=df)
            plt.title("Grade Distribution Across Majors")
            plt.xlabel("Major")
            plt.ylabel("Grade")
            # Saves plot to your desktop or the file your .py file is in , dpi effects quality
            plt.savefig('Grade_Major_Plot.png',dpi=300)
            plt.show()
        elif choice == "3":
            sns.violinplot(x='Gender', y='Grade', data=df, palette="coolwarm")
            plt.title("Grade Distribution by Gender")
            plt.xlabel("Gender")
            plt.ylabel("Grade")
            #Saves plot to your desktop or the file your .py file is in , dpi effects quality
            plt.savefig('Gender_Grade_Plot.png',dpi=300)
            plt.show()
        elif choice == "4":
            sns.boxplot(x='Major', y='Age', data=df)
            plt.title("Age Distribution Across Majors")
            plt.xlabel("Major")
            plt.ylabel("Age")
            # Saves plot to your desktop or the file your .py file is in , dpi effects quality
            plt.savefig('Age_Major_Plot.png')
            plt.show()

        elif choice == "5":
            #Grouping by Major and we need Grades
            major_averages = df.groupby(['Major'])['Grade'].mean().reset_index()

            #Creating success graph
            sns.violinplot(x="Major", y="Grade", data=df, palette="coolwarm")
            plt.title("Average Grades and Success Graph by Majors")
            plt.xlabel("Major")
            plt.ylabel("Grade")

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
            plt.title("Average Grades and Success Graph by Gender")
            plt.xlabel("Gender")
            plt.ylabel("Grade")

            #Shows average grades on the graph
            for index, row in gender_averages.iterrows():
                plt.text(index, row["Grade"], f"{row['Grade']:.2f}", ha='center', va='bottom')

            plt.savefig('average_grade_by_gender.png')
            plt.show()
        elif choice == "7":
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
                        #Fields must be different
                        if selected_fields[0] == selected_fields[1]:
                            raise ValueError("You must select two different fields")
                        else:
                            break


                except ValueError as e:
                    print(f"Error: {e}")

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
                    plt.title(f"Count Plot of {selected_fields[0]} by {selected_fields[1]}")
                    plt.xlabel(selected_fields[0])
                    plt.ylabel("Count")

                    #Creating a countplot selected fields
                    plt.subplot(2,1,2)
                    sns.countplot(x=selected_fields[1], hue=selected_fields[0], data=df)
                    plt.title(f"Count Plot of {selected_fields[1]} by {selected_fields[0]}")
                    plt.xlabel(selected_fields[1])
                    plt.ylabel("Count")

                    # Saves plot to your desktop or the file your .py file is in , dpi effects quality
                    plt.savefig(f'{field[0]}_{field[1]}_cplot.png')
                    plt.tight_layout()
            elif chart_type == "2":
                if len(selected_fields) == 2:
                    #Creating a barplot selected fields 0 to 1
                    plt.subplot(2,1,1)
                    sns.barplot(x=selected_fields[0], y=selected_fields[1], data=df)
                    plt.title(f"Bar Plot of {selected_fields[1]} by {selected_fields[0]}")
                    plt.xlabel(selected_fields[0])
                    plt.ylabel(selected_fields[1])

                    #Creating a barplot selected fields 1 to 0
                    plt.subplot(2,1,2)
                    sns.barplot(x=selected_fields[1], y=selected_fields[0], data=df)
                    plt.title(f"Bar Plot of {selected_fields[0]} by {selected_fields[1]}")
                    plt.xlabel(selected_fields[1])
                    plt.ylabel(selected_fields[0])

                    # Saves plot to your desktop or the file your .py file is in , dpi effects quality
                    plt.savefig(f'{field[0]}_{field[1]}_barplot.png')
                    plt.tight_layout()
            elif chart_type == "3":
                if len(selected_fields) == 2:
                    #Creating a boxplot selected fields 0 to 1
                    plt.subplot(2,1,1)
                    sns.boxplot(x=selected_fields[0], y=selected_fields[1], data=df)
                    plt.title(f"Box Plot of {selected_fields[1]} by {selected_fields[0]}")
                    plt.xlabel(selected_fields[0])
                    plt.ylabel(selected_fields[1])

                    #Creating a boxplot selected fields 1 to 0
                    plt.subplot(2,1,2)
                    sns.boxplot(x=selected_fields[1], y=selected_fields[0], data=df)
                    plt.title(f"Box Plot of {selected_fields[0]} by {selected_fields[1]}")
                    plt.xlabel(selected_fields[1])
                    plt.ylabel(selected_fields[0])

                    # Saves plot to your desktop or the file your .py file is in , dpi effects quality
                    plt.savefig(f'{field[0]}_{field[1]}_boxplot.png')
                    plt.tight_layout()

            elif chart_type == "4":
                if len(selected_fields) == 2:
                    #Creating a violinplot with selected fields 0 to 1
                    plt.subplot(2,1,1)
                    sns.violinplot(x=selected_fields[0], y=selected_fields[1], data=df)
                    plt.title(f"Violin Plot of {selected_fields[1]} by {selected_fields[0]}")
                    plt.xlabel(selected_fields[0])
                    plt.ylabel(selected_fields[1])

                    #Creating a violinplot with selected fields 1 to 0
                    plt.subplot(2,1,2)
                    sns.violinplot(x=selected_fields[1], y=selected_fields[0], data=df)
                    plt.title(f"Violin Plot of {selected_fields[0]} by {selected_fields[1]}")
                    plt.xlabel(selected_fields[1])
                    plt.ylabel(selected_fields[0])

                    # Saves plot to your desktop or the file your .py file is in , dpi effects quality
                    plt.savefig(f'{field[0]}_{field[1]}_violinplot.png')
                    plt.tight_layout()
            elif chart_type == "5":
                if len(selected_fields) == 2:
                    #Creating a scatterplot with selected fields 0 to 1
                    plt.subplot(2, 1, 1)
                    sns.scatterplot(x=selected_fields[0], y=selected_fields[1], data=df)
                    plt.title(f"Scatter Plot of {selected_fields[1]} by {selected_fields[0]}")
                    plt.xlabel(selected_fields[0])
                    plt.ylabel(selected_fields[1])

                    #Creating a scatterplot with selected fields 1 to 0
                    plt.subplot(2, 1, 2)
                    sns.scatterplot(x=selected_fields[1], y=selected_fields[0], data=df)
                    plt.title(f"Scatter Plot of {selected_fields[0]} by {selected_fields[1]}")
                    plt.xlabel(selected_fields[1])
                    plt.ylabel(selected_fields[0])

                    # Saves plot to your desktop or the file your .py file is in , dpi effects quality
                    plt.savefig(f'{field[0]}_{field[1]}_scatterplot.png')
                    plt.tight_layout()

            elif chart_type == "6":
                if len(selected_fields) == 2:
                    #For first field
                    #Creating a histplot
                    plt.subplot(2, 1, 1)
                    plt.hist(df[selected_fields[0]], bins=20)
                    plt.title(f"Histogram of {selected_fields[0]}")
                    plt.xlabel(selected_fields[0])
                    plt.ylabel("Frequency")

                    #For second field
                    #Creating a histplot
                    plt.subplot(2, 1, 2)
                    plt.hist(df[selected_fields[1]], bins=20)
                    plt.title(f"Histogram of {selected_fields[1]}")
                    plt.xlabel(selected_fields[1])
                    plt.ylabel("Frequency")

                    plt.tight_layout()
                    # Saves plot to your desktop or the file your .py file is in , dpi effects quality
                    plt.savefig(f'{field[0]}_{field[1]}_histplot.png')
            elif chart_type == "7":
                if len(selected_fields) == 2:
                    #For first field
                    #Creating a dist plot
                    plt.subplot(2, 1, 1)
                    sns.histplot(df[selected_fields[0]], kde=True)
                    plt.title(f"Distribution Plot of {selected_fields[0]}")
                    plt.xlabel(selected_fields[0])
                    plt.ylabel("Density")

                    plt.subplot(2, 1, 2)
                    sns.histplot(df[selected_fields[1]], kde=True)
                    plt.title(f"Distribution Plot of {selected_fields[1]}")
                    plt.xlabel(selected_fields[1])
                    plt.ylabel("Density")

                    # Saves plot to your desktop or the file your .py file is in , dpi effects quality
                    plt.savefig(f'{field[0]}_{field[1]}_distplot.png')
                    plt.tight_layout()
            elif chart_type == "8":
                if len(selected_fields) == 2:
                    #Creating a line plot with selected fields 0 to 1
                    plt.subplot(2, 1, 1)
                    sns.lineplot(x=selected_fields[0], y=selected_fields[1], data=df)
                    plt.title(f"Line Plot of {selected_fields[1]} by {selected_fields[0]}")
                    plt.xlabel(selected_fields[0])
                    plt.ylabel(selected_fields[1])

                    #Creating a line plot with selected fields 1 to 0
                    plt.subplot(2, 1, 2)
                    sns.lineplot(x=selected_fields[1], y=selected_fields[0], data=df)
                    plt.title(f"Line Plot of {selected_fields[0]} by {selected_fields[1]}")
                    plt.xlabel(selected_fields[1])
                    plt.ylabel(selected_fields[0])

                    # Saves plot to your desktop or the file your .py file is in , dpi effects quality
                    plt.savefig(f'{field[0]}_{field[1]}_lineplot.png')
                    plt.tight_layout()
            else:
                print("Error: Invalid chart type.")
            #Show the plot
            plt.show()
        else:
            print("Error: Invalid Input! Please enter a number between 1-4")
            continue
        break
    input("Press anys key to continue")

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
        break
    else:
        print("--- Invalid input ---")
        input("Press any key to continue")
print("-------------------------------")
print(" Thank you for using our system")
print("-------------------------------")
