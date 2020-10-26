from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

WEBDRIVER_PATH= 'bin/chromedriver'
driver = webdriver.Chrome(executable_path=WEBDRIVER_PATH)
# suite
driver.get("https://instagram.com")
sleep(4)

#message navigateur
accepter = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/button[1]")
accepter.click()

#login 
username = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
username.send_keys("your username")

password = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
password.send_keys("your password")

submit = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]")
submit.click()

sleep(3)
print("go to home")
#enregistrer le mot de passe ?
home = driver.find_element_by_xpath("//button[contains(text(), 'Plus tard')]")
home.click()

sleep(3)
# les notification
notif = driver.find_element_by_xpath("//button[contains(text(), 'Plus tard')]")
notif.click()

sleep(3)

for i in range(5) :

	follow = driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[2]/div[2]/div/div/div/div[1]/div[3]/button/div")
	follow.click()
	sleep(1)
	driver.refresh()
