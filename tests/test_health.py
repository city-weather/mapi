import pytest
from mapi import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_health_endpoint(client):
    response = client.get("/mapi-health")
    assert response.status_code == 200
    assert b"healthy" in response.data
