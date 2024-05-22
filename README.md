# ITU Student Record Management System

## Project Description
The ITU Student Record Management System is a console-based application designed to manage student records. This project provides various functions to add, view, search, update, delete student records, and perform statistical analysis and visualization of these records.

## Libraries Used
1. **Pandas:** Used for data processing and analysis.
2. **Seaborn and Matplotlib:** Used for data visualization.
3. **CSV:** Used for data storage and manipulation with CSV files.
4. **Faker:** Used to generate fake data.
5. **Random:** Used for generating random data.

## Project Code Features
This system includes the following 7 main functions:

1. **add_student:** Adds a new student record. There are 9 fields in the CSV file: `["Roll no.","Name Surname","Age","Gender","Students id","Grade","Email","Phone","Major"]`. Each field must adhere to specific rules. User inputs are validated using validation functions, and the added student data is displayed.
2. **view_student:** Displays existing student records. Data is sorted as in the database: by roll number, by gender, by major, by grade, in alphabetical order, by gender in a specific major, and by grades in a specific major.
3. **search_student:** Searches for students based on specific criteria. You can search for students by their name surname, ID, and roll number.
4. **update_student:** Updates an existing student record by entering the student's ID.
5. **delete_student:** Deletes a student record by entering the student's ID.
6. **visualization:** Visualizes student data. It offers various options and creates a chart based on user selection (although it may be meaningless). The generated chart is saved where your ProjectCode.py file is located.
7. **student_statistics:** Performs statistical analysis on student records. It offers various options and saves the analysis results to a text file.

## About Fakedata.py
This Python file generates fake data for the dataset.csv file. It configures the faker library for Turkish and generates fake names, student IDs, and phone numbers. Student IDs, roll numbers, and email addresses are unique. By default, it generates 300 fake data, but you can adjust this number by changing the `num_students` variable.

## Usage Guide
1. First, run fakedata.py to generate fake data (There is data in dataset.csv you don't have to do this).
2. Then run ProjectCode.py to start the main program.
3. When the program starts, select the desired operation through the provided options and follow the instructions.

## Requirements and Python Version

To run this project, you need to have Python installed on your system. Additionally, the following libraries are required:

- **Pandas:** Used for data processing and analysis.
- **Seaborn and Matplotlib:** Used for data visualization.
- **Faker:** Used to generate fake data.

You can find the versions of libraries in requirements.txt.

### Python Version

This project is developed using Python 3.11.2. It should work with a any Python version ,but I recommend using Python 3.11.2


