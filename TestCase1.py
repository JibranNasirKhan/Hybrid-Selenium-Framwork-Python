from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


class Filter_all_1stops():
    def search_all(self ):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        # wait = driver.implicitly_wait(10)
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        # driver.find_element(By.XPATH,"//a[@title='One Way']").click()
        # driver.find_element(By.XPATH, "// input[ @ id = 'BE_flight_origin_city']").click()
        wait = WebDriverWait(driver,10)
        wait.until(EC.element_to_be_clickable((By.XPATH,"// input[ @ id = 'BE_flight_origin_city']"))).click()
        dep_city = driver.find_element(By.XPATH, "// input[ @ id = 'BE_flight_origin_city']")
        dep_city.click()
        dep_city.send_keys("pune")

        search = driver.find_elements(By.XPATH,"(//div[@class='ac_results origin_ac'])[1]")
        print(len(search))
        for result in search:
            print(result.text)
            if "Pune (PNQ)" in result.text:
                result.click()
                break

        # driver.find_element(By.XPATH, "// input[ @ id = 'BE_flight_origin_city']").send_keys("pune")
        # time.sleep(2)
        # pune.send_keys(Keys.ENTER)
        # time.sleep(2)
        wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='BE_flight_arrival_city']")))
        arr_city = driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        arr_city.click()
        arr_city.send_keys("Delhi")
        # delhi.send_keys(Keys.ENTER)
        search2 = driver.find_elements(By.XPATH, "(//div[@class='ac_results dest_ac'])[1]")
        print(len(search2))
        for result in search2:
            print(result.text)
            if "New Delhi (DEL)" in result.text:
                result.click()
                break

        origin_date = driver.find_element(By.XPATH, "(// input[@ id='BE_flight_flsearch_btn'])[1]")
        # origin_date.click()
        wait = WebDriverWait(driver,10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_date'])[1]"))).click()
        all_dates = driver.find_elements(By.XPATH,"(//div[@id='month-scroll2'])[1]")
        # all_dates - driver.find_elements(By.CSS_SELECTOR,"body > div:nth-child(2) > div:nth-child(1) > section:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > section:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(2) > ul:nth-child(1) > li:nth-child(1) > section:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > table:nth-child(1) > tbody:nth-child(1)")
        print(len(all_dates))
        for date in all_dates:
            print(date.text)
            if "05 / 10 / 2022" in date.text:
                date.click()
                break

        # driver.find_element(By.ID, "05 / 10 / 2022").click()
        driver.find_element(By.XPATH, "(// input[@ id='BE_flight_flsearch_btn'])[1]").click()
        driver.find_element(By.XPATH, "//p[normalize-space()='1']").click()


run = Filter_all_1stops()
run.search_all()





