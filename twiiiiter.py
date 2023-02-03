
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from os import system
import time
import pickle

from selenium.webdriver.common.by import By
from get_tweet import *
import traceback


class Scraper:
    wait_time = 5
    options = webdriver.ChromeOptions()
    #options.add_argument('headless')
    driver = webdriver.Chrome(executable_path="chromedriver", options=options)  # to open the chromedriver    
    username_xpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input'
    
    button_xpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div'
    password_xpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'
    login_button_xpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div'
    like_button_xpath = '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[1]/div/div/div[1]/article/div/div/div/div[3]/div[7]/div/div[3]/div'
    test_tweet = 'https://twitter.com/Twitter/status/1580661436132757506'
    cookie_button_xpath = '//*[@id="layers"]/div/div/div/div/div/div[2]/div[1]/div/span/span'
    notification_button_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/div/span/span'
    reetweet_button_xpath = '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[1]/div/div/div[1]/article/div/div/div/div[3]/div[7]/div/div[2]/div'
    reetweet_confirm_button_xpath = '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div/div/div/div/div[2]/div/span'
    comment_button_xpath = '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[1]/div/div/div[1]/article/div/div/div/div[3]/div[7]/div/div[1]/div'
    textbox_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[2]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div'
    send_tweet_xpath = '/html/body/div[1]/div/div/div[2]/main/div/div/div[2]/div/div/div/div/div[3]/div/div'
    follow_button_xpath = "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[1]/div[2]/div[3]/div[1]/div"
    
def login(S,_username,_password):

    S.driver.get("https://twitter.com/i/flow/login")
    print("Starting Twitter")

    #USERNAME
    element = WebDriverWait(S.driver, 30).until(
    EC.presence_of_element_located((By.XPATH, S.username_xpath)))

    username = S.driver.find_element(By.XPATH,S.username_xpath)
    username.send_keys(_username)    
    
    element = WebDriverWait(S.driver, 30).until(
    EC.presence_of_element_located((By.XPATH, S.button_xpath)))


    #FIRST BUTTON

    button = S.driver.find_element(By.XPATH,S.button_xpath)
    button.click()
    print("button click")


    #PASSWORD

    element = WebDriverWait(S.driver, 30).until(
    EC.presence_of_element_located((By.XPATH, S.password_xpath)))
    
    password = S.driver.find_element(By.XPATH,S.password_xpath)
    password.send_keys(_password)
    print("password done")


    #LOGIN BUTTON

    element = WebDriverWait(S.driver, 30).until(
    EC.presence_of_element_located((By.XPATH, S.login_button_xpath)))
    
    login_button = S.driver.find_element(By.XPATH,S.login_button_xpath)
    login_button.click()
    print("login done")

    #print("Closing Twitter")


def accept_coockie(S):
    try:
        S.driver.get(S.test_tweet)

        element = WebDriverWait(S.driver, 30).until(
        EC.presence_of_element_located((By.XPATH, S.cookie_button_xpath)))
        
        cookie_button = S.driver.find_element(By.XPATH,S.cookie_button_xpath)
        cookie_button.click()

    except:
        print("error")
        pass    
    
    
    print("coockie done")


def accept_notification(S):
    try:
        S.driver.get(S.test_tweet)

        element = WebDriverWait(S.driver, 30).until(
        EC.presence_of_element_located((By.XPATH, S.notification_button_xpath)))
        
        cookie_button = S.driver.find_element(By.XPATH,S.notification_button_xpath)
        cookie_button.click()
    except:
        pass    
    try:
        S.driver.get(S.test_tweet)

        element = WebDriverWait(S.driver, 30).until(
        EC.presence_of_element_located((By.XPATH, S.cookie_button_xpath)))
        
        cookie_button = S.driver.find_element(By.XPATH,S.cookie_button_xpath)
        cookie_button.click()

    except:
        print("error")
        pass    
    
    print("notification done")
    
    
