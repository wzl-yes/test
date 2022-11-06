
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # 可以选择chromium、firefox和webkit
    browser_type = p.chromium
    # 运行chrome浏览器，executablePath指定本地chrome安装路径
    #browser = browser_type.launch(headless=False,executablePath="C:\\Users\\wzl\AppData\\Local\\ms-playwright\\firefox.exe")
    browser = browser_type.launch(headless=False)
    page = browser.new_page()
    page.goto('https://www.baidu.com/')
    print(page.title())
    page.screenshot(path=f'example-{browser_type.name}.png')
    browser.close()
