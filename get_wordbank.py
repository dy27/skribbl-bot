from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()

# Disable browser notifications
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs", prefs)

chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.set_page_load_timeout("100")


driver.get("https://skribbliohints.github.io/")
print(WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "wordDiv0"))).text)

with open("wordbank.txt", "w") as f:
    i = 0
    while True:
        word = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, "wordDiv" + str(i)))).text
        f.write(word + '\n')
        print(word)
        i += 1



