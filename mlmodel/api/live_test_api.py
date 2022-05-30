"""
Example script for querying the live API hosted on
Heroku.
"""
import os
import requests

#URL = "https://udacity3_project.herokuapp.com"
URL = "http://127.0.0.1:8000"


response = requests.post(os.path.join(URL, "predictions"), json={
                    "age": 55,
                    "workclass": "Private",
                    "fnlgt": 77516,
                    "education": "Masters",
                    "education_num": 16,
                    "marital_status": "Never-married",
                    "occupation": "Adm-clerical",
                    "relationship": "Not-in-family",
                    "race": "White",
                    "sex": "Female",
                    "capital_gain": 10000,
                    "capital_loss": 400,
                    "hours_per_week": 45,
                    "native_country": "United-States",
            })

print(response.status_code)
print(response.json())