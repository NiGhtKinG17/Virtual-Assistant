import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import os
from dotenv import load_dotenv
load_dotenv()

email = os.getenv('TWITTER_MAIL')
password = os.getenv('TWITTER_PASS')

def tweet_func(tweet):
    PATH = "C:\\Users\\Hritik\\Documents\\Projects\\KarenVA\\bot\\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://twitter.com/login")
    driver.implicitly_wait(3)
        
    driver.maximize_window()
    lemail = driver.find_element(By.XPATH,"//input[@autocomplete='username']")
    lemail.send_keys(email)
        
    next_btn = driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[6]/div')        
    next_btn.click()
    
    user_name = driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
    user_name.send_keys("botjake884")
    
    user_btn = driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div')
    user_btn.click()
        
    driver.implicitly_wait(5)
    lpassword = driver.find_element(By.XPATH,"//input[@autocomplete='current-password']")
    lpassword.send_keys(password)
        
    login_btn = driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div')
    login_btn.click()

    time.sleep(4)

    tweet_btn = driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div')
    tweet_btn.click()

    message_tf = driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
    message_tf.send_keys(tweet)

    send_tweet_btn = driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]')
    send_tweet_btn.click()
    time.sleep(10)