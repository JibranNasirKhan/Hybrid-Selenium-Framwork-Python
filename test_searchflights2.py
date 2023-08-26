# searching flight using pytest and launch page defined functions to search flights
import sys
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
sys.path.insert(0, "/pages")
from pages.yatra_launch_page import LaunchPage

@pytest.mark.usefixtures("setup")
class Search_file_verify():
    def Test_flight_are_correct(self):
        #   Launch website Yatra.com
        lp = LaunchPage(self.driver, self.wait)

        #   select departure city as pune
        lp.depart_from("Pune")
        #   select arrival city as London
        lp.depart_from("Lond")
        #   select date
        # Selecting the date as 13th Dec 2022
        date = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//label[@for='BE_flight_origin_date'])[1]")))
        date.click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//td[@id='13/12/2022'])[1]"))).click()

        # Searching the flights
        self.driver.find_element(By.XPATH, "(//input[@id='BE_flight_flsearch_btn'])[1]").click()
        time.sleep(4)

print("All good!!!")
time.sleep(4)
