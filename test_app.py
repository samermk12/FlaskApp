import pytest
from app import app

def test_index():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 500
    assert b"Hello, World!" in response.data
    