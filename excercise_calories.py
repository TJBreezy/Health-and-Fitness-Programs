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
print("Total calories burned:", total_calories)
