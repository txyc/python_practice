# selenium是一个用于操控网页的测试框架，需要安装与浏览器配套的driver工具使用
# selenium进行浏览器操控时，可以采用有界面模式和无界面模式，无界面模式可以有效地降低服务器开销
# selenium可以采用多种方式进行元素定位，常见的有：id定位、name定位、class定位、xpath定位、css定位
# 老版本的selenium用于定位元素的方法一般为find_element_by_xx('{value}')，新版本的一般表示为find_element(By.XX, '{value}')
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

# 创建浏览器选项实例
chrome_options = webdriver.ChromeOptions()
# 配置headless无界面浏览器模式
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
# 使用指定的浏览器选项打开指定网页，当前选项为无界面模式
# browser = webdriver.Chrome(chrome_options=chrome_options)
browser = webdriver.Chrome()
# 设置隐式等待时长
browser.implicitly_wait(5)

# 连接指定连接
browser.get('http://www.baidu.com/')

# 使用显示等待时间
WebDriverWait(browser,10).until(EC.title_is(u"百度一下，你就知道"))

# ########百度输入框的定位方式##########
# 通过id方式定位
input_id = browser.find_element(By.ID, "kw")
input_id.send_keys("selenium")
browser.find_element(By.ID, "su").click()
WebDriverWait(browser,10).until(EC.title_is(u"selenium_百度搜索"))
browser.find_element(By.ID, "kw").clear()

# 通过name方式定位
input_name = browser.find_element(By.NAME, "wd")
input_name.send_keys("python")
browser.find_element(By.XPATH, '//*[@id="su"]').click()
WebDriverWait(browser,10).until(EC.title_is(u"python_百度搜索"))
browser.find_element(By.NAME, "wd").clear()

# 通过class name方式定位
input_class_name = browser.find_element(By.CLASS_NAME, "s_ipt")
input_class_name.send_keys("selenium")
browser.find_element(By.XPATH, '//*[@id="su"]').click()
WebDriverWait(browser,10).until(EC.title_is(u"python_百度搜索"))
browser.find_element(By.CLASS_NAME, "s_ipt").clear()

# 通过CSS方式定位
input_css_selector = browser.find_element(By.CSS_SELECTOR, "#kw")
input_css_selector.send_keys("selenium")
browser.find_element(By.XPATH, '//*[@id="su"]').click()
WebDriverWait(browser,10).until(EC.title_is(u"selenium_百度搜索"))
browser.find_element(By.CSS_SELECTOR, "#kw").clear()

# 通过xpath方式定位
input_xpath = browser.find_element(By.XPATH, '//*[@id="kw"]')
input_xpath.send_keys("python")
browser.find_element(By.XPATH, '//*[@id="su"]').click()
WebDriverWait(browser,10).until(EC.title_is(u"python_百度搜索"))
browser.find_element(By.XPATH, '//*[@id="kw"]').clear()

time.sleep(3)
browser.close()