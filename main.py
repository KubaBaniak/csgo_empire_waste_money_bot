from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from pathlib import Path
import urllib.request
import zipfile
from datetime import datetime


PATH_DRIVER = r"C:\Program Files (x86)\chromedriver.exe"
PATH_DOWNLOADS = r"C:\Users\Kuba\Pobrane"
chromediver_file = Path(PATH_DRIVER)

if not chromediver_file.is_file():
    print("Downloading chromedriver and moving it into safe folder...")
    urllib.request.urlretrive("https://chromedriver.storage.googleapis.com/105.0.5195.52/chromedriver_win32.zip", "chromedriver_win32.zip")
    with zipfile.ZipFile("{}\chromedriver_win32.zip".format(PATH_DOWNLOADS), 'r') as zip_ref:
        zip_ref.extractall(PATH_DRIVER)
    print("Downloaded and moved, we can begin")
else:
    print("Chromedirver already installed")

driver = webdriver.Chrome(PATH_DRIVER)
print("Input bet size (automatically set to 0.1 coins)")
BET_SIZE = float(input(">").replace(",", "."))
if not isinstance(BET_SIZE, float):
    print("Incorrect bet size\nRestart program and try again\nEx. 1.15 / 1.00 / 10\nFOR NOW, BET SIZE IS SET TO 0.10")
    BET_SIZE = 0.1


print("Log into your steam account via browser which just opened")

driver.get("https://csgoempire.com/")

_ = input("PRESS ENTER WHEN READY")

current_coins = float(driver.find_element(By.XPATH,
                                          '/html/body/div[1]/div[1]/div[2]/div[2]/div/div[1]/div/div/span/span/div/span').text.replace(',', '.'))
print(current_coins)

while True:
    coins_at_the_beggining = float(driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div[1]/div[2]/div[2]/div/div[1]/div/div/span/span/div/span'
                                                       ).text.replace(',', '.'))

    print(datetime.now().strftime("%H:%M:%S"), coins_at_the_beggining)

    if coins_at_the_beggining >= current_coins:
        BET_SIZE = 0.1

        driver.find_element(By.XPATH,
                            '/html/body/div/div[1]/div[3]/div/div/div[1]/div[2]/div/div[4]/div/div[1]/input'
                            ).clear()

        driver.find_element(By.XPATH,
                            '/html/body/div/div[1]/div[3]/div/div/div[1]/div[2]/div/div[4]/div/div[1]/input'
                            ).send_keys(BET_SIZE)

    else:
        driver.find_element(By.XPATH,
                            '/html/body/div[1]/div[1]/div[3]/div/div/div[1]/div[2]/div/div[4]/div/div[2]/div/div[8]/button'
                            ).click()

    driver.find_element(By.XPATH,
                        '/html/body/div[1]/div[1]/div[3]/div/div/div[1]/div[2]/div/div[5]/div[1]/button'
                        ).click()

    time_to_wait = float(driver.find_element(By.XPATH,
                                             '/html/body/div[1]/div[1]/div[3]/div/div/div[1]/div[2]/div/div[2]/div[3]/div/div[2]'
                                             ).text.replace(',', '.'))

    current_coins = float(driver.find_element(By.XPATH,
                                              '/html/body/div[1]/div[1]/div[2]/div[2]/div/div[1]/div/div/span/span/div/span'
                                              ).text.replace(',', '.'))
    sleep(time_to_wait+10)
    BET_SIZE *= 2