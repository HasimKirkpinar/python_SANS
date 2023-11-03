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


# type SEC504 search course
driver.find_element("xpath", "//input[@id='search-query']").send_keys("SEC504")

#Click for search course results
driver.find_element("xpath", "//a[@aria-label='Clear filter button']").click()

#verify course results
driver.find_element("xpath", "//div[contains(text(),'SEC504: Hacker Tools, Techniques, and Incident Han')]").is_displayed()

#Clear search  parameterr for new  choise 
driver.find_element("xpath", "//a[@aria-label='Clear filter button']").click()

# type FOR508 search course
driver.find_element("xpath", "//input[@id='search-query']").send_keys("FOR508")

#Click for search course results
driver.find_element("xpath", "//a[@aria-label='Clear filter button']").click()

#verify course results
driver.find_element("xpath", "//div[@class='title'][normalize-space()='FOR508: Advanced Incident Response, Threat Hunting, and Digital Forensics']").is_displayed()


# close webdriver
driver.quit()
