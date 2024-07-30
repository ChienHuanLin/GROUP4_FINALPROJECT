import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# 設置 Selenium WebDriver 的路徑
chrome_driver_path = 'C:/SeleniumDrivers/chromedriver.exe'
service = Service(chrome_driver_path)

# 設置 Chrome 選項
options = Options()
options.add_experimental_option("detach", True)  # 保留瀏覽器開啟
options.add_experimental_option("excludeSwitches", ["enable-logging"])


# 創建 WebDriver 實例
def create_driver():
    return webdriver.Chrome(service=service, options=options)


def retry_on_timeout(func, retries=3):
    for attempt in range(retries):
        try:
            func()
            return
        except TimeoutException:
            if attempt < retries - 1:
                print(f"Retrying {func.__name__} (Attempt {attempt + 2})...")
                continue
            else:
                print(f"{func.__name__} Failed after {retries} attempts")
                raise


driver = create_driver()

try:
    # 自動測試1：打開網站
    def test_open_website():
        driver.get("https://myanimelist.net/")
        driver.implicitly_wait(15)
        assert "MyAnimeList.net" in driver.title
        print("Test 1 Passed: Website opened successfully")


    retry_on_timeout(test_open_website)


    # 自動測試2：自動關閉網頁
    def test_close_website():
        time.sleep(5)  # 等待 5 秒鐘以確保網站完全加載
        driver.quit()
        print("Test 2 Passed: Website closed successfully")


    retry_on_timeout(test_close_website)


    # 自動測試3：格 3 秒後再次開啟網頁
    def test_reopen_website():
        time.sleep(3)  # 等待 3 秒鐘
        global driver  # 使用 global 關鍵字來重新賦值 driver 變量
        driver = create_driver()  # 重新創建 WebDriver 實例
        driver.get("https://myanimelist.net/")
        driver.implicitly_wait(15)
        assert "MyAnimeList.net" in driver.title
        print("Test 3 Passed: Website reopened successfully")


    retry_on_timeout(test_reopen_website)


    # 自動測試4：點擊「Hide Ads」按鈕
    def test_click_hide_ads():
        hide_ads_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//a[@class="btn-mal-service ga-click ga-impression" and contains(@href, "membership")]'))
        )
        hide_ads_button.click()
        print("Test 4 Passed: 'Hide Ads' button clicked successfully")


    retry_on_timeout(test_click_hide_ads)

    # 等待10秒後進行測試5
    time.sleep(10)


    # 自動測試5：跳轉到指定URL
    def test_redirect_to_url():
        driver.get("https://myanimelist.net/")
        driver.implicitly_wait(15)
        assert "MyAnimeList.net" in driver.title
        print("Test 5 Passed: Redirected to the specified URL and verified title")


    retry_on_timeout(test_redirect_to_url)


    # 自動測試6：在搜索框中輸入 'one piece' 並點擊搜索按鈕
    def test_search_one_piece():
        search_box = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.ID, 'topSearchText'))
        )
        search_box.send_keys("one piece")

        search_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.ID, 'topSearchButon'))
        )
        search_button.click()
        print("Test 6 Passed: 'one piece' entered and search button clicked")


    retry_on_timeout(test_search_one_piece)

# 自動測試7：點選「Search for 'one piece' in Manga」連結
    def test_click_search_in_manga():
        search_link = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//a[@class="btn-search-more" and contains(@href, "q=one+piece&cat=manga")]')
            )
        )
        search_link.click()
        print("Test 7 Passed: 'Search for \"one piece\" in Manga' link clicked")

    retry_on_timeout(test_click_search_in_manga)



except TimeoutException as e:
    print("Timeout error:", e)
except Exception as e:
    print("An error occurred:", e)
finally:
    pass  # 測試結束後不關閉網頁



