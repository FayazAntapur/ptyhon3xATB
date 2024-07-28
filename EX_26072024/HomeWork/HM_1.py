import allure
import pytest
import requests


@allure.title("Verify Create Booking is successful")
@pytest.mark.smoke
def test_verify_create_booking(create_booking):
    assert create_booking is not None
    print(f"Booking ID: {create_booking}")


@allure.title("Verify Update First Name Booking is successful")
@pytest.mark.smoke
def test_update_first_name(create_token, create_booking):
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/"+str(create_booking)
    print(create_booking)
    PUT_URL = base_url + base_path
    cookie = "token="+create_token
    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie
    }
    josn_payload = {
        "firstname": "Fayaz",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.put(url=PUT_URL, headers=headers, json=josn_payload)
    assert response.status_code == 200
    data = response.json()
    print(data)
    assert data["firstname"] == "Fayaz"
