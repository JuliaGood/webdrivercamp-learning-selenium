from selenium.webdriver.remote.webdriver import WebDriver
from components.base import Base


class LeftFilter(Base):
    LOCATOR = "//*"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def select_option(self, option, visible=False):
        print(Base.BASE_VAR)
        print(self.LOCATOR)
        print(option)
        print(visible)
