from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

source_drop_down = 'x'

driver = webdriver.Chrome("/Users/jitendra_sahay/PycharmProjects/selenium_study/drivers/chromedriver")
driver.get("https://scholar.google.com/")
login_link = driver.find_element(By.ID, 'gs_hdr_act_s')
try:
    login_link.click()
    driver.get_screenshot_as_file('gs_sign_in.png')
    email_space = driver.find_element(By.NAME, "identifier")
    email_space.send_keys('jitendra.sahay89')
    driver.find_element(By.XPATH,"//span[text()='Next']").click()
    driver.implicitly_wait(2)
    driver.get_screenshot_as_file('Enter_Password.png')
finally:
    driver.close()
