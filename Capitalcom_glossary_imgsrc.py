import webdriver_manager.core.manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.ie.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def interceptor(request):
    request.headers['accept-language'] = 'en-Us'


options = webdriver.ChromeOptions()
options.add_argument("--lang= en")



driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.request_interceptor = interceptor

driver.get('https://capital.com/financial-dictionary')
articles = driver.find_element(by=By.XPATH, value='//div[@class=\'alphabet-category\']')
urls = articles.find_elements(by=By.TAG_NAME, value='a')
links = []
for url in urls:
    links.append(url.get_attribute('href'))

for link in links:
    driver.get(link)
    image = driver.find_element(by=By.XPATH, value='//figure[@class=\'detail__preview gapXs\']/img')
    img_src = image.get_attribute('src')
    # if '%20' in img_src:
    driver.get(img_src)
    try:
        driver.find_element(by=By.TAG_NAME, value='html')
    except:
        print(link + "=>" + img_src)





