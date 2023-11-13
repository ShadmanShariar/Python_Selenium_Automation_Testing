import time
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

def test_annotator():
    edge_options = webdriver.EdgeOptions()
    edge_options.binary_location = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

    driver = webdriver.Edge(options=edge_options)
    driver.maximize_window()
    driver.get("http://182.163.99.86/dashboard")

    email_field = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "username")))
    email_field.send_keys("szrchayan@gmail.com")
    time.sleep(1)  # Introduce a delay after entering email

    password_field = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "password")))
    password_field.send_keys("Annotator@123")
    time.sleep(1)  # Introduce a delay after entering password

    login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/form/button")))
    login_button.click()
    time.sleep(3)  # Introduce a delay after clicking login

    WebDriverWait(driver, 20).until(EC.url_contains("dashboard"))
    assert "dashboard" in driver.current_url  # Check successful login

    project_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/section/main/aside/div/div/div/div[2]/a/div/span[2]")))
    project_button.click()
    time.sleep(3)

    view_project_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/section/main/div[2]/div[2]/section/div/div[2]/div/table/tbody/tr/td[9]/div/a")))
    view_project_button.click()
    time.sleep(3)

    # Click the ner_checkbox button
    start= driver.find_element(By.XPATH,'/html/body/div/section/main/div[2]/div[2]/section/section[4]/div/div/div[2]/div/table/tbody/tr/td[9]/div/a')
    start.click()

    loc1_tag = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/section/main/div[2]/div[2]/section[2]/div[1]/div/span[3]")))
    loc1_tag.click()
    time.sleep(3)

    actions = ActionChains(driver);
    search_field = driver.find_element(By.XPATH,"/html/body/div[1]/section/main/div[2]/div[2]/section[3]/div/div/div/span[6]")
    actions.double_click(search_field).perform()
    time.sleep(3)

    loc1_tag2 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section/main/div[2]/div[2]/section[2]/div[1]/div/span[2]")))
    loc1_tag2.click()
    time.sleep(3)

    actions = ActionChains(driver);
    search_field2 = driver.find_element(By.XPATH,"/html/body/div[1]/section/main/div[2]/div[2]/section[3]/div/div/div/span[7]")
    actions.double_click(search_field2).perform()
    time.sleep(3)

    actions = ActionChains(driver);
    search_field3 = driver.find_element(By.XPATH,"/html/body/div[1]/section/main/div[2]/div[2]/section[3]/div/div/footer/button[1]")
    actions.click(search_field3).perform()
    time.sleep(3)

    # Click the admin profile button
    admin_profile_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/section/main/div[2]/div[1]/nav/div/button/div/p[1]/span")))
    admin_profile_button.click()
    time.sleep(5)  # Introduce a delay after clicking admin

    # Click the logout button (which appears after clicking admin)
    logout_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div")))
    logout_button.click()
    time.sleep(3)  # Introduce a delay after clicking logout

    WebDriverWait(driver, 20).until(EC.url_contains("login"))
    assert "login" in driver.current_url  # Check successful logout

    time.sleep(1)  # Keep the browser open for 3 seconds after the test passes

    driver.quit()  # Quit the driver at the end of the test