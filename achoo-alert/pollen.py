import requests
import os
from dotenv import load_dotenv
import logging
import logging_config


load_dotenv()

POLLEN_ENDPOINT = os.getenv("POLLEN_ENDPOINT")
POLLEN_PLACE = os.getenv("POLLEN_PLACE")
POLLEN_API_KEY = os.getenv("POLLEN_API_KEY")

POLLEN_URL = f"{POLLEN_ENDPOINT}?place={POLLEN_PLACE}"
headers = {"x-api-key": POLLEN_API_KEY}

RISK_LEVEL_ORDER = ["Low", "Moderate", "High", "Very High"]


def fetch_highest_risk():
    """
    Calls other functions that fetch data, extract risk data, and determine the highest risk level.
    """
    data = fetch_pollen_data()
    if data is None:
        return None
    risk_data = extract_risk_data(data)
    return determine_highest_risk(risk_data)


def fetch_pollen_data():
    """
    Fetches pollen data from the API and returns the parsed JSON.
    """
    try:
        response = requests.get(POLLEN_URL, headers=headers)
        # https://stackoverflow.com/questions/61463224/when-to-use-raise-for-status-vs-status-code-testing
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"Request error: {e}")
        return None


def extract_risk_data(data):
    """
    Extracts the 'Risk' dictionary from the API response.
    """
    if not data.get("data"):
        logging.error("Error: No data returned from the API.")
        return None

    return data["data"][0].get("Risk")


def determine_highest_risk(risk_data):
    """
    Determines the highest risk level from the given risk data.
    """
    if not risk_data:
        logging.error("Error: No risk data available.")
        return None

    # max() iterates over the values of risk_data. Lambda ensures that max() uses the index in RISK_LEVEL_ORDER to compare risk levels.
    # https://stackoverflow.com/questions/18296755/python-max-function-using-key-and-lambda-expression
    return max(risk_data.values(), key=lambda level: RISK_LEVEL_ORDER.index(level))


if __name__ == "__main__":
    print(fetch_highest_risk())
