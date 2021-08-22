from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

import time

favoriteMusic = "Maneskin Beggin"
driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

action = ActionChains(driver)

driver.get("https://www.google.com.br/")

driver.find_element(By.NAME, "q").send_keys("Youtube" + Keys.ENTER)

driver.maximize_window()

driver.find_element(
    By.XPATH, '/html/bod  y/div[7]/div/div[8]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[1]/a/h3').click()

driver.find_element(By.ID, "search").click()
driver.find_element(By.ID, "search").send_keys(
    favoriteMusic + Keys.ENTER)

time.sleep(2)

driver.find_element(
    By.XPATH, '/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/ytd-thumbnail/a/yt-img-shadow/img').click()

time.sleep(2)

fullscreen = driver.find_element(By.ID, "movie_player")

action.double_click(fullscreen)
action.perform()

# driver.quit()
