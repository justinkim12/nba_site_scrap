from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
def set_site(num,year):
    SCROLL_PAUSE_TIME=0.5
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    url=f'https://www.nba.com/stats/search/team-game/?Season={year}&TeamID={num}&sort=GAME_DATE&dir=1&CF=PTS*gt*130'
    driver=webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get(url)
    driver.maximize_window()
    time.sleep(1)
    #elem=driver.find_element_by_name('q')
    #elem.send_keys('stephen curry')
    #elem.send_keys(Keys.RETURN)
    #driver.find_element_by_css_selector('.onetrust-accept-btn-handler').click()
    driver.find_element_by_css_selector('.fa.fa-times').click()
    time.sleep(0.5)
    driver.find_element_by_css_selector('.run-it').click()
    time.sleep(0.5)
    for c in range(0,5):
        driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
        time.sleep(SCROLL_PAUSE_TIME)
    driver.find_element_by_css_selector('.addrows__button').click()
    for c in range(0,3):
        driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
        time.sleep(SCROLL_PAUSE_TIME)
    html=driver.page_source
    #driver.find_elements_by_css_selector('.nowrap.text').click()

    return html
#set_site()
#def visit_site()        
