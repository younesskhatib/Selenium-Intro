import selenium
from selenium import webdriver
path= '/Users/younes/Downloads/chromedriver'
driver=webdriver.Chrome(path)
driver.get('https://www.instagram.com')
# driver.implicitly_wait(10)
#print(driver.title)
cookies=driver.find_element_by_xpath('/html/body/div[2]/div/div/button[1]')
cookies.click()
username_login=driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
username_login.clear()
username_login.send_keys('Computer Programming for Everybody')
password=driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
password.send_keys('yoooo12345')
# login_button=driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')
# login_button.click()

