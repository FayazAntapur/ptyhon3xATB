import allure
import pytest
import requests


@allure.title("Invalid Creation - enter a wrong payload or Wrong JSON")
@allure.description("First Name passed as Integer Value")
@pytest.mark.smoke
def test_invalid_create_booking():
    URL = "https://restful-booker.herokuapp.com/booking"
    HEADERS = {"Content-Type": "application/json"}
    josn_payload = {
        "firstname": 1234,
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": "True",
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=URL, headers=HEADERS, json=josn_payload)
    assert response.status_code == 500
