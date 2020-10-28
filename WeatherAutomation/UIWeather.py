import time

from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class UIWeather:
    def get_temperature_gui(self,GUIDataDict):
        driver = webdriver.Chrome()
        driver.implicitly_wait(15)
        driver.maximize_window()
        driver.delete_all_cookies()
        driver.get("https://weather.com/")
        UI_Dict = {"city": ["PrimaryTemperature", "WeatherType"]}
        wait = 15

        try:
            for i in GUIDataDict["City"]:
                try:
                    CityPostalCode = WebDriverWait(driver, wait).until(EC.element_to_be_clickable((By.ID, 'LocationSearch_input')))
                    CityPostalCode.click()
                    CityPostalCode.send_keys(i)
                except StaleElementReferenceException as e:
                    print("Stale Element Exception occurred, retrying to interact with the element ")
                    time.sleep(5)
                    CityPostalCode = WebDriverWait(driver, wait).until(
                        EC.element_to_be_clickable((By.ID, 'LocationSearch_input')))
                    CityPostalCode.click()
                    CityPostalCode.send_keys(i)
                SearchResult = f"//button[@data-testid='ctaButton' and  contains(text(),'{i}')][1]"
                driver.find_element_by_xpath(SearchResult).click()
                PrimaryTemperatureElement = WebDriverWait(driver, wait).until(EC.element_to_be_clickable((By.XPATH,"//div[contains(@class,'primary')]/span[@data-testid='TemperatureValue']")))
                PrimaryTemperatureValue = float((PrimaryTemperatureElement.text).replace('°',''))
                PrimaryPhrase = driver.find_element_by_xpath(
                    "//div[contains(@class,'primary')]/div[@data-testid='wxPhrase']").text
                UI_Dict[i] = [PrimaryTemperatureValue, PrimaryPhrase]

        except Exception as e:
            print(e)
        finally:
            driver.close()
            driver.quit()
        return UI_Dict
