from selenium import webdriver
import winsound
import time

# Retrieve the username from the environment
username = "ur_username"
password = "ur_password"
frequency = 1500
duration = 800
value1 = 7
value2 = 13

url = "https://academic.ui.ac.id/main/Authentication/"

driver = webdriver.Chrome(
    executable_path=r"C:\Users\luthf\Downloads\chromedriver\chromedriver.exe")
driver.get(url)


def make_sound():
    for i in range(1, 3):
        winsound.Beep(frequency, duration)


driver.find_element("xpath", "//*[@id=\"u\"]").send_keys(username)
driver.find_element(
    "xpath", "//*[@id=\"login\"]/form/p[2]/input").send_keys(password)
driver.find_element("xpath", "//*[@id=\"submit\"]/input").click()

driver.get("https://academic.ui.ac.id/main/Academic/HistoryByTerm#")
driver.find_element(
    "xpath", "//*[@id=\"ti_m1\"]/div[3]/table/tbody/tr/td/table/tbody/tr[35]/td[8]/span/a").click()
driver.find_element("xpath", "//*[@id=\"proceed-button\"]").click()

print("Value 1:", value1)
print("Value 2:", value2)

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

time.sleep(30)
