import allure
import pytest
import requests


@allure.title("Trying to Update on a Delete ID")
@pytest.mark.smoke
def test_delete(create_token, create_booking):
    baser_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/" + create_booking
    headers = {
        "Content-Type": "application/json",
        "Cookie": "token=" + create_token
    }
    url = baser_url + base_path
    response = requests.delete(url=url, headers=headers)
    print(create_booking)
    assert response.status_code == 201

    get_response = requests.get(url)
    assert get_response.status_code == 404
    json_payload = {
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
    put_response = requests.put(url=url, json=json_payload, headers=headers)
    assert put_response.status_code == 405
