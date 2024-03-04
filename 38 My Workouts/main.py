import requests
import datetime as dt

APP_ID = "8c3c8534"
API_KEY = "135b65b510f5e40e69d9c76ce9c05f76"
AUTHENTICATION = "Basic cGFzYW5tYWRodXJhbmdhOnJ1czc5Ng=="

# when user enters what they did as a normal string, get the relevant exercises, durations and calories.
user_params = {
    "query": input("Tell me what exercises you did: "),
    "gender": "male",
    "weight_kg": 73.2,
    "height_cm": 172.9,
    "age": 21,
}
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
response = requests.post(url=exercise_endpoint, data=user_params, headers=headers)
all_exercises_list = response.json()["exercises"]

exercises_names_durations_calories = [
    {"name": exercise["name"], "duration": exercise["duration_min"], "calories": exercise["nf_calories"]}
    for exercise in all_exercises_list]

# get the current date and time.
today = dt.datetime.now()
current_date = today.strftime("%d/%m/%Y")
current_time = today.strftime("%H:%M:%S")

headers2 = {
    "Authorization": AUTHENTICATION,
    "Content-Type": "application/json",
}

# Post all the exercises to the google sheet.
for exercise in exercises_names_durations_calories:
    row_config = {
        "workout": {
            "date": current_date,
            "time": current_time,
            "exercise": exercise["name"].title(),
            "duration": round(float(exercise["duration"])),
            "calories": exercise["calories"],
        }
    }
    sheet_end_point = "https://api.sheety.co/d9b6498affde17f134d087d65eb61e1d/myDailyWorkouts/workouts"

    response2 = requests.post(url=sheet_end_point, json=row_config, headers=headers2)
