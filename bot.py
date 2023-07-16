from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import time

driver = webdriver.Chrome()
driver.get(url="http://orteil.dashnet.org/experiments/cookie/")
timeout = time.time() + 60 * 5

while True:
    try:
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='cookie']"))).click()
        money = int(
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='money']"))).text)
        # checks every 5 seconds
        if round(time.time() % 5) == 0:

            if money > int(WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located((By.XPATH, "//*[@id='buyTime machine']/b"))).text.split()[-1].replace(
                ",", "")) \
                    :
                WebDriverWait(driver, 1).until(
                    EC.element_to_be_clickable((By.XPATH, "//*[@id='buyTime machine']/b"))).click()

            elif money > int(WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located((By.XPATH, "//*[@id='buyPortal']/b"))).text.split()[-1].replace(",",
                                                                                                                     "")) \
                    :
                WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='buyPortal']/b"))).click()

            elif money > int(WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located((By.XPATH, "//*[@id='buyAlchemy lab']/b"))).text.split()[-1].replace(
                ",", "")) \
                    :
                WebDriverWait(driver, 1).until(
                    EC.element_to_be_clickable((By.XPATH, "//*[@id='buyAlchemy lab']/b"))).click()

            elif money > int(WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located((By.XPATH, "//*[@id='buyShipment']/b"))).text.split()[-1].replace(",",
                                                                                                                       "")) \
                    :
                WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='buyShipment']/b"))).click()

            elif money > int(WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located((By.XPATH, "//*[@id='buyMine']/b"))).text.split()[-1].replace(",", "")) \
                    :
                WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='buyMine']/b"))).click()

            elif money > int(WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located((By.XPATH, "//*[@id='buyFactory']/b"))).text.split()[-1].replace(",",
                                                                                                                      "")) \
                    :
                WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='buyFactory']/b"))).click()

            elif money > int(WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located((By.XPATH, "//*[@id='buyGrandma']/b"))).text.split()[-1].replace(",",
                                                                                                                      "")) \
                    :
                WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='buyGrandma']/b"))).click()

            elif money > int(WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located((By.XPATH, "//*[@id='buyCursor']/b"))).text.split()[-1].replace(",",
                                                                                                                     "")) \
                    :
                WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='buyCursor']/b"))).click()
    except StaleElementReferenceException:
        pass
