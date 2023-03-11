# Health-and-Fitness-Programs
1. Calories_burned_combinations.py
    This code is a program that calculates various fitness-related measurements based on user input.

    The first section of the code defines a dictionary of calories burned per minute for different types of exercise. It prompts the user to input the number of each exercise they did, their body weight, and the amount of time they spent doing each exercise, then calculates the total number of calories burned and prints the result.

    The second section defines a function to calculate calories burned while running, prompts the user to input their weight, distance, and duration of their run, calculates the calories burned, and prints the result.

    The third section defines variables for the target time frame and prompts the user to input their target body fat percentage, current weight, age, sex, height, waist, hip, and neck circumference. It calculates the current body fat percentage using the U.S. Navy method and the total number of calories needed to maintain current weight using the Harris-Benedict equation. It then determines the number of calories that need to be burned per week to reach the target body fat percentage in the target time frame, calculates the number of calories that need to be burned per day to reach the target body fat percentage in the target time frame, and prints the result.

2. Calories_burned_upgrade.py
    This code calculates the total number of calories burned by the user during a workout session that includes exercises like push-ups, sit-ups, pull-ups, squats, and planks. It also calculates the number of calories burned by running and adds it to the total calories burned during the workout session.

    The code first defines a dictionary exercise_calories_per_minute that contains the number of calories burned per minute for each exercise. Then, it asks the user to input the number of each exercise they completed, their body weight, the amount of time they spent doing each exercise, and the rest period for the session. It uses a try-except block to handle cases where the user enters a non-integer value for the number of exercises.

    The code then calculates the total number of calories burned by multiplying the number of exercises completed by the corresponding calories burned per minute and summing over all exercises. It multiplies this value by the net time spent doing exercises (total time - rest time).

    Next, the code defines a function calories_burned that calculates the number of calories burned by running, given the user's weight, distance, and duration. It prompts the user to input the distance they ran and the duration of their run, and checks if the user has entered valid values for their weight, distance, and duration using if statements. It then calculates the number of calories burned using the calories_burned function and adds it to the total calories burned during the workout session.

    Finally, the code prints the total number of calories burned by the user during the workout session and while running, using f-strings
    
3. Exercise_calories.py
    This code is a simplified version of the previous one. It calculates the total number of calories burned based on the number of each type of exercise completed, the user's body weight, and the amount of time spent doing each exercise. The number of calories burned per minute for each exercise is defined in a dictionary called "exercise_calories_per_minute".

    However, this code does not handle cases where the user enters non-integer values for the number of exercises completed or the amount of time spent doing each exercise. It also does not include any prompts or error messages to guide the user. Therefore, it may not be as user-friendly or robust as the previous code.
    
4. Running_calories.py
    This code defines a function calories_burned that takes in a person's weight, distance run, and duration of the run as inputs, and calculates the number of calories burned during the run using the formula calories_burned = calories_per_km * (distance / (duration / 60)).

    It then prompts the user to input their weight, distance, and duration of the run, and calculates the calories burned using the calories_burned function. Finally, it prints the result in a formatted string.

    This code is a simple implementation for calculating calories burned during a run based on a person's weight, distance, and duration, and could be useful in fitness tracking applications.
    
5. Fitnesspal.py
    This code is a body fat percentage calculator that takes several inputs from the user and calculates the number of calories that need to be burned per day to reach a target body fat percentage within a specified time frame.

    It first defines the target time frame and prompts the user to input their target body fat percentage, current weight, age, and sex. It then prompts the user to input their height, waist circumference, hip circumference, and neck circumference.

    The code calculates the current body fat percentage using the U.S. Navy method and the total number of calories needed to maintain the current weight using the Harris-Benedict equation. It then determines the number of calories that need to be burned per week and per day to reach the target body fat percentage in the target time frame.

    Finally, it prints out the current body fat percentage, the target body fat percentage, and the number of calories that need to be burned per day to reach the target body fat percentage in the target time frame.
