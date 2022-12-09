# Define the target time frame and other relevant variables
target_time_frame = 8  # weeks

# Prompt the user for the target body fat percentage, current weight, age, and sex
target_body_fat_percentage = float(
    input("Enter your target body fat percentage: "))
current_weight = float(input("Enter your current weight in kilograms: "))
current_age = float(input("Enter your current age: "))
current_sex = input("Enter your sex (male or female): ")

# Prompt the user for the relevant measurements
height = float(input("Enter your height in centimeters: "))
waist = float(input("Enter your waist circumference in centimeters: "))
hip = float(input("Enter your hip circumference in centimeters: "))
neck = float(input("Enter your neck circumference in centimeters: "))

# Calculate the current body fat percentage using the U.S. Navy method
# https://en.wikipedia.org/wiki/Body_fat_percentage#Measurement
body_fat_percentage = 86.010 * \
    (1.20 * (log10(waist - neck) - log10(height))) - \
    70.041 * (log10(height)) + 36.76
starting_body_fat_percentage = round(body_fat_percentage, 2)

# Calculate the total number of calories needed to maintain the current weight using the Harris-Benedict equation
if current_sex == "male":
    bmr = 66.5 + (13.75 * current_weight) + \
        (5.003 * height) - (6.755 * current_age)
else:
    bmr = 655.1 + (9.563 * current_weight) + \
        (1.850 * height) - (4.676 * current_age)
total_calories_needed = bmr * 1.2  # factor in slight activity level

# Determine the number of calories that need to be burned per week to reach the target body fat percentage in the target time frame
calories_to_burn_per_week = (
    target_body_fat_percentage - starting_body_fat_percentage) / target_time_frame

# Calculate the number of calories that need to be burned per day to reach the target body fat percentage in the target time frame
calories_to_burn_per_day = calories_to_burn_per_week / 7

# Print the results
print("Your current body fat percentage is", starting_body_fat_percentage, "%")
print("To reach a body fat percentage of",
      target_body_fat_percentage, "in", target_time_frame, "weeks,")
print("you will need to burn", calories_to_burn_per_day,
      "calories per day on average.")
