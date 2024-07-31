# weather_django
This Project was developed using Pycharm, Python and Django.
Pycharm provides virtual environment.

# The Weather Comparison App is live at:
https://weather-django.onrender.com

# About the Project.
1. This project lists the temperatures and compares the temperatures of two different cities.
2. It uses the OpenWeather API to fetch details and display them.
3. You need to enter two different cities to view their weather details.
4. The project handles all edge cases: City_1 is required, while City_2 may or may not exist.

# How to run on Local Machine
1. Open PyCharm and create a virtual environment if one has not already been created.
2. Navigate to the directory where the project is stored.
3. Open the terminal in PyCharm and run "python manage.py runserver" (without quotes). This will start the application locally and provide a URL.
4. Navigate to the URL to try out the application.

# Instruction on how to deploy on Render.com
1. Commit the entire project to GitHub, excluding the virtual environment directory.
2. On Render.com, click on + New, then select Web Services. Link your GitHub repository to Render.com.
3. Connect to the directory, fill in all the fields, and for the Start Command field, enter "gunicorn weather_api_project.wsgi:application". Deploy the application successfully.
4. Copy the provided link, open it in your browser, and explore the application.

