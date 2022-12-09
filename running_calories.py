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
print(f"You burned approximately {calories_burned} calories.")