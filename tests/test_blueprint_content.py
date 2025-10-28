
"""This is a test script to test flask application"""
import pytest
from wsgi import app


@pytest.fixture(name="client")
def create_client():
    """initialize a fixture test client for flask unit testing"""
    with app.test_client() as app_client:
        yield app_client


def test_main_page_content(client):
    """flask unit testing for content in default page"""
    # should connect and return 200
    resp = client.get("/")
    assert resp.status_code == 200
    # ensure keyword "Blueprint" exists in the returned content
    assert b"Blueprint" in resp.data


def test_about_page_content(client):
    """flask unit testing for content in about page"""
    # should connect and return 200
    resp = client.get("/about")
    assert resp.status_code == 200
    # ensure keyword "Blueprint" exists in the returned content
    assert b"Blueprint" in resp.data
