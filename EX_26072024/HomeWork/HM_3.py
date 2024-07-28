import allure
import pytest
import requests


@pytest.mark.smoke
@allure.title("Get an Existing Booking id from Get All Bookings Ids , Update a Booking and Verify using GET by id")
def test_get_all_bookings(create_token):
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/"
    url = base_url + base_path

    # Get all bookings, filter one booking id
    response = requests.get(url)
    response_json = response.json()
    booking_id = response_json[0]["bookingid"]
    print(booking_id)
    assert response.status_code == 200

    headers = {
        "Content-Type": "application/json",
        "Cookie": "token=" + create_token
    }
    base_path_id = str(booking_id)
    change_first_name = "Fayaz"
    json_payload = {
        "firstname": change_first_name,
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    put_url = base_url + base_path + base_path_id
    print(put_url)

    # update filtered booking_id by firstname
    response_put = requests.put(url=put_url, headers=headers, json=json_payload)
    assert response_put.status_code == 200
    data = response_put.json()
    updated_first_name = data["firstname"]
    assert updated_first_name == change_first_name

    # get the updated first and verify
    response_get = requests.get(put_url)
    assert response_get.status_code == 200

    data_get = response_get.json()
    get_first_name = data_get["firstname"]
    assert change_first_name == get_first_name
