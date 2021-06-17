import requests

base_url = "http://localhost:8000/api/"


def test_post_order():
    data = {"user_id": 123, "stock": "ALPHA", "quantity": 200, "price": 100.00}

    response = requests.post(url=base_url, json=data)

    assert response.status_code == 201


def test_get_portfolio():
    user_id = 123
    get_url = f"{base_url}portfolio/{user_id}"

    response = requests.get(url=get_url)

    assert response.status_code == 200
