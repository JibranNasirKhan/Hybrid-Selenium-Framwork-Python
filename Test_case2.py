import time
from selenium import webdriver
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class Exp_Time():
    def all_search(self):
        # Launching the browser
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        wait = WebDriverWait(driver, 10)
        driver.get("https://Yatra.com")
        driver.maximize_window()

        # Provide departure city as Pune
        dep_city = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_city']")))
        dep_city.click()
        dep_city.send_keys("Pune")
        dep_city.send_keys(Keys.ENTER)

        search = driver.find_elements(By.XPATH, "(//div[@class='ac_results origin_ac'])[1]")
        print(len(search))
        for result in search:
            print(result.text)
            if "Pune (PNQ)" in result.text:
                result.click()
                break

        # Provide arrival city as London
        dep_city = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id='BE_flight_arrival_city'])[1]")))
        dep_city.click()
        dep_city.send_keys("Lond")

        search2 = wait.until(EC.element_to_be_clickable((By.XPATH,"(//div[@class='ac_results dest_ac'])[1]")))\
            .find_elements(By.XPATH,"(//div[@class='ac_results dest_ac'])[1]")
        print(len(search2))
        for result in search2:
            print(result.text)
            if "London (LON)" in result.text:
                result.click()
                break

        # Selecting the date as 13th Dec 2022
        date = wait.until(EC.element_to_be_clickable((By.XPATH,"(//label[@for='BE_flight_origin_date'])[1]")))
        date.click()
        wait.until(EC.element_to_be_clickable((By.XPATH,"(//td[@id='13/12/2022'])[1]"))).click()

        # Searching the flights
        driver.find_element(By.XPATH,"(//input[@id='BE_flight_flsearch_btn'])[1]").click()
        time.sleep(4)


print("All good!!!")
time.sleep(4)

All_city = Exp_Time()
All_city.all_search()

