import datetime
import os
import sys

# Allowing us to access the external "WorkoutStorage.txt" file

ExtFile = os.path.join(sys.path[0], 'WorkoutStorage.txt')

# Obtaining user input to determine which outcome they want, accepting start capitalizing or not

objective = input("What would you like to do? ").lower()

# Ensuring user can only ask 3 questions

if objective in ('provide daily workout', 'get my last workout',
                 'get date of workout'):

  # Inputting the user's daily workout

  if objective == 'provide daily workout':
    DailyWorkout = input("What did you train today? ")
    DailyWorkout = DailyWorkout.capitalize()
    with open(ExtFile, 'a') as fout:
      fout.write(DailyWorkout + " " + str(datetime.date.today()) + "\n")
    print(DailyWorkout + " has been added for today's date: " +
          str(datetime.date.today()) + "\nGreat work!")

  # Returning the user's last workout

  elif objective == 'get my last workout':
    if os.path.exists(ExtFile):
      with open(ExtFile, 'r') as fout:
        workout_records = fout.readlines()
        if workout_records:
          last_workout = workout_records[-1]
          print("Last workout:", last_workout)
        else:
          print("No workout records found.")
    else:
      print("No workout records found.")

  #Return a specific workout with a date

  elif objective == 'get date of workout':
    specific_workout = input(
      "Which workout are you interested in? ").capitalize()
    if os.path.exists(ExtFile):
      with open(ExtFile, 'r') as fout:
        workout_records = fout.readlines()
        last_time = None
        for record in reversed(workout_records):
          workout, date = record.strip().split()
          if workout.lower() == specific_workout.lower():
            last_time = date
            break
        if last_time:
          print("Last time", specific_workout, "was done:", last_time)
        else:
          print("Workout", specific_workout, "was not found in the records.")
    else:
      print("No workout records found.")

else:
  print(
    'The only 3 statements that can be input here are, "provide daily workout", "get my last workout", or "get date or workout".'
  )
