# Prompt User to insert weight, height and age
weight = float(input("Enter weight in kilogram:"))
height = float(input("Enter height in centimetre:"))
age = int(input("Enter age in years:"))
gender = input("Enter gender: (female/male):")
activity_level = input("Enter level of activity: (sedentary/lightly active/moderately active/very active/super active):")
carbohydrate_percentage = float(input("Enter carbohydrate percentage without %:"))
protein_percentage = float(input("Enter protein percentage without %:"))
fat_percentage = float(input("Enter fat percentage without %:"))
vegetables = float(input("Enter servings of vegetables:"))
fruits = float(input("Enter servings of fruits:"))
milk = float(input("Enter servings of milk:"))
milk_fat = float(input("Enter grams of fat in recommended type of milk:")) 
meat_fat = float(input("Enter grams of fat in recommended type of meat:"))
# Define activity factors
if activity_level == "sedentary":
    activity_factor = 1.2
elif activity_level == "lightly active":
    activity_factor = 1.375
elif activity_level == "moderately active":
    activity_factor = 1.55
elif activity_level == "very active":
    activity_factor = 1.725
elif activity_level == "super active":
    activity_factor = 1.9
# Calculate Daily Calorie Requirement using BMR and activity factor based on gender
if gender == "female":
    daily_calorie = ((10 * weight) + (6.25 * height) - (5 * age) - 161) * activity_factor
    print("Daily Calorie Requirement:", daily_calorie)
elif gender == "male":
    daily_calorie = ((10 * weight) + (6.25 * height) - (5 * age) + 5) * activity_factor
    print("Daily Calorie Requirement:", daily_calorie)
if carbohydrate_percentage + protein_percentage + fat_percentage != 100:
    print("Invalid")
# Calculate grams of carbohydrate, protein and fat
if gender == "female":
    carbohydrate = ((carbohydrate_percentage / 100) * daily_calorie) / 4
    print("Grams of carbohydrate:", carbohydrate)
    protein = ((protein_percentage / 100) * daily_calorie) / 4
    print("Grams of protein:", protein)
    fat = ((fat_percentage / 100) * daily_calorie) / 9
    print("Grams of fat:", fat)
elif gender == "male":
    carbohydrate = ((carbohydrate_percentage / 100) * daily_calorie) / 4
    print("Grams of carbohydrate:", carbohydrate)
    protein = ((protein_percentage / 100) * daily_calorie) / 4
    print("Grams of protein:", protein)
    fat = ((fat_percentage / 100) * daily_calorie) / 9
    print("Grams of fat:", fat)
# Calculate servings of starch
if gender == "female":
    starch = (carbohydrate - ((5 * vegetables) + (15 * fruits) + (12 * milk))) / 15
    print(f"Servings of starch:, {round(starch)}")
    meat = (protein - ((3 * starch) + (2 * vegetables) + (8 * milk))) / 7
    print(f"Servings of meat:, {round(meat)}")
    oil = (fat - ((meat_fat * meat) + (milk_fat * milk))) / 5
    print(f"Servings of oil:, {round(oil)}")
elif gender == "male":
    starch = (carbohydrate - ((5 * vegetables) + (15 * fruits) + (12 * milk))) / 15
    print(f"Servings of starch:, {round(starch)}")
    meat = (protein - ((3 * starch) + (2 * vegetables) + (8 * milk))) / 7
    print(f"Servings of meat:, {round(meat)}")
    oil = (fat - ((meat_fat * meat) + (milk_fat * milk))) / 5
    print(f"Servings of oil:, {round(oil)}")
