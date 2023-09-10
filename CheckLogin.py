from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options  

chrome_options = Options()
chrome_options.add_argument('--headless')  # Enable headless mode

# Create a WebDriver instance with ChromeOptions
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://shayansaha85.github.io/LoginPageDemoFromPipeline/")

username_input_box = driver.find_element(By.ID, "username")
password_input_box = driver.find_element(By.ID, "password")

username_input_box.send_keys("admin")
password_input_box.send_keys("admin")

driver.find_element(By.XPATH, "//*[@id=\"loginForm\"]/input[3]").click()
driver.implicitly_wait(5)

assertionText = driver.find_element(By.XPATH, "/html/body/h1").text
print(assertionText)
expected_text = "Hey Admin! Login successful"
assert expected_text == assertionText

driver.quit()
