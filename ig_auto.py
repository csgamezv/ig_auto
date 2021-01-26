from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
#from csv import *
import time
PATH = "/Users/cesargamez/Selenium/chromedriver"
YEAR = 2021
def main(bypass=False ):
    #password : AMEZG88ESA

    #takes input from user and checks to insure that can login
    print("Input username and password")
    user_and_pass = get_login_info()
    username = user_and_pass[0]
    password = user_and_pass[1]
    ig_tag =  str(input("Ig tag you want to send message to? : "))
    message = str(input("Type in message you want to send: "))
    #time input
    print("Now input the date and time you want it to send in numbers only")
    month = int(input("Month:"))
    day = int(input("Day:"))
    hour = int(input("Hour:"))
    minute = int(input("Minute:"))
    #makes the time go by until needed execution
    TimeDiff(YEAR, month, day,hour, minute)
    #starts creating browser and executes message
    browser  = Chrome(PATH)
    browser.get("https://instagram.com")
    login(username,password,browser)
    access_messages(ig_tag,browser)
    send_message(message,browser)
    browser.quit()

def get_login_info():
    
    verified = False
    while not verified:
        username = str(input("Username: "))
        password = str(input("Password: "))
        print("Verifying....")
        verified = verify_login(username, password)
        if verified == False:
            print("Incorrect login info try again.")
    return [username,password]
def verify_login(username,password):
    verified_or_not = False
    with Chrome(PATH) as tester_browser:
        tester_browser.get("https://instagram.com")
        login(username, password, tester_browser)
        #implement if it finds "incorrect" then return False if not then return True,
        try:
            
            main = WebDriverWait(tester_browser, timeout=5).until(
            EC.presence_of_element_located((By.ID,"slfErrorAlert" ))
            )
            print(main)
            print("Not verified")
            
            verified_or_not = False
        except:   
            print("Verified")
            verified_or_not = True
    return verified_or_not

def login(username,password,browser):
    typebox_username = Waits("username",By.NAME,browser,"login")
    typebox_password = browser.find_element_by_name("password")
    typebox_username.send_keys(username)
    typebox_password.send_keys(password)
    typebox_password.send_keys(Keys.RETURN)
    
def access_messages(ig_tag,browser):
  
    press_inbox= Waits("bqXJH",By.CLASS_NAME,browser, "access_messages")
    press_inbox.click()
    
    press_Notnow= Waits("aOOlW.HoLwm",By.CLASS_NAME,browser, "access_messages")
    press_Notnow.click()
   
    press_igtag = Waits("//div[text()='"+ ig_tag + "']",By.XPATH,browser, "access_messages")
    press_igtag.click()
    
def send_message(text,browser):
    textarea = browser.find_element_by_tag_name("textarea")
    textarea.send_keys(text)
    textarea.send_keys(Keys.RETURN)

def Waits(id_name, class_name, browser,function_type):
    try:
        
        main = WebDriverWait(browser, timeout=7).until(
            EC.presence_of_element_located((class_name, id_name))
            )
        return main
    except:
        #troubleshooting
        if function_type == "login":
            print("Login page did not load in time or unresponsive.")
        elif class_name == By.XPATH:
            print("Could not find name.")
        elif function_type == "access_messages":
            print("Instagram home page did not load.")
        else:
            print("Error: Couldn't load page in 10 seconds")
        raise TypeError 
def sleep(n):
    for _ in range(n):
        time.sleep(1)

def TimeDiff(year, month, day, hour, minute):
    current_time = datetime.now()
    time_until_execute = datetime(year, month, day, hour, minute)

    TimePrinter(current_time,time_until_execute)
    Time_yet = False
    while not Time_yet:
        sleep(30)
        current_time = datetime.now()
        if current_time >= time_until_execute:
            Time_yet = True
            break
        TimePrinter(current_time,time_until_execute)
def TimePrinter(current_time, time_until_execute):
    difference = time_until_execute - current_time
    in_minutes = int(difference.total_seconds()) // 60
    print(str(in_minutes) + " minutes until execution")

main(False)


