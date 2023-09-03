from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait  # Update the import
from selenium.webdriver.support import expected_conditions as EC
import time
# Create a new instance of the Chrome driver (make sure the ChromeDriver executable is in your PATH)

# Open the URL

roll_numbers = ['22BCA50265', '22BCA50266', '22BCA50267', '22BCA50268', '22BCA50269', '22BCA50270', '22BCA50271', '22BCA50272', '22BCA50273', '22BCA50274', '22BCA50275', '22BCA50276', '22BCA50277', '22BCA50278', '22BCA50279', '22BCA50280', '22BCA50281', '22BCA50282', '22BCA50283', '22BCA50284', '22BCA50285', '22BCA50286', '22BCA50287', '22BCA50288', '22BCA50289']
# Wait for the input element to be present and interact with it
try:

    for roll_number in roll_numbers:
        print(roll_number)
        driver = webdriver.Chrome()
        url = "https://jnvuiums.in/(S(utngqx2epnkpvwjwsas1y12w))/Results/ExamResultDeclare.aspx"  # Replace with your URL
        driver.get(url)
        
        wait = WebDriverWait(driver, 7)
        find_link_main = driver.find_element("css selector", "#LinkAnnual2023") #finding for current year result main link
        find_link_main.click() #after finding it will click

        find_link_BCA = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#dgResultUG_ctl04_lnkResultUG")))
        find_link_BCA.click()

        input_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".form-control")))
        input_element.clear()
        input_element.send_keys(roll_number)

        # Find and click the submit button
        submit_button = driver.find_element("css selector", "#btnGetResult")
        submit_button.click()


        # Close the browser window

        time.sleep(8)
        driver.quit()
except:
    e = Exception
    print(e)