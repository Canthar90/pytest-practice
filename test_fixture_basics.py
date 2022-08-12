# to invoke program with pytest name must start with test and every test function also should start with it

import pytest


@pytest.fixture
def example_fixture():
    return 1


def test_with_fixture(example_fixture):
    assert example_fixture == 1