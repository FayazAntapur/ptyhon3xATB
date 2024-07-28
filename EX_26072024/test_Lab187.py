import pytest
import requests
import allure


def create_token():
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "username": "admin",
        "password": "password123"
    }

    response = requests.post(url=url, headers=headers, json=json_payload)
    token = response.json()["token"]
    print(token)
    return token

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
    print(booking_id)
    return str(booking_id)

@allure.id("TC1")
@pytest.mark.smoke
def test_put_request_positive():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/"+str(create_booking())
    PUT_URL = base_url + base_path
    cookie = "token="+create_token()
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

@allure.id("TC12")
@pytest.mark.smoke
def test_delete():
    baser_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/"+str(create_booking())
    headers = {
        "Content-Type": "application/json",
        "Cookie": "token="+create_token()
    }
    url = baser_url+base_path
    response = requests.delete(url=url, headers=headers)
    assert response.status_code == 201