import pytest

@pytest.fixture(scope="function")
def testcase_data(request):
    testcase_name = request.function.__name__
    return testcase_name