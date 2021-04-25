import json
import datetime

import pytest
from mock import patch, call
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


parametrize = pytest.mark.parametrize

def test_health(test_client):
    response = test_client.get('/v1/')
    assert response.status_code == 200

def test_device_category(test_client, init_database):
    response = test_client.get('/v1/device-category')
    assert response.status_code == 200
    assert response.json == {'device_category': ['category']}

