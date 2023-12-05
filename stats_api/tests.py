import pytest
import json
from django.test import Client

@pytest.fixture
def client():
    return Client()

def test_all_berry_stats(client):
    response = client.get('/allBerryStats/')
    assert response.status_code == 200
    assert 'data' in response.context
    data = json.loads(response.context['data'])
    assert 'berries_names' in data

def test_histogram(client):
    response = client.get('/histogram/')
    assert response.status_code == 200