# AutoScraperX

AutoScraperX 是一个基于 Selenium 和 undetected_chromedriver 的通用爬虫框架，旨在提供强大而灵活的 Web 自动化功能。它支持自动化浏览、元素操作、页面截图、cookie 管理等功能，适用于各种爬取任务。

## 功能特点

* **支持多种浏览器选项**（无头模式、用户数据目录、自定义 Chrome 位置等）
* **支持移动端仿真**（iPhone X 模拟）
* **智能等待机制**，确保元素加载完毕再进行操作
* **页面截图**，可保存完整网页截图
* **Cookie 读写**，支持持久化登录
* **自动滚动、刷新、切换标签页等操作**
* **异常处理**，确保爬虫稳定运行

## 安装

确保你的环境中安装了以下依赖：

```
pip install selenium undetected-chromedriver beautifulsoup4
```

此外，请下载并配置相应的 WebDriver，例如 [ChromeDriver]()。

## 使用方法

### 初始化爬虫

```
from AutoScraperX import common_spider  # 确保 Spider 类已正确导入

options = {
    'headless': True,  # 以无头模式运行
    'binary_location': "C:\\Path\\To\\chrome.exe",  # 指定 Chrome 位置
    'user_data_dir': "C:\\Users\\User\\AppData\\Local\\Google\\Chrome\\User Data",
    'driver_executable_path': "C:\\Path\\To\\chromedriver.exe"
}

spider = common_spider.Spider(options)
```

### 打开网页

```
spider.open("https://example.com")
```

### 获取页面源码

```
html = spider.get_source()
print(html)
```

### 等待元素加载

```
spider.wait_element("//div[@id='content']", by=By.XPATH)
```

### 进行交互

```
spider.comment("测试评论", "#comment-box")
```

### 保存截图

```
spider.save_screenshot("screenshot.png")
```

### 处理 Cookie

```
spider.save_cookie("cookies.pkl")
spider.load_cookie("cookies.pkl", domain="example.com")
```

### 退出爬虫

```
spider.quit()
```

## 贡献

如果你对 AutoScraperX 有任何改进建议或贡献，请提交 PR 或 Issue。

## 联系方式

* 作者: czy
* 邮箱: [1060324818@qq.com]()
* 项目地址：https://github.com/chenziying1/AutoScraperX
* 项目示例：https://github.com/chenziying1/AutoScraperX/test/test.py
