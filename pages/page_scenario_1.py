
from utils.helper import Hepler
from selenium.webdriver.common.by import By

class Page_Scenario_1(Hepler):
    BaseUrl = "https://www.sans.org/"
    train_And_Certify_El= (By.XPATH,"//a[contains(text(),'Train and Certify')]")
    full_course_list_El= (By.XPATH, "//a[@aria-label='Full Course List']")
    cybersecurity_Courses_Certifications_El= (By.XPATH, "//h1[normalize-space()='Cybersecurity Courses & Certifications']")

    def __init__(self,driver):
        super.__init__(driver)

    def verify_scenario_1(self):
        Hepler.webelement_click(self.train_And_Certify_El)
        Hepler.webelement_click(self.full_course_list_El)   