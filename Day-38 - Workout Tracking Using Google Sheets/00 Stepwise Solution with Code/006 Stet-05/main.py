import requests
from datetime import datetime

# --- User Data ---
GENDER = "YOUR GENDER"
WEIGHT_KG = "YOUR WEIGHT"
HEIGHT_CM = "YOUR HEIGHT"
AGE = "YOUR AGE"

# --- Nutritionix API Credentials (Use Environment Variables or .env File in Real Use) ---
APP_ID = "YOUR_APP_ID_HERE"  #  Replace with your actual Nutritionix APP ID
API_KEY = "YOUR_API_KEY_HERE"  #  Replace with your actual Nutritionix API Key

# --- Nutritionix API Endpoint ---
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

# --- User Input ---
exercise_text = input("Tell me which exercises you did: ")

# --- Nutritionix API Call ---
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(f"Nutritionix API call:\n{result}\n")

# --- Date & Time Setup ---
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

# --- Sheety API Setup ---
GOOGLE_SHEET_NAME = "workout"
sheet_endpoint = "https://api.sheety.co/YOUR_PROJECT_ID/YOUR_SHEET_NAME/workouts"  #  Replace with your actual Sheety endpoint

# --- Posting to Sheety ---
for exercise in result["exercises"]:
    sheet_inputs = {
        GOOGLE_SHEET_NAME: {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    # --- Authorization via Bearer Token ---
    bearer_token = "YOUR_BEARER_TOKEN_HERE"  #  Replace with your Sheety Bearer Token
    bearer_headers = {
        "Authorization": f"Bearer {bearer_token}"
    }

    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        headers=bearer_headers
    )

    print(f"Sheety Response:\n{sheet_response.text}")