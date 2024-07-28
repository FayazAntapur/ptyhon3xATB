import allure
import pytest
import requests


@allure.id("TC12")
@allure.title("Delete created booking")
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


@allure.title("Verfiy deleted booking not present")
@pytest.mark.smoke
def test_get_deleted_id(create_token, create_booking):
    baser_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/"+create_booking
    url = baser_url+base_path
    headers = {
        "Content-Type": "application/json",
        "Cookie": "token="+create_token
    }
    url = baser_url+base_path
    requests.delete(url=url, headers=headers)
    response = requests.get(url)
    print(create_booking)
    assert response.status_code == 404