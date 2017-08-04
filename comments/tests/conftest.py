import pytest

from comments.core.tools.webdriver_utils import WebDriverFactoryFromConfig


@pytest.fixture(scope="module")
def webdriver_setup(request):
    webdriver = WebDriverFactoryFromConfig().init_driver()

    def tear_down():
        webdriver.stop()

    request.addfinalizer(tear_down)
    return webdriver
