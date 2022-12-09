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

# use a try-except block to handle cases where the user enters a non-integer value
try:
    push_ups = int(input("Push-ups: "))
    sit_ups = int(input("Sit-ups: "))
    pull_ups = int(input("Pull-ups: "))
    squats = int(input("Squats: "))
    planks = int(input("Planks: "))
except ValueError:
    print("Error: Please enter a valid number for each exercise.")
    exit()

# ask the user to input their body weight
weight = int(input("Enter your body weight in kilograms: "))

# ask the user to input the amount of time they spent doing each exercise
total_time = float(
    input("Enter the amount of time spent doing each exercise in minutes: "))

# ask the user for rest time
rest_time = float(input("Enter the rest period for this session in minutes: "))

# net time for each excercise
time = total_time - rest_time

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


# prompt the user for their duration and distance
distance = float(input("Enter the distance you ran in kilometers: "))
duration = float(input("Enter the duration of your run in minutes: "))

# use an if statement to check if the user has entered a valid weight
if weight <= 0:
    print("Error: Please enter a valid weight.")
    exit()

# use an if statement to check if the user has entered a valid distance
if distance <= 0:
    print("Error: Please enter a valid distance.")
    exit()

# use an if statement to check if the user has entered a valid duration
if duration <= 0:
    print("Error: Please enter a valid duration.")
    exit()

# calculate calories burned
calories_burned = calories_burned(weight, distance, duration)

# print the result using an f-string
print(f"You burned approximately {calories_burned} calories by running.")

# total calories burned
total = calories_burned + total_calories

# print the total using an f-string
print(f"You burned approximately {total} calories in total.")
