import time

import pytest
# from selenium import webdriver
from selenium.webdriver import Keys
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


# from selenium.webdriver.support.wait import WebDriverWait

@pytest.mark.usefixtures("setup")
class Test_Exp_Time():
    def test_all_search(self):
        # Launching the browser will be used using pytest conftest.py file


        # Provide departure city as Pune
        dep_city = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_city']")))
        dep_city.click()
        dep_city.send_keys("Mum")
        dep_city.send_keys(Keys.ENTER)

        search = self.driver.find_elements(By.XPATH, "(//div[@class='ac_results origin_ac'])[1]")
        print(len(search))
        for result in search:
            print(result.text)
            if "Mumbai (Bom)" in result.text:
                result.click()
                break

        # Provide arrival city as London
        dep_city = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id='BE_flight_arrival_city'])[1]")))
        dep_city.click()
        dep_city.send_keys("Lond")

        search2 = self.wait.until(EC.element_to_be_clickable((By.XPATH,"(//div[@class='ac_results dest_ac'])[1]")))\
            .find_elements(By.XPATH,"(//div[@class='ac_results dest_ac'])[1]")
        print(len(search2))
        for result in search2:
            print(result.text)
            if "London (LON)" in result.text:
                result.click()
                break

        # Selecting the date as 13th Dec 2022
        date = self.wait.until(EC.element_to_be_clickable((By.XPATH,"(//label[@for='BE_flight_origin_date'])[1]")))
        date.click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH,"(//td[@id='13/12/2022'])[1]"))).click()

        # Searching the flights
        self.driver.find_element(By.XPATH,"(//input[@id='BE_flight_flsearch_btn'])[1]").click()
        time.sleep(4)


print("All good!!!")
time.sleep(4)


