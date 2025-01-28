Worklogger Stopwatch

Worklogger is a simple Python-based stopwatch application that helps you track the time you spend on various tasks. It integrates with Excel to log the time spent on each task for easy tracking and reference.
Features

    Start and stop a stopwatch to track time.
    Time is recorded in minutes and seconds.
    Logs time in an Excel file (Data.xlsx), with today's date and the time spent on tasks.
    Displays time with a glitchy, hacker-like visual effect.
    Provides a simple user interface (UI) built with Tkinter.

Requirements

    Python 3.x
    openpyxl library for working with Excel files
    Tkinter (usually comes pre-installed with Python)

To install the required libraries, run:

pip install openpyxl

How to Use

    Run the application:

    python stopwatch.py

    Click Start to begin tracking time. The stopwatch will start running.
    Click Finish when you're done. The time will be saved to Data.xlsx (if it's more than 1 minute).
    The Excel file will store the date and total time for each task.

Example Usage

Once you've finished a task, your Data.xlsx might look like this:
Date Time Spent (minutes)
28/01/2025 15
