import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 設置 Selenium WebDriver 的路徑
os.environ["PATH"] = r"C:/SeleniumDrivers"

# 設置 Chrome 選項
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-logging"])

# 創建 WebDriver 實例
driver = webdriver.Chrome(options=options)


def print_status(message):
    print(message)


try:
    # 自動測試1：打開網站
    def test_open_website():
        driver.get("https://myanimelist.net/")
        driver.implicitly_wait(15)
        print_status("Test 1: Website opened successfully. Please proceed with the following manual tests.")


    test_open_website()


    # 自動測試2：等待用戶點擊 Login 按鈕並檢查跳轉
    def test_click_login():
        print_status("Waiting for user to click the Login button...")

        # 等待 URL 發生變化並檢查是否跳轉到預期的 URL
        WebDriverWait(driver, 300).until(
            EC.url_to_be("https://myanimelist.net/login.php?from=%2F&")
        )
        assert driver.current_url == "https://myanimelist.net/login.php?from=%2F&", "URL did not match expected login URL"
        print_status("Test 2: Login button clicked and successfully redirected to login page.")


    test_click_login()


    # 自動測試3：等待用戶點擊 Sign Up 按鈕並檢查跳轉
    def test_click_signup():
        print_status("Waiting for user to click the Sign Up button...")

        # 等待 URL 發生變化並檢查是否跳轉到預期的 URL
        WebDriverWait(driver, 300).until(
            EC.url_to_be("https://myanimelist.net/register.php?from=%2F&")
        )
        assert driver.current_url == "https://myanimelist.net/register.php?from=%2F&", "URL did not match expected signup URL"
        print_status("Test 3: Sign Up button clicked and successfully redirected to registration page.")


    test_click_signup()


    # 自動測試4：點擊 MyAnimeList.net 連結返回首頁
    def test_click_home_link():
        print_status("Please click the MyAnimeList.net link to return to the homepage.")

        # 等待用戶點擊 MyAnimeList.net 連結並檢查 URL 是否變回首頁
        WebDriverWait(driver, 300).until(
            EC.url_to_be("https://myanimelist.net/")
        )
        assert driver.current_url == "https://myanimelist.net/", "URL did not return to homepage"
        print_status("Test 4: MyAnimeList.net link clicked and successfully returned to homepage.")


    test_click_home_link()


    # 自動測試5：等待用戶點擊 OK 按鈕並檢查動作
    def test_click_ok_button():
        print_status("Please click the OK button.")

        # 等待按鈕被點擊並檢查元素是否存在
        ok_button = WebDriverWait(driver, 300).until(
            EC.element_to_be_clickable((By.XPATH, '//button[text()="OK"]'))
        )
        ok_button.click()
        print_status("Test 5: OK button clicked successfully.")


    test_click_ok_button()

finally:
    pass  # 測試結束不關閉網頁
