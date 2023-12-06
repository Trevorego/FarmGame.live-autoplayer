# Metin Ege Özdemir / Trevorego
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def shop(driver):
    driver.get("https://farmgame.live/shop")
    time.sleep(5)
    
    buttons = driver.find_elements(By.XPATH, "//button[text()='x30']")

    for _ in range(8):
        buttons[13].click()

def farm(driver):
    driver.get("https://farmgame.live/plants")
    time.sleep(5)
    
    button = driver.find_element(By.XPATH, "//button[@class='item-slot']")
    tiles = driver.find_elements(By.XPATH, "//div[@style='width: 100%; height: 100%; position: relative; display: flex; justify-content: center; align-items: center;']")
    
    for i in range(4):
        button.click()
        
        for tile in tiles:
            tile.click()
        
        time.sleep(31)
        
        for _ in range(5):
            for tile in tiles:
                tile.click()
                time.sleep(6)

def market(driver):
    driver.get("https://farmgame.live/market")
    time.sleep(5)
    
    buttons = driver.find_elements(By.XPATH, "//button[@class='item-slot']")
    buttons[0].click()
    
    sell_button = driver.find_element(By.XPATH, "//div[text()='SELL ALL']")
    sell_button.click()
    

def gameplay(driver):
    farm(driver)
    """while True:
        shop(driver)
        
        farm(driver)
        
        market(driver)"""
        
        

def setup():
    #create chromeoptions instance
    options = webdriver.ChromeOptions()     

    #provide location where chrome stores profiles
    options.add_argument(r"--user-data-dir=C:\Users\metin\AppData\Local\Google\Chrome\User Data")

    #provide the profile name with which we want to open browser
    options.add_argument(r"--profile-directory=Default")

    #specify where your chrome driver present in your pc
    driver = webdriver.Chrome(options=options)

    #provide website url here
    driver.get("https://farmgame.live/shop")
    time.sleep(5)
    
    return driver

def main():
    driver = setup()
    
    gameplay(driver)

if __name__ == "__main__":
    main()

while True:
    pass