# Prompt User to insert weight, height and age
weight = float(input("Enter weight in kilogram:"))
height = float(input("Enter height in centimetre:"))
age = int(input("Enter age in years:"))
gender = input("Enter gender: (female/male):")
# Calculate BMR
if gender == "female":
  BMR = (10 * weight) + (6.25 * height) - (5 * age) - 161
  print("BMR:", BMR)
if gender == "male":
  BMR = (10 * weight) + (6.25 * height) - (5 * age) + 5
  print("BMR:", BMR)
# Prompt User to choose activity factor
activity_factor = input("Enter level of activity: (sedentary/lightly active/moderately active/very active/super active):")
# Calculate daily calorie required
if activity_factor == "sedentary":
  daily_calories = BMR * 1.2
  print("Daily Calories:", daily_calories)
elif activity_factor == "lightly_active":
  daily_calories = BMR * 1.375
  print("Daily Calories:", daily_calories)
elif activity_factor == "moderately_active":
  daily_calories = BMR * 1.55
  print("Daily Calories:", daily_calories)
elif activity_factor == "very_active":
  daily_calories = BMR * 1.725
  print("Daily Calories:", daily_calories)
elif activity_factor == "super_active":
  daily_calories = BMR * 1.9
  print("Daily Calories:", daily_calories)
elif activity_factor == "sedentary":
  daily_calories1 = BMR * 1.2
  print("Daily Calories:", daily_calories1)
elif activity_factor == "lightly_active":
  daily_calories1 = BMR * 1.375
  print("Daily Calories:", daily_calories1)
elif activity_factor == "moderately_active":
  daily_calories1 = BMR * 1.55
  print("Daily Calories:", daily_calories1)
elif activity_factor == "very_active":
  daily_calories1 = BMR * 1.725
  print("Daily Calories:", daily_calories1)
elif activity_factor == "super_active":
  daily_calories1 = BMR * 1.9
  print("Daily Calories:", daily_calories1)
# Prompt User to insert carbohydrate, protein and fat percentages
carbohydrate_percentage = float(input("Enter carbohydrate percentage without %:"))
protein_percentage = float(input("Enter protein percentage without %:"))
fat_percentage = float(input("Enter fat percentage without %:"))
if carbohydrate_percentage+protein_percentage+fat_percentage != 100:
  print("Invalid")
# Calculate grams of carbohydrate,protein and fat
if gender == "female":
  carbohydrate = ((carbohydrate_percentage / 100) * daily_calories) / 4
print("Grams of carbohydrate:", carbohydrate)
protein = ((protein_percentage / 100) * daily_calories) / 4
print("Grams of protein:", protein)
fat = ((fat_percentage / 100) * daily_calories) / 9
print("Grams of fat:", fat)
if gender == "male":
  carbohydrate = ((carbohydrate_percentage / 100) * daily_calories) / 4
print("Grams of carbohydrate:", carbohydrate)
protein1 = ((protein_percentage / 100) * daily_calories) / 4
print("Grams of protein:", protein1)
fat = ((fat_percentage / 100) * daily_calories) / 9
print("Grams of fat:", fat)
# Prompt User to insert servings of vegetables, fruits, milk as well as grams of fat in milk and meat
vegetables = float(input("Enter servings of vegetables:"))
fruits = float(input("Enter servings of fruits:"))
milk = float(input("Enter servings of milk:"))
milk_fat = float(input("Enter grams of fat in recommended type of milk:")) 
meat_fat = float(input("Enter grams of fat in recommended type of meat:"))
# Calculate servings of starch
starch = (carbohydrate - ((5 * vegetables) + (15 * fruits) + (12 * milk))) / 15
print("Servings of starch:", starch)
meat = (protein - ((3 * starch) + (2 * vegetables) + (8 * milk))) / 7
print("Servings of meat:", meat)
oil = (fat - ((meat_fat * meat) + (milk_fat * milk))) / 5
print("Servings of oil:", oil)



