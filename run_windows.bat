@echo off
echo Activating virtual environment...
call venv\Scripts\activate

echo Running daily content generation...
python backend\automation\daily_content.py

echo Daily content complete. Press any key to exit.
pause
