import selenium.common.exceptions
from selenium.webdriver.common.by import By
import time


def Login(Driver, username_str, password_str):
    print('Searching User and Password...')

    '''
    # e = driver.find_element(By.XPATH, "//form[@name='f3']/input[0]")  子控件不是从 0 开始！
    a = driver.find_element(By.XPATH, "//form[@name='f3']/input[1]")  # 校园网登陆用户名的输入控件ID, F12 查询
    b = driver.find_element(By.XPATH, "//form[@name='f3']/input[2]")  # 校园网登陆密码的输入控件ID, F12 查询
    c = driver.find_element(By.XPATH, "//form[@name='f3']/input[3]")
    d = driver.find_element(By.XPATH, "//form[@name='f3']/input[4]")
    # print(e.get_attribute('type'))
    print(a.get_attribute('type'))
    print(b.get_attribute('type'))
    print(c.get_attribute('type'))
    print(d.get_attribute('type'))
    time.sleep(500)
    '''

    try:
        username_input = Driver.find_element(By.XPATH, "//form[@name='f3']/input[2]")
        password_input = Driver.find_element(By.XPATH, "//form[@name='f3']/input[3]")
    except selenium.common.exceptions.NoSuchElementException:
        username_input = Driver.find_element(By.XPATH, "//form[@name='f3']/div[1]/input[1]")
        password_input = Driver.find_element(By.XPATH, "//form[@name='f3']/div[2]/input[2]")

    if username_input.get_attribute('type') == 'text' and password_input.get_attribute('type') == 'password':
        print('Searching Successfully')
    else:
        print('Searching Failed')

    '''
    print(username_input.size)
    print(username_input.get_attribute('nextElementSibling'))
    print(password_input.get_attribute('nextElementSibling'))
    print(username_input.get_attribute('type'))
    print(password_input.get_attribute('type'))
    print(username_input.is_displayed())
    print(username_input.is_enabled())
    print(username_input.is_selected())
    print(username_input.tag_name)
    print(username_input.text)
    print(username_input.tag_name)

    ActionChains(driver).move_to_element(username_input).perform()
    driver.execute_script("arguments[0].click()", username_input)
    username_input.click()
    '''

    print('Passing UserName and Password...')
    username_input.send_keys(username_str)
    password_input.send_keys(password_str)
    time.sleep(1)
    username_input.submit()
    password_input.submit()

    print('Login Successfully')
    time.sleep(1)
    Driver.quit()

    return None
