import selenium.common.exceptions as SelenException
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from Login import Login

Time = input('请问您需要我工作多少分钟：')

Lost = True
while Lost:
    try:
        times = int(Time)
        print('收到！')
        Lost = False
    except ValueError:
        Time = input('别再耍我，我已经很痛苦了。请输入正确的工作时长：')

username_str = eval("input('请输入你的校园网登陆用户名：')")
password_str = eval("input('请输入你的校园网登陆密码：')")

while times:
    driver = webdriver.Edge()
    driver.get("http://10.123.0.253/")

    try:
        Form = driver.find_element(By.XPATH, "//form[@name='f1']/input[1]").get_attribute('value')
        print('校园网正常连接...')
        driver.quit()
        time.sleep(60)
    except SelenException.NoSuchElementException:
        Login(Driver=driver, username_str=username_str, password_str=password_str)
        time.sleep(60)
    finally:
        times -= 1

print('我的工作已结束，祝您醒来后度过开心的一天。')

