import pytest
import requests


@pytest.fixture()
def create_token():
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "username": "admin",
        "password": "password123"
    }

    response = requests.post(url=url, headers=headers, json=json_payload)
    token = response.json()["token"]
    return token


@pytest.fixture()
def create_booking():
    URL = "https://restful-booker.herokuapp.com/booking"
    HEADERS = {"Content-Type": "application/json"}
    josn_payload = {
        "firstname": "Amit",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=URL, headers=HEADERS, json=josn_payload)
    data = response.json()
    booking_id = data["bookingid"]
    return str(booking_id)
