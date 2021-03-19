from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestSelenium:
    def __init__(self, url_insert):
        # SetUp
        self.driver = webdriver.Chrome()
        self.url = url_insert
        self.driver.get(self.url)
        self.search_bar = None
        self.search_button = None
        self.search = None

    def __repr__(self):
        return 'Now accessing to %s' % self.url

    def func(self, *search_items):
        """
        Can not assign element-locator to vars and reuse them in the loop, have to re-locate in the loop
        self.search_bar = self.driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']")
        self.search_button = self.driver.find_element_by_xpath("//*[@id='nav-search-submit-button']")
        """
        # Element locator
        for i in search_items:
            self.search_bar = self.driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']")
            self.search_button = self.driver.find_element_by_xpath("//*[@id='nav-search-submit-button']")
            self.search_bar.send_keys(i)
            '''
            used to code 
                self.search=self.search_bar.send_keys(i)
                self.search.submit() -->  couldn't work
            correct way
                self.search_bar.submit() --> works
            '''
            self.search_button.click()
            print('Found %s items on Amazon' % i)
            self.driver.back()
            # self.search_bar.clear()

    def mouse_operation(self, search_item):
        self.search_bar = self.driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']")
        self.search = self.search_bar.send_keys(search_item)
        self.search_bar.submit()

        try:
            WebDriverWait(self.driver, 10).until(
                ec.presence_of_element_located((By.PARTIAL_LINK_TEXT, "The Complete Reference")))
        except TimeoutError:
            print('Time out')
            self.driver.quit()

        element_link = self.driver.find_element(By.PARTIAL_LINK_TEXT, "The Complete Reference")
        ActionChains(self.driver).move_to_element(element_link).perform()
        WebDriverWait(self.driver, 5)
        ActionChains(self.driver).click().perform()

        try:
            WebDriverWait(self.driver, 10).until(
                ec.presence_of_element_located((By.XPATH, "//*[@id='add-to-cart-button']")))
        except TimeoutError:
            print('Time out')
            self.driver.quit()

        element_button = self.driver.find_element(By.XPATH, "//*[@id='add-to-cart-button']")
        ActionChains(self.driver).move_to_element(element_button).perform()
        ActionChains(self.driver).click().perform()
        try:
            WebDriverWait(self.driver, 5).until(
                ec.text_to_be_present_in_element((By.XPATH, "//*[@id='huc-v2-order-row-confirm-text']/h1"),
                                                 "Added to Cart"))
            print('Ready to buy')
        except NoSuchElementException:
            print('Time out')
            self.driver.quit()

    # def set_windows(self):
    # self.driver.set_window_size(480,800)
    # self.driver.maximize_window()

    # break
    def tear_down(self):
        self.driver.quit()

amazon_url = "http://www.amazon.com"
amazon = TestSelenium(amazon_url)

print(amazon)
amazon.func('selenium book', 'java', 'python')
amazon.mouse_operation('Java')
amazon.tear_down()

if __name__ == "__main__":
    mian()