import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class CNKISpider:
    """CNKI 爬虫类"""

    def __init__(self):
        self.driver = self.init_driver()

    def init_driver(self):
        """初始化 Selenium WebDriver"""
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        return webdriver.Chrome(options=options)

    def search(self, keyword):
        """打开 CNKI 并搜索关键词"""
        self.driver.get("https://kns.cnki.net/kns8/AdvSearch")
        time.sleep(2)

        opt = self.driver.find_element(By.CSS_SELECTOR, 'div.sort-list')
        self.driver.execute_script("arguments[0].setAttribute('style', 'display: block;')", opt)

        ActionChains(self.driver).move_to_element(
            self.driver.find_element(By.CSS_SELECTOR, 'li[data-val="RP"]')
        ).perform()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="gradetxt"]/dd[1]/div[2]/input'))
        ).send_keys(keyword)

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="ModuleSearch"]/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div[3]/input')
            )
        ).click()

        print("正在搜索，请稍后...")

        res_num = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="countPageDiv"]/span[1]/em'))
        ).text
        res_num = int(res_num.replace(",", ""))
        return res_num

    def download_papers(self, papers_need):
        """开始下载文献"""
        count = 1

        while count <= papers_need:
            time.sleep(3)

            title_list = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "fz14"))
            )

            for i in range(min(20, papers_need - count + 1)):
                print(f"📌 正在爬取第 {count} 篇...")

                try:
                    title_list[i].click()
                    self.driver.switch_to.window(self.driver.window_handles[-1])
                    time.sleep(3)

                    # 点击 PDF 下载
                    try:
                        download_button = WebDriverWait(self.driver, 5).until(
                            EC.element_to_be_clickable((By.CLASS_NAME, "btn-dlpdf"))
                        )
                        download_button.click()
                        print(f"✅ {count} - 下载触发")

                        # 检测滑块验证码
                        self.handle_slider_verification()

                    except Exception as e:
                        print(f"❌ 下载失败: {e}")

                finally:
                    if len(self.driver.window_handles) > 1:
                        self.driver.close()
                        self.driver.switch_to.window(self.driver.window_handles[0])

                count += 1
                if count > papers_need:
                    return

            # 翻页
            try:
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//a[@id='PageNext']"))
                ).click()
            except:
                print("无法翻页，爬取结束")
                break

    def handle_slider_verification(self):
        """处理滑块验证码"""
        time.sleep(3)
        all_iframes = self.driver.find_elements(By.TAG_NAME, "iframe")

        if len(all_iframes) > 0:
            print("⚠️ 发现滑块验证码，请手动解决")
            self.driver.switch_to.frame(all_iframes[0])

            while True:
                try:
                    WebDriverWait(self.driver, 1).until_not(
                        EC.presence_of_element_located((By.CLASS_NAME, "nc-container"))
                    )
                    print("✅ 滑块验证完成")
                    break
                except:
                    time.sleep(1)

            self.driver.switch_to.default_content()

    def close(self):
        """关闭 WebDriver"""
        self.driver.quit()


def search_and_download(keyword, papers_need=10):
    """对外接口：搜索并下载"""
    spider = CNKISpider()
    total_results = spider.search(keyword)
    papers_need = min(total_results, papers_need)
    spider.download_papers(papers_need)
    spider.close()