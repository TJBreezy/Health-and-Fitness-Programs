# define the number of calories burned per minute for each exercise
exercise_calories_per_minute = {
    "push-ups": 3.5,
    "sit-ups": 2.3,
    "pull-ups": 4.5,
    "squats": 3.5,
    "planks": 2.3
}

# ask the user to input the number of each type of exercise they did
print("Enter the number of each exercise you completed:")
push_ups = int(input("Push-ups: "))
sit_ups = int(input("Sit-ups: "))
pull_ups = int(input("Pull-ups: "))
squats = int(input("Squats: "))
planks = int(input("Planks: "))

# ask the user to input their body weight
weight = int(input("Enter your body weight in kilograms: "))

# ask the user to input the amount of time they spent doing each exercise
time = int(input("Enter the amount of time spent doing each exercise in minutes: "))

# calculate the total number of calories burned
total_calories = (push_ups * exercise_calories_per_minute["push-ups"] +
                  sit_ups * exercise_calories_per_minute["sit-ups"] +
                  pull_ups * exercise_calories_per_minute["pull-ups"] +
                  squats * exercise_calories_per_minute["squats"] +
                  planks * exercise_calories_per_minute["planks"]) * time

# print the results
print("Total calories burned by exercises:", total_calories)


# define the function to calculate calories burned
def calories_burned(weight, distance, duration):
    # calculate calories burned per kilometer
    calories_per_km = 0.75 * weight

    # calculate total calories burned
    calories_burned = calories_per_km * (distance / (duration / 60))

    return calories_burned


# prompt the user for their weight and distance
weight = float(input("Enter your weight in kilograms: "))
distance = float(input("Enter the distance you ran in kilometers: "))
duration = float(input("Enter the duration of your run in minutes: "))

# calculate calories burned
calories_burned = calories_burned(weight, distance, duration)

# print the result
print(f"You burned approximately {calories_burned} calories by running.")

# total calories burned
total = calories_burned + total_calories

# print the total
print(f"You burned approximately {total} calories in total.")


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
calories_to_burn_per_day = (calories_to_burn_per_week / 7) + total

# Print the results
print("Your current body fat percentage is", starting_body_fat_percentage, "%")
print("To reach a body fat percentage of",
      target_body_fat_percentage, "in", target_time_frame, "weeks,")
print("you will need to burn", calories_to_burn_per_day,
      "calories per day on average.")
