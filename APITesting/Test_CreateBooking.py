from playwright.sync_api import Playwright


def test_create_booking(playwright: Playwright):
    base_url = "https://restful-booker.herokuapp.com"

    request_context = playwright.request.new_context()

    request_body = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 1000,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-07-01",
            "checkout": "2025-07-05"
        },
        "additionalneeds": "super bowls"
    }

    response = request_context.post(
        url=f"{base_url}/booking",
        data=request_body
    )


    response_body = response.json()

    assert response.status == 200
    print(response_body)

    # validations

    assert response.ok
    assert response.status == 200

    response_body = response.json()
    print("Response body=====>", response_body)

    # field/attribute validations

    assert "bookingid" in response_body
    assert "booking" in response_body

    # data validation

    booking = response_body["booking"]

    assert booking["firstname"] == "Jim"
    assert booking["lastname"] == "Brown"
    assert booking["totalprice"] == 1000
    assert booking["depositpaid"] is True
    assert booking["additionalneeds"] == "super bowls"

    # nested json data validation
    assert booking["bookingdates"]["checkin"] == "2025-07-01"
    assert booking["bookingdates"]["checkout"] == "2025-07-05"

    request_context.dispose()