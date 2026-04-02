import pytest
from django.test import Client

from brand.application.landing import GetLandingPage


@pytest.mark.django_db
def test_landing_page_returns_200():
    client = Client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Retro Fizz" in response.content


def test_get_landing_use_case_has_flavors():
    page = GetLandingPage().execute()
    assert page.brand_name == "Retro Fizz"
    assert len(page.flavors) == 3
