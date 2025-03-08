# -*- encoding: utf-8 -*-
'''
file       :common_spider.py
Description:
Date       :2025/03/07 18:24:54
Author     :czy
version    :v0.01
email      :1060324818@qq.com
'''

import time
import math
import uuid
import random
from datetime import datetime
import base64
from selenium import webdriver  # 导入selenium的webdriver模块
from selenium.webdriver.common.by import By  # 引入By类选择器
from selenium.webdriver.support.wait import WebDriverWait  # 等待类
from selenium.webdriver.support import expected_conditions as EC  # 等待条件类
from selenium.webdriver.common.action_chains import ActionChains  # 动作类
from logging import DEBUG, INFO, WARNING, ERROR
from dateutil.parser import parse
import re
import os
from os import path
from pathlib import Path
import json
import traceback
import pickle
import undetected_chromedriver as uc
from undetected_chromedriver import ChromeOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

class Spider():
    def __init__(self, options: dict = {}, path: str=None, name: str = None):

        self.options = options

        self.urls = []
        if self.urls:
            self.url = ''
        
        if options.get('urls'):
            self.urls = options.get('urls')

        if options.get('url'):
            self.url = options.get('url')
        
        if options.get('mobile'):
            mobile_emulation = {
                "deviceName": "iPhone X"
            }
            defualt_options.add_experimental_option("mobileEmulation", mobile_emulation)

        # 创建 undetected_chromedriver 的选项
        defualt_options = uc.ChromeOptions()
        # 设置性能日志记录能力
        defualt_options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})

        

        if options.get('logging_level'):
            defualt_options.add_argument(f"--verbose")
            defualt_options.add_argument(f"--enable-logging")
            defualt_options.add_argument(f"--v={options.get('logging_level')}")

        # 注意！！ 一个user-data-dir只能实例化一个chrome，多个共用是会创建session失败，连接失败的 要配置让用户决定是否删除
        if options.get('user_data_dir'):
            # 这里有个黑科技，删除preferences文件夹，因为我还没搞懂为什么指定了userdatadir会一直增大变为3g大小，最后崩溃
            # 创建Path对象
            file_path = Path(options.get('user_data_dir')).joinpath('Default').joinpath('Preferences')

            # 删除文件
            if file_path.exists():
                file_path.unlink()  # 删除文件
                print(f'{file_path} 已删除')
            else:
                print(f'{file_path} 不存在')

            defualt_options.add_argument(f"--user-data-dir={options.get('user_data_dir')}") 
            defualt_options.add_argument(f"--profile-directory={options.get('profile_directory', 'Default')}")  # 指定默认配置文件
        
        
        if options.get('headless', False):
            defualt_options.add_argument('--headless')
        if options.get('maximized', True):
            defualt_options.add_argument('--start-maximized')
        
        # 设置浏览器选项
        defualt_options.binary_location = options.get('binary_location', r"C:\Users\Administrator\AppData\Local\Google\Chrome\Bin\chrome.exe")
             
        if options.get('fastest', False):
            defualt_options.add_argument("--disable-extensions")
            defualt_options.add_argument('--disable-application-cache')
            defualt_options.add_argument('--disable-gpu')
            defualt_options.add_argument("--no-sandbox")
            defualt_options.add_argument("--disable-setuid-sandbox")
            # defualt_options.add_argument("--disable-dev-shm-usage")

        # 配置日志捕获
        capabilities = DesiredCapabilities.CHROME
        capabilities['goog:loggingPrefs'] = {'performance': 'ALL'}
        try:
            import ssl
            ssl._create_default_https_context = ssl._create_unverified_context
            self.driver = uc.Chrome(
                use_subprocess=True,
                options=defualt_options,
                desired_capabilities=capabilities,
                driver_executable_path=options.get('driver_executable_path', None)
            )
        except:
            traceback.print_exc()
            raise RuntimeError("Spider Chrome 启动失败")

        
        # self.driver.execute_cdp_cmd("Network.enable", {})
        # self.driver.execute_cdp_cmd("Page.enable", {})
        # self.driver.execute_script("console.log('DevTools Network tab is enabled.')")


        # 获取用户提供的页面加载超时时间（默认设置为300秒）
        page_load_timeout = options.get('page_load_timeout', 60*30)  # 用户可以传递超时时间，默认为300秒

        # 检查是否启用页面加载超时
        if options.get('enable_page_load_timeout', True):  # 用户可以选择是否启用此功能，默认为启用
            self.driver.set_page_load_timeout(page_load_timeout)

        self.waiter_second = options.get('waiter_seconds', 300)
        self.waiter = WebDriverWait(self.driver, self.waiter_second)

    def __del__(self):
        if hasattr(self, 'driver'):
            self.driver.quit()
        
    def get_log(self, category: str = 'performance'):
        return self.driver.get_log(category)
    
    def get_driver(self):
        return self.driver
    
    def save_screenshot(self, file_path):
        page_rect = self.driver.execute_cdp_cmd('Page.getLayoutMetrics', {})
        screenshot_config = {'captureBeyondViewport': True,
                             'fromSurface': True,
                             'clip': {'width': page_rect['contentSize']['width'],
                                      'height': page_rect['contentSize']['height'],
                                      'x': 0,
                                      'y': 0,
                                      'scale': 1},
                             }
        base_64_png = self.driver.execute_cdp_cmd('Page.captureScreenshot', screenshot_config)
        with open(file_path, "wb") as fh:
            fh.write(base64.urlsafe_b64decode(base_64_png['data']))

    
    
    def open(self, url: str = None):
        url = url or self.url
        driver = self.driver
        try:
            driver.get(url)
        except:
            msg = traceback.format_exc()
            print(msg)
            self.quit()
    
    def get_source(self):
        return self.driver.page_source

    def get_waiter(self, seconds: int = None):
        return self.waiter if seconds == None else WebDriverWait(self.driver, seconds)

    def wait_element(self, selector, by=By.XPATH, seconds: int = None):
        waiter = self.get_waiter(seconds)
        waiter.until(EC.presence_of_element_located((by, selector)))

    def wait_element_visible(self, selector, by=By.XPATH, seconds: int = None):
        waiter = self.get_waiter(seconds)
        waiter.until(EC.visibility_of_element_located((by, selector)))

    def wait_title(self, title='', seconds: int = None):
        waiter = self.get_waiter(seconds)
        waiter.until(EC.title_contains(title))
    
    def wait_for_element_and_execute(self, selector, by=By.CSS_SELECTOR, seconds=30):
        try:
            # 等待指定元素可见
            self.waiter.until(EC.visibility_of_element_located((by, selector)))
            # 执行后续操作
            print("Element is visible, executing code...")
        except Exception as e:
            print(f"Error: {e}")

    def comment(self, text, css_selector='#comment', reset=False, br=True):
        driver = self.driver
        if br:
            text += '\n'
        textarea = driver.find_element(By.CSS_SELECTOR, css_selector)
        driver.execute_script("arguments[0].selectionStart = arguments[0].selectionEnd = arguments[0].value.length;", textarea)
        if reset:
            textarea.clear()
            self.comments = ''
        textarea.send_keys(text)
        self.comments += text

    def element(self, selector, by=By.CSS_SELECTOR):
        try:
            return self.driver.find_element(by, selector)
        except:
            return None
        
    def elements(self, selector, by=By.CSS_SELECTOR):
        try:
            return self.driver.find_elements(by, selector)
        except:
            return None
        
    def save_cookie(self, path: str = 'data/cookies.pkl'):
        pickle.dump(self.driver.get_cookies(), open(path, 'wb'))

    def load_cookie(self, path: str = 'data/cookies.pkl', domain=''):
        cookies = pickle.load(open(path, 'rb'))
        for cookie in cookies:
            print(cookie)
            cookie_dict = {
                'domain' : domain,
                'name' : cookie.get('name'),
                'value' : cookie.get('value'),
            }
            self.driver.add_cookie(cookie_dict)
        
    def refresh(self):
        self.driver.refresh()
        
    def scroll_to_view(self, css_selector):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", self.element(css_selector))
    
    def scroll_to_top(self):
        self.driver.execute_script("window.scrollTo(0, 0);")

    def sleep(self, seconds):
        time.sleep(seconds)

    def submit(self, css_selector='button[type="submit"]'):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR, css_selector).click()
    
    def cancel(self):
        driver = self.driver
        driver.find_element(By.CLASS_NAME, 'cancel').click()

    def switch_tab(self, index=0):
        self.driver.switch_to.window(self.driver.window_handles[index])

    def close_tab(self):
        self.driver.close()
        self.switch_tab()
        self.refresh()

    def quit(self):
        self.driver.quit()