def like_a_tweet(S,url):
    S.driver.get(url)
    element = WebDriverWait(S.driver, 30).until(
    EC.presence_of_element_located((By.XPATH, S.like_button_xpath)))
    
    like_button = S.driver.find_element(By.XPATH,S.like_button_xpath)
    #time.sleep(3000)
    # check the "aria-pressed" attribute
    like_button.click()
    
    #if like_button.get_attribute("aria-label") != "Aimer":
    #    print("You have liked the tweet.")
    #    return False
    #else:
    #    like_button.click()
    #    print("You have not liked the tweet yet.")
    #    return True

def reetweet_a_tweet(S,url):
    S.driver.get(url)
    element = WebDriverWait(S.driver, 30).until(
    EC.presence_of_element_located((By.XPATH, S.reetweet_button_xpath)))
    
    reetweet_button = S.driver.find_element(By.XPATH,S.reetweet_button_xpath)
    reetweet_button.click()

    element = WebDriverWait(S.driver, 30).until(
    EC.presence_of_element_located((By.XPATH, S.reetweet_confirm_button_xpath)))
    
    reetweet_button = S.driver.find_element(By.XPATH,S.reetweet_confirm_button_xpath)
    reetweet_button.click()
    
    print("reetweet done")



def comment_a_tweet(S,url,text):

    print("coment part zero")

    S.driver.get(url)
    element = WebDriverWait(S.driver, 30).until(
    EC.presence_of_element_located((By.XPATH, S.comment_button_xpath)))
    
    comment_button = S.driver.find_element(By.XPATH,S.comment_button_xpath)
    comment_button.click()

    print("coment part one")
    
    element = WebDriverWait(S.driver, 30).until(
    EC.presence_of_element_located((By.XPATH, S.textbox_xpath)))
    
    textbox = S.driver.find_element(By.XPATH,S.textbox_xpath)
    textbox.click()
    time.sleep(S.wait_time)
    textbox.send_keys(text)
    
    print("coment part two")
    time.sleep(5)
    
    element = WebDriverWait(S.driver, 30).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="tweetButton"]')))

    wait = WebDriverWait(S.driver, 10)
    target_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="tweetButton"]')))

    S.driver.execute_script("arguments[0].scrollIntoView();", target_element)

    target_element.click()

#    send_tweet = S.driver.find_element(By.CSS_SELECTOR,'[data-testid="tweetButton"]')
#    send_tweet.click()
    print("comment part three")
    

def follow_an_account(S,account):
    
    S.driver.get("https://twitter.com/"+account)
    element = WebDriverWait(S.driver, 30).until(
    EC.presence_of_element_located((By.XPATH, S.follow_button_xpath)))
    
    follow_button = S.driver.find_element(By.XPATH,S.follow_button_xpath)
    follow_button.click()

    print("You've followed another account")

def main():

    with open("configuration.yml", "r") as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
    
    print("Starting the program")
    print("Searching for Giveaway")
    username_password = data["account_info"]
    tweets_text,tweets_url,tweets_full_comment,tweets_account_to_follow = search_giveaway()
    time.sleep(1)
    S = Scraper()
    login(S,username_password[0],username_password[1])
    time.sleep(3)   
    accept_coockie(S)
    time.sleep(S.wait_time)    
    accept_notification(S)
    time.sleep(S.wait_time)
    accept_coockie(S)
    time.sleep(S.wait_time)
    
    for i in range(len(tweets_url)):
        like = like_a_tweet(S,tweets_url[i])
        time.sleep(S.wait_time)    
        
        #if like == True or like == False:
        reetweet_a_tweet(S,tweets_url[i])
        time.sleep(S.wait_time)        
        
        comment_a_tweet(S,tweets_url[i],"ça_ne_marche_pas_quand_je_tag_des_comptes_jsp_pk")
        time.sleep(S.wait_time)
        
    for account_to_follow in tweets_account_to_follow:
        follow_an_account(S,account_to_follow)
        time.sleep(S.wait_time)
    
    print("End of the program")
    #comment_a_tweet(S,"cacaboudin")
    #time.sleep(S.wait_time)
    #make_tweet()
    #else:
    #    print("caca boudin")

try:
    main()
except Exception as e:
    print("Bip Bip Elon Musk")
    if "Message: unknown error: net::ERR_INTERNET_DISCONNECTED" in str(e):
        print("No connection")
    else:
        print("Another type of error")
        print(traceback.format_exc())