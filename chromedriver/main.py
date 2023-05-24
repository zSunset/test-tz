from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time


def get_proxy(url):
    # опции
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(
        executable_path='/home/sunset/Рабочий стол/test-tz/silen/test-tz/chromedriver', options=options)

    try:
        driver.get(url=url)
        my_in = driver.find_element(By.LINK_TEXT, 'Войти').click()
        time.sleep(1)

        email_input = driver.find_element(
            By.XPATH, "//input[@autofocus]")
        email_input.clear()
        email_input.send_keys('logist26rus@gmail.com')

        password_input = driver.find_element(By.ID, 'login-password')
        password_input.clear()
        password_input.send_keys('stavropol26')
        time.sleep(55)
        driver.find_element(
            By.XPATH, '//*[@id="form-login"]/div[7]/button').click()
        time.sleep(5)
        check_mark = driver.find_element(
            By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/div[2]/ul/li[6]/a').click()
        time.sleep(5)
        export_txt = driver.find_element(
            By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/div[2]/ul/li[6]/div/form/button').click()
        time.sleep(5)
        proxy_list = driver.find_element(
            By.LINK_TEXT, 'Прокси на странице').click()
        time.sleep(5)
        proxy_file = driver.find_element(
            By.CSS_SELECTOR, '#proxylist > td > div > textarea').get_attribute("innerHTML")
        print(proxy_file)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


def main():
    get_proxy(url="https://proxy6.net")


if __name__ == '__main__':
    main()
