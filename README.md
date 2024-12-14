# Workout Tracker

This Python script is designed to help you keep track of your daily workouts. Here's what you can do with it:

## Features

- **Log Daily Workouts**: Input your workout for the day and save it with the current date.
- **View Last Workout**: Check what your most recent workout was.
- **Find Workout by Date**: Retrieve the date of your last session for a specific workout.

 ## How to Use

1. **Setup:**
   - Ensure you have Python installed on your system.
   - Save `main.py` and `WorkoutStorage.txt` (an empty text file) in the same directory where you want to keep your workout data.

2. **Running the Script:**
   - Open a terminal, navigate to the directory with the script, and run:
     ```
     python main.py
     ```

3. **Commands:**
   - **Provide Daily Workout:** Type `provide daily workout` to log today's workout.
   - **Get My Last Workout:** Type `get my last workout` to see your latest recorded workout.
   - **Get Date of Workout:** Type `get date of workout` to find out when you last did a specific workout.

## Usage Example

Here's how you would interact with the script:

- **Input:** `provide daily workout`
  - **Follow-up:** You'll be prompted to enter today's workout, e.g., "push-ups". This will be saved with today's date.

- **Input:** `get my last workout`
  - **Output:** Displays your most recent workout from the file.

- **Input:** `get date of workout`
  - **Follow-up:** You'll be asked which workout you're looking for, e.g., "Squats". The script will then tell you the date of your last session with that workout.

## File Structure

- `WorkoutStorage.txt`: This file is created in the same directory as the script to store workout data. It's formatted as:
