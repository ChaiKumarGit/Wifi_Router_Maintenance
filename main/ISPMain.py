"""
Module to perform browser based operations.
"""
import time

from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Variables.GlobalVariables import *


def initialise_web_driver():
    global driver
    chrome_driver = webdriver.Chrome(seleniumDriverPath)
    # chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver = chrome_driver


def launch_isp_home():
    """
    Launch the default home page of router
    """
    initialise_web_driver()
    driver.get(host)
    driver.maximize_window()
    driver.find_element(By.XPATH, xpathUsername).send_keys(userName)
    driver.find_element(By.XPATH, xpathPassword).send_keys(userPassword)
    driver.find_element(By.XPATH, xpathLoginBtn).click()
    time.sleep(5)
    driver.close()


def reboot_router():
    """
    Launch the default home page of router and reboot router
    """
    initialise_web_driver()
    driver.get(host)
    driver.maximize_window()
    driver.find_element(By.XPATH, xpathUsername).send_keys(userName)
    driver.find_element(By.XPATH, xpathPassword).send_keys(userPassword)
    driver.find_element(By.XPATH, xpathLoginBtn).click()
    WebDriverWait(driver, waitTimeToLoad).until(
        EC.presence_of_element_located((By.LINK_TEXT, 'Administration'))).click()
    WebDriverWait(driver, waitTimeToLoad).until(
        EC.presence_of_element_located((By.LINK_TEXT, 'Reboot'))).click()
    # Switch to iframe of Reboot button
    driver.switch_to.frame(
        WebDriverWait(driver, waitTimeToLoad).until(
            EC.presence_of_element_located((By.XPATH, xpathRebootBtn_iframe))))
    WebDriverWait(driver, waitTimeToLoad).until(
        EC.presence_of_element_located((By.XPATH, xpathRebootBtn))).click()
    time.sleep(1)
    alert = driver.switch_to.alert
    alert.accept()
    time.sleep(120)
    driver.close()
    driver.quit()


if __name__ == "__main__":
    launch_isp_home()
    # reboot_router()
