import csv
import random
#Will generate random data
from faker import Faker
#It will be Turkish
fake = Faker('tr_TR')
#Trying to assign accurate genders to names
from faker.providers import person
fake.add_provider(person)


#Student id, roll no , phone and email must be unique
def generate_unique_value(existing_values, generate_func):
    while True:
        value = generate_func()
        if value not in existing_values:
            existing_values.add(value)
            return value

#in Email part it ensures email ends with "@itu.edu.tr"
def generate_student_data(existing_roll_nos,existing_phones, existing_student_ids,existing_emails):
    #Assign Gender
    gender = fake.random_element(elements=('Male', 'Female'))
    # Not using fake.name() because I dont want titles and using male or female for gender
    if gender == "Male":
        name = fake.first_name_male() + " " + fake.last_name_male()
    else:
        name = fake.first_name_female() + " " + fake.last_name_female()
    first_name = name.split()[0]
    last_name = name.split()[1]
    #Generating suitable phone numbers
    phone = "05" + fake.msisdn()[4:]
    email = first_name.lower().replace("ş","s").replace("ı","i").replace("ö","o").replace("ç","c").replace("ğ","g").replace("ü","u") + last_name.lower().replace("ş","s").replace("ı","i").replace("ö","o").replace("ç","c").replace("ğ","g").replace("ü","u") + "@itu.edu.tr"

    #With using fake library generating random data
    student_data = {
        "Roll no.": generate_unique_value(existing_roll_nos, lambda: random.randint(1, 300)),
        "Name Surname" : name,
        "Age": random.randint(17,30),
        "Gender" : gender,
        "Students id": generate_unique_value(existing_student_ids, lambda: random.randint(100000000, 999999999)),
        "Grade": round(random.uniform(0,4) ,2),
        "Email": generate_unique_value(existing_emails, lambda: email),
        "Phone": generate_unique_value(existing_phones, lambda: phone),
        "Major": random.choice(["Computer Engineering", "Mineral Processing Engineering",
                                "Environmental Engineering", "Maritime Transportation Management Engineering", "Economy",
                                "Electrical Engineering", "Chemical Engineering", "Electronics and Communications Engineering",
                                "Industrial Engineering", "Industrial Products Engineering", "Physics Engineering",
                                "Naval Construction and Ship Machinery Engineering", "Ship Machinery Management Engineering",
                                "Ship and Marine Technology Engineering", "Geomatic Engineering", "Food Engineering",
                                "Interior Architecture", "Manufacturing Engineering", "Civil Engineering", "Management Engineering",
                                "Geophysical Engineering", "Geological Engineering", "Control and Automation Engineering",
                                "Mining Engineering", "Mechanical Engineering", "Mathematics Engineering", "Metallurgy and Materials Engineering",
                                "Meteorological Engineering", "Architecture", "Molecular Biology and Genetics", "Petroleum and Natural Gas Engineering",
                                "Landscape Architecture", "City and Region Planning", "Textile Engineering",
                                "Textile Development and Marketing", "Aircraft Engineering", "Astronautical Engineering",
                                "Artificial Intelligence and Data Engineering"])
    }
    return student_data


def save_students_to_csv(file_name, students):
    fields = ["Roll no.","Name Surname","Age","Gender","Students id","Grade","Email","Phone","Major"]
    #Opening CSV file in writing mode
    with open(file_name, 'w', newline='',encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        #Writing data
        for student in students:
            writer.writerow(student)


num_students = 300
#They should be unique so we are using set
existing_roll_nos = set()
existing_phones = set()
existing_student_ids = set()
existing_emails = set()
students = [
    generate_student_data(existing_roll_nos, existing_phones, existing_student_ids, existing_emails)
    for _ in range(num_students)
]

filename = 'dataset.csv'
save_students_to_csv(filename, students)

print(f"Saved {num_students} student records to {filename}")
