import time
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

def logintest1(email,password):

    edge_options = webdriver.EdgeOptions()
    edge_options.binary_location = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    driver = webdriver.Edge(options=edge_options)
    driver.get("http://182.163.99.86/dashboard")
    # Test Case 1
    email_field = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "username")))
    email_field.send_keys(email)
    time.sleep(1)
    password_field = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "password")))
    password_field.send_keys(password)
    time.sleep(1)
    login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/form/button")))
    login_button.click()
    time.sleep(3)
    driver.quit()
    
def logintest2(email,password):

    edge_options = webdriver.EdgeOptions()
    edge_options.binary_location = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    driver = webdriver.Edge(options=edge_options)
    driver.get("http://182.163.99.86/dashboard")
    # Test Case 2
    email_field = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "username")))
    email_field.send_keys(email)
    time.sleep(1)
    password_field = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "password")))
    password_field.send_keys(password)
    time.sleep(1)
    login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/form/button")))
    login_button.click()
    time.sleep(3)
    driver.quit()

def test_automation():

    # Automation Connection For Testing
    edge_options = webdriver.EdgeOptions()
    edge_options.binary_location = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    driver = webdriver.Edge(options=edge_options)
    driver.get("http://182.163.99.86/dashboard")

    #logintest1("admin@gigatech.com","Abc@122")
    #logintest2("admin@gigatech.com","Abc@123")

    email_field = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "username")))
    email_field.send_keys("admin@gigatech.com")
    time.sleep(1)
    password_field = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "password")))
    password_field.send_keys("Abc@123")
    time.sleep(1)


    login_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/form/button")))
    login_button.click()
    time.sleep(3)

    WebDriverWait(driver, 20).until(EC.url_contains("dashboard"))
    assert "dashboard" in driver.current_url
    user_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/section/main/aside/div/div/div/div[3]/a/div/span[2]")))
    user_button.click()
    time.sleep(3)

    add_user = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/section/main/div[2]/div[2]/section/div[2]/button")))
    add_user.click()
    time.sleep(3)

    user_name_field = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "full_name")))
    user_name_field.send_keys("all2")
    time.sleep(1)

    user_email_field = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "email")))
    user_email_field.send_keys("all2@gmail.com")
    time.sleep(1)

    gender_dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "gender")))
    gender_select = Select(gender_dropdown)
    gender_select.select_by_visible_text("Male")
    time.sleep(1)

    institutionfield = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "institution_name")))
    institutionfield.send_keys("North South University")
    time.sleep(1)

    qualificationfield = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "qualification")))
    qualificationfield.send_keys("Bsc in Computer Science")
    time.sleep(1)

    passwordfield = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "password")))
    passwordfield.send_keys("AbCd123@")
    time.sleep(1)

    mobilefield = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "mobile")))
    mobilefield.send_keys("01705745847")
    time.sleep(1)

    role_dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "role")))
    role = Select(role_dropdown)
    role.select_by_visible_text("VALIDATOR")
    time.sleep(3)

    add_user_form = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div[3]/button")))
    add_user_form.click()
    time.sleep(3)

    add_user_form = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section/main/aside/div/div/div/div[1]/a/div")))
    add_user_form.click()
    time.sleep(3)

    add_user_form = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section/main/div[2]/div[2]/section/div/div[1]/div[1]/div/button")))
    add_user_form.click()
    time.sleep(3)

    add_user_form = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section/main/div[2]/div[2]/section/div[1]/button")))
    add_user_form.click()
    time.sleep(3)

    p_name_field = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "name")))
    p_name_field.send_keys("Sqat")
    time.sleep(1)

    description_name_field = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "description")))
    description_name_field.send_keys("This is a project for Quality Assurance")
    time.sleep(1)

    cb = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "1")))
    cb.click()
    time.sleep(3)

    org_tag = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div/section[1]/div[2]/div/div/div/div[2]/button/div")))
    org_tag.click()
    time.sleep(3)

    # cb2 = WebDriverWait(driver, 20).until(
    #     EC.element_to_be_clickable((By.ID, "3")))
    # cb2.click()
    # time.sleep(3)
    #
    # cb3 = WebDriverWait(driver, 20).until(
    #     EC.element_to_be_clickable((By.ID, "5")))
    # cb3.click()
    # time.sleep(3)

    # caa = WebDriverWait(driver, 20).until(
    # EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div/div[3]/button")))
    # caa.click()
    # time.sleep(3)

    driver.quit()
