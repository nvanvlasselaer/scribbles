import csv
import random

# Functie om een willekeurige naam te genereren
def generate_name():
    first_names = ["John", "Jane", "Alice", "Bob", "Emma", "Michael", "Sophia", "William", "Olivia", "James"]
    last_names = ["Doe", "Smith", "Johnson", "Brown", "Lee", "Taylor", "Wilson", "Anderson", "Clark", "Thomas"]
    return random.choice(first_names) + " " + random.choice(last_names)

# Functie om een willekeurig gewicht te genereren (in kg)
def generate_weight():
    return round(random.uniform(50, 100), 2)

# Functie om een willekeurige lengte te genereren (in cm)
def generate_height():
    return round(random.uniform(150, 200), 2)

# Functie om een willekeurige leeftijd te genereren
def generate_age():
    return random.randint(18, 80)

# Functie om een willekeurige score voor kracht te genereren
def generate_strength_score():
    return random.randint(1, 10)

# Functie om een willekeurige score voor uithoudingsvermogen te genereren
def generate_endurance_score():
    return random.randint(1, 10)

# Functie om een willekeurige score voor lenigheid te genereren
def generate_flexibility_score():
    return random.randint(1, 10)

# Aantal rijen in het CSV-bestand
num_rows = 5

# Header van het CSV-bestand
header = ["Name", "Weight (kg)", "Height (cm)", "Age", "Strength Score", "Endurance Score", "Flexibility Score"]

# Lijst van willekeurige gegevens genereren
data = [
    [generate_name(), generate_weight(), generate_height(), generate_age(),
     generate_strength_score(), generate_endurance_score(), generate_flexibility_score()]
    for _ in range(num_rows)
]

# CSV-bestand schrijven
with open('DATA/random_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(data)

print("CSV-bestand met willekeurige gegevens is gegenereerd.")
