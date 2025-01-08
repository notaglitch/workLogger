# UNDER CONSTRUCTION

## WorkLogger

WorkLogger is a personal work/focus logger designed to help you track your work duration, stay conscious of how much time you spend on tasks, and easily track your productivity. It works as a stopwatch, recording your work sessions and enabling you to add notes (such as the project or task you worked on). It automatically logs your work data into an Excel file and can send updates directly to your Telegram.

Whether you're tracking your work on a project, skill development, or focusing on personal tasks, WorkLogger helps you stay accountable and productive.

Features

    Stopwatch: Start and stop a stopwatch for each work session.
    Notes: Add notes during or after a work session (e.g., which project you worked on).
    Excel Export: Work data is automatically written to an Excel file for easy tracking.
    Telegram Notifications: Sends real-time updates about your work sessions directly to your Telegram.
    Daily Focus Tracking: Stay aware of how much time you're spending on tasks or projects each day.

Installation

    Clone the repository to your local machine:

git clone https://github.com/your-username/WorkLogger.git
cd WorkLogger

Install the required dependencies using pip:

pip install -r requirements.txt

Set up your Telegram Bot:

    Create a bot on Telegram by chatting with the BotFather.
    Note down the bot API token and your Telegram chat ID.

Create a .env file in the root of the project and add the following:

TELEGRAM_API_TOKEN=your-telegram-bot-api-token
TELEGRAM_CHAT_ID=your-chat-id

Run the script to start tracking your work sessions:

    python worklogger.py

Usage
Start a Work Session

    When you want to begin tracking a work session, simply start the stopwatch by running the script and click the Start button.

    You can add a note for the session (e.g., project or task name).

Stop a Work Session

    After completing your work session, stop the stopwatch.

    The work duration will be recorded and written to an Excel file, and a notification will be sent to your Telegram.

Daily Report

    At the end of the day, WorkLogger provides a summary of your work hours, and this data can be reviewed in your Excel file or Telegram.

Output
Excel File

WorkLogger logs all your work sessions into an Excel file with the following columns:

    Date: The date of the work session.
    Duration: Time spent working.
    Note: The note entered for the work session (project name, task, etc.).

The file will be saved in the current working directory as work_log.xlsx.
Telegram Notifications

After each work session, you'll receive the following information in your Telegram:

    Duration of your work session.
    The note (if provided).

This helps you keep track of your progress throughout the day.
Example:

Work session: 2 hours 15 minutes
Note: Worked on Project X

Total work today: 7 hours 30 minutes

Requirements

    Python 3.6+
    Telegram Bot API
    pandas library (for handling Excel data)
    openpyxl library (for writing to Excel)
    python-telegram-bot library (for Telegram notifications)
