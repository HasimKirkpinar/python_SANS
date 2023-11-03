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
CyberCourse= driver.find_element("xpath", "//h1[normalize-space()='Cybersecurity Courses & Certifications']")
if CyberCourse.is_displayed():
  print("CyberCourse found")
else:
  print(" CyberCourse not found")

#Focus Area - Filter for Cyber Defense
driver.find_element("xpath", "//label[normalize-space()='Cyber Defense']").click()

# verify Defensible Security Architecture and Engin displayed
SEC530Course= driver.find_element("xpath", "//div[contains(text(),'SEC530: Defensible Security Architecture and Engin')]")
if SEC530Course.is_displayed():
  print("SEC530Course found")
else:
  print("SEC530Course not found")

#Skill Levels - Filter for Essentials
driver.find_element("xpath", "//label[contains(text(),'Essentials (400-499)')]").click()

# verify SEC497: Practical Open-Source Intelligence (OSINT) displayed
SEC497PracticalCourse = driver.find_element("xpath", "//div[contains(text(),'SEC497: Practical Open-Source Intelligence (OSINT)')]")
if SEC497PracticalCourse.is_displayed():
  print("SEC497PracticalCourse found")
else:
  print("SEC497PracticalCourse not found")

# close webdriver
driver.quit()
