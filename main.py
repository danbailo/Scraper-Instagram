from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_browser(url):
	options = webdriver.ChromeOptions()
	options.add_argument('headless')
	options.add_argument('no-sandbox')
	options.add_argument('disable-dev-shm-usage')
	driver = webdriver.Chrome(options=options)
	driver.get(url)
	return driver


if __name__ == "__main__":
    url = r"https://www.instagram.com/danbailo1"
    driver = get_browser(url)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    
    a_tags = soup.find("article").findAll("a")

    for a in a_tags:
        print(a.find("img"))

    # for link in a_tags:
    #     get_browser(url+link.get("href")).get_screenshot_as_file(f"{i}.png")
    #     i += 1
    # driver.quit()