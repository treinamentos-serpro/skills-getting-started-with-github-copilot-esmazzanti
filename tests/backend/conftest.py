from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def client():
    # Arrange: create a fresh API client for each test.
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities():
    # Arrange: capture the original in-memory state.
    original_activities = deepcopy(activities)

    yield

    # Assert: restore the state to keep tests isolated.
    activities.clear()
    activities.update(deepcopy(original_activities))
