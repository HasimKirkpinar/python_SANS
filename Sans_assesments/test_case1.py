from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
options =Options()
options.add_experimental_option("detach", True)

#SetUP Driver

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# Go to Web  page
driver.get("https://www.sans.org/")
driver.maximize_window()
# Find Train and Certify  and click
driver.find_element("xpath", "//li[@aria-label='Train and Certify']").click()

#Find Full Course List  and click
driver.find_element("xpath", "//a[@aria-label='Full Course List']").click()

# verify Cybersecurity Courses & Certifications list displayed
driver.find_element("xpath", "//h1[normalize-space()='Cybersecurity Courses & Certifications']").is_displayed()

# close webdriver
driver.quit()
