import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

#user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
drivers_path="C:\\Users\\Raghav\\chromedriver_win32 (2)\\chromedriver.exe"
chrome_service=Service(drivers_path)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")
browser=webdriver.Chrome(service=chrome_service,options=options)
browser.get("https://www.google.com/")
x=browser.find_element(By.NAME, "q")
x.send_keys("python")
x.send_keys(Keys.ENTER)
browser.find_element(By.PARTIAL_LINK_TEXT,"python.org").click()
browser.execute_script("window.scrollTo(0,200)")
browser.find_element(By.PARTIAL_LINK_TEXT,"docs.python").click()
time.sleep(5)
browser.execute_script("window.open('');")
browser.execute_script("window.open('');")
browser.execute_script("window.open('');")
browser.switch_to.window(browser.window_handles[1])
time.sleep(5)
browser.get("https://www.google.com/")
time.sleep(5)
y=browser.find_element(By.NAME, "q")
y.send_keys("fb")
time.sleep(3)
y.send_keys(Keys.ENTER)

