import pytest
from mapi import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_quote_endpoint(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Quote" in response.data
