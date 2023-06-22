# 这里主要是对selenium控制网页免登陆方法的一种总结:
# 方法一：使用已打开的完成了网页登陆操作的浏览器来避免已登录
#       需要在浏览器快捷方式属性页的快捷栏后面添加 --remote-debugging-port=9222 --user-data-dir="C:\selenium\ChromeProfile"
# 方法二：设置用户数据目录免登陆——该方法未实现
#       将selenium运行chrome的数据临时存储目录设置为长期目录
# 方法三：登陆指定网址获取cookies后，用于切换到其他网页时保持登陆
#       cookies的获取使用方法cookies = driver.get_cookies()
#       cookie添加是需要根据需要过滤，并逐个添加
# 
import os
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pywinauto import Desktop
from pywinauto.keyboard import send_keys  # 键盘操作
import time

# 方法一：该函数使用通过快捷方式打开的chrome浏览器来实现避免网页登陆的调试方法
def login_opened_browser(web_url):
    # 创建浏览器实例，连接指定的网址
    # 创建浏览器选项实例
    chrome_options = webdriver.ChromeOptions()
    # 打开已有的浏览器，用于调试时免登陆
    chrome_options.add_experimental_option(
        "debuggerAddress", "127.0.0.1:9222")
    new_browser = webdriver.Chrome(options=chrome_options)
    # 切换到指定网址
    new_browser.get(web_url)
    time.sleep(30)

# 方法二：该函数采用通过更改selenium操控chrome临时目录为长期目录进来免登陆的方法-该方法未实现
def login_browser_with_userdata(login_url, username, password, web_url):
    # 指定浏览器实例的属性选项
    chrmoe_options = webdriver.ChromeOptions()
    chrmoe_options.add_argument(r'--user-data-dir=C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\User Data')
    # 创建浏览器实例
    browser = webdriver.Chrome(options=chrmoe_options)
    # 设置隐式等待时长
    browser.implicitly_wait(5)
    # 连接指定连接
    browser.get(login_url)

    # 使用指定账户登陆指定网页
    # 指定登陆方式
    login_type_button = browser.find_element(
        By.XPATH, '//*[@id="TANGRAM__PSP_4__changePwdCodeItem"]')
    login_type_button.click()
    # 输入账户名密码后登陆账户
    username_input = browser.find_element(
        By.XPATH, '//*[@id="TANGRAM__PSP_4__userName"]')
    username_input.send_keys(username)
    password_input = browser.find_element(
        By.XPATH, '//*[@id="TANGRAM__PSP_4__password"]')
    password_input.send_keys(password)
    login_submit = browser.find_element(
        By.XPATH, '//*[@id="TANGRAM__PSP_4__submit"]')
    login_submit.click()

    # 切换到指定网址
    browser.get(web_url)
    time.sleep(30)

# 方法三：登陆指定网址获取cookies后，用于切换到其他网页时保持登陆
def login_save_session(login_url, username, password, yaml_path):
    # 创建浏览器选项实例
    browser = webdriver.Chrome()
    print(browser.capabilities['browserVersion'])
    # 设置隐式等待时长
    browser.implicitly_wait(5)
    # 连接指定连接
    browser.get(login_url)
    browser.delete_all_cookies()

    # 使用指定账户登陆指定网页
    # 指定登陆方式
    login_type_button = browser.find_element(
        By.XPATH, '//*[@id="TANGRAM__PSP_4__changePwdCodeItem"]')
    login_type_button.click()
    # 输入账户名密码后登陆账户
    username_input = browser.find_element(
        By.XPATH, '//*[@id="TANGRAM__PSP_4__userName"]')
    username_input.send_keys(username)
    password_input = browser.find_element(
        By.XPATH, '//*[@id="TANGRAM__PSP_4__password"]')
    password_input.send_keys(password)
    login_submit = browser.find_element(
        By.XPATH, '//*[@id="TANGRAM__PSP_4__submit"]')
    login_submit.click()

    # 获取连接cookies信息
    cookies = browser.get_cookies()
    for cookie in cookies:#列表
        if cookie['domain'] == '.baidu.com':
            browser.add_cookie({'domain':'.baidu.com',#添加cookie
                                'name':cookie['name'],
                                'value':cookie['value'],
                                'path':'/',
                                'expires':None})
    time.sleep(8)
    browser.get(web_url)
    time.sleep(30)

if __name__ == "__main__":
    login_url = "https://login.bce.baidu.com/?account="
    web_url = "https://cloud.baidu.com/product/ocr/general?p=%E5%8A%9F%E8%83%BD%E6%BC%94%E7%A4%BA&from=experience"
    username = "18384121601"
    password = "Tianxin_2015"
    yaml_path = './session.yaml'
    # login_opened_browser(web_url)
    # login_browser_with_userdata(login_url, username, password, web_url)
    login_save_session(login_url, username, password, yaml_path)
