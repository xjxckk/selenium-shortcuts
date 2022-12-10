from selenium.webdriver.common.by import By

class setup:
    ''' '''
    def __init__(self, driver):
        self.driver = driver
        
    def find(self, css_selector, attribute=None, parent=None):
        if not parent:
            parent = self.driver
        element = parent.find_element(By.CSS_SELECTOR, css_selector)
        if attribute:
            attribute = element.get_attribute(attribute)
            return element, attribute
        return element

    def finds(self, css_selector, parent=None, wait=None):
        if not parent:
            parent = self.driver
        if wait:
            self.driver.implicitly_wait(wait)
        elements = parent.find_elements(By.CSS_SELECTOR, css_selector)
        if wait:
            self.driver.implicitly_wait(15)
        return elements

    def click(self, css_selector, parent=None):
        if not parent:
            parent = self.driver
        element = parent.find_element(By.CSS_SELECTOR, css_selector)
        element.click()

    def text(self, css_selector, parent=None):
        if not parent:
            parent = self.driver
        element = parent.find_element(By.CSS_SELECTOR, css_selector)
        return element.text

    def send(self, css_selector, text, clear=True, parent=None):
        if not parent:
            parent = self.driver
        element = parent.find_element(By.CSS_SELECTOR, css_selector)
        if clear:
            element.clear()
        element.send_keys(text)
    
    def get(self, url):
        if not parent:
            parent = self.driver
        if parent.current_url != url:
            parent.get(url)
