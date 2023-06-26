from http.server import executable
from lib2to3.pgen2 import driver
from selenium import webdriver
import requests
import winsound
import time
import random
# import sys
import ssl
# Credit to @luthfiimm
username = "ur_username"
password = "ur_password"
frequency = 1500  # Set Frequency To 2500 Hertz
duration = 800  # Set Duration To 1000 ms == 1 second
loop = 0
max = 2
value1 = 7
value2 = 13

url = "https://academic.ui.ac.id/main/Authentication/"

driver = webdriver.Chrome(
    executable_path=r"C:\Users\luthf\Downloads\chromedriver\chromedriver.exe")

driver.get(url)

driver.find_element("xpath", "//*[@id=\"u\"]").send_keys(username)
driver.find_element(
    "xpath", "//*[@id=\"login\"]/form/p[2]/input").send_keys(password)
driver.find_element("xpath", "//*[@id=\"submit\"]/input").click()

# Goes to path this https://academic.ui.ac.id/main/Academic/HistoryByTerm#
driver.get("https://academic.ui.ac.id/main/Academic/HistoryByTerm#")

# Real case

# looping from number 28 to 35
for i in range(27, 35):
    try:
        # Click this XPATH //*[@id="ti_m1"]/div[3]/table/tbody/tr/td/table/tbody/tr[28]/td[8]/span/a to click edom
        driver.find_element(
            "xpath", "//*[@id=\"ti_m1\"]/div[3]/table/tbody/tr/td/table/tbody/tr[" + str(i) + "]/td[8]/span/a").click()
        # Click continue the page in XPATH //*[@id="proceed-button"]
        driver.find_element("xpath", "//*[@id=\"proceed-button\"]").click()

        # Reset value to the max
        value1 = 7
        value2 = 13
        # Check index of matkul
        if i == 30:  # Matkul DMJ, bu diyana = 6(5), pak elvian = 13(6)
            value1 = 6
        # Matkul MATEK atau matkul SBD, pak Yan = 2(1)
        elif i == 31 or i == 33:
            value1 = 2
        elif i == 34:  # Matkul OS, pak Yan = 2(1)
            value2 = 2

        print("Value 1:", value1)
        print("Value 2:", value2)
        # Loop from 3 to 21
        for j in range(3, 22):
            try:
                # Select radio button for teacher 1
                driver.find_element(
                    "xpath", f"//*[@id=\"pertanyaan\"]/tbody/tr[{j}]/td[{value1}]/input").click()
                print("Pass 1 for teacher 1")
                # Check if the radio button for teacher 2 exists
                if driver.find_element("xpath", "//*[@id=\"pertanyaan\"]/tbody/tr[3]/td[13]/input"):
                    # Select radio button for teacher 2
                    driver.find_element(
                        "xpath", f"//*[@id=\"pertanyaan\"]/tbody/tr[{j}]/td[{value2}]/input").click()
                    print("Pass 2 for teacher 2")
            except Exception as e:
                print("Error:", str(e))

        # Pause 5 seconds to check the input
        time.sleep(5)
        # Submit the form in xpath //*[@id="pertanyaan"]/tbody/tr[23]/td/input
        driver.find_element(
            "xpath", "//*[@id=\"pertanyaan\"]/tbody/tr[23]/td/input").click()
    except Exception as e:
        print("Error:", str(e))
