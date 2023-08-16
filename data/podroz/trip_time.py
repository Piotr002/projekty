import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import datetime

dataframe = pd.DataFrame(columns=["czas", "Wroclaw - Bialy Dunajec", "Wroclaw - Krakow", "Krakow - Bialy Dunajec"])

options = webdriver.ChromeOptions()
options.headless = False
options.add_argument("--window-size=1920,1080")
options.add_argument("–disable-gpu")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.maximize_window()
driver.get("https://www.google.com/maps/dir///@52.4010064,16.920086,17z/data=!4m2!4m1!3e0?hl=pl-PL&entry=ttu")

zaakceptuj = driver.find_element(By.XPATH, "//span[text()='Zaakceptuj wszystko']")
zaakceptuj.click()

while datetime.datetime.now().hour < 11:
    try:
        driver.get("https://www.google.com/maps/dir///@52.4010064,16.920086,17z/data=!4m2!4m1!3e0?hl=pl-PL&entry=ttu")
        samochodem = driver.find_element(By.XPATH, "//img[@data-tooltip='Samochodem']")
        samochodem.click()
        wroclaw = driver.find_element(By.XPATH, "//input[@tooltip='Wybierz punkt początkowy lub kliknij mapę...']")
        bialy = driver.find_element(By.XPATH, "//input[@tooltip='Wybierz punkt docelowy...']")
        wroclaw.send_keys("Wrocław")
        bialy.send_keys("Biały Dunajec")
        bialy.send_keys(Keys.ENTER)
        time.sleep(5)
        czas = driver.find_element(By.XPATH, "//div[@jstcache='82' and @class='cGRe9e']")
        temp = czas.text.replace(" h ", " ").replace(" min", "").split(" ")
        wro_bia = 60 * int(temp[0]) + int(temp[1])
        driver.get("https://www.google.com/maps/dir///@52.4010064,16.920086,17z/data=!4m2!4m1!3e0?hl=pl-PL&entry=ttu")
        samochodem = driver.find_element(By.XPATH, "//img[@data-tooltip='Samochodem']")
        samochodem.click()
        wroclaw = driver.find_element(By.XPATH, "//input[@tooltip='Wybierz punkt początkowy lub kliknij mapę...']")
        krakow = driver.find_element(By.XPATH, "//input[@tooltip='Wybierz punkt docelowy...']")
        wroclaw.send_keys("Wrocław")
        krakow.send_keys("Balice, 32-083")
        krakow.send_keys(Keys.ENTER)
        time.sleep(5)
        czas = driver.find_element(By.XPATH, "//div[@jstcache='82' and @class='cGRe9e']")
        temp = czas.text.replace(" h ", " ").replace(" min", "").split(" ")
        wro_kra = 60 * int(temp[0]) + int(temp[1])
        driver.get("https://www.google.com/maps/dir///@52.4010064,16.920086,17z/data=!4m2!4m1!3e0?hl=pl-PL&entry=ttu")
        samochodem = driver.find_element(By.XPATH, "//img[@data-tooltip='Samochodem']")
        samochodem.click()
        krakow = driver.find_element(By.XPATH, "//input[@tooltip='Wybierz punkt początkowy lub kliknij mapę...']")
        bialy = driver.find_element(By.XPATH, "//input[@tooltip='Wybierz punkt docelowy...']")
        krakow.send_keys("Balice, 32-083")
        bialy.send_keys("Biały Dunajec")
        bialy.send_keys(Keys.ENTER)
        time.sleep(5)
        czas = driver.find_element(By.XPATH, "//div[@jstcache='82' and @class='cGRe9e']")
        temp = czas.text.replace(" h ", " ").replace(" min", "").split(" ")
        kra_bia = 60 * int(temp[0]) + int(temp[1])
        day = datetime.datetime.now().day if len(str(datetime.datetime.now().day)) == 2 else f"0{datetime.datetime.now().day}"
        month = datetime.datetime.now().month if len(str(datetime.datetime.now().month)) == 2 else f"0{datetime.datetime.now().month}"
        minute = datetime.datetime.now().minute if len(str(datetime.datetime.now().minute)) == 2 else f"0{datetime.datetime.now().minute}"
        new_row = {"czas":f"{day}.{month}, {datetime.datetime.now().hour}:{minute}",
            "Wroclaw - Bialy Dunajec":wro_bia,
            "Wroclaw - Krakow": wro_kra,
            "Krakow - Bialy Dunajec": kra_bia}
        dataframe.loc[len(dataframe)] = new_row
        time.sleep(600)
    except:
        pass

driver.close()
driver.quit()

dataframe.to_csv("czas.csv", index=False)