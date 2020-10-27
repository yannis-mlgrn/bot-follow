from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from random import *

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

sleep(6)
print("go to home")
#enregistrer le mot de passe ?
home = driver.find_element_by_xpath("//button[contains(text(), 'Plus tard')]")
home.click()

sleep(3)
# les notification
notif = driver.find_element_by_xpath("//button[contains(text(), 'Plus tard')]")
notif.click()

sleep(3)
nbfollow = 0

while True :

	print("bot start")

	for i in range(5) :
		nbfollow =int(nbfollow)
		follow = driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[2]/div[2]/div/div/div/div[1]/div[3]/button/div")
		#compte = driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[1]/div/span/a")
		#str(compte)
		follow.click()
		sleep(1)
		nbfollow = nbfollow + 1
		nbfollow = str(nbfollow)
		print("["+ nbfollow+ "]")
		print("le bot a follow " + nbfollow + " personnes")
		driver.refresh()

	pause = randrange(20,120)
	pause = str(pause)
	print("pause : " + pause + "s")
	pause = int(pause)
	sleep(pause)


