# -*- encoding: utf-8 -*-
'''
file       :test.py
Description:
Date       :2025/03/08 10:45:10
Author     :czy
version    :v0.01
email      :1060324818@qq.com
'''

from AutoScraperX import common_spider  # 确保 Spider 类已正确导入

def main():
    # 创建 Spider 实例
    # 配置爬虫选项
    options = {
        "driver_executable_path": "chromedriver\\chromedriver.exe",  # 替换为你的 chromedriver 路径
        "user_data_dir": "data\\User Data",  # Chrome 用户数据路径
        "profile_directory": "Default",  # Chrome 配置文件
        "headless": False,  # 是否启用无头模式（True = 不显示浏览器窗口）
        "maximized": True,  # 是否最大化窗口
        "logging_level": 2  # 日志级别
    }

    # 创建 Spider 实例
    spider = common_spider.Spider(options=options)
    
    try:
        # 打开网页
        url = "https://example.com"
        spider.open_page(url)
        print(f"成功打开 {url}")
        
        # 获取网页标题
        title = spider.get_title()
        print(f"页面标题: {title}")
        
        # 等待某个元素出现（假设有 id 为 'content' 的元素）
        spider.wait_for_element("id", "content", timeout=10)
        print("元素 'content' 已出现")
        
        # 截图并保存
        spider.save_screenshot("screenshot.png")
        print("截图已保存")
        
        # 获取 cookies
        cookies = spider.get_cookies()
        print("获取的 Cookies:", cookies)
        
        # 关闭浏览器
        spider.quit()
        print("爬虫已关闭")
    
    except Exception as e:
        print(f"发生错误: {e}")
        spider.quit()

if __name__ == "__main__":
    main()