import json
import os

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from project import create_app, db
from project.models import DeviceMatrix, Base


@pytest.fixture(scope='module')
def new_device():
    device = DeviceMatrix(
        'devicetype',
        'category',
        'description',
        'article',
        True
    )
    return device

@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app('flask_test.cfg')

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            yield testing_client  # this is where the testing happens!

@pytest.fixture(scope='module')
def init_database(test_client):
    # Create the database and the database table
    db.create_all()

    dm = DeviceMatrix(devicetype='devicetype', category='category', article='article', description='description', jws=True)
    db.session.add(dm)
    db.session.commit()

    yield  # this is where the testing happens!

    db.drop_all()

