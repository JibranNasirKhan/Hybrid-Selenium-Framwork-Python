from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class LaunchPage():
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        # selecting the Departure city

    def depart_from(self, departure_city):
        dep_city = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_city']")))
        dep_city.click()
        dep_city.send_keys(departure_city)
        dep_city.send_keys(Keys.ENTER)

        search = self.driver.find_elements(By.XPATH, "(//div[@class='ac_results origin_ac'])[1]")
        print(len(search))
        for result in search:
            print(result.text)
            if departure_city in result.text:
                result.click()
                break

        # selecting the arrival city
    def arrival_city(self, arrival_city):
        dep_city = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id='BE_flight_arrival_city'])[1]")))
        dep_city.click()
        dep_city.send_keys(arrival_city)
        dep_city.send_keys(Keys.ENTER)

        search2 = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='ac_results dest_ac'])[1]"))) \
            .find_elements(By.XPATH, "(//div[@class='ac_results dest_ac'])[1]")
        print(len(search2))
        for result in search2:
            print(result.text)
            if arrival_city in result.text:
                result.click()
                break

        # Selecting the date as 13th Dec 2022

    def Select_date(self):
        date = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//label[@for='BE_flight_origin_date'])[1]")))
        date.click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//td[@id='13/12/2022'])[1]"))).click()

