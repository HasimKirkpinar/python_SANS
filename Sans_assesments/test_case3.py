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


#Focus Area - Filter for Cyber Defense
driver.find_element("xpath", "//label[normalize-space()='Cyber Defense']").click()


# verify Defensible Security Architecture and Engin displayed
driver.find_element("xpath", "//div[contains(text(),'SEC530: Defensible Security Architecture and Engin')]").is_displayed()

#Skill Levels - Filter for Essentials
driver.find_element("xpath", "//label[contains(text(),'Essentials (400-499)')]").click()

# verify SEC497: Practical Open-Source Intelligence (OSINT) displayed
driver.find_element("xpath", "//div[contains(text(),'SEC497: Practical Open-Source Intelligence (OSINT)')]").is_displayed()

# close webdriver
driver.quit()
