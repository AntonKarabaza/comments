import pytest

from comments.core.tools.webdriver_utils import WebDriverFactoryFromConfig


@pytest.fixture(scope="module")
def webdriver_on_main_page(request):
    webdriver = WebDriverFactoryFromConfig().init_driver()
    webdriver.load('http://commentssprintone.azurewebsites.net')

    def tear_down():
        webdriver.stop()

    request.addfinalizer(tear_down)
    return webdriver

