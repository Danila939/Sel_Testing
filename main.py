from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from auth_data import okta_password
import time

firefox_binary = FirefoxBinary()
s = Service('C:\\Users\\danil\\Desktop\\pythonProject1\\seleniumProj\\DriverFireFox\\geckodriver.exe')
driver = webdriver.Firefox(firefox_binary=firefox_binary, service=s)
url = "https://portal.corepartners.ru/Nrdr.Next/Nrdr/Dashboard"


try:
    driver.get(url=url)
    time.sleep(5)

    log_in_button = driver.find_element(By.PARTIAL_LINK_TEXT, 'Login with ACR Account').click()
    time.sleep(5)

    log_in_input = driver.find_element(By.ID, 'idp-discovery-username')
    log_in_input.clear()
    log_in_input.send_keys('cuu86738@nezid.com')
    log_in_input.send_keys(Keys.ENTER)
    time.sleep(7)

    pass_input = driver.find_element(By.ID, 'okta-signin-password')
    pass_input.clear()
    pass_input.send_keys(okta_password)
    pass_input.send_keys(Keys.ENTER)
    time.sleep(7)

    managePhyGroup = driver.find_element(By.PARTIAL_LINK_TEXT, 'Manage Physician Groups').click()
    time.sleep(5)

    Add_new_PhyGroup = driver.find_element(By.ID, 'addPhysicianGroupBtn').click()
    time.sleep(5)

    Name_of_Group = driver.find_element(By.ID, 'Name')
    Name_of_Group.clear()
    Name_of_Group.send_keys('NewGroup')
    time.sleep(5)

    Choose_Facilities = driver.find_element(By.ID, 'FacilityIds_input').click()
    time.sleep(2)

    Click_on_Facility = driver.find_element(By.ID, 'FacilityIds_item_0').click()
    time.sleep(2)

    Save_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div[6]/div/form/div/div/div[4]/div/button[1]').click()
    time.sleep(7)







    #cuu86738@nezid.com



except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
