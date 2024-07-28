import allure
import pytest
import requests


@allure.title("Create a BOOKING, Delete It")
@pytest.mark.smoke
def test_delete(create_token, create_booking):
    baser_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/"+create_booking
    headers = {
        "Content-Type": "application/json",
        "Cookie": "token="+create_token
    }
    url = baser_url+base_path
    response = requests.delete(url=url, headers=headers)
    print(create_booking)
    assert response.status_code == 201
