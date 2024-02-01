import csv
import random

# Function to generate a random subject name
def generate_name():
    first_names = ['John', 'Emma', 'Michael', 'Sophia', 'William', 'Olivia', 'James', 'Ava', 'Alexander', 'Isabella']
    last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez']
    return random.choice(first_names) + ' ' + random.choice(last_names)

# Generate random data for subjects
def generate_subject_data():
    name = generate_name()
    length = round(random.uniform(150, 200), 2)  # in centimeters
    weight = round(random.uniform(50, 100), 2)   # in kilograms
    age = random.randint(20, 80)                 # in years
    return name, length, weight, age

# Generate data for 50 subjects
subjects_data = [generate_subject_data() for _ in range(50)]

# Write data to a CSV file
with open('subjects_data.csv', 'w', newline='') as csvfile:
    fieldnames = ['Name', 'Length (cm)', 'Weight (kg)', 'Age (years)']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for subject in subjects_data:
        writer.writerow({'Name': subject[0], 'Length (cm)': subject[1], 'Weight (kg)': subject[2], 'Age (years)': subject[3]})

print("CSV file generated successfully.")
