import pytest

from pages.page_scenario_1 import Page_Scenario_1

#@pytest.mark.usefixtures("browser_setup")

class Test_Scenario_1:

    def setup_class(self):
        self.page_scenario_1 = Page_Scenario_1(self.driver)


    def validate_test_scenario_1(self):
        self.page_scenario_1.BaseUrl
        self.page_scenario_1.verify_scenario_1()
        self.assert_element_visible(Page_Scenario_1.cybersecurity_Courses_Certifications_El)

    def teardown_class(self):
        self.driver.quite()   