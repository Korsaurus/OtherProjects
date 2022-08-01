import requests
import secrets
parameters = {
    "amount": 10,
    "type": "boolean"
}

response = requests.get(secrets.API_PRACTICE, params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]

