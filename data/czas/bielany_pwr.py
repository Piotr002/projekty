import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import datetime

dataframe = pd.DataFrame(columns=["czas", "Bielany - pwr"])

options = webdriver.ChromeOptions()
options.headless = False
options.add_argument("--window-size=1920,1080")
options.add_argument("–disable-gpu")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.maximize_window()
driver.get("https://www.google.com/maps/dir///@52.4010064,16.920086,17z/data=!4m2!4m1!3e0?hl=pl-PL&entry=ttu")

zaakceptuj = driver.find_element(By.XPATH, "//span[text()='Zaakceptuj wszystko']")
zaakceptuj.click()

while datetime.datetime.now().hour < 20:
    try:
        driver.get("https://www.google.com/maps/dir///@52.4010064,16.920086,17z/data=!4m2!4m1!3e0?hl=pl-PL&entry=ttu")
        samochodem = driver.find_element(By.XPATH, "//img[@data-tooltip='Samochodem']")
        samochodem.click()
        bielany = driver.find_element(By.XPATH, "//input[@tooltip='Wybierz punkt początkowy lub kliknij mapę...']")
        pwr = driver.find_element(By.XPATH, "//input[@tooltip='Wybierz punkt docelowy...']")
        bielany.send_keys("Bielany Wrocławskie")
        pwr.send_keys("Politechnika Wrocławska")
        pwr.send_keys(Keys.ENTER)
        time.sleep(6)
        czas = driver.find_element(By.XPATH, "//div[@jstcache='82' and @class='cGRe9e']")
        temp = czas.text.replace(" h ", " ").replace(" min", "").split(" ") if "h" in czas.text else czas.text.replace(" min", "")
        bie_pwr = 60 * int(temp[0]) + int(temp[1]) if "h" in czas.text
        day = datetime.datetime.now().day if len(str(datetime.datetime.now().day)) == 2 else f"0{datetime.datetime.now().day}"
        month = datetime.datetime.now().month if len(str(datetime.datetime.now().month)) == 2 else f"0{datetime.datetime.now().month}"
        minute = datetime.datetime.now().minute if len(str(datetime.datetime.now().minute)) == 2 else f"0{datetime.datetime.now().minute}"
        new_row = {"czas":f"{day}.{month}, {datetime.datetime.now().hour}:{minute}",
            "Bielany - pwr":bie_pwr}
        dataframe.loc[len(dataframe)] = new_row
        time.sleep(180)
    except:
        pass

driver.close()
driver.quit()

dataframe.to_csv(f"czas{datetime.datetime.now().hour}.csv", index=False